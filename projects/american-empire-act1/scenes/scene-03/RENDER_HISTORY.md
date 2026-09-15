# Scene 03 Render History

## 2026-09-15 — Pre-production and score lock

- Locked `L'Atmosphère.wav` to 98.000 editorial seconds / 2352 frames at 24 fps.
- Locked storyboard, script and canon caption timing.
- Preserved Scene 02 terminal frame as Scene 03 continuity anchor.

## 2026-09-15 — Hero and Assembly01 pass

- Generated eight Scene 03 hero plates and received explicit user approval of the hero imagery.
- Built initial localized diegetic FX loops.
- Rendered `Scene03_ASSEMBLY01_HERO_FX_CAPTIONS.mp4`.
- Assembly01 was technically valid but its loop manifest correctly recorded `camera_motion:none`.

## 2026-09-15 — User-directed matched-angle correction

The user required copies of each hero with slightly different angles for movement. Rather than generatively redraw the approved heroes, the correction uses deterministic source-locked projection:

- hero A: `-0.85°` Y-axis micro-yaw
- hero B: `+0.85°` Y-axis micro-yaw
- 1.025x overscan / 1700 px focal model
- existing localized FX retained before viewpoint projection
- no identity or environment regeneration

Created eight matched-angle pairs and eight corrected GIF loops.

## Assembly02 — approved pre-production basis

Rendered `Scene03_ASSEMBLY02_ANGLE_FX_CAPTIONS.mp4`.

- SHA-256: `3baa68d24c02e985f9c1c67396cec7ce8f9d1fc1940374837886e5402868efa5`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- canon captions burned in
- continuous score
- exact script shot frame counts preserved

The current user accepted Assembly02 as good pre-production: the feel, character continuation and city design are the foundation for further work. It is not the final master because production/debug annotations remain visible and several scripted effects/actions are incomplete.

## Assembly03 — effects-completion proof

Built directly from Assembly02 using the same eight shot spans. The render was performed shot-by-shot/resumably and reassembled to the exact original timing.

Added or strengthened:
- coherent exterior/window rain response
- wet-road/reflection movement
- corridor/access-light progression
- elevator route/indicator progression
- lobby access/exit state progression
- traffic signal synchronization and restrained vehicle-light flow
- municipal/public-display state progression
- continuing coordinated city state in the closing shot

`Scene03_ASSEMBLY03_EFFECTS_PROOF.mp4`

- SHA-256: `77e2ea51c3ea22ed3c1b3dab4c46a64d9f99ae71bf301fd25bfa866246584438`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- continuous Assembly02 audio/caption track
- Drive ID: `1sNbipscEqAKSoCQX_FpljMKsrc7mlbXI`

Assembly03 is retained as the effects rollback reference.

## Assembly04 — artifact-clean effects review

Built directly from Assembly03, preserving its successful effect behavior and exact edit timing while suppressing production/debug corner-note contamination. No shot was reordered, retimed or compositionally redesigned.

`Scene03_ASSEMBLY04_CLEAN_ACTION_PASS.mp4`

- SHA-256: `07bccc75f5e54b6b89b0142c90c3d7224cd976d2a91afce1030997f9219a5bb7`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- existing score/caption track preserved
- Drive ID: `1udCJWNJMpK2oSdSir6Qfwmcndzx6p9Og`

QC spot comparison against Assembly03 shows changes concentrated in the production-note edge regions with negligible central-composition drift. Assembly04 is a review candidate only; Assembly02 remains the approved pre-production basis until a later candidate is explicitly accepted.