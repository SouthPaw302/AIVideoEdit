# AIVideoEdit Project Template

Copy this structure into `projects/<song-slug>/` for every new production.

## Required files

### `PROJECT.md`
Stable concept, non-negotiable rules, source material, and creative identity.

### `STATUS.md`
Living handoff document. Update after meaningful work and before changing chats/agents.

Minimum fields:
- state
- canonical source assets
- completed work
- rejected ideas
- current approved direction
- known artifact/technical issues
- storage locations/references
- exact next actions

### `LYRICS.md`
Use when lyrics materially drive direction. Preserve user-approved canonical text.

### `VISUAL_DNA.md`
Document:
- emotion arc
- world type
- subject/character continuity
- palette
- textures
- camera language
- animation density
- visualizer role
- transition language
- ending logic

## Recommended future files

- `SHOT_LIST.md` or `shots.json`
- `ASSET_MANIFEST.json`
- `RENDER_MANIFEST.json`
- `QC.md` or `qc.json`
- `PROMPTS.md`
- `DECISIONS.md`

## Handoff rule

A new agent must be able to continue the project by reading GitHub alone and then resolving any large media through the asset manifest/project storage.

Do not leave critical decisions only inside chat history.