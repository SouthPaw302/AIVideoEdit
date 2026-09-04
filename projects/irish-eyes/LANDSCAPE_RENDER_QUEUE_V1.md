# Irish Eyes — Landscape Render Queue V1

Branch: `song/irish-eyes`
Target working format: 1280x720 / 30 fps / H.264 / Rec.709

Run this queue before the first full landscape rough. Each item must pass local visual QC before it is considered a usable master.

## Priority A — real Brandi landscape masters

### L15 — Arrival Real

- source frames: 000001–000150
- source duration: 5.0 s
- strategy: real 16:9 crop from upright portrait source
- framing: upper-body/medium; preserve eyes, hair, dress neckline, real horizon
- camera: restrained 3–4% push, slight off-axis drift
- FX: restoration, subtle warm halation, independent water shimmer only if source crop includes enough water
- do not: blur sidebars, over-brighten face, add portal language
- QC: face/hair, crop stability, exposure, no edge jitter

### L16 — Irish Eyes Portrait

- source frames: 000245–000335
- source duration: ~3.03 s
- strategy: tighter horizontal portrait crop
- framing: sunglasses/eyes/hair/upper shoulders
- camera: slow off-axis push toward sunglasses
- FX: dark physically plausible lens reflection, very thin horizon/glint cue; no white-goggle behavior
- do not: spread reflection across face
- QC: eye/sunglass geometry, hair edge, highlight clipping

### L17 — Hair Real Motion

- source frames: 000360–000445
- source duration: ~2.87 s
- strategy: landscape medium crop preserving real hair/dress wind motion
- camera: slight lateral drift
- FX: face-protected temporal highlight history, very restrained prism, warm hair-edge glow
- do not: duplicate face/body or create ghost trail
- QC: natural hair continuity and temporal artifacts

### L18 — Full-Body Waterfront 2.5D

- hero source: frame 000420
- real subject alpha: `shot_packages/IE_P01_BREEZE_MEMORY/alpha/subject_alpha.png`
- background source: real source-derived water/sky from frame 520 / P10 layer
- strategy: subject + source-derived landscape extension
- composition: Brandi full body on left third; water/horizon fills right two-thirds
- motion: subject 1–2% drift, background 2–4% differential push, water ripple independent of sky
- FX: motivated sun/light volume, subtle dress/hair micro-motion only where safe
- do not: stretch anatomy, fabricate person, blur background into fake phone-video bars
- QC: matte edge, feet/dress edge, horizon, source identity

### L19 — Last Look Real

- source frames: 000840–000953
- source duration: ~3.8 s
- strategy: real horizontal crop
- framing: quiet upper-body/face/hair with water/light still present
- motion: restrained crop drift / lens breathing
- FX: protected shadow recovery, subtle rim warmth, minimal water movement
- do not: introduce new magic family in last look
- QC: skin/face exposure, no crop jump, final emotional hold

## Priority B — landscape effect-family rebuilds if current working crops are insufficient

Rebuild from highest-quality source/shot-package layers rather than enlarging portrait proofs:

- L03/P04 spatial entry;
- L04/P10 sunglasses portal;
- L06/P11 water→road;
- L07/P12 road/rain glass;
- L08/P13 warm window;
- L09/P14 dark lake;
- L10/T02 return gate;
- L12/P05 closing time dilation.

Only rebuild a family if the 1280x720 continuity component fails full-resolution QC.

## Priority C — rough-cut render

Once L15–L19 pass:

1. assemble exact picture map in `ROUGH_CUT_16X9_PLAN_V1.md`;
2. output a silent/guide-audio structure only if the remastered WAV is still unavailable;
3. once the original remastered WAV is restored, attach it losslessly/at 48 kHz and retime cuts to real musical events;
4. export `IRISH_EYES_ROUGH_16X9_V1.mp4` as review master, not final;
5. full-runtime scan: black frames, freeze runs, crop glitches, duplicated frames, transition seams, subject identity, over-dark memory run, exposure jumps;
6. no final grade until rough structure is accepted.

## Execution fallback order

1. active local ffmpeg/OpenCV renderer;
2. connected CloudConvert custom FFmpeg workflow using mounted local inputs;
3. Cloudflare/R2-backed remote workflow if Wrangler becomes available/authenticated;
4. GitHub remains checkpoint/manifest layer, not large-media render storage.
