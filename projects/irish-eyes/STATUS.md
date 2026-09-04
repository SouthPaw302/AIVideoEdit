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

- **P02 Reflection Portal V3** — KEEP; camera destination is source-derived water.
- **P04 Spatial Entry V2** — KEEP; real frames 451–530, subject clears naturally while sky/far-water/near-water move at different rates.
- **P05 Still Here / Time Dilation V2/V3** — KEEP; quiet closing magic / tonal refinement.
- **P06 Opening Arrival V1** — KEEP; photographic reality anchor.
- **P07 Hair Memory V2** — KEEP; real hair/dress motion + face-protected temporal trails.
- **P08 Return Human Anchor V3/V4** — KEEP; photographic return anchor / tonal refinement.
- **P10 Eyes Within / Sunglasses Portal V4/V5** — KEEP; dark lens reflection → source-derived waterfront / color refinement.
- **T01 Sun / Water Memory Gate V1** — KEEP; reality→memory transition.
- **T02 Water / Reality Return V2/V3** — KEEP; memory→reality transition / tonal refinement.
- **P11 Water → Wet Road Memory V4** — KEEP provisional; water organically folds into wet reflective road/track memory.
- **P12 Road Travel / Rain Glass V2** — KEEP provisional environmental pass.
- **P13 Warm Window / Candle Memory V2** — KEEP provisional environmental pass.
- **P14 Dark Lake / Ridge Horizon V2** — KEEP provisional environmental magic pass.
- **T03 Glasses → Water → Road → Water V2** — KEEP provisional micro-hinge.

## 16:9 working master library

See `LANDSCAPE_MASTER_LIBRARY_V1.md`.

The already-rendered 1280x720 / 30 fps continuity components are now registered as the working landscape library:

- L00 P06 arrival;
- L01 T01 reality→memory;
- L02 P07 hair memory;
- L03 P04 spatial entry;
- L04 P10 eyes portal;
- L05 T03 glasses/water/road/water;
- L06 P11 water→road;
- L07 P12 rain-glass road travel;
- L08 P13 warm window/candle;
- L09 P14 dark lake/ridge;
- L10 T02 memory→reality;
- L11 P08 photographic return;
- L12 P05 quiet closing.

These are working picture assets, not automatically final-quality shots. Important shots should still be rebuilt directly from the highest-quality source when media execution is available.

## Landscape-native real Brandi shots queued next

Direct-from-source recipes are locked for:

- **L15 Arrival Real** — early source motion, landscape medium/close framing;
- **L16 Irish Eyes Portrait** — sunglasses/face/hair real-source passage;
- **L17 Hair Real Motion** — strongest wind/hair source window;
- **L18 Full-Body Waterfront 2.5D** — real Brandi subject plate + real source-derived waterfront extension;
- **L19 Last Look Real** — late-source human passage for the ending.

A batch render was attempted, then retried in smaller chunks, but the active local media executor began refusing all execution jobs. **Do not claim L15–L19 are rendered yet.** The recipes and intended narrative roles are preserved in the branch.

## Continuity validation

### Landscape Continuity Reel V4 — 16:9

- `landscape_16x9/continuity/IRISH_EYES_LANDSCAPE_CONTINUITY_REEL_V4_16x9.mp4`
- 1280x720
- 30 fps
- approximately 55.47 s

Purpose: verify that the established effect language survives cinematic 16:9 reframing before the 187.12 s rough assembly.

Portrait continuity reels remain effect-development references only.

## 187.12-second rough-cut structure locked

See `ROUGH_CUT_16X9_PLAN_V1.md`.

The full picture structure is now mapped from 00:00.00 through 03:07.12, including:

- title inside the opening reality rather than extra pre-song runtime;
- long real-Brandi sections in Acts I, III and IV;
- Irish-eyes/sunglasses portal;
- Spanish-hair motion language;
- spatial entry;
- water→road→rain-glass→warm-window→dark-lake environmental memory run;
- return to photographic reality;
- deep-memory loop in Act III;
- progressive removal of effects in the final refrain;
- separate YouTube post-roll after the artistic 187.12 s film ends.

The remastered Irish Eyes WAV is not currently mounted in the active runtime, so the rough-cut plan uses the already-measured musical boundaries. Exact transient/phrase sync resumes when the original audio master is restored.

## YouTube packaging — 16:9

- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_INTRO_16x9_V2.mp4`
- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_OUTRO_16x9_V2.mp4`

Both are 1280x720 / 30 fps. The intro is designed to live over the song opening; the outro remains separate post-film packaging.

## Tool resilience / current execution fallback

The project rule remains tool-first. The local media executor is currently refusing video jobs. CloudConvert has been surfaced as the preferred connected fallback because it supports local-file video processing and custom FFmpeg workflows. It is not yet assumed connected/usable until the user completes the plugin connection. GitHub remains the canonical checkpoint layer while execution is unavailable.

## Literal 3D Gaussian Splatting decision

This specific source clip does not show enough trustworthy real camera baseline for a forced 3DGS training pass. Reserve true splatting for deliberate multiview/translated-camera footage. Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

## Exact next action

1. when local or connected media execution becomes available, render **L15–L19** first at 1280x720 / 30 fps directly from the real source;
2. QC those real-human landscape masters for crop quality, face/hair/hands, exposure and repeated composition;
3. assemble the first **187.12 s landscape visual rough** from `ROUGH_CUT_16X9_PLAN_V1.md`;
4. restore the original remastered Irish Eyes WAV before claiming true song-sync/audio-reactive timing;
5. inspect the rough for repetition, pacing, visual fatigue and real-Brandi percentage;
6. do **not** render/deliver the final master yet;
7. after picture structure stabilizes, apply shot-by-shot exposure/white-balance/skin/dress matching, saturation/vibrance, contrast, highlight recovery, selective sky/water work, halation cleanup, denoise/sharpening/grain matching and transition polish;
8. final export must pass full-runtime visual/technical QC before delivery.
