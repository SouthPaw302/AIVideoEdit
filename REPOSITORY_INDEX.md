# AIVideoEdit Repository and Recovery Index

This is the durable index for the ChatGPT **Video Creation** project. It maps the system, projects, branches, styles, and recoverable assets so a future agent can resume without relying on chat history.

## Canon entrypoints

| Path | Purpose |
|---|---|
| `AGENT_HANDOFF.md` | Primary operating instructions for every new agent/chat |
| `README.md` | Short repository orientation |
| `REPOSITORY_INDEX.md` | Complete recovery map and branch registry |
| `PROJECT_INDEX.md` | Active and reference production registry |
| `docs/CANON_WORKFLOW.md` | Ten-phase music-video production workflow |
| `docs/VISUAL_STYLE_CATALOG.md` | Named rendering, animation, narrative, visualizer, and transition languages |
| `docs/ARCHITECTURE.md` | Direction, asset, QC, animation, edit, render, and archive layers |
| `docs/STORAGE_AND_CONNECTORS.md` | GitHub/workspace/object-storage roles and connector rules |
| `projects/PROJECT_TEMPLATE.md` | Required structure for every new song |

## Branch registry

| Branch | Scope | Current role |
|---|---|---|
| `main` | Repository-wide canon and merged project records | Default recovery branch |
| `song/silver-coin` | Silver Coin production | Active song branch; Living Pre-Raphaelite Folk Romanticism locked |

New songs should normally use `song/<slug>`. A future agent must check `PROJECT_INDEX.md` before assuming the active branch.

## Project registry

### IronFlame

- Canonical path on `main`: `projects/ironflame/`
- Status source: `projects/ironflame/STATUS.md`
- Core files: `PROJECT.md`, `LYRICS.md`, `VISUAL_DNA.md`, `SHOT_LIST.md`, `PROMPTS.md`, `QC.md`, `ASSET_MANIFEST.json`, `AUDIO_RECOVERY.md`
- Assets include analysis, source/reference imagery, production images, QC material, and lossless-audio recovery parts.
- Critical canon: the IronFlame is a woman; the canonical film is rebuilt from scratch.

### Silver Coin

- Active branch: `song/silver-coin`
- Project path: `projects/silver-coin/`
- Canonical style: **Living Pre-Raphaelite Folk Romanticism**
- Narrative world already associated with the project: muddy village/road and wagon imagery, warm firelit tavern interiors, musicians and fiddler performance, dancing crowds, merchant/barmaid action, and recurring silver-coin symbolism.
- Required recovery files: `PROJECT.md`, `STATUS.md`, `LYRICS.md`, `VISUAL_DNA.md`, `STYLE_REFERENCE.md`, and `ASSET_MANIFEST.json`
- Small GitHub reference still and motion preview preserve the supplied style even when the original attachments are unavailable.

## Silver Coin durable source references

### Canonical audio

- Filename: `Silver Coin  (Remastered).wav`
- SHA-256: `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`
- Format: 48 kHz, stereo, 16-bit PCM WAV
- Duration: 207.440 seconds
- Library reference recorded in the song manifest; the full source is not duplicated here.

### Supplied visual-style clips

1. `imagine-d04b484c.mp4`
   - SHA-256: `8f14739f3eb4f7e7dcc639dfe9fab398623f4a7b5c31ce8b2c0131fab89e6c9c`
   - 560 x 560, 24 fps, 6.041667 seconds
2. `imagine-5558fc80.mp4`
   - SHA-256: `162b3c5cf6c41cc1b85800a1e6111a94df3e3dd829935521aa8c90de15e51803`
   - 560 x 560, 24 fps, 6.041667 seconds

The originals define the canonical look and motion. Reduced GitHub previews are recovery aids, not generation masters.

## Production and chat discipline

- One major music-video production per fresh chat when practical.
- One song branch per production.
- GitHub is the persistent brain; large masters normally remain in Library/workspace/object storage.
- Store small critical previews in GitHub when losing them would make the style ambiguous.
- Update `STATUS.md` and manifests after meaningful work and before handing off.
- Record rejections as well as approvals so later agents do not repeat failed directions.
- Preserve shot ratings, timing decisions, prompts, continuity rules, hashes, and archive references.

## What “indexed” means

A recoverable project records:

1. branch and project path;
2. canonical source filenames and hashes;
3. available storage or Library references;
4. named visual style and precise visual DNA;
5. representative reference still/motion preview when practical;
6. current state, completed work, rejected directions, and exact next action;
7. shot/timing/QC data as production matures.

## Mandatory recovery sequence

1. Start on `main` and read `AGENT_HANDOFF.md`.
2. Read this file and `PROJECT_INDEX.md`.
3. Identify and switch to the active song branch.
4. Read the complete active project directory.
5. Resolve original media through `ASSET_MANIFEST.json`.
6. Continue from `STATUS.md`; do not reconstruct settled decisions from memory.
