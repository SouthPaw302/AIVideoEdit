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

A passing run creates `V3_FX_LOCK.json`; that lock must verify immediately before final compile so code/config changes cannot silently alter the render after approval.

The same gate is enforced in GitHub Actions with both a positive approved-core test and a negative test that deliberately requests an unapproved effect and requires rejection.

## Current production files

Read in this order:
1. `AGENT_HANDOFF.md`
2. `V3_REFINEMENT_PLAN.md`
3. `V3_FX_MANIFEST.json`
4. `EFFECTS_PLAN.md`
5. `REFERENCE_MOTION_TARGETS.md`
6. `FULL_V2_QC.json`
7. `scripts/render_full_native24_v2.py`
8. `../../general/reusable/fx_v2/SPATIAL_3DGS_SUPERSPLAT.md`

## Next production action

Build the V3 refinement renderer from the V2 shot architecture, using canonical FX V2 calls and lower camera amplitude. Render resumably at true 24 fps, add intro/outro, run full QC, save the YouTube master, and wrap final delivery in a ZIP.

## Storage

GitHub is the persistent control/source-of-truth layer for code, manifests, status, effect locks and QC metadata. Large media masters remain in the active workspace/Library or approved object storage, with hashes/recovery locations recorded here when created.
