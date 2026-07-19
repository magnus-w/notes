# GCE VM cost analysis — "Silverclaude" remote-control VM

_Saved 2026-07-19. Written on the VM itself; goal was to make a 50 SEK/month GCP budget last a full month._

## The VM

- **Instance:** `e2-small` (2 shared vCPU, 2 GB RAM) — ~1.2 GB of 2 GB in use
- **Project / zone:** `sixth-utility-492415-b8`, `europe-north1-b` (Finland — already a cheap region)
- **Pricing:** on-demand (not preemptible/spot)
- **Boot disk:** 30 GB **pd-balanced**, ~13 GB used
- **External IP:** `35.228.213.57` — **ephemeral, not reserved static** (confirmed: `gcloud compute addresses list` empty). So no idle-IP charge while stopped.
- **Tailscale:** installed and up — VM reachable at `100.124.88.29`
- **Runtime pattern:** up every day ~08:30–22:00 ≈ **13.5 h/day**
- Served by systemd `claude-rc.service` → tmux `claude-rc` → `claude remote-control --name "Silverclaude"` rooted at `~/GitHub`. Needs the VM running + outbound internet to be reachable.

## Cost model (the key distinction)

All figures ~±10%. USD→SEK ≈ 10.6. Rates are us-central1 baseline; europe-north1 runs a few % higher.

**Fixed — billed 24/7 even while the VM is stopped:**
- 30 GB pd-balanced disk @ $0.10/GB/mo = $3.00/mo ≈ **~32 SEK/mo**

**Variable — billed only while the VM is running (~0.22 SEK/hr total):**
- e2-small compute ≈ $0.017/hr ≈ 0.18 SEK/hr
- ephemeral IP ≈ $0.004/hr ≈ 0.04 SEK/hr (free while stopped)

**At 13.5 h/day (~410 h/mo):**
- Variable ≈ 410 × 0.22 ≈ **~90 SEK/mo**
- + disk ~32 SEK
- **≈ ~120 SEK/month total** — so 50 SEK will not cover current usage without real cuts.

> NOTE: an earlier "~1 hour/day fits the budget" estimate was a **10× arithmetic error** (2.2 SEK/hr instead of the correct 0.22 SEK/hr). Corrected above. Compute — not the disk — is the dominant cost at this runtime.

## Answers to the two questions

### Q1: Shrinking the boot disk 30 → 20 GB
pd-balanced is $0.10/GB/mo:
- 30 GB = $3.00/mo ≈ 32 SEK → 20 GB = $2.00/mo ≈ 21 SEK
- **Savings ≈ ~11 SEK/month** from the shrink alone.
- If also switched to **pd-standard (HDD, $0.04/GB/mo)** while recreating: 20 GB = $0.80/mo ≈ 8.5 SEK → **~23 SEK/mo saved** vs today. Slower I/O but fine for this workload.
- GCP can't shrink or change disk type in place — requires snapshot → create new disk → swap boot disk.

### Q2: Do we need the external IP when using Tailscale?
- **Inbound (reaching the VM):** No — Tailscale (`100.124.88.29`) covers that without a public IP.
- **Outbound (VM → internet):** The external IP is *also* the egress path (`ONE_TO_ONE_NAT`). Remove it and the VM loses internet access, which **breaks the remote-control daemon**, git, npm, etc.
- Replacing egress without a per-VM external IP means **Cloud NAT** (~$0.044/hr + data — *more* expensive) or a **Tailscale exit node** (needs a second always-on node, adds latency).
- The ephemeral IP is only ~$0.004/hr ≈ **~17 SEK/mo** at current usage, free while stopped.
- **Verdict: keep the ephemeral IP.** Tailscale replaces the need for a public IP for *access*, but not for the VM's *outbound* connectivity.

## Levers to actually fit ~50 SEK/month (ranked by impact)

1. **e2-small → e2-micro** — halves compute rate, ~**36 SEK/mo saved**. Risk: 1 GB RAM vs 1.2 GB currently used → needs a swapfile, accept OOM risk / slowness. Biggest single lever.
2. **Fewer runtime hours** — each hour/day trimmed ≈ ~6.5 SEK/mo. E.g. 13.5 → 8 h/day ≈ ~35 SEK/mo saved.
3. **Disk → 20 GB pd-standard** — ~23 SEK/mo saved (or ~11 SEK just shrinking pd-balanced).

Stacking e2-micro + 20 GB HDD + shorter days makes 50 SEK realistic. Keeping current comfort ≈ ~100–120 SEK/mo → just raise the budget instead.

## Caveats worth remembering
- A GCP **budget is an alert, not a hard cap** — hitting 50 SEK doesn't stop the VM or the charges; spend keeps accruing. A true cap needs a budget-triggered Cloud Function that stops the VM.
- e2-micro **free tier** applies only in us-west1/us-central1/us-east1 — **not** europe-north1, so no free-tier relief here.
- This VM's service account lacks Compute API scopes, so resource enumeration / disk changes must be done from Cloud Console or an account with proper scopes, not from inside the VM.

## Not yet done (open follow-ups)
- Exact `gcloud` steps for the snapshot → pd-standard disk swap
- e2-micro resize procedure + swapfile setup
