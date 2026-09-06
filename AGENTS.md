# AIVideoEdit Universal Agent Contract

This file applies to **any agent or automation** working in this repository: hosted agents, coding agents, chat agents, local agents, future agents, scripts, and human-operated automation.

## Authority
1. Current explicit user instruction.
2. Active `song/<slug>` branch state/manifests.
3. Current `main` contracts and reusable systems.

Nothing else is automatically authoritative. Historical chats, summaries, unrelated production branches, old visual DNA/storyboards, prior generated media, and project-specific provenance are prohibited as production inputs unless the current user explicitly authorizes them.

## Mandatory boot
1. Read `general/reusable/PRODUCTION_CONTRACT.json`.
2. Read `SYSTEM_INDEX.md` and `general/reusable/MEDIA_CAPABILITY_MATRIX.json`.
3. Read `general/reusable/fx_v2/registry.json` and its gate documentation before FX selection.
4. Run `python general/reusable/tools/production_guard.py --branch <current-branch>` before advancing a production stage.

## Non-negotiable sequence
Source ingest -> reference extraction/analysis -> visual/media approach -> storyboard -> shot packages -> short finished proofs -> FX lock -> assembly -> actual-export QC -> archive.

Short reference videos are fully extracted. Long references use recorded meaningful sampling. If there is no visual reference, no original media may be generated until the proposed story/visual/media approach has been shown to the user and recorded as established.

A storyboard is never a substitute for shot production. A successful command is never artistic QC. Effects must be visible and traceable. Technology names must be truthful.
