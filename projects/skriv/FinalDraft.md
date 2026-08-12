# Final Draft Sync Problems

Status as of 2026-08-09 16:45. This replaces the earlier hash-mismatch analysis,
which was based on a misreading — see "Superseded" at the bottom.

## Summary

Two separate things, neither of them the local sync client:

1. **The web app won't load in any browser.** `cloud.finaldraft.com` serves its HTML
   fine, but the JavaScript bundles it depends on hang most of the time. Without them
   the app can't boot, so every browser shows a page that never finishes loading.
2. **Edits made in the web app never reached the server.** The cloud copy of
   `Transit.fdx` is byte-identical to the local one. The likely cause is the same
   server fault — saves that silently failed.

The sync client itself is behaving correctly. Local and cloud are genuinely in sync,
and its steady `0 downloads` is the right answer, not a bug.

## The web app failure

The HTML document is healthy. The static chunks are not:

```
root try1: http=200 total=0.85s
root try2: http=200 total=0.86s
root try3: http=200 total=0.82s

webpack try1: http=000 total=8.00s   (timeout, 0 bytes)
webpack try2: http=000 total=8.00s
webpack try3: http=000 total=8.00s
webpack try4: http=200 total=0.71s
webpack try5: http=000 total=8.00s
```

Failure signature: TCP connects, TLS completes, then **zero response bytes** until
timeout. Not a 4xx/5xx — the connection just hangs.

Fetching every asset the page references, `/_next/static/chunks/webpack-*.js` and
`/_next/static/chunks/app/page-*.js` both fail routinely. Those two are required for
the app to start at all, which is why the browser symptom is total rather than
partial.

Reproduce:

```bash
curl -sS -o /dev/null -w "%{http_code} %{time_total}s\n" --max-time 8 \
  https://cloud.finaldraft.com/_next/static/chunks/webpack-<hash>.js
```

(The hash changes on each deploy; pull a current one out of the root HTML.)

### Ruled out

- **Not local browser state.** Fails in Safari, never used for this app. Clearing
  Chrome site data and hunting service workers achieved nothing — there was no
  finaldraft.com service worker registered in the first place.
- **Not DNS.** Tailscale's resolver (`100.100.100.100`) and `1.1.1.1` return the same
  four CloudFront IPs. No AAAA record, so no IPv6 fallback problem.
- **Not proxy/VPN/hosts.** No proxies configured; the only `/etc/hosts` oddity is a
  dangling Adobe Creative Cloud WAM line with an IP and no hostname, which is inert.
- **Not the network path.** Same machine, same moment: the sync client's API calls
  succeed on their 60-second cycle while the browser chunks hang.

The API surface (`/api/*`) is markedly healthier than static asset delivery — 10/10
responded in one sample. That asymmetry is why sync keeps working while the web app
is unusable.

## The missing edits

Changes made in the browser app on 2026-08-09 never appeared locally. They also never
reached the server:

| | md5 | size |
|---|---|---|
| Local `Documents/Final Draft Vault/Transit.fdx` | `cea7fdcc…142a` | 62 258 |
| Downloaded from cloud, 16:08 | `cea7fdcc…142a` | 62 258 |
| Client DB `lastSyncedHash` | `cea7fdcc…142a` | — |

Byte-identical. The client reporting `synced` with `0 downloads` is correct — the
server has nothing it doesn't already have.

Most likely the saves hit the same hang and failed silently. A second possibility,
not ruled out: the document metadata carries `latestVersionId` and
`proposedVersionId`, so edits could exist as a version that was never promoted and
that the download endpoint doesn't serve. Distinguishing them needs the web app to
load — check whether the edits are visible there, and check version history.

## Where things live

Not obvious, and `find ~/Library -iname "*inaldraft*"` misses the important one
because the directory name doesn't contain "finaldraft":

```
~/Library/Application Support/FDVaultSync/FDVaultSync.sqlite   sync DB
~/Library/Application Support/FDVaultSync/Logs/                daily logs
~/Library/Application Support/com.finaldraft.finaldraft.sync/shared-config.plist
~/Library/Caches/com.finaldraft.finaldraft.sync/Cache.db       NSURLCache
```

`FDVaultSync.sqlite` has two tables: `fdFileRecord` (path, remoteId, hash,
lastSyncedHash, status) and `fdSyncJournal` (currently empty). Read it with
`?mode=ro` while the app is running.

Config worth knowing: `fdSyncMode = bidirectional`, `deleteServerCopy = true`. The
second one means local deletions propagate to the server — `shared-config.plist` has
an `AuthorizedDeletes` dict recording real ones. Quit the app before moving anything
out of the Vault folder.

## The app is LSUIElement

`LSUIElement = true` — no Dock icon, no window. The menu bar item is the entire UI.
If it's missing, the usual cause is menu bar crowding (macOS silently drops status
items that don't fit rather than overflowing them), not a crash. Check
System Settings → Control Center → Menu Bar Only.

Three concurrent `.appex` instances accumulated at one point. They're **FinderSync**
extensions (`com.finaldraft.finaldraft.sync.FinderSync`), badge overlays only — they
don't perform uploads. Finder spawns them lazily, so they won't respawn from shell
access.

## Superseded: the Aug 8 hash-mismatch analysis

The earlier note concluded the client was writing to the same `remoteId` with
mismatched content, citing `[ERROR] INTEGRITY: Upload hash mismatch`. That error no
longer occurs — the logs for 2026-08-09 contain no errors at all.

A follow-on theory, that the client stores a locally derived `lastSyncedHash` and so
can never detect remote changes, was **wrong**. It came from comparing today's DB
against a cached `/api/vault/documents/…` response from Aug 8 13:22 — the newest
entry in `Cache.db`, and two hours stale. The logs show what happened in between:

```
Aug 8 13:21:56  Uploading: Transit.fdx
Aug 8 13:22:07  Successfully uploaded          ← cached metadata: 62 376, bad9e028
Aug 8 15:19:25  Successfully downloaded: Transit.fdx
Aug 8 15:25:19  Successfully downloaded: Transit.fdx
Aug 8 15:35:46  Successfully downloaded: Transit.fdx   ← local becomes 62 258, cea7fdcc
```

The local file was replaced by a download two hours after that snapshot. The 118-byte
gap was an artifact of the comparison, not evidence of drift.

Whether the Aug 8 upload corruption shares a root cause with today's hanging
responses is plausible but unproven.

## For a support ticket

- Static chunks under `/_next/static/chunks/` hang with no response bytes, ~80% of
  requests in sampling, while `/` returns 200 consistently.
- Signature: connection accepted, TLS complete, zero bytes, indefinite hang. Not a
  status code.
- `/api/*` is comparatively healthy, so it appears specific to asset delivery.
- Edge: CloudFront, POP ARN53-P3, origin behind API Gateway (`x-amz-apigw-id`),
  `x-powered-by: Next.js`.
- Consequence: the web app cannot boot in any browser, and edits made in it are lost
  without warning.
