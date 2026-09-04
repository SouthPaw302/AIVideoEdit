# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: living-asset build / effect-laboratory proofing. **No full-movie assembly yet.**

Source:

- `Brandi South Florida 2017.mp4`
- 1280x720 container / 720x1280 displayed portrait orientation
- 30 fps
- 31.766344 s
- 953 source frames

Native-cadence extraction exists in the active runtime:

- `frame_000001.png` through `frame_000953.png`
- `FRAME_MANIFEST.csv`
- working path: `/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

## Governing rule

Do not assemble the final Irish Eyes film until multiple distinct moving assets have passed the Magic Gate and the source-derived visual language is proven repeatable.

Real footage / real frames remain the identity and reality anchor. Generated material may support transitions, environment extensions, surreal memory material, textures and missing visual beats, but failed drifted generations must be rejected. All effects must survive rendered QC.

## Current Magic Gate library

### P02 Reflection Portal V3

**KEEP — provisional Magic Gate pass.**

The corrected portal route hands off to source-derived water before the dive becomes close enough to stretch Brandi. The camera destination is water/reflection rather than her body.

### P04 Spatial Entry V2

**KEEP — provisional Magic Gate pass.**

Real frames 451–530. Brandi naturally clears left while sky, far water and near water move at different rates and the virtual camera enters the real waterfront.

SHA-256: `c5f32d69e01c08bb2f71ac1ca7933e6e99da0685b2af3b05f4d11935063416c2`

### P05 Still Here / Time Dilation V2

**KEEP — provisional quiet-magic pass.**

Closing-family treatment: retained real motion, protected shadow recovery, independent water/sky movement, restrained depth breathing and warm rim light without spectacle.

### P06 Opening Arrival V1

**KEEP — reality anchor.**

Real frames 40–160. Modest optical approach, independent water, motivated Gaussian-shaped light fields, warm water glint, restrained halation/prism and finishing.

- 4.033333 s
- 121 frames
- 0 black frames
- mean frame delta 2.510968689718364
- SHA-256 `e61470fc2aff67ade3a53789f2a926147da52fe22843ef53d7d20ba9c9683f08`

### P07 Hair Memory V2

**KEEP — provisional Magic Gate pass.**

Real frames 360–445 retimed to 4.0 s. Uses actual hair/dress motion plus short real temporal history, face-protected motion echoes, localized prism, independent water, motivated sun shafts, luminous hair wake, halation and a restrained off-axis push.

- 4.0 s
- 120 frames
- 0 black frames
- mean frame delta 6.816052888169156
- SHA-256 `67d067c4bb585c3316c0085b1093e7278255d21ed5d370a9a31ea22772723ef3`

### T01 Sun / Water Memory Gate V1

**KEEP — provisional transition pass.**

Connects P06 into P07 without a prolonged full-body dissolve. Background morphs under a motivated upper-right sun flare and lower-frame water refraction; the subject switch happens at the flare peak rather than as a long double exposure.

- 3.3 s
- 99 frames
- 0 black frames
- mean frame delta `3.392242580191799`
- SHA-256 `35f9851d663f2fcfe8fa265a6a0ec2f30ad41b310a60ff1ac7c1bb1daed58d0f`

### P08 Return Human Anchor

V1: **REVISE** — subject too dark.

V2: **REVISE** — stronger depth differential, but cutout-derived blend produced soft contamination near lower-left edge.

V3 rendered technically clean:

- 4.0 s
- 120 frames
- 0 black frames
- mean frame delta 1.5297097849556494
- SHA-256 `5ca6cccfe4ca7a896ce606f45a590828dd2459fa1aa1b489ed42b2c2a692dde0`

**Status: QC HOLD — not promoted until final visual inspection passes.**

## P09 Memory Clone Refraction

V1, V2 and V3 have all been rendered and QC'd.

- V1 SHA-256 `954cc39c243fb33b96b5ec7149cf64a5b615594e0629ce2ca0deac35d34747ef`
- V2 SHA-256 `8cfd9acf0892013c7a8d6a8dd2bf91deb47117033f28be85dd21dd27d444613c`
- V3 SHA-256 `8dd8e3d0b89078a8fc9a55936377eac181e2e181da9d81d9ad80d1aa062c1469`

**Decision: DO NOT PROMOTE.**

The experiment moved from a floating translucent clone to water-constrained refraction, but even V3 still reads too much like an apparition/shadow rather than premium scene-native water memory. Preserve the lesson, not the asset.

## P10 Eyes Within / Sunglasses Portal

V1 rendered and QC'd:

- 5.2 s
- 156 frames
- 0 black frames
- mean frame delta `3.3174941942951017`
- SHA-256 `276ae8c747b7f5879d904b3dfc1e49a6f971c9fe63b969fc0d16f53a08cd06f7`

Concept: real South Florida water/sky appears inside Brandi's sunglasses and the camera pushes into a lens until that real source-derived waterfront becomes the whole frame.

**Decision: REVISE / STRONG CONCEPT.**

The perception move and water destination work, but the reflection treatment appears too early/broadly across the face. V2 recipe is locked: tighter two-lens geometry, near-zero reflection in the first ~18% of the shot, then a controlled ramp as the lens push commits. Keep the source-water portal ending.

See `MAGIC_GATE_BATCH_03.md`.

## Storm family status

P03 V1/V2/V3/V4 remain rejected from the moving-asset library. Preserve the ideas, not the current renders.

## Literal 3D Gaussian Splatting decision

A source-camera/parallax viability test has been run. See `3DGS_VIABILITY_2026-09-04.md`.

The most stable background pairs are explained very well by a planar/global transform with roughly 1–2 px residual at proof resolution. This clip is dominated by distant sky/water/horizon and does not currently provide strong evidence of the multi-view camera baseline needed to justify a real 3DGS training pass.

**Decision: do not force/train literal 3DGS from this clip right now.**

Continue with source-derived depth/perception methods. Reserve actual 3DGS for footage with deliberate real camera translation or additional multiview capture. Gaussian-shaped light fields remain available but must not be mislabeled 3DGS.

## Current accepted language

The project now has several distinct successful families rather than one repeated trick:

- reality-anchor enhancement;
- real spatial entry into the waterfront;
- reflection/water portal;
- hair/memory temporal trails;
- quiet time-dilation / depth breathing;
- source-derived water / light / halation / prism behavior;
- a motivated reality-to-memory optical transition.

This is enough to continue expanding the moving-asset library, but **not yet permission to render the final 3:07 film**.

## Exact next action

1. render and QC P10 V2 with tightened/delayed lens reflection;
2. complete visual QC on P08 V3 and either KEEP or REVISE;
3. build a second return-to-reality transition family from an approved Magic Gate shot;
4. begin coverage mapping against the lyric-film map only after the moving-asset library has enough variety to avoid repetition;
5. still do not assemble the final master until asset coverage and magic level are verified.
