# Project Index

This file tracks productions inside AIVideoEdit. Each project must be recoverable from GitHub without relying on chat history.

## General archive

All known Video Creation production branches are now consolidated on `main` under [`general/`](general/README.md), with complete Git-tree snapshots in `general/branch-snapshots/` and machine-readable recovery state in `general/ARCHIVE_INDEX.json`.

Point-in-time backup branches:

- `archive/video/ironflame`
- `archive/video/silver-coin`
- `archive/video/leave-it-by-the-door`
- `archive/video/sigh-no-more`

## Active / completed productions

### IronFlame

Branch: [`song/ironflame`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/ironflame)  
Archive branch: `archive/video/ironflame`  
General snapshot: `general/branch-snapshots/ironflame/`  
Project path: `projects/ironflame/`

Status: **V1 rendered and delivered / exact final MP4 archive identity still needs recovery**

Core direction:
- female mythic protagonist; she **is** the IronFlame
- dark folk / mythic fantasy / haunted but resolute
- ember orange -> iron blue -> ash gray -> dawn gold
- living scenes, not slideshow frames
- advanced micro-animation, parallax, particles, audio-reactive light/FX, and selective integrated visualizer language
- rebuilt from scratch; old IronFlame MP4s are excluded as production sources

Production/recovery package includes `PROJECT.md`, `STATUS.md`, `LYRICS.md`, `VISUAL_DNA.md`, `SHOT_LIST.md`, `ASSET_MANIFEST.json`, `PROMPTS.md`, `QC.md`, `AUDIO_RECOVERY.md`, and `RENDER_HISTORY.md` on the song/archive snapshots.

Known delivered result: 12 scenes, 04:04.680, 1280x720 master plus 540p compact delivery. Exact final filenames/hashes/storage IDs remain a documented gap.

A 1536x1024 storyboard visible in the 2026-09-03 runtime is fingerprinted in `general/SESSION_ASSET_RECOVERY.md` as SHA-256 `27cbb1a5b7ac00f65f23ea3f57477781adbd725e6a8a2a8b18513ea8bd8bdc4b`.

### Silver Coin

Branch: [`song/silver-coin`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/silver-coin)  
Archive branch: `archive/video/silver-coin`  
General snapshot: `general/branch-snapshots/silver-coin/`  
Project path: `projects/silver-coin/`

Status: **V8 FINAL COMPLETE / QC PASSED**

Canonical style: **Living Pre-Raphaelite Folk Romanticism**

Core direction:
- luminous oil-brush surfaces, emerald-and-gold natural light, flowers and folk-period detail
- natural character performance and environmental motion inside a visibly painted world
- recurring blonde flower-crowned protagonist from the accepted reference direction
- village/road, tavern, musicians/fiddler, dancing crowd, workers/procession, merchant/barmaid, rain/lightning and coin imagery
- build living scenes, not a slideshow or sequence of slow zooms

Final master: `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`  
SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`  
Persistent Library ID: `libfile_acfb04300bd88191b67e23b2ad736870`

The final master is >100 MB, so GitHub preserves exact metadata/hashes while the large binary remains in persistent archive storage. The branch/general snapshot preserves the complete Git-tracked production state including source references, scripts, effects, timing maps, QC, manifests and representative media.

Reusable Silver Coin FX/tooling is also exposed directly at:
- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`

## Recovered / partial song projects

### Leave It by the Door

Branch: [`song/leave-it-by-the-door`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/leave-it-by-the-door)  
Archive branch: `archive/video/leave-it-by-the-door`  
General snapshot: `general/branch-snapshots/leave-it-by-the-door/`

Status: **Recovery / partial**

Recovered evidence: warm tavern narrative treatment and lyric-timed multi-image/living-scene experiments informed the canon workflow. Exact source audio, lyrics, render filenames, hashes, and confirmed delivery status have not yet been recovered.

### Sigh No More / Irish Eyes, Spanish Hair

Branch: [`song/sigh-no-more`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/sigh-no-more)  
Archive branch: `archive/video/sigh-no-more`  
General snapshot: `general/branch-snapshots/sigh-no-more/`

Status: **Recovery / partial**

Recovered evidence: Veo/Sora-style sequential video prompt architecture around Lake Hartwell, mountain roads, old houses, wet pavement, candlelight, rural night, Spanish hair, Irish eyes, and ancestral ghosts. No completed render was confirmed.

## Reference / prior experiments

Earlier experiments demonstrated:
- single-image living-cover animation
- rain/fog/glow/lightning compositing
- lyric-timed multi-image cuts
- warm tavern narrative treatment for “Leave It by the Door”
- efficient pre-rendered scene/loop assembly
- painterly motion transfer and music-directed living-painting methods
- Gaussian light/volumetric effects
- 2.5D depth-parallax scene graphs
- tiny-NeRF volumetric experiments
- temporal/pigment transitions and localized audio-reactive effect layers

The reusable methods are indexed through `docs/VISUAL_STYLE_CATALOG.md` and the `general/reusable/` trees.

## Adding a project

Create `song/<slug>` and `projects/<slug>/` with at minimum:
- `PROJECT.md`
- `STATUS.md`
- `LYRICS.md` if applicable
- `VISUAL_DNA.md`
- `EFFECTS_PLAN.md`
- `ASSET_MANIFEST.json`

Checkpoint during production. At a major milestone/final state, update this index, `general/ARCHIVE_INDEX.json`, the corresponding `general/branch-snapshots/<slug>/` snapshot, and a point-in-time `archive/video/<slug>` branch.
