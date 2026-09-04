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

This is intentionally less surreal so the movie retains photographic truth.

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

See `MAGIC_GATE_BATCH_03.md`.

### P08 Return Human Anchor

V1: **REVISE** — subject too dark.

V2: **REVISE** — stronger depth differential, but cutout-derived blend produced soft contamination near lower-left edge.

V3 rendered technically clean:

- 4.0 s
- 120 frames
- 0 black frames
- mean frame delta 1.5297097849556494
- SHA-256 `5ca6cccfe4ca7a896ce606f45a590828dd2459fa1aa1b489ed42b2c2a692dde0`

V3 replaces the hard cutout with broad feathered subject/face fields, stronger backlight recovery, separate subject/background depth breathing, independent water, motivated sun volume and rim light.

**Status: QC HOLD — not promoted until final visual inspection passes.**

See `MAGIC_GATE_BATCH_02.md`.

## Storm family status

P03 V1/V2 remain rejected from the moving-asset library.

P03 V3:

- source-coupled cloud/water/light treatment;
- 4.333333 s / 130 frames / 0 black frames;
- SHA-256 `7e5e776c04ac5d7da9f7cd031ddb8103b62a20a29c49bac046424c5c31321bb2`;
- **REVISE** — stronger cinematic integration but still not a distinct high-magic event.

P03 V4 Temporal Glass:

- environment-only nearby-time panes around protected real Brandi;
- 4.333333 s / 130 frames / 0 black frames;
- SHA-256 `405481840eb5056428e2c0c8ecd4d4f1149be130b11f3875c96871d4a5f5f2a4`;
- **REVISE / DO NOT PROMOTE** — original idea, but glass lines are too graphic and the backlit face still lacks enough recovery.

See `MAGIC_GATE_BATCH_03.md`.

## Earlier revisions still rejected

- P01 Breeze Memory V3 — too much animated-photograph feel;
- P03 Storm Revelation V1/V2/V3/V4 — not yet good enough for the movie;
- P02 earlier portal versions — camera landed on/stretched subject rather than entering water;
- two generative clean-plate attempts — changed person/location and were rejected from production.

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

1. complete `IE_P09_MEMORY_CLONE_REFRACTION` using the real frame-420 subject alpha and source-derived background/water; duplicates must read as refracted memory, not literal extra people;
2. complete visual QC on P08 V3 and either KEEP or REVISE;
3. preserve P03 V4's temporal-fracture concept for later adaptation, but do not reuse the current vertical glass-line treatment;
4. build another transition family connecting a Magic Gate shot back into photographic reality;
5. begin coverage mapping against the lyric-film map only after the moving-asset library has enough variety to avoid repetition;
6. still do not assemble the final master until asset coverage and magic level are verified.