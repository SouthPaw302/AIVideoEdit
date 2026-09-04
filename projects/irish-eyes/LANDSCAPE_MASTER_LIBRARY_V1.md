# Irish Eyes — Landscape Master Library V1

Branch: `song/irish-eyes`

This registry is the working 16:9 production library for Irish Eyes. Final-film format is 1280x720 / 30 fps or higher 16:9; portrait proofs are reference-only and must not be used as final-format masters when a direct source rebuild is possible.

## Existing landscape continuity masters

| ID | Source family | Landscape working file | Role |
|---|---|---|---|
| L00 | P06 | `landscape_16x9/continuity/tmp_clips/00_P06.mp4` | photographic arrival / reality anchor |
| L01 | T01 | `landscape_16x9/continuity/tmp_clips/01_T01.mp4` | sun-water reality→memory gate |
| L02 | P07 | `landscape_16x9/continuity/tmp_clips/02_P07.mp4` | Spanish-hair real-motion memory |
| L03 | P04 | `landscape_16x9/continuity/tmp_clips/03_P04.mp4` | spatial entry into waterfront |
| L04 | P10 | `landscape_16x9/continuity/tmp_clips/04_P10.mp4` | Irish-eyes / sunglasses portal |
| L05 | T03 | `landscape_16x9/continuity/tmp_clips/05_T03.mp4` | glasses→water→road→water hinge |
| L06 | P11 | `landscape_16x9/continuity/tmp_clips/06_P11.mp4` | water→wet-road memory |
| L07 | P12 | `landscape_16x9/continuity/tmp_clips/07_P12.mp4` | road travel / rain glass |
| L08 | P13 | `landscape_16x9/continuity/tmp_clips/08_P13.mp4` | warm window / candle memory |
| L09 | P14 | `landscape_16x9/continuity/tmp_clips/09_P14.mp4` | dark lake / ridge horizon |
| L10 | T02 | `landscape_16x9/continuity/tmp_clips/10_T02.mp4` | memory→reality return gate |
| L11 | P08 | `landscape_16x9/continuity/tmp_clips/11_P08.mp4` | photographic return anchor |
| L12 | P05 | `landscape_16x9/continuity/tmp_clips/12_P05.mp4` | quiet time-dilation / closing |

These components are represented together in `IRISH_EYES_LANDSCAPE_CONTINUITY_REEL_V4_16x9.mp4`.

## Landscape-native real-source masters — rendered

All of the following were rebuilt directly from the real 953-frame Brandi source at 1280x720 / 30 fps rather than upscaling portrait proof clips.

### L15 — Arrival Real

File: `landscape_16x9/masters/IE_L15_ARRIVAL_REAL_16x9_V1.mp4`

- 5.033333 s / 151 frames
- 0 black frames
- 0 freeze candidates
- mean frame delta `2.1286863088348764`
- SHA-256 `38a2213e3bdc9521f4b072a5f0dd922470a76772008ee3016836efe2764c12d4`
- real early-source motion with landscape medium framing and restrained warm/halation treatment

Decision: **KEEP — landscape photographic anchor.**

### L16 — Irish Eyes Portrait

File: `landscape_16x9/masters/IE_L16_IRISH_EYES_PORTRAIT_16x9_V1.mp4`

- 3.366667 s / 101 frames
- 0 black frames
- 0 freeze candidates
- mean frame delta `1.6496843749999999`
- SHA-256 `41e4e7157a62189731a2f8f14e461ad04e70f45e4de706bef58846bbada35745`
- real-source face/sunglasses/hair motion, gentle push and scene-motivated glint

Decision: **KEEP — real Irish-eyes portrait family.**

### L17 — Hair Real Motion

File: `landscape_16x9/masters/IE_L17_HAIR_REAL_MOTION_16x9_V1.mp4`

- 2.866667 s / 86 frames
- 0 black frames
- 0 freeze candidates
- mean frame delta `8.668883837997003`
- SHA-256 `1614cf2934039f80505e46db12b77f500feb970f8c64f1b7dfef3627e1f800d3`
- strongest real wind/hair passage with restrained bright-edge temporal memory

Decision: **KEEP — real Spanish-hair motion family.**

### L18 — Full-Body Waterfront 2.5D

V1 was rendered and **rejected** because the background source still contained a giant partial Brandi at frame left, producing an obvious duplicate-person artifact.

V2 file: `landscape_16x9/masters/IE_L18_FULL_BODY_WATERFRONT_25D_16x9_V2.mp4`

- rebuilt from the clean right-side portion of the real frame-520 waterfront, mirrored/extended into a 16:9 source-derived environment;
- contains only one Brandi: the real frame-420 alpha subject plate;
- independent subject/background motion and restrained moving water are retained;
- SHA-256 `08ef5521787fa935ab3aca157a1c5ce8b5b4ec665782777d5cdaf3a33cf231e1`.

Decision: **QC HOLD until full V2 visual scan is completed.** Never use L18 V1.

### L19 — Last Look Real

File: `landscape_16x9/masters/IE_L19_LAST_LOOK_REAL_16x9_V1.mp4`

- 4.466667 s / 134 frames
- 0 black frames
- 0 freeze candidates
- mean frame delta `3.453348018483709`
- SHA-256 `95d7b61aef858553f5e269cebde08619c68dbce037db62e9b96937df46d0d763`
- real late-source human passage, slow push and restrained resolution treatment

Decision: **KEEP — closing real-human family, with final shadow lift deferred to finishing.**

QC contact sheet: `landscape_16x9/qc/LANDSCAPE_MASTERS_L15_L19_QC.jpg`.

## YouTube packaging masters

- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_INTRO_16x9_V2.mp4`
- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_OUTRO_16x9_V2.mp4`

The intro may be integrated over the song's opening picture without extending the film duration. The outro is a separate post-film YouTube card so the artistic film itself still ends on water/light.

## Next landscape-native masters

Build these directly at 1280x720 from source plates / deterministic effects rather than enlarging portrait proofs:

- `L20 Water → Wet Road`;
- `L21 Road Travel / Rain Glass`;
- `L22 Warm Window / Candle Memory`;
- `L23 Dark Lake / Ridge Horizon`;
- landscape-native transition rebuilds where the rough exposes visible quality mismatch.

## Quality rule

The 16:9 masters may use tight horizontal crops where they make photographic sense and source-derived landscape extension where a wider human composition is needed. **No blurred phone-video sidebars, no accidental portrait canvases, no duplicated real subject, and no low-resolution portrait proof should be upscaled into the final master if the source can be rebuilt directly.**