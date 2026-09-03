# Continuous GitHub Checkpoint Policy

This policy implements the user's requirement that AIVideoEdit survive chat freezes, context/cache limits, failed tool runs, and agent handoffs.

## Core rule

**Do not wait until the end of a production session to update GitHub.** Work in recoverable phases and commit the active song branch after every meaningful phase.

## Required checkpoint events

Checkpoint after:

1. receiving and fingerprinting source audio or a visual reference;
2. approving or changing story, style, character, palette, format, or effects;
3. completing audio, lyric, beat, section, or emotional-arc analysis;
4. generating/reviewing a meaningful image batch;
5. approving, rejecting, repairing, or replacing an image;
6. creating/evaluating a motion, loop, transition, or effects test;
7. changing prompts, shot list, timing map, scene graph, or continuity rules;
8. producing an intermediate scene segment, assembly, master, or delivery encode;
9. finding/resolving a material QC problem;
10. moving an asset between workspace, Library, GitHub, or object storage;
11. beginning another expensive generation/render phase;
12. leaving the chat, switching agents, or approaching a context/tool limit.

## Minimum checkpoint contents

Update the files affected by the work:

- `STATUS.md` — current state, completed/rejected work, blockers, exact next action
- `DECISIONS.md` — approved and rejected creative/technical decisions
- `ASSET_MANIFEST.json` — filenames, hashes, dimensions/duration, storage, IDs, approval state
- `VISUAL_DNA.md` — locked story/style/camera/motion/transition language
- `EFFECTS_PLAN.md` — effects selected from the repository catalog and their actual use
- `PROMPTS.md` — prompt versions tied to shots/assets
- `SHOT_LIST.md` or timeline data — timing and edit changes
- `QC.md` — visual, temporal, audio, render, and artifact results
- `RENDER_HISTORY.md` — every meaningful output encode

## Generated-image record

For each canonical or candidate image, preserve when available:

- project/shot ID
- prompt and prompt version
- generation tool/model
- generation date
- dimensions/format
- SHA-256
- GitHub path or external/Library ID
- character/style reference used
- approval state: candidate / approved / rejected / repaired / superseded
- QC notes and rejection reason

Commit practical-size canonical images and contact sheets to the song branch. If the full original is too large, commit a representative preview and record the original's hash and durable storage reference.

## Effects record

All effects begin from `docs/VISUAL_STYLE_CATALOG.md`.

Each song must have an `EFFECTS_PLAN.md` that states:

- selected technique
- narrative purpose
- scene/section
- audio driver, if reactive
- intensity and limits
- implementation or tool
- test asset path
- approval/QC state

Do not use every effect. Use only those serving the song's visual DNA.

## Commit size and frequency

A checkpoint should represent one meaningful recovery unit, not every tiny mechanical action. Save before the cost or risk of repeating the work becomes material.

## Branch rule

- global workflow/index updates -> `main`
- song production -> `song/<slug>`
- never mix two active song productions on one branch
- never leave a project only in chat

## Handoff test

Before pausing, ask: **Could a new agent start from GitHub, locate the correct branch and assets, understand approvals/rejections, and execute the exact next action without this chat?**

If not, the checkpoint is incomplete.
