# IronFlame V2 — Active Status

**Branch:** `song/ironflame-20260905-0216`  
**Started:** 2026-09-05  
**Canonical runtime source:** `main@e6ba077cabeed8e799090d3d505d82bc96d2fd02`

## Current state

Production has started using the new generative-engine roadmap and FX V2 system.

Completed:

- three supplied reference videos fully decomposed to native frames (145 each / 435 total);
- 12-frame contact-sheet extraction for each reference;
- hard visual-style lock written in `V2_REFERENCE_STYLE_LOCK.md`;
- 12-shot lyric/hero structure written in `V2_HERO_SHOT_MAP.md`;
- V2 roadmap written in `V2_PRODUCTION_ROADMAP.md`;
- full song analyzed at native production 24 fps using the canonical reactive-control algorithm;
- 5,873 frame-aligned control records generated;
- control summary preserved under `assets/analysis/v2_control_summary_24fps.json`;
- first REF-A wide hero produced strictly from an extracted source frame, using source-derived side expansion only;
- authored depth map created for that hero;
- repo `streaming_living_parallax` implementation reproduced from `main@e6ba077c` and proof-tested at low amplitude;
- first proof was rejected as too subtle by temporal delta check;
- second proof increased motion slightly and passed the local visible-motion threshold without adding unrelated effects.

## Durable production files

Library root: `/AIVideoEdit/IronFlame_V2_20260905/`

- full 24 fps reactive controls: `/AIVideoEdit/IronFlame_V2_20260905/ironflame_controls_24fps.json`
  - Library ID: `libfile_bfe938e7a17881918c3bdf4f9fbadb66`
  - SHA-256: `70a94ccb4d0239af7ab8748c876566ccc6a9f7a4b02af496bddaf5b0bd343594`
- Shot 01 wide hero: `/AIVideoEdit/IronFlame_V2_20260905/shot01_refA/shot01_refA_hero_wide_source_preserved.png`
  - Library ID: `libfile_bdc918f8be5081918e20a69e4e228390`
- Shot 01 authored depth: `/AIVideoEdit/IronFlame_V2_20260905/shot01_refA/shot01_refA_authored_depth.png`
  - Library ID: `libfile_1e25fcdbe81481918050e65354894a19`
- Shot 01 4-second proof with song audio: `/AIVideoEdit/IronFlame_V2_20260905/shot01_refA/shot01_refA_proof_v2_with_audio.mp4`
  - Library ID: `libfile_0450a784e5f48191b8b3283bf042b231`

## Shot 01 proof result

- duration: 4.0 s
- 24 fps / 96 frames
- depth mode: provided authored depth map
- mean temporal delta: 0.0005010
- max temporal delta: 0.0011847
- minimum frame mean luma: 41.13
- black frames: none detected
- decision: **KEEP AS MOTION PROOF**, not yet a final shot package.

The motion is deliberately small because the supplied references move through internal flow, glow, rings and controlled deformation rather than large camera motion.

## Next production actions

1. Build REF-C Shot 03 hero package and ring/ribbon proof using the same control bus.
2. Build REF-B Shot 05 hero package and warm-head/palm glow proof.
3. Add palette-aware compositor adapters described in Phase 2 of `general/reusable/generative-engine/PLAN.md` when needed, keeping them song-specific until proof/QC.
4. Create side-by-side source-reference proof sheets before promoting any generated/expanded hero.
5. Continue checkpointing every accepted/rejected proof here and in the manifest.