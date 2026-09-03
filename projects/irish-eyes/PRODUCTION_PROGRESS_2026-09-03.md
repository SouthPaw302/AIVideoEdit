# Irish Eyes — Moving-Footage Production Progress

Date: 2026-09-03

No additional storyboard/concept assets are being produced. Work is advancing only through actual movie shots, effects, transitions, and sequence renders.

## Rendered production assets

### Approved 2.5D shots

- `shot_25d_001_arrival.mp4` — 6 s, real source frame 00100, depth-differential push
  - SHA-256 `4a710d21fbc8ac8a7bf7eaefd9fa0fe1852e77b6ee4705eb41e01e5cfb34eaee`
- `shot_25d_002_hair_water.mp4` — 6 s, real source frame 00600, lateral depth drift
  - SHA-256 `eef5280b68494150a7acbb0ee1176fca5789cd0d0a89d48a6b7bcdee197d9f0d`
- `shot_25d_003_horizon.mp4` — 6 s, real source frame 00850, shallow orbit
  - SHA-256 `3fb2744ceac299d277aaeb4c8bc57e4cb1caf45223a0e7c85634ca40d80763c7`

### Real-motion loops

The first cross-blended loop prototype was rejected after sequence QC exposed visible double-image ghosting at the seam. It is not approved for the final movie.

Replacement loops use real frame windows whose endpoints were independently searched for low visual difference, avoiding long cross-dissolves:

- `loop_real_v2_001_smile_breeze.mp4`
  - source frames 00060–00104
  - 45-frame natural-motion cycle
  - SHA-256 `457f5caeddd39a43af5f0c0e386ffd79304939aa4249b170059d22ded2e65ad9`
- `loop_real_v2_002_smile_horizon.mp4`
  - source frames 00255–00299
  - 45-frame natural-motion cycle
  - SHA-256 `2be87ef24728d0f72a09193e8c56159ffce29926efe8a84806a1ef5244acc0b1`

### Dream / reflection transition

Earlier full-body dissolve versions were rejected for visible double-image ghosting.

Current approved direction:

- `transition_sun_water_gate_v3.mp4`
- 4 s
- uses real source frames 00600 -> 00850
- water-region ripple + highlight bloom + warm sun wash
- subject change happens under a flare gate instead of a prolonged identity dissolve
- SHA-256 `e364ca30da6bd310f5ed9e0ea2e4dde5bb2de76ea16e7220db8cc5fed98d37c2`

## Actual Act I WIP render

`IRISH_EYES_ACT1_WIP_v2_30s.mp4`

- duration: 30 s
- portrait 720×1280 / 30 fps
- includes the actual remastered song audio from 00:00
- uses restored real footage + clean real-motion loop + approved 2.5D + sun/water transition + hair/water depth shot
- SHA-256 `4cd0eea2855be5c8bdc4c0a51bbfc87a3091cc555ad0873461a37c30f5bc2028`
- workspace size: approximately 14 MB

This is a production WIP sequence, not a storyboard or preview concept.

## QC lesson retained

A frame can look acceptable while a motion sequence still fails. All loop/transition effects must therefore be reviewed across the seam and around transition centers, not only by representative still frames.

## Next moving-footage work

1. extend Act I toward the first measured musical boundary at ~00:57.59;
2. create independent water/cloud motion layered onto selected 2.5D shots;
3. build additional source-derived close portrait and hair-motion shots;
4. create the first photoreal non-source narrative insert only when it is intended for final timeline use;
5. begin Act II memory-world footage after Act I has enough visual diversity.