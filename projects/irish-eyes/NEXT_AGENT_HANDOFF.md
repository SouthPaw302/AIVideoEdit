# Irish Eyes — Next Agent Handoff

Branch: `song/irish-eyes`

This is the canonical recovery note for the next agent continuing the Irish Eyes music-video project.

## Current baseline

Use the last Brandi-based V4 master as the current visual baseline:

`/mnt/data/irish_eyes_movie_assets/IRISH_EYES_V4_REVIEW_MASTER.mp4`

Verified properties:

- duration: 187.120000 s
- resolution: 720x1280 portrait
- frame rate: 30 fps
- total video frames: 5,611
- SHA-256: `4ac2a1e3f8b4556d0a384029686cfdf246042c81fed6a9b38a0592fd74637614`

Do not substitute the discarded clean-room visualizer experiment for this baseline.

## Full-frame extraction of the V4 baseline

Every frame of the V4 master has been extracted one-by-one into:

`/mnt/data/irish_eyes_v4_frames/`

Verified extraction:

- 5,611 PNG frames
- first: `frame_000001.png`
- last: `frame_005611.png`
- resolution: 720x1280
- no missing sequential frame numbers
- total folder size at handoff: 5,554,819,589 bytes (~5.17 GiB)
- manifest: `/mnt/data/irish_eyes_v4_frames/FRAME_MANIFEST.csv`

`FRAME_MANIFEST.csv` maps each extracted frame to its timestamp at 30 fps.

The frame folder is intentionally a local production artifact because of its size; it is not represented as 5,611 binary PNG files in GitHub. This handoff records its exact workspace location and verified count.

## User directives that remain binding

1. **No image/asset previews in chat unless the user explicitly asks.** Internal QC images/contact sheets are fine; do not surface them.
2. Keep this production in the current project/chat workflow. **Do not move it to ChatGPT Work unless the user explicitly asks.**
3. The user wants a real music movie, not a slideshow, visualizer, or barely visible effect pass.
4. Use the repository's existing reusable effect stack instead of recreating the style from scratch.
5. Effects must be visibly present in the final exported video and checked after export.
6. Scan/QC the actual final video before presenting it. Do not assume a render is good because the code completed.
7. Keep meaningful production decisions/checkpoints on GitHub so another agent can recover immediately.
8. User specifically asked to keep the entry shoreline footage with the boy and remove the busier beach/crowd/high-rise footage from future Brandi-based builds.
9. The supplied Brandi footage is an identity/reality anchor, but the user does not want it to be the only media in the movie.
10. The user may supply more B-roll if a specific missing scene would materially help.

## Clean-room experiment status

A later fully procedural clean-room version was attempted and rejected by the user because it collapsed into an abstract visualizer/dot-like result rather than cinematic authored media.

The user explicitly ordered that version and its artifacts deleted.

Do not revive it, do not treat it as a candidate master, and do not reuse its visualizer approach.

The current baseline remains the Brandi V4 master above.

## Existing reusable effects to use

Repository-wide reusable stack on `main` includes, among other tools:

- `general/reusable/depth-parallax-25d/`
  - continuous depth-field 2.5D parallax
- `general/reusable/irish-eyes-tools/south_florida_memory_fx.py`
  - restoration
  - audio-reactive water shimmer
  - halation/bloom
- `general/reusable/silver-coin-tools/video_fx/`
  - camera breathing / motion signatures
  - volumetric/light-shaft language
  - lightning / wet-reflection effects
  - temporal motion extensions
  - prism/refraction-like treatments
  - reusable temporal QC tooling

For Irish Eyes, the approved effect language includes:

- strong but photoreal 2.5D depth differential
- water/reflection distortion
- halation / motivated bloom
- prism/chromatic edge separation
- temporal echo trails where aesthetically useful
- storm haze / volumetric light shafts
- lightning/reflection accents
- audio-reactive modulation driven by `Irish eyes (Remastered).wav`

Do not dial these down until they become invisible.

## Important prior QC lessons

- Earlier real-motion loops with long crossfades produced double-image ghosting and were rejected.
- Earlier dream transitions with prolonged full-body dissolves produced identity double exposure and were rejected.
- One V4 Brandi 2.5D insert initially read almost like a still; it was rerendered with stronger motion after freeze detection exposed the issue.
- The boy shoreline source had a white foreground pole/sign sweep late in one section; the accepted V4 rebuild removed that obstruction.
- Full-runtime scanning is mandatory because individual effect proofs can pass while the final timeline still fails.

## Relevant project documents

Read these before changing the movie:

- `projects/irish-eyes/PRODUCTION_RULES.md`
- `projects/irish-eyes/USER_DIRECTIVES.md`
- `projects/irish-eyes/LYRIC_FILM_MAP.md`
- `projects/irish-eyes/EFFECT_PROOF_01.md`
- `projects/irish-eyes/EFFECT_PROOF_02_25D.md`
- `projects/irish-eyes/ACTUAL_MOVIE_ASSET_MANIFEST.md`
- `projects/irish-eyes/BROLL_INGEST_01.md`
- `projects/irish-eyes/V4_EFFECTS_REBUILD.md`

If a listed document has moved or been renamed, inspect the current `projects/irish-eyes/` tree before guessing.

## What happened immediately before this handoff

The user asked to return to the last Brandi version before the clean-room attempt and then requested a frame-by-frame extraction of that V4 master.

That extraction is complete and verified.

The user then requested this handoff be saved for the next agent.

## Start point for next agent

1. Treat `IRISH_EYES_V4_REVIEW_MASTER.mp4` as source/master baseline.
2. Treat `/mnt/data/irish_eyes_v4_frames/` as the canonical frame-level working set for the current pass.
3. Read the production rules and user directives before making changes.
4. Do **not** show frame/contact-sheet previews in chat.
5. Do **not** start a new visualizer/clean-room direction.
6. Do not code/render new work until the user's next instruction if this handoff is being read immediately after creation.
7. When new work begins, use the frame set for deliberate frame-level inspection, enhancement, masking, depth work, effect placement, continuity analysis, and targeted shot replacement—not merely automated global filtering.
8. After any full render, scan the exported file itself for black frames, freezes, repeated sections, visible effect presence, removed-footage leakage, and continuity before delivery.

## Repository state note

The useful V4/effect work remains the active production lineage. The rejected clean-room experiment was removed from the working direction and should not influence future agents.

This handoff should be updated whenever the accepted baseline or frame-level working set changes.
