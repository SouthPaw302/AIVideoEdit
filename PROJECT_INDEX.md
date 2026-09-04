# Project Index

This file tracks productions inside AIVideoEdit. Each project must be recoverable from GitHub without relying on chat history.

## General archive

All known Video Creation production branches are consolidated on `main` under `general/`, with point-in-time archive branches used for completed productions.

Known archive branches include:

- `archive/video/ironflame`
- `archive/video/silver-coin`
- `archive/video/leave-it-by-the-door`
- `archive/video/sigh-no-more`
- `archive/video/irish-eyes`

## Active / completed productions

### Irish Eyes

Branch: [`song/irish-eyes`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/irish-eyes)  
Archive branch: `archive/video/irish-eyes`  
Project path: `projects/irish-eyes/`

Status: **V1.2 FINAL COMPLETE / QC PASSED**

Canonical artistic master: `IRISH_EYES_V1_2_FINAL_YouTube_720p30.mp4`  
SHA-256: `a7bc3cd9674b8eaf6a55c28dc6898dc136afc5c668bd95409dce06dc9f10dba7`  
Library ID: `libfile_f35a75d11c748191ae3d25960667b0a9`

Canonical YouTube upload with post-roll: `IRISH_EYES_V1_2_FINAL_UPLOAD_WITH_OUTRO_720p30.mp4`  
SHA-256: `edae4a9b65a23c705228d58a41aa1e6eba14a378e3096657f6f22d62c9f3e362`  
Library ID: `libfile_e6ace24d89c8819183d12bcbb471ef98`

Core direction:
- 16:9 source-derived memory cinema
- real Brandi footage/frames remain the identity anchor
- authored horizontal reframing; no blurred portrait sidebars
- spatial entry, 2.5D depth, water/reflection portals, rain glass, warm-window/candle memory, dark lake/ridge, prism/halation and optical reality↔memory gates
- environmental support serves the real source rather than replacing it
- progressive removal of effects in the final refrain

Final recovery files include `STATUS.md`, `FINAL_MASTER.md`, `FINAL_QC.md`, `ACTUAL_MOVIE_ASSET_MANIFEST.md`, `VISUAL_DNA.md`, `ROUGH_CUT_16X9_PLAN_V1.md`, `LANDSCAPE_NATIVE_BATCH_02.md`, and `YOUTUBE_PACKAGING_MANIFEST.md`.

### IronFlame

Branch: [`song/ironflame`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/ironflame)  
Archive branch: `archive/video/ironflame`  
General snapshot: `general/branch-snapshots/ironflame/`  
Project path: `projects/ironflame/`

Status: **V1 rendered and delivered / exact final MP4 archive identity still needs recovery**

Core direction:
- female mythic protagonist; she is the IronFlame
- dark folk / mythic fantasy / haunted but resolute
- ember orange -> iron blue -> ash gray -> dawn gold
- living scenes, not slideshow frames
- advanced micro-animation, parallax, particles, audio-reactive light/FX, and selective integrated visualizer language
- rebuilt from scratch; old IronFlame MP4s are excluded as production sources

Known delivered result: 12 scenes, 04:04.680, 1280x720 master plus 540p compact delivery. Exact final filenames, hashes, and durable storage IDs remain an archive gap.

### Silver Coin

Branch: [`song/silver-coin`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/silver-coin)  
Archive branch: `archive/video/silver-coin`  
General snapshot: `general/branch-snapshots/silver-coin/`  
Project path: `projects/silver-coin/`

Status: **V8 FINAL COMPLETE / QC PASSED**

Canonical style: **Living Pre-Raphaelite Folk Romanticism**

Final master: `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`  
SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`  
Persistent Library ID: `libfile_acfb04300bd88191b67e23b2ad736870`

Core direction:
- luminous oil-brush surfaces, emerald-and-gold natural light, flowers and folk-period detail
- natural character performance and environmental motion inside a visibly painted world
- recurring blonde flower-crowned protagonist
- village/road, tavern, musicians/fiddler, dancing crowd, workers/procession, merchant/barmaid, rain/lightning and coin imagery

Reusable Silver Coin tooling is exposed under `general/reusable/`.

## Recovered / partial song projects

### Leave It by the Door

Branch: `song/leave-it-by-the-door`  
Archive branch: `archive/video/leave-it-by-the-door`

Status: **Recovery / partial**

Recovered evidence: warm tavern narrative treatment and lyric-timed multi-image/living-scene experiments. Exact source audio, lyrics, render filenames, hashes, and confirmed completion record remain incomplete.

### Sigh No More / Irish Eyes, Spanish Hair — historical precursor

Branch: `song/sigh-no-more`  
Archive branch: `archive/video/sigh-no-more`

Status: **Recovery / partial historical precursor**

This branch preserves the earlier prompt-architecture lineage around Lake Hartwell, mountain roads, old houses, wet pavement, candlelight, rural night, Spanish hair, Irish eyes and ancestral ghosts. It is not the completed Irish Eyes film. The completed production is `song/irish-eyes`.

## Reference / prior experiments

The repository also preserves method precedents including:
- single-image living-cover animation
- rain/fog/glow/lightning compositing
- lyric-timed multi-image cuts
- efficient pre-rendered loop/scene assembly
- painterly motion transfer
- Gaussian light/volumetric effects
- 2.5D depth-parallax scene graphs
- tiny-NeRF experiments
- temporal/pigment transitions
- localized audio-reactive effect layers

See `docs/VISUAL_STYLE_CATALOG.md` and `general/reusable/`.

## Adding or closing a project

Use one branch per song: `song/<slug>`. At minimum preserve project status, visual DNA, manifests, QC, final hashes, persistent media references, and exact recovery instructions. At a final milestone, update this index, the general archive index/snapshot, and create a point-in-time archive branch.
