# IronFlame V3 — Spatial Proof Precheck (2026-09-05)

## Scope

This checkpoint records the preconditions for the next IronFlame spatial/model proof. It does **not** promote any spatial system to production-approved status and does **not** authorize final assembly.

## Verified repo state

- Working branch: `song/ironflame-20260905-0216`
- The branch contains the IronFlame V3 project/audit material, but does not itself contain the current `general/reusable/generative-engine/spatial/living_parallax.py` implementation.
- The canonical implementation currently exists on `main` at:
  - `general/reusable/generative-engine/spatial/living_parallax.py`
- Implementation SHA on `main`: `541c8d53847edeffec8a69b1bf807fd0bcfe793e`

## Provenance finding

The canonical renderer has two explicit depth modes:

- `provided_depth_map` — real supplied depth image
- `synthetic_radial_fallback` — fallback/proof-only synthetic radial depth

A spatial proof intended to graduate beyond fallback must therefore provide an authored depth map and must record `depth_mode=provided_depth_map` in the execution evidence.

## Registry state

`general/reusable/generative-engine/registry_entries.json` on `main` lists:

- ID: `DF-25D-001`
- Name: `Streaming continuous soft-depth living parallax`
- Category: `spatial`
- Status: `experimental`
- Implementation: `spatial/living_parallax.py`
- Note: real depth preferred; synthetic radial depth is fallback/proof mode only.

Therefore, a successful real-depth IronFlame proof is evidence for promotion/review, **not** automatic production approval.

## Candidate IronFlame source stills already registered

The branch asset manifest registers 12 production stills. Strong candidates for the first authored-depth pass are:

1. `assets/stills/08-hallway-without-end.jpg` — long hallway geometry is useful for foreground/midground/background separation.
2. `assets/stills/09-underground-reflection.jpg` — useful for restrained reconnection/identity depth.
3. `assets/stills/11-morning-enters.jpg` — useful for quiet-resolution spatial motion.
4. A character-led hero from the newer V3 verified shot-state set if available locally, because the current V3 story grammar supersedes the older V2 assembly.

## Required proof package

For each chosen hero:

1. Source image hash.
2. Authored grayscale depth map.
3. Depth-map hash.
4. Exact renderer implementation SHA.
5. Exact command/arguments.
6. Renderer stdout proving `depth_mode=provided_depth_map`.
7. Output MP4 hash.
8. Temporal-motion metrics.
9. Black/freeze QC.
10. Human visual review: KEEP / REVISE / REJECT.

## Fail-closed rule

Do not add `DF-25D-001` to the IronFlame production FX requirements/lock until the real-depth proof is complete and the registry/approval discipline allows it. Do not use an ad-hoc custom parallax substitute to bypass this proof.

## Next action

Recover 2–4 strongest V3 hero images into the active sandbox, author real depth maps, run the canonical `living_parallax.py` implementation from its verified `main` SHA, and record the complete proof package before any production compile.
