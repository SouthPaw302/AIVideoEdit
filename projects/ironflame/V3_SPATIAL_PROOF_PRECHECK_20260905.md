# IronFlame V3 — Spatial Proof Precheck + Recovery Proof (2026-09-05)

## Scope

This checkpoint records the preconditions and first successful **provided-depth** IronFlame spatial/model proof. It does **not** promote any spatial system to production-approved status and does **not** authorize final assembly.

## Verified repo state

- Working branch: `song/ironflame-20260905-0216`
- The branch contains the IronFlame V3 project/audit material, but does not itself contain the current `general/reusable/generative-engine/spatial/living_parallax.py` implementation.
- The canonical implementation exists on `main` at `general/reusable/generative-engine/spatial/living_parallax.py`.
- Verified implementation Git blob SHA: `541c8d53847edeffec8a69b1bf807fd0bcfe793e`.
- The renderer distinguishes `provided_depth_map` from `synthetic_radial_fallback`; only the former is acceptable for this recovery proof.

## Registry state

`general/reusable/generative-engine/registry_entries.json` lists:

- ID: `DF-25D-001`
- Name: `Streaming continuous soft-depth living parallax`
- Category: `spatial`
- Status: `experimental`
- Implementation: `spatial/living_parallax.py`
- Note: real depth preferred; synthetic radial depth is fallback/proof mode only.

A successful real-depth proof is therefore evidence for promotion/review, **not** automatic production approval.

## Runtime recovery note

The original `/mnt/data/ironflame_v3/` sandbox did not survive into the new runtime. Library recovery found the verified FX2 proof videos for shots 01–04, but not the original V3 hero PNG source plates. The new spatial pass therefore uses frames recovered from those verified proof videos and labels them explicitly as **recovered proof-frame sources**. They are not represented as original hero plates.

This is sufficient to verify the canonical real-depth model path and visual behavior, but it is not sufficient to mark a production shot package approved.

## Canonical renderer verification

Before rendering, the recovered local renderer copy was checked with Git's blob hash and matched the canonical implementation exactly:

`541c8d53847edeffec8a69b1bf807fd0bcfe793e`

All four executions returned:

`depth_mode=provided_depth_map`

Parameters used for each proof:

- frames: 96
- fps: 24
- duration: 4.0 s
- amplitude: 0.72
- strength: 0.026
- codec path: canonical renderer -> FFmpeg `libx264`, `yuv420p`, CRF 18

## Authored depth strategy

Four composition-specific grayscale maps were authored from the inspected recovered proof frames rather than using the synthetic radial fallback:

- Shot 01: foreground woman / near orb / looming face / ribbon depth separation.
- Shot 02: foreground woman / near luminous spirit / contact point / background field separation.
- Shot 03: foreground small woman / giant crystalline face / near eye-core / ribbon planes.
- Shot 04: foreground small woman / giant crystalline head / halo / multiple ribbon planes.

Depth boundaries were intentionally softened to reduce cardboard-cutout motion.

## Proof metrics

| Shot | Adjacent delta mean | Adjacent p95 | Black frames | Longest freeze proxy | Video SHA-256 | Depth SHA-256 |
|---|---:|---:|---:|---:|---|---|
| 01 | 0.382260 | 0.597669 | 0 | 0 frames | `78a025fedb09e984c096bd525c6cc3d72476e50f303c59226e5ea142a780e6ef` | `0d51392b0e7a11846dc1e4dbfa02dc42287e1034e3b325951ec54bb66deed981` |
| 02 | 0.395702 | 0.604445 | 0 | 0 frames | `18726afe996cdf228b76d01aa1e31cd0d845205f4e99b04bbaf8c6b7697182e8` | `ff05b61e33b778f6c540cb149bc09f2743784e8b92b995b9f42ae746025d2d77` |
| 03 | 0.345420 | 0.524869 | 0 | 0 frames | `ba40f29b980aa33a6e3637f1109c8cd679fc1bfa56fccab8788c2f62fc075125` | `dd09d78b7def16ead6979e17f3de04f85e39a45c836542796423d81867fbb1fd` |
| 04 | 0.355609 | 0.572485 | 0 | 0 frames | `4cb7dc16db46b0e2c723b63f30b989dceea90f0c461c57fd2e95502ac89ed5dc` | `4662ccdd2c7739265c59f5e564acf4570156e3d4c673075fda9c4a19c3318993` |

All four retained measurable temporal motion with no detected black frames and no freeze-proxy runs.

## Human visual review

Decision for shots 01–04: **KEEP AS CANONICAL REAL-DEPTH MODEL PROOFS / NOT PRODUCTION SHOT APPROVAL**.

Observed sampled behavior:

- silhouettes remain intact;
- large face geometry remains readable;
- contact/orb highlights retain visual hierarchy;
- depth movement is restrained at the chosen strength and does not dominate the FX2 language;
- no sampled frame showed portal/gate drift;
- no sampled frame showed obvious identity tearing.

Remaining limitation: these depth maps were authored against recovered FX2 proof frames, not original source hero plates. Before production use, repeat the strongest mappings against the original hero plates if/when those assets are recovered.

## Durable proof package

Library:

`/AIVideoEdit/IronFlame_V3_20260905/verified_models/provided_depth_recovery_pass/`

Contains:

- four `shot##_provided_depth.mp4` canonical proof renders;
- four `shot##_authored_depth.png` maps;
- `SPATIAL_QC_METRICS.json`;
- `SPATIAL_PROOF_CONTACT.png`.

## Fail-closed decision

`DF-25D-001` remains **experimental** in the registry. Do **not** add it to the IronFlame production FX requirements/lock as an approved production dependency solely because this recovery proof passed. The proof establishes that the actual canonical renderer works with real supplied depth and produces useful IronFlame spatial motion.

## Next action

1. Check selected transition IDs and current registry/proof status.
2. Re-review the chosen short transition set, including the corrected 04→05 boundary.
3. Build the unified KEEP / REVISE / REJECT artistic grammar for verified shots + transitions.
4. Only after sufficient acceptance, draft `projects/ironflame/FX_REQUIREMENTS.fx.json` and run the fail-closed precompile gate.
5. No final assembly yet.
