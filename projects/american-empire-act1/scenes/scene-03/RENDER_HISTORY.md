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

## Assembly02

Rendered `Scene03_ASSEMBLY02_ANGLE_FX_CAPTIONS.mp4`.

- SHA-256: `3baa68d24c02e985f9c1c67396cec7ce8f9d1fc1940374837886e5402868efa5`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- canon captions burned in
- continuous score
- exact script shot frame counts preserved

Assembly02 supersedes Assembly01 as the active technical candidate. Final artistic/master acceptance remains pending.
