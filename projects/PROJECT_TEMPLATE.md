# AIVideoEdit Project Template

Copy this structure into `projects/<song-slug>/` on a dedicated `song/<slug>` branch.

Before starting production, read `AGENT_HANDOFF.md`, `BIBLE.md`, `general/reusable/PRODUCTION_PIPELINE.md`, and `general/reusable/STYLE_CONTRACT.md` from `main`.

## Required files

### `PROJECT.md`

Stable concept, source material, non-negotiable rules, branch, project path, and creative identity.

### `STATUS.md`

Living handoff document. Update after every meaningful phase and before changing chats/agents.

Minimum fields:

- updated date and branch
- state
- canonical source assets
- completed work
- rejected/superseded work
- current approved direction
- known artifact/technical issues
- storage locations/references
- exact next actions

### `LYRICS.md`

Use when lyrics materially drive direction. Preserve verified user-approved canonical text. Never invent missing lyrics.

### `VISUAL_DNA.md`

Document:

- emotion arc and world
- primary/secondary style using `general/reusable/STYLE_CONTRACT.md` as the acceptance boundary
- subject/character continuity
- palette, lighting, and textures
- camera language
- motion density and loop strategy
- audio-reactive logic
- visualizer role
- transition language
- ending logic
- failure modes to reject

### `EFFECTS_PLAN.md`

Map chosen canonical techniques to story purpose, song section/shot, audio driver, intensity, implementation/test path, and approval/QC state. Reuse the registry before inventing new effects.

### `DECISIONS.md`

Dated approval/rejection log. Preserve reasons so future agents do not repeat failed directions.

### `ASSET_MANIFEST.json`

Track source audio, references, generated images, masks/layers, effect tests, scene renders, masters, delivery files, hashes, technical metadata, approval states, and storage IDs/URIs.

## Add as production matures

- `STYLE_REFERENCE.md`
- `SHOT_LIST.md` or `shots.json`
- `PROMPTS.md`
- `RENDER_MANIFEST.json`
- `QC.md` or `qc.json`
- `RENDER_HISTORY.md`
- `references/`
- `assets/analysis/`
- `assets/stills/`
- `assets/effects/`
- `assets/scenes/`
- `assets/qc/`
- `shot_packages/<shot_id>/` using the package layout in `general/reusable/PRODUCTION_PIPELINE.md`

## Continuous checkpoint rule

Follow the checkpoint and handoff rules in `AGENT_HANDOFF.md` and `BIBLE.md`: make meaningful durable checkpoints, keep `STATUS.md` executable, preserve asset identities and recovery locations, and do not postpone all repository updates until the end of a long production session.

A new agent must be able to continue by reading GitHub, switching to the correct branch, resolving media through the manifest, and executing the exact next action in `STATUS.md`.
