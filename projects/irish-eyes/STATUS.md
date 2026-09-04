# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: **moving-asset build / Magic Gate proofing / coverage expansion**. The source-derived visual language has now passed continuity testing. **No final 3:07 master render yet.**

Source:

- `Brandi South Florida 2017.mp4`
- 1280x720 container / 720x1280 displayed portrait orientation
- 30 fps
- 31.766344 s
- 953 extracted source frames

Working extraction:

`/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

## Governing rule

Real footage and real extracted frames remain the identity/reality anchor. Generated material may support surreal transitions, environments or missing visual beats when it genuinely improves the film, but drifted/synthetic-looking results are rejected. Effects must survive rendered QC.

Do not render the final master until story coverage is sufficient, the song-timed rough cut has been inspected, the professional finishing stack has been applied, and the exported file passes complete QC.

## Approved / provisional moving-asset library

- **P02 Reflection Portal V3** — KEEP; camera destination is source-derived water.
- **P04 Spatial Entry V2** — KEEP; real frames 451–530, subject clears naturally while sky/far-water/near-water move at different rates. SHA `c5f32d69e01c08bb2f71ac1ca7933e6e99da0685b2af3b05f4d11935063416c2`.
- **P05 Still Here / Time Dilation V2** — KEEP; quiet closing magic.
- **P05 V3** — continuity tonal refinement. SHA `eebad3d6b8b760ec964979eca83533e3d4591493a6428ac35f8a28eca8cbb037`.
- **P06 Opening Arrival V1** — KEEP; photographic reality anchor. SHA `e61470fc2aff67ade3a53789f2a926147da52fe22843ef53d7d20ba9c9683f08`.
- **P07 Hair Memory V2** — KEEP; real hair/dress motion + face-protected temporal trails. SHA `67d067c4bb585c3316c0085b1093e7278255d21ed5d370a9a31ea22772723ef3`.
- **P08 Return Human Anchor V3** — KEEP; photographic return anchor. SHA `5ca6cccfe4ca7a896ce606f45a590828dd2459fa1aa1b489ed42b2c2a692dde0`.
- **P08 V4** — continuity tonal refinement. SHA `c774e97d29d6a56d856ecd7c00dc1ff497f50689eeb2010d0f3dfaefa791a7e5`.
- **P10 Eyes Within / Sunglasses Portal V4** — KEEP; real frame 291 → dark lens reflection → source-derived waterfront. SHA `5e84a025fbac476b16046cc913f7abc1b3515544b0f05147bc6792933bb8305d`.
- **P10 V5** — continuity color refinement reducing cyan bias. SHA `03e834dfe7ed059fc24c08bbd06a2c0ec8c6a9e94ba683565000f6b87816a0ee`.
- **T01 Sun / Water Memory Gate V1** — KEEP; reality→memory transition. SHA `35f9851d663f2fcfe8fa265a6a0ec2f30ad41b310a60ff1ac7c1bb1daed58d0f`.
- **T02 Water / Reality Return V2** — KEEP; memory→reality transition.
- **T02 V3** — continuity tonal refinement. SHA `405a1d86f20c18879f62cadc5d9b9b447b17e7e8bfdb0d874d11439d78aeeb90`.

## Rejected / lesson only

- P01 Breeze Memory V3 — too much animated-photograph feel.
- P03 Storm Revelation V1/V2/V3/V4 — did not cross the current Magic Gate.
- P09 Memory Clone Refraction V1/V2/V3 — read as ghost/apparition rather than premium refraction.
- P02 earlier portal versions — camera landed on/stretched subject.
- generated clean-plate/support attempts that changed person/location/style — rejected.
- P10 V2 — glowing white-goggle behavior.

## Continuity validation

See `CONTINUITY_REEL_QC.md`.

### Continuity Reel V2

Approved assets were placed sequentially with transition-overlap removed:

P06 → T01 → P07 → P04 → P10 V5 → T02 V3 → P08 V4 → P05 V3

Render:

- 28.433333 s
- 30 fps
- 360x640 proof
- 853 frames
- 0 black events
- 0 freeze events
- SHA `314ba5d49a34d47de577594213ecc86a6385fd65630c76a1f2229f8ba0b95a5b`

Decision: **KEEP AS STYLE-COHERENCE / CONTINUITY PROOF.**

The current effect families can coexist as one film language. This validates the visual system but does not yet authorize final assembly because Act II and the deep Act III memory world remain under-covered.

## Coverage state

See `COVERAGE_MAP_01.md`.

Strong coverage:
- Act I arrival / Irish Eyes / Spanish Hair / memory opening;
- return-to-Brandi sections;
- quiet closing / final refrain language;
- reality↔memory optical gates.

Major gaps:
- wet road / road travel;
- ancestry / old architecture;
- rain-on-glass / POV travel;
- warm house/window/candle memory;
- dark lake / ridge horizon;
- deepest Act III memory progression.

## P11 — Water → Wet Road Memory

P11 has now gone through four proof versions. None is promoted.

### V1

Source-derived water motion + camera dive + reflective-plane transformation. Rejected because the orange reflection streaks read like procedural/fake headlights.

- 5.2 s / 156 frames / 0 black frames
- SHA `f1a09ac1dccafb110e0c80a60b4aca9fda6e56b702ff3d65d2132dbfc86708fa`

### V2

Tried a stronger source-only perspective fold. Rejected because the asphalt read as a dark geometric wedge rather than a believable environment.

- 5.2 s / 156 frames / 0 black frames
- SHA `50703f9aa0ec457c4517041a73579aa1b1b48f20c3ceefdb2d16e5369976a063`

### V3

Made the road category more explicit. Rejected because the trapezoid/dashed-centerline language looked constructed and procedural.

- 5.2 s / 156 frames / 0 black frames
- SHA `8167c33153e98d05ba24ddb5e35a959ec411fe9694ce36c85ae1a6601e522529`

### V4

Removed lane markings and hard road geometry. Used source-derived wet texture, soft roadside falloff, narrowed real-water sheen and horizon haze.

- 5.2 s
- 30 fps
- 156 frames
- 0 black frames
- mean frame delta `0.7097589419056153`
- SHA `ea072b1e8f8692269f042bf5cb17e0a53f393fed5e5ae2bb5c5f8b203cd7da97`

**Decision: REVISE / DO NOT PROMOTE.** V4 is less artificial but the final surface remains too murky to convincingly read as a wet road.

New route: use real licensed environmental photography as the road/window/lake destination plates and animate/composite them ourselves. See `SUPPORT_PLATES_01.md`. Prefer CC0/public-domain sources so the memory-world expansion stays grounded in real imagery rather than AI-video generation.

## YouTube packaging

Full-resolution separate intro/outro assets exist under `projects/irish-eyes/youtube_packaging/`. They are packaging assets, not replacements for the film's emotional ending.

See `YOUTUBE_PACKAGING_MANIFEST.md`.

## Literal 3D Gaussian Splatting decision

See `3DGS_VIABILITY_2026-09-04.md`.

This specific source clip does not show enough trustworthy real camera baseline for a forced 3DGS training pass. Reserve true splatting for deliberate multiview/translated camera footage. Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

## Exact next action

1. ingest the selected CC0 rainy-road support plate and build **P12 Road Travel / Rain Glass** as a real-photo moving scene;
2. use P12 as the destination for a new P11 water→road optical handoff rather than synthesizing asphalt from scratch;
3. ingest/build **P13 Warm House Window / Candle Memory** from CC0 window/architecture photography;
4. ingest/build **P14 Dark Lake / Ridge Horizon** from CC0 lake/ridge photography;
5. build the 1.8–2.5 s micro hinge glasses → water → road → water;
6. rerun continuity with at least one environmental memory-world asset inserted;
7. only after Act II / Act III coverage is adequate begin a song-timed rough assembly;
8. final master remains blocked until editorial/color/texture finishing and exported-file QC pass.
