# HANDOFF — Pandora clean rebuild

## Authority
Current explicit user instruction is to use the media/videos they supplied, scrap other agents' creative work such as v3, follow the repository, scan the whole repo, and build a real story before continuing.

## Current production state
- Branch: `song/the-door-between-the-seconds`
- Current-main Director Brain v2 is already merged into this branch.
- `PROJECT_STATE.json` was rolled back after the user rejected the prior v3 creative path and is now `STORYBOARD_LOCKED` after the clean story and 31-shot script passed both current-main guards.
- `OPERATING_ORDER.json` now exists and is Director Brain v2 authority.
- Direction authority: `music_led` with explicit current-user constraints.
- Production mode: `hybrid`.

## Locked canon
- Pandora the Vampire is the single protagonist/identity anchor.
- Verified lyrics and measured source master drive narrative timing.
- Six-second silent cold open before the song.
- Current user-supplied images and authorized source video may be used as final-picture material.
- Old v3 production-specific generated media, shot choices and renders are rejected as current creative authority.

## New story
Read `STORY.md` before doing anything else. Premise: Pandora enters a temporal house made from the moments she abandoned when she became a vampire. She is seeking the last human morning she never lived. The lyric's sleeping distance is the separation between her present vampire self and that buried human time; the apparent second Pandora is a reflection/temporal state of the same identity.

## Visual language
Read `VISUAL_DNA.md`. Red fabric/roses are the continuity thread; rain, inward windows, footprints, iron, mirrors, candles, cathedral distance, crypt stone and pale underground dawn each have explicit story jobs.

## Source analysis
- WAV: 163.12 s; measured tempo 112.347 BPM.
- `rebuild_v1/analysis/edit_map.json` and `reactive_controls.json` were regenerated from the current user WAV.
- Current user long source video was sampled across its full duration; it is primarily one living Pandora chamber/window composition rather than conventional multi-shot coverage.
- Short window benchmark: all 240 frames extracted under `rebuild_v1/reference_samples/window_all/`.
- Fifteen current-chat images were visually inspected and assigned story roles in `REFERENCE_MANIFEST.json`; their exact binary bytes still need addressable ingestion before shot packages can claim hashes.

## Forbidden drift
Do not resume `production/generated_scene_bank`, `production/final_pandora_v2_gate`, old v3 `shot_packages`, `production/v3_snapshot_inputs`, or prior v3 story/shot choices as production truth. Reusable main tools are allowed; v3-specific creative decisions are not.

## Storyboard/script state
The clean rebuild now has a fresh locked 31-shot / 5074-frame storyboard and hybrid `SCRIPT.json`. It passed both current-main guards at `STORYBOARD_LOCKED`.

## Exact next action
Make the fifteen current-chat image binaries addressable, then create fresh `rebuild_v1/shot_packages/` with hashes and real media evidence. Build representative living-scene/cinematic proofs before FX lock or assembly.
