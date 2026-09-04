# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: **16:9 landscape master build / rough-cut preparation**. The visual language and environmental memory world have passed continuity validation strongly enough to begin rough assembly. **No final 3:07 master render yet.**

Primary source:
- `Brandi South Florida 2017.mp4`
- encoded 1280x720 with a -90 degree display matrix
- correct displayed capture is portrait-oriented
- 30 fps
- 31.766344 s
- 953 extracted upright source frames

Working extraction:
`/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

## Locked landscape rule

The finished Irish Eyes film and YouTube packaging are **16:9 landscape only**. Portrait/vertical renders created during effect-laboratory development are reference/proof assets only.

Disabling the source rotation is not a valid solution because it produces a sideways picture. Landscape production uses authored horizontal reframing, real-source closeups/medium crops, subject/environment extension, and landscape memory-world shots. **No blurred vertical-video sidebars or pillarboxed phone-video treatment in the finished film.**

See `LANDSCAPE_MASTER_SPEC.md`.

## Governing creative rule

Real footage and real extracted frames remain the identity/reality anchor. Real CC0/public-domain photography is preferred for missing environmental memory plates when available. Generated material may support surreal transitions or missing visual beats when it genuinely improves the film, but drifted/synthetic-looking results are rejected. Effects must survive rendered QC.

Do not render the final master until the song-timed rough cut has been inspected, picture structure is stable, the professional editorial/color/texture finishing stack has been applied, and the exported file passes complete QC.

## Approved / provisional visual families

- P02 Reflection Portal V3 — KEEP
- P04 Spatial Entry V2 — KEEP
- P05 Still Here / Time Dilation — KEEP
- P06 Opening Arrival — KEEP
- P07 Hair Memory — KEEP
- P08 Return Human Anchor — KEEP
- P10 Eyes Within / Sunglasses Portal — KEEP
- T01 Sun / Water Memory Gate — KEEP
- T02 Water / Reality Return — KEEP
- P11 Water → Wet Road Memory V4 — KEEP provisional
- P12 Road Travel / Rain Glass V2 — KEEP provisional
- P13 Warm Window / Candle Memory V2 — KEEP provisional
- P14 Dark Lake / Ridge Horizon V2 — KEEP provisional
- T03 Glasses → Water → Road → Water V2 — KEEP provisional

## 16:9 working master library

See `LANDSCAPE_MASTER_LIBRARY_V1.md` and `LANDSCAPE_NATIVE_BATCH_01.md`.

The earlier 1280x720 continuity components remain useful working assets L00–L12.

### Newly rendered landscape-native real Brandi masters

- **L15 Arrival Real V1** — KEEP — SHA `38a2213e3bdc9521f4b072a5f0dd922470a76772008ee3016836efe2764c12d4`
- **L16 Irish Eyes Portrait V1** — KEEP — SHA `41e4e7157a62189731a2f8f14e461ad04e70f45e4de706bef58846bbada35745`
- **L17 Hair Real Motion V1** — KEEP — SHA `1614cf2934039f80505e46db12b77f500feb970f8c64f1b7dfef3627e1f800d3`
- **L18 Full-Body Waterfront 2.5D V1** — REJECTED because the background retained a giant duplicate Brandi
- **L18 Full-Body Waterfront 2.5D V2** — rebuilt from clean real waterfront + one real Brandi alpha; QC HOLD — SHA `08ef5521787fa935ab3aca157a1c5ce8b5b4ec665782777d5cdaf3a33cf231e1`
- **L19 Last Look Real V1** — KEEP — SHA `95d7b61aef858553f5e269cebde08619c68dbce037db62e9b96937df46d0d763`

Batch QC sheet:
`landscape_16x9/qc/LANDSCAPE_MASTERS_L15_L19_QC.jpg`

The QC pass caught and removed the L18 V1 duplicate-person failure before rough assembly.

## Continuity validation

### Landscape Continuity Reel V4 — 16:9

- `landscape_16x9/continuity/IRISH_EYES_LANDSCAPE_CONTINUITY_REEL_V4_16x9.mp4`
- 1280x720
- 30 fps
- approximately 55.47 s

Purpose: verify that the established effect language survives cinematic 16:9 reframing before the 187.12 s rough assembly.

Portrait continuity reels remain effect-development references only.

## 187.12-second rough-cut structure

See `ROUGH_CUT_16X9_PLAN_V1.md`.

The full picture structure is mapped from 00:00.00 through 03:07.12, including title-over-opening reality, long real-Brandi sections, Irish-eyes portal, Spanish-hair movement, spatial entry, environmental memory-world sequence, return to reality, deep-memory Act III passage, and progressive removal of effects in the final refrain.

The remastered Irish Eyes WAV is **not currently mounted in the active runtime**. Rough picture timing can follow the already-measured structural boundaries, but true transient/phrase sync and audio-reactive modulation must wait until the original audio master is restored.

## YouTube packaging — 16:9

- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_INTRO_16x9_V2.mp4`
- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_OUTRO_16x9_V2.mp4`

Both are 1280x720 / 30 fps. The intro lives over the song opening; the outro is separate post-film packaging.

## Literal 3D Gaussian Splatting decision

This specific source clip does not show enough trustworthy real camera baseline for a forced 3DGS training pass. Reserve true splatting for deliberate multiview/translated-camera footage. Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

## Current execution condition

The local container rendered L15–L19 in smaller chunks but is intermittently refusing new media jobs again. Plugin discovery did not surface a connected deterministic FFmpeg/video-processing service suitable for this custom workflow, so GitHub remains the canonical checkpoint while the next render surface is retried.

## Exact next action

1. visually clear or revise L18 V2;
2. render landscape-native environmental masters **L20 Water→Road, L21 Rain-Glass Travel, L22 Warm Window/Candle, L23 Dark Lake/Ridge** at 1280x720;
3. assemble the first **187.12 s landscape visual rough** from `ROUGH_CUT_16X9_PLAN_V1.md` using L15–L23 plus approved transition families;
4. preserve long real-Brandi passages so the movie does not become an effects reel;
5. restore the original remastered Irish Eyes WAV before claiming true song sync;
6. inspect the rough for repetition, pacing, visual fatigue and real-Brandi percentage;
7. do **not** render/deliver the final master yet;
8. after picture structure stabilizes, apply shot-by-shot exposure/white-balance/skin/dress matching, saturation/vibrance, contrast, highlight recovery, selective sky/water work, halation cleanup, denoise/sharpening/grain matching and transition polish;
9. final export must pass full-runtime visual/technical QC before delivery.