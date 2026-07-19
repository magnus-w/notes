# GCE VM cost analysis — "Silverclaude" remote-control VM

_Saved 2026-07-19. Written on the VM itself; goal was to make a 50 SEK/month GCP budget last a full month._

## The VM

- **Instance:** `e2-small` (2 shared vCPU, 2 GB RAM) — ~1.2 GB of 2 GB in use
- **Project / zone:** `sixth-utility-492415-b8`, `europe-north1-b` (Finland — already a cheap region)
- **Pricing:** on-demand (not preemptible/spot)
- **Boot disk:** 30 GB **pd-standard** (switched from pd-balanced 2026-07-19), ~13 GB used
- **External IP:** `35.228.213.57` — **ephemeral, not reserved static** (confirmed: `gcloud compute addresses list` empty). So no idle-IP charge while stopped.
- **Tailscale:** installed and up — VM reachable at `100.124.88.29`
- **Runtime pattern:** instance-schedule resource policy `silvercloud-schedule` (Europe/Stockholm), updated 2026-07-19 to start 09:00 / stop 18:00, **weekdays only** (cron `0 9 * * 1-5` / `0 18 * * 1-5`) ≈ **9 h/day × 5 days/week** (was 08:00–22:30 every day ≈ 13.5 h/day). Can still be started manually on weekends via the `vmstart` alias — the schedule only governs automatic starts.
- Served by systemd `claude-rc.service` → tmux `claude-rc` → `claude remote-control --name "Silverclaude"` rooted at `~/GitHub`. Needs the VM running + outbound internet to be reachable.

## Cost model (the key distinction)

All figures ~±10%. USD→SEK ≈ 10.6. Rates are us-central1 baseline; europe-north1 runs a few % higher.

**Fixed — billed 24/7 even while the VM is stopped:**
- 30 GB pd-standard disk @ $0.04/GB/mo = $1.20/mo ≈ **~13 SEK/mo** (was pd-balanced @ $0.10/GB/mo ≈ 32 SEK/mo until 2026-07-19)

**Variable — billed only while the VM is running (~0.22 SEK/hr total):**
- e2-small compute ≈ $0.017/hr ≈ 0.18 SEK/hr
- ephemeral IP ≈ $0.004/hr ≈ 0.04 SEK/hr (free while stopped)

**At 9 h/day × weekdays only (~196 h/mo), since the 2026-07-19 schedule change (09:00–18:00, Mon–Fri):**
- Variable ≈ 196 × 0.22 ≈ **~43 SEK/mo**
- + disk ~13 SEK (pd-standard)
- **≈ ~56 SEK/month total** — right at the edge of the 50 SEK budget. A small trim (e.g. e2-micro, or a slightly shorter window) would close the rest of the gap.

(At the original always-on 13.5 h/day schedule this was ≈ ~103 SEK/month; at 9h/day every day it was ≈ ~73 SEK/month.)

> NOTE: an earlier "~1 hour/day fits the budget" estimate was a **10× arithmetic error** (2.2 SEK/hr instead of the correct 0.22 SEK/hr). Corrected above. Compute — not the disk — is the dominant cost at this runtime.

## Answers to the two questions

### Q1: Shrinking the boot disk 30 → 20 GB
pd-balanced is $0.10/GB/mo:
- 30 GB = $3.00/mo ≈ 32 SEK → 20 GB = $2.00/mo ≈ 21 SEK
- Savings from the shrink alone would only be ~11 SEK/month.
- GCP can't shrink **or** change disk type in place for a normal zonal PD — confirmed hands-on 2026-07-19 (`gcloud compute disks update` has no `--type` flag, and `gcloud compute disks create --source-disk=... --type=...` is rejected: "Requested disk type must be the same as the source disk type"). Either change requires rebuilding the disk (snapshot → new disk → swap boot disk), so the size shrink and the type switch cost the same effort/risk.
- **Decision:** since the type switch alone (~19 SEK/mo) beats the size shrink alone (~11 SEK/mo) for the same rebuild cost, we did **only** the type switch (30 GB pd-balanced → 30 GB pd-standard) and left the size at 30 GB. See "What was actually done" below. The 20 GB shrink is still available as a follow-up if ~11 more SEK/month is worth another rebuild.

#### What was actually done (2026-07-19)
Switched the boot disk from pd-balanced to pd-standard at the same 30 GB size, via:
1. Stopped the VM.
2. Took a fresh manual snapshot (`linux-pretypeswitch-20260719`) in addition to the existing daily schedule, as a rollback point.
3. `gcloud compute disks create --source-disk=linux --type=pd-standard` was rejected (type must match source when cloning directly from a disk) — worked instead via `gcloud compute disks create --source-snapshot=<fresh snapshot> --type=pd-standard`, which created `linux-pdstandard` (30 GB, pd-standard) with guest OS features (UEFI_COMPATIBLE, etc.) and the Debian 12 license carried over correctly.
4. Reattached the `linux-daily-snapshots` resource policy to the new disk (it does not carry over automatically on create).
5. Detached the old disk, attached `linux-pdstandard` as boot (`--boot --device-name=linux`), re-enabled auto-delete.
6. Started the VM; verified via serial console that `claude-rc.service` started and Tailscale reconnected on the same address (100.124.88.29).
7. Deleted the old 30 GB pd-balanced disk.

Total downtime was a few minutes. No partition/filesystem resize was needed since the size didn't change, which kept this low-risk (straight data copy, no fstab/bootloader changes).

### Q2: Do we need the external IP when using Tailscale?
- **Inbound (reaching the VM):** No — Tailscale (`100.124.88.29`) covers that without a public IP.
- **Outbound (VM → internet):** The external IP is *also* the egress path (`ONE_TO_ONE_NAT`). Remove it and the VM loses internet access, which **breaks the remote-control daemon**, git, npm, etc.
- Replacing egress without a per-VM external IP means **Cloud NAT** (~$0.044/hr + data — *more* expensive) or a **Tailscale exit node** (needs a second always-on node, adds latency).
- The ephemeral IP is only ~$0.004/hr ≈ **~17 SEK/mo** at current usage, free while stopped.
- **Verdict: keep the ephemeral IP.** Tailscale replaces the need for a public IP for *access*, but not for the VM's *outbound* connectivity.

## Levers to actually fit ~50 SEK/month (ranked by impact)

1. **e2-small → e2-micro** — halves compute rate, ~**21 SEK/mo saved** at the current 9h/day×weekdays. Risk: 1 GB RAM vs 1.2 GB currently used → needs a swapfile, accept OOM risk / slowness. Biggest remaining lever, would bring total to ~35 SEK/mo — under budget.
2. ~~Fewer runtime hours — each hour/day trimmed ≈ ~6.5 SEK/mo. E.g. 13.5 → 8 h/day ≈ ~35 SEK/mo saved.~~ **Done, 2026-07-19:** schedule moved from every day 08:00–22:30 to weekdays-only 09:00–18:00 (13.5 h/day×7 → 9 h/day×5), ~47 SEK/mo saved total from the original.
3. ~~Disk → 20 GB pd-standard — ~23 SEK/mo saved~~ **Done (partial), 2026-07-19:** switched to pd-standard at 30 GB, ~19 SEK/mo saved. Shrinking to 20 GB on top would add ~4 more SEK/mo but requires another rebuild — not done, low priority given the small remaining delta.

Current total ≈ ~56 SEK/mo (down from ~120 SEK/mo originally) — right at the budget edge. The e2-micro lever alone would clear it comfortably.

## Caveats worth remembering
- A GCP **budget is an alert, not a hard cap** — hitting 50 SEK doesn't stop the VM or the charges; spend keeps accruing. A true cap needs a budget-triggered Cloud Function that stops the VM.
- e2-micro **free tier** applies only in us-west1/us-central1/us-east1 — **not** europe-north1, so no free-tier relief here.
- This VM's service account lacks Compute API scopes, so resource enumeration / disk changes must be done from Cloud Console or an account with proper scopes, not from inside the VM.

## Not yet done (open follow-ups)
- Optional: shrink 30 GB → 20 GB on top of the pd-standard switch already done (only ~4 SEK/mo more, needs another disk rebuild)
- e2-micro resize procedure + swapfile setup
