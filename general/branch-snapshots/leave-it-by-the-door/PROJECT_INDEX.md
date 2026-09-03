# Project Index

This file tracks productions inside AIVideoEdit. Each project must be recoverable from GitHub without relying on chat history.

## Active

### IronFlame
Branch: [`song/ironflame`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/ironflame)  
Project path on branch: `projects/ironflame/`

Status: **V1 rendered and delivered / Final MP4 archive references must be recovered**

Purpose: First full flagship project for the canonical AIVideoEdit workflow.

Core direction:
- female mythic protagonist; she **is** the IronFlame
- dark folk / mythic fantasy / haunted but resolute
- ember orange -> iron blue -> ash gray -> dawn gold
- living scenes, not slideshow frames
- advanced micro-animation, parallax, particles, audio-reactive light/FX, and selective integrated visualizer language
- rebuilt from scratch; old IronFlame MP4s are excluded as production sources

Read:
- `projects/ironflame/PROJECT.md`
- `projects/ironflame/STATUS.md`
- `projects/ironflame/LYRICS.md`
- `projects/ironflame/VISUAL_DNA.md`

Production package:
- `projects/ironflame/SHOT_LIST.md`
- `projects/ironflame/ASSET_MANIFEST.json`
- `projects/ironflame/PROMPTS.md`
- `projects/ironflame/QC.md`
- `projects/ironflame/AUDIO_RECOVERY.md`
- `projects/ironflame/RENDER_HISTORY.md`

### Silver Coin
Branch: [`song/silver-coin`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/silver-coin)  
Project path on branch: `projects/silver-coin/`

Status: **Visual style locked / Project and references indexed**

Core direction:
- canonical style: **Living Pre-Raphaelite Folk Romanticism**
- luminous oil-brush surfaces, emerald-and-gold natural light, flowers and folk-period detail
- natural character performance and environmental motion inside a visibly painted world
- adapt the style to Silver Coin's village, road, tavern, musicians, dancing crowd, merchant/barmaid, and coin imagery
- the square source clips define painting surface and motion quality; they do not dictate final aspect ratio or literal characters
- build living scenes, not a slideshow or a sequence of slow zooms

Recovery files on the song branch:
- `projects/silver-coin/PROJECT.md`
- `projects/silver-coin/STATUS.md`
- `projects/silver-coin/LYRICS.md`
- `projects/silver-coin/VISUAL_DNA.md`
- `projects/silver-coin/STYLE_REFERENCE.md`
- `projects/silver-coin/EFFECTS_PLAN.md`
- `projects/silver-coin/DECISIONS.md`
- `projects/silver-coin/ASSET_MANIFEST.json`

## Recovered / Partial Song Projects

### Leave It by the Door

Branch: [`song/leave-it-by-the-door`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/leave-it-by-the-door)

Recovered evidence: a warm tavern narrative treatment and lyric-timed multi-image/living-scene experiments informed the canon workflow. Exact source audio, lyrics, render filenames, hashes, and delivery status have not yet been recovered. The branch preserves this honestly as a recovery project rather than claiming completion.

### Sigh No More / Irish Eyes, Spanish Hair

Branch: [`song/sigh-no-more`](https://github.com/SouthPaw302/AIVideoEdit/tree/song/sigh-no-more)

Recovered evidence: Veo/Sora-style sequential video prompt architecture was drafted around Lake Hartwell, mountain roads, old houses, wet pavement, candlelight, rural night, Spanish hair, Irish eyes, and ancestral ghosts. No completed render was confirmed. The branch preserves the concept and next action.

## Reference / Prior Experiments

Earlier experiments in the working ChatGPT environment demonstrated:
- single-image living-cover animation
- rain/fog/glow/lightning compositing
- lyric-timed multi-image cuts
- warm tavern narrative treatment for “Leave It by the Door”
- efficient pre-rendered scene/loop assembly

These experiments informed the canon workflow, but their binary assets are not guaranteed to persist across sessions unless archived externally.

## Adding a project

Create `projects/<slug>/` with at minimum:
- `PROJECT.md`
- `STATUS.md`
- `LYRICS.md` if applicable
- `VISUAL_DNA.md`

Then add it to this index.