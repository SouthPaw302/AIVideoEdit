# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: moving-asset build / Magic Gate proofing / continuity validation. **No final full-film render yet.**

Source:

- `Brandi South Florida 2017.mp4`
- 1280x720 container / 720x1280 displayed portrait orientation
- 30 fps
- 31.766344 s
- 953 extracted source frames

Working extraction:

`/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

## Governing rule

Real footage and real extracted frames remain the identity/reality anchor. Generated material may support surreal transitions or missing visual elements when it genuinely improves the film, but drifted or synthetic-looking results are rejected. Every meaningful effect must survive rendered QC.

Do not render the final 3:07 master until the approved moving-asset language works sequentially and enough coverage exists to avoid repetition.

## Current approved / provisional moving-asset library

### P02 Reflection Portal V3

**KEEP — provisional Magic Gate pass.**

Camera hands off to source-derived water before the dive gets close enough to stretch Brandi.

### P04 Spatial Entry V2

**KEEP — provisional Magic Gate pass.**

Real frames 451–530. Brandi naturally clears left while sky, far water and near water move at different rates; the virtual camera enters the real waterfront.

SHA-256 `c5f32d69e01c08bb2f71ac1ca7933e6e99da0685b2af3b05f4d11935063416c2`

### P05 Still Here / Time Dilation V2

**KEEP — provisional quiet-magic pass.**

Retained real motion, protected shadow recovery, independent water/sky movement, restrained depth breathing and warm rim light.

### P06 Opening Arrival V1

**KEEP — photographic reality anchor.**

Real frames 40–160 with modest optical approach, independent water, motivated Gaussian-shaped light fields, warm water glint, restrained halation/prism and finishing.

- 4.033333 s
- 121 frames
- 0 black frames
- SHA-256 `e61470fc2aff67ade3a53789f2a926147da52fe22843ef53d7d20ba9c9683f08`

### P07 Hair Memory V2

**KEEP — provisional Magic Gate pass.**

Real frames 360–445 retimed to 4.0 s. Actual hair/dress motion plus face-protected short temporal history, localized prism, independent water, motivated sun shafts, luminous hair wake and off-axis push.

- 4.0 s
- 120 frames
- 0 black frames
- SHA-256 `67d067c4bb585c3316c0085b1093e7278255d21ed5d370a9a31ea22772723ef3`

### P08 Return Human Anchor V3

**KEEP — provisional photographic return anchor.**

Visual QC now passed. Earlier lower-left contamination from V2 is gone. V3 uses broad feathered shadow recovery rather than a hard cutout, separate subject/background depth breathing, independent water, motivated sun volume and rim light.

- 4.0 s
- 120 frames
- 0 black frames
- SHA-256 `5ca6cccfe4ca7a896ce606f45a590828dd2459fa1aa1b489ed42b2c2a692dde0`

The shot remains intentionally backlit and will receive final shadow/color refinement in the editorial finishing pass.

### P10 Eyes Within / Sunglasses Portal V4

**KEEP — provisional Magic Gate pass.**

Story role: `Irish eyes / the story within`.

Real Brandi frame 291 remains the identity anchor. A dark, water/horizon-biased source reflection appears only inside the real sunglass geometry; a thin moving horizon/glint cue makes the inner world readable; the camera then commits to the right lens and crosses into real source-derived waterfront from frame 520.

- 5.2 s
- 156 frames
- 0 black frames
- mean frame delta `3.3031936043906813`
- SHA-256 `5e84a025fbac476b16046cc913f7abc1b3515544b0f05147bc6792933bb8305d`

V1/V2/V3 remain revision lineage only. V2 produced bright white-goggle behavior; V3 restored dark glass but the inner-world cue was too subtle.

### T01 Sun / Water Memory Gate V1

**KEEP — provisional reality→memory transition pass.**

Connects P06 into P07 with a motivated sun/reflection gate instead of a long person dissolve.

- 3.3 s
- 99 frames
- 0 black frames
- SHA-256 `35f9851d663f2fcfe8fa265a6a0ec2f30ad41b310a60ff1ac7c1bb1daed58d0f`

### T02 Water / Reality Return V2

**KEEP — provisional magic→reality transition pass.**

Lineage: P10 V4 water-world endpoint → P08 V3 real Brandi return. The identity handoff occurs at a motivated sun/water optical peak; no prolonged double-exposure person.

- 3.3 s
- 99 frames
- 0 black frames
- mean frame delta `2.9471884300595246`
- SHA-256 `79e6d04bb751d542e3cf92291c4a926bb9020cf6bde66336aa82842ac3163434`

## Rejected / preserve lesson only

- P01 Breeze Memory V3 — too much animated-photograph feel;
- P03 Storm Revelation V1/V2/V3/V4 — progressively better but never crossed the current Magic Gate;
- P09 Memory Clone Refraction V1/V2/V3 — literal clone/reflection language kept reading as ghost/apparition rather than premium refraction;
- P02 earlier portal versions — camera landed on/stretched the subject;
- two generated clean-plate attempts — changed person/location and were rejected;
- P10 V2 — lens reflection became glowing white goggles.

See `MAGIC_GATE_BATCH_03.md` and `MAGIC_GATE_BATCH_04.md` for detailed lineage.

## Literal 3D Gaussian Splatting decision

See `3DGS_VIABILITY_2026-09-04.md`.

The stable background in this clip is largely explained by planar/global camera motion with only about 1–2 px residual at proof resolution. This is weak evidence for useful real multiview depth.

**Decision: do not force a true 3DGS training pass from this particular source clip.** Reserve literal Gaussian splatting for footage captured with genuine camera translation/arc/multiview baseline. Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

## Visual language now proven across multiple families

- clean photographic reality anchor;
- real spatial entry into the waterfront;
- water/reflection portal;
- sunglasses/eyes portal;
- hair-memory temporal trails;
- quiet time-dilation/depth breathing;
- source-derived water/light/halation/prism behavior;
- reality→memory and memory→reality optical gates.

## Exact next action

1. build a short continuity reel from approved assets to verify that these families work sequentially and do not feel like disconnected effect demos;
2. QC that reel for repetition, abrupt visual-language changes, exposure/color mismatch and transition logic;
3. use the lyric-film map to identify uncovered story durations/visual families after continuity QC;
4. build additional approved moving assets for those gaps;
5. only after coverage is sufficient should full-song rough assembly begin;
6. still no final master until full editorial/color/texture finishing and exported-file QC pass.
