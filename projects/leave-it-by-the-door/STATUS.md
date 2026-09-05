# Leave It by the Door — Status

**Updated:** 2026-09-05 UTC  
**Branch:** `song/leave-it-by-the-door`  
**State:** Native-24 V2 accepted as picture baseline; V3 YouTube refinement active

## V2 baseline

Canonical V2 master:
`Leave_It_By_The_Door_NATIVE24_FULL_V2_720p24.mp4`

Properties:
- 198.833333 s
- 1280×720
- true 24 fps
- 4,772 individually rendered frames
- H.264 ~7.23 Mbps
- AAC stereo 48 kHz ~320 kbps
- ~187.9 MB
- SHA-256: `c82bdb31e7610c7de8d3da506940ebfade5fa6fa1a5af6d6d2ae6e2c4c43c05e`

V2 retired the rejected 10 fps intermediate workflow. It measured ~62% more adjacent-frame motion than V1.1 and had zero near-exact duplicate frame pairs in the direct scan.

User response to V2: **better / awesome** and keep it as the base.

## Current user direction for V3

The final YouTube pass should:
- keep V2's successful native-24 picture language;
- reduce the visible shaking/global camera wobble;
- add more believable internal loops;
- strengthen animated fires, candles, embers, smoke, rain, water and reflections;
- feel like premium long-form dynamic animated imagery on YouTube rather than obvious AI video;
- keep characters/anatomy/painterly identity stable;
- add intro and outro;
- deliver the final upload file wrapped in a ZIP.

## Canonical FX V2 now integrated

The repository-wide centralized FX runtime is now available directly on this song branch at:
`general/reusable/fx_v2/`

This runtime consolidates effect implementations/lineage from Silver Coin, Irish Eyes, IronFlame and Leave It by the Door behind stable IDs.

Selected approved V3 effects are recorded in:
`projects/leave-it-by-the-door/V3_FX_MANIFEST.json`

Current approved core includes localized living flow, water flow, advected smoke, rain plane, living flame, embers, practical-light breath, moving light field and temporal canvas lock.

Transitions that remain `proof_required` are not allowed into the V3 FX manifest merely because code exists.

## Spatial / Gaussian-splat rule

True 3D Gaussian Splatting is now explicitly separated from 2D Gaussian masks, glow fields and 2.5D depth/parallax effects.

Canonical workflow:
`general/reusable/fx_v2/SPATIAL_3DGS_SUPERSPLAT.md`

SuperSplat is the preferred open-source inspection/editing layer when genuine splat geometry exists. Current Leave It hero paintings remain Tier 1/2 living-painting assets unless valid multi-view or reconstructed 3DGS geometry is produced. Do not label ordinary 2D Gaussian effects as 3DGS.

## Hard precompile gate

Before V3 final compile/render, run:
`general/reusable/fx_v2/precompile_gate.py`

The gate fails closed if an effect is only a registry placeholder, not wired into runtime code, contains placeholder/TODO/no-op logic, lacks approved rendered proof/QC, fails pixel-change/temporal tests, or violates effect-specific quality limits.

`V3_FX_LOCK.json` currently records PASS for all nine requested V3 effects. The lock must still verify immediately before final compile so code/config changes cannot silently alter the render after approval.

## V3 implementation checkpoint

Executable refinement renderer committed:
`scripts/render_v3_refinement.py`

It consumes the accepted 25 native-24 V2 shot masters as source plates, damps high-frequency whole-frame translation, then layers canonical approved FX by scene family. It creates both an artistic song master and a separate YouTube version with intro/outro.

A Library restore showed that the persistent V2 ZIP contains the final master but not the 25 intermediate shot files. The final V2 master was therefore scanned directly. The 24 strongest true visual joins recover the original 25-shot architecture exactly.

Canonical recovered cut-frame map at 24 fps:
`[153,305,478,645,813,906,1162,1385,1608,1840,2039,2269,2518,2762,2947,3127,3291,3480,3660,3876,4107,4328,4438,4649]`

Recovery utility committed:
`scripts/recover_v2_shots_from_master.py`

It validates the accepted V2 fingerprint (24 fps / 4,772 frames), recreates frame-accurate CRF16 source plates and writes `RECOVERY_MAP.json`. This makes the final V2 master sufficient to resume V3 even when the original shot directory is gone.

Sandbox proof status:
- 2-second V3 proof rendered successfully;
- 1280×720;
- true 24 fps;
- 48 frames;
- character/identity remained visually stable in the inspected proof frame;
- rain/water/light motion was added without introducing a new default camera zoom.

## Current production files

Read in this order:
1. `AGENT_HANDOFF.md`
2. `STATUS.md`
3. `V3_REFINEMENT_PLAN.md`
4. `V3_FX_MANIFEST.json`
5. `V3_FX_LOCK.json`
6. `scripts/recover_v2_shots_from_master.py`
7. `scripts/render_v3_refinement.py`
8. `EFFECTS_PLAN.md`
9. `REFERENCE_MOTION_TARGETS.md`
10. `FULL_V2_QC.json`
11. `general/reusable/fx_v2/SPATIAL_3DGS_SUPERSPLAT.md`

## Next production action

Recover the 25 V2 source plates from the Library master, verify the FX lock immediately before compile, run the V3 refinement shot-by-shot/resumably, inspect representative storm/hearth/celebration/dawn proofs, then complete full QC, artistic master, YouTube intro/outro master and final ZIP delivery.

## Storage

GitHub is the persistent control/source-of-truth layer for code, manifests, status, effect locks and QC metadata. Large media masters remain in the active workspace/Library or approved object storage, with hashes/recovery locations recorded here when created.
