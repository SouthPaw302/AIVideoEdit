# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: **moving-asset build / Magic Gate proofing / environmental coverage expansion**. The source-derived visual language has passed continuity testing. **No final 3:07 master render yet.**

Primary source:
- `Brandi South Florida 2017.mp4`
- 1280x720 container / portrait display orientation
- 30 fps
- 31.766344 s
- 953 extracted source frames

Working extraction:
`/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

## Governing rule

Real footage and real extracted frames remain the identity/reality anchor. Real CC0/public-domain photography is preferred for missing environmental memory plates when available. Generated material may support surreal transitions or missing visual beats when it genuinely improves the film, but drifted/synthetic-looking results are rejected. Effects must survive rendered QC.

Do not render the final master until story coverage is sufficient, the song-timed rough cut has been inspected, the professional finishing stack has been applied, and the exported file passes complete QC.

## Approved / provisional moving-asset library

- **P02 Reflection Portal V3** — KEEP; camera destination is source-derived water.
- **P04 Spatial Entry V2** — KEEP; real frames 451–530, subject clears naturally while sky/far-water/near-water move at different rates. SHA `c5f32d69e01c08bb2f71ac1ca7933e6e99da0685b2af3b05f4d11935063416c2`.
- **P05 Still Here / Time Dilation V2/V3** — KEEP; quiet closing magic / tonal refinement.
- **P06 Opening Arrival V1** — KEEP; photographic reality anchor. SHA `e61470fc2aff67ade3a53789f2a926147da52fe22843ef53d7d20ba9c9683f08`.
- **P07 Hair Memory V2** — KEEP; real hair/dress motion + face-protected temporal trails. SHA `67d067c4bb585c3316c0085b1093e7278255d21ed5d370a9a31ea22772723ef3`.
- **P08 Return Human Anchor V3/V4** — KEEP; photographic return anchor / tonal refinement.
- **P10 Eyes Within / Sunglasses Portal V4/V5** — KEEP; dark lens reflection → source-derived waterfront / color refinement.
- **T01 Sun / Water Memory Gate V1** — KEEP; reality→memory transition.
- **T02 Water / Reality Return V2/V3** — KEEP; memory→reality transition / tonal refinement.
- **P11 Water → Wet Road Memory V4** — KEEP provisional; source water organically folds into a wet reflective road/track memory without lane markers, fake headlights or hard road geometry. SHA `ea072b1e8f8692269f042bf5cb17e0a53f393fed5e5ae2bb5c5f8b203cd7da97`.
- **P12 Road Travel / Rain Glass V2** — KEEP provisional environmental pass; stronger forward travel, refracting glass droplets, rain trails, subtle windshield distortion, restrained dashboard edge. SHA `acc170d19fba35fafe1ce497fcf7145e28c80b114dfc99ed1d411ddc93b3fd67`.

## P13 Warm Window / Candle Memory

V1: **REVISE** — composition works but reads too much like a static frame-over-footage treatment.

V2 rendered cleanly:
- 5.4 s
- 30 fps
- 162 frames
- 0 black frames
- mean frame delta `0.2659996207873246`
- SHA `2825535c1e27d9c58f9cf372f703cf3ebbc4075b5717ee00800f356e31a2e1a3`

V2 adds focus choreography between rain/glass and outside memory, tiny pane-specific depth shifts, foreground rain, warm offscreen candle/practical reflection and soft wood-edge light.

**Status: QC HOLD.** Local image inspection failed before final visual clearance. Do not promote until the QC sheet is inspected.

See `MAGIC_GATE_BATCH_05.md`.

## Rejected / preserve lesson only

- P01 Breeze Memory V3 — too much animated-photograph feel.
- P03 Storm Revelation V1/V2/V3/V4 — did not cross the current Magic Gate.
- P09 Memory Clone Refraction V1/V2/V3 — ghost/apparition feel rather than premium refraction.
- P02 earlier portal versions — camera landed on/stretched subject.
- generated clean-plate/support attempts that changed person/location/style — rejected.
- P10 V2 — glowing white-goggle behavior.
- P11 V1/V2/V3 — fake light streaks / geometric wedge / procedural lane geometry.

## Continuity validation

`IRISH_EYES_MAGIC_CONTINUITY_REEL_V2.mp4` is the current style-coherence proof:
- 28.433333 s
- 30 fps
- 853 frames
- 0 black events
- 0 freeze events
- SHA `314ba5d49a34d47de577594213ecc86a6385fd65630c76a1f2229f8ba0b95a5b`

Decision: **KEEP AS STYLE-COHERENCE / CONTINUITY PROOF.**

## Coverage state

Strong coverage:
- Act I arrival / Irish Eyes / Spanish Hair / memory opening;
- return-to-Brandi sections;
- quiet closing / final refrain language;
- reality↔memory optical gates;
- first water→road and rain-glass environmental families.

Remaining major coverage:
- warm house/window/candle memory — P13 pending QC;
- dark lake / ridge horizon;
- ancestry / old architecture details;
- deepest Act III memory progression;
- glasses → water → road → water micro hinge.

## Real-photo support plate route

Tool-first search identified real CC0/public-domain Wikimedia Commons candidates for environmental memory material:
- `Wet road.jpg` — CC0;
- `Mountain Lake at Night (30608828696).jpg` — CC0;
- `Old cabin window (Unsplash).jpg` — pre-June-2017 Unsplash CC0 archived on Commons.

When binary ingest is available, compare these real-photo support routes against P11/P12/P13 rather than defaulting to AI-generated environments.

## YouTube packaging

Full-resolution separate intro/outro assets exist under `projects/irish-eyes/youtube_packaging/`. They are packaging assets, not replacements for the film's emotional ending.

See `YOUTUBE_PACKAGING_MANIFEST.md`.

## Literal 3D Gaussian Splatting decision

This specific source clip does not show enough trustworthy real camera baseline for a forced 3DGS training pass. Reserve true splatting for deliberate multiview/translated-camera footage. Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

## Exact next action

1. visually clear or revise P13 V2;
2. build **P14 Dark Lake / Ridge Horizon**, preferably from real CC0 photography if binary ingest is available;
3. build the 1.8–2.5 s glasses → water → road → water micro hinge;
4. rerun continuity with P11/P12/P13/P14 environmental memory assets inserted;
5. only after Act II / Act III coverage is adequate begin a song-timed rough assembly;
6. final master remains blocked until editorial/color/texture finishing and exported-file QC pass.
