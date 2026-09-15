# Scene 03 QC Record

## Current technical candidate

`Scene03_ASSEMBLY02_ANGLE_FX_CAPTIONS.mp4`

- SHA-256: `3baa68d24c02e985f9c1c67396cec7ce8f9d1fc1940374837886e5402868efa5`
- duration: `98.000 s`
- frame rate: `24 fps`
- total frames: `2352`
- resolution: `1280x720`
- score: continuous `L'Atmosphère.wav` editorial range `0–98 s`
- dialogue/captions: nine canon Daniel/Claire lower-third events

## Picture / movement QC

- Eight approved hero plates are retained without generative redraw.
- Each hero has a deterministic matched-angle A/B pair at `-0.85°` and `+0.85°` Y-axis micro-yaw.
- 1.025x overscan plus reflected edge padding prevents synthetic black edge gaps.
- Existing localized rain/reflection/haze/practical/access/elevator/display/traffic-state FX are retained inside the angle loops.
- No translation wobble, fake handheld, orbit, lens jump, zoom pumping, identity redraw, or topology mutation is introduced.

## Timing QC

Locked shot frame counts are `192 / 168 / 360 / 456 / 408 / 288 / 264 / 216`. They total exactly `2352` frames with no gaps or overlaps.

## Gate status

- hero-set creative approval: `PASS` by current user
- matched-angle technical QC: `PASS`
- project-local FX lock: pending exact GitHub commit verification
- exact branch Production Contract: pending exact GitHub commit verification
- final artistic/master acceptance: `PENDING`

Assembly02 may advance to `FINAL_QC` after the exact branch checks pass. It is not yet the accepted Scene 03 master.
