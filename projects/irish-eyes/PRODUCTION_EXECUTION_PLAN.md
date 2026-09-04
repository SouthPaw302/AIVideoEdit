# Irish Eyes — Production Execution Plan

Branch: `song/irish-eyes`

This is the active execution plan. Follow it in order unless a specific shot proves that a different order is materially better.

## Core target

Build a dynamic long-form music film from a mixture of:

- real Brandi source footage and extracted frames;
- living still-frame shots;
- source-derived loops;
- generated environmental/support imagery when needed;
- surreal but identity-safe transformations;
- spatial/depth effects;
- authored camera/perception changes;
- music-directed optical and atmospheric behavior;
- professional final editorial/grade/finishing.

The result must feel like a directed film, not a slideshow, generic visualizer, or one clip with weak overlays.

## Mandatory tool-first preflight

Before writing new rendering/effect code for any shot:

1. inspect `main/general/reusable/CANONICAL_EFFECT_REGISTRY.md`;
2. inspect the relevant implementation under `main/general/reusable/`;
3. check whether GitHub-native capabilities can recover/search/compare/package the needed work;
4. check currently available ChatGPT tools/connectors/plugins for a purpose-built capability;
5. use an existing proven implementation when it fits;
6. only write new code when the existing stack or available tooling cannot produce the required result cleanly;
7. if new code creates a reusable technique, prove it on Irish Eyes and promote/register it on `main`.

### GitHub capabilities already available

The connected GitHub surface exposes repository search, branches, commits, trees, blobs, file reads/writes, comparisons, PRs/issues, GitHub Actions run/job/log/artifact inspection and retry capabilities, among other repository-management functions.

Use GitHub aggressively for recovery, indexing, checkpointing, asset manifests, proof/QC metadata and reusable-tool discovery. Do not mistake GitHub repository tooling for a native video-effects renderer.

### Optional external/plugin capabilities discovered

Potential fallbacks discovered in the plugin directory include:

- Cloudinary — image/video hosting and transformation;
- CloudConvert — conversion/processing, including custom FFmpeg workflows;
- AI Video Maker — Seedance-based image/text-to-video generation;
- sync.labs — image animation/lip-sync/video transformation;
- Pixlie — AI-video prompt/camera planning;
- Krikey AI Animation — 3D character/music animation.

These are optional, may require accounts/credits, and should not be installed or used merely because they exist. Prefer our built-in/local/repository stack when it can achieve the shot.

## Current source state

Canonical photographic source:

`Brandi South Florida 2017.mp4`

Verified source properties:

- 1280x720
- 30 fps
- 31.766344 s
- 953 frames

Current production extraction in the active runtime:

- `frame_000001.png` through `frame_000953.png`
- native 30 fps frame mapping
- `FRAME_MANIFEST.csv`

Raw extracted frames are working media. Selected canonical frames, shot packages, manifests, proof media references and important source fingerprints belong in the song branch/archive system.

## Phase 1 — Frame scan and hero selection

Scan all 953 source frames deliberately.

Do not choose only sharp portraits. Select frames/windows for different cinematic jobs:

- arrival / reality anchor;
- portrait / eyes / sunglasses;
- hair and dress motion;
- shoreline walking;
- water/reflection geometry;
- wide environmental space;
- silhouette/backlight;
- storm/dream compatibility;
- transition geometry;
- final-return/closure.

For each keeper record frame number, timestamp, intended storyboard beat, visual strengths, usable neighboring motion window, and planned effect family.

## Phase 2 — Build real shot packages

Each selected hero moment becomes a mini scene package, not merely a JPEG.

As applicable preserve:

- original source frame / neighboring source window;
- identity-safe subject alpha;
- clean/background plate;
- foreground / subject / water / shoreline / sky layers;
- depth map / mattes / holdouts;
- reflection and water assets;
- atmosphere/light/optical assets;
- generated environmental extensions/support imagery;
- transition entry/exit material;
- loop assets;
- short proof render;
- QC notes.

## Phase 3 — Camera, zoom and perception design

Zoom is an authored cinematography tool, not a default Ken Burns effect.

Use several distinct perception moves:

### A. Optical push-in
Slow push toward eyes, sunglasses, face, hand, reflection, or another story object. Combine with depth differential so the environment shifts at a different rate than the subject.

### B. Pull-back revelation
Begin intimate and reveal the water, horizon, boy, storm, generated memory environment, or impossible wider world.

### C. Vertigo / dolly-zoom perception
Where a depth scene supports it, change virtual focal perception while compensating camera distance so Brandi stays relatively stable while the background expands or compresses. Use sparingly for memory realization, emotional pressure, or transition moments.

### D. Depth-rack perception
Move attention from foreground optical material/reflection to Brandi, from Brandi to the horizon, or from reality plate to generated memory layer. Combine focus breathing with actual layer/depth movement.

### E. Reflection-entry zoom
Push into sunglasses, water reflection, sun streak, glass, wet sand, or another reflective surface until it becomes the next scene.

### F. Impossible-scale zoom
Transition from a macro detail to a wide landscape or from a landscape into a detail by matching shape/light/color. This may use generated intermediate material, pigment/fog transport, temporal echoes or object portals.

### G. Lateral perception shift
Do not rely only on forward/back zoom. Use small arcs, horizon slides, foreground occlusion, depth parallax and asymmetric reframing to create the sensation of a real camera changing position.

Every perception move must preserve Brandi's identity and photographic integrity.

## Phase 4 — Wizard effect assignment

Choose effects artistically per shot; do not stack everything everywhere.

Canonical families available for Irish Eyes:

1. actual 3D Gaussian Splatting / SuperSplat when source coverage is sufficient;
2. hybrid NeRF volumetric light/atmosphere;
3. continuous soft-depth 2.5D;
4. living-image micro-motion / mesh breath;
5. water and wet-reflection systems;
6. volumetric weather, storm haze, rain, mist and motivated lightning;
7. prism/refraction/halation/glint optics;
8. controlled temporal memory echoes;
9. transformative reflection/object/fog/pigment/match transitions;
10. measured music-directed cinematography and effect modulation.

Supporting generated content is encouraged when it expands the story without replacing the real identity anchor.

## Phase 5 — Proof gate

Before any effect family enters the long edit:

- render a short representative proof;
- compare it against the source;
- verify the effect is clearly visible but artistically motivated;
- verify face/body/hair/clothing identity integrity;
- inspect edges, masks, disocclusions, reflection logic and temporal stability;
- reject frozen-looking, ghosted, waxy, synthetic or generic-overlay results;
- record keep/revise/reject.

No effect counts because a file, shader or plan exists.

## Phase 6 — Build the moving-asset library

Create enough approved 3–10 second moving assets to cover the complete musical narrative without obvious repetition.

Favor variation in:

- scale;
- camera direction;
- depth;
- subject framing;
- environmental state;
- color temperature;
- motion density;
- reality vs memory balance;
- transition style.

The original 31.77 s footage remains a recurring reality anchor but must not be the only media in the 3:07 film.

## Phase 7 — Full edit

Only after the moving-asset library is sufficiently complete:

- assemble against the song/story map;
- use original footage between more magical passages to restore photographic truth;
- use hard cuts, motivated transitions, match geometry, reflection portals and short dissolves as appropriate;
- avoid prolonged full-body crossfades and obvious loop repetition;
- preserve the shoreline-boy opening direction and exclude rejected busy crowd/high-rise beach material.

## Phase 8 — Professional editorial finishing

After picture lock, apply the complete finishing stack defined in `EDITORIAL_FINISHING_STACK.md`.

This includes shot matching, exposure, white balance, skin consistency, dress-color consistency, contrast, blacks, saturation/vibrance, selective color, sky/water shaping, highlight recovery, optical refinement, denoise, sharpening, grain/texture matching, stabilization/motion consistency and transition cleanup.

Finishing is not optional.

## Phase 9 — Final-output QC

Scan the actual exported movie, not merely individual proofs.

Verify:

- complete runtime;
- no black/blank frames;
- no unexpected freezes;
- no duplicated sections;
- no loop jumps;
- no identity drift;
- no rejected footage leakage;
- effects visibly survive encoding/scaling;
- grade is consistent;
- transitions are clean;
- motion density remains cinematic across the full runtime;
- audio/video duration and sync are correct.

## GitHub checkpoint cadence

Update `song/irish-eyes` after every meaningful production gate:

1. source/extraction changes;
2. hero-frame selection batch;
3. completed shot package;
4. approved/rejected effect proof;
5. generated-support batch;
6. moving-asset batch;
7. timeline/structure change;
8. major render;
9. QC finding/fix;
10. picture lock and final master.

At each checkpoint preserve the exact next action so another agent can resume immediately.

## Governing artistic rule

Use zoom, depth, movement, generated material and effects to **alter perception**, not merely decorate a still.

The viewer should sometimes feel that a photograph opened into a place, a reflection became a memory, the horizon moved farther away, the world breathed, or the camera entered something that could not physically exist — while Brandi remains the recognizable photographic center of the film.
