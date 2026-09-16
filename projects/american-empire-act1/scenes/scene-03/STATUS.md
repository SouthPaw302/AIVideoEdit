# Scene 03 — Status

Branch: `project/american-empire-act1/scene-03`  
Canonical project root: `project/american-empire-act1/main`  
Stage: `ASSEMBLED / ASSEMBLY02_PREPRODUCTION_APPROVED / ASSEMBLY05_MULTIIMAGE_REVIEW / ASSEMBLY06_FULLMEDIA_FX_PREPARED`

## Continuity and timing
- Starts from the actual extracted final frame of Scene 02.
- Score authority: `L'Atmosphère.wav`.
- Duration: `98.000 s`; frame rate: `24 fps`; frames: `2352`; resolution: `1280x720`.

## Approved foundation
Assembly02 remains the immutable user-approved pre-production reference for feel, Claire continuity, Paris/city design, shot order and score timing.

Assembly03 established the approved effects direction. Assembly04 demonstrated artifact cleanup but still inherited the overly literal one-storyboard-image-per-beat structure.

## Assembly05 — current review candidate
Assembly05 corrects the structural problem identified by the user: the eight storyboard beats are timing/narrative authority, not eight final picture cards. The scene uses 29 existing clean media segments while retaining the original eight beat durations.

`Scene03_ASSEMBLY05_MULTIIMAGE_GIF_FX_REVIEW_COMPACT.mp4`
- SHA-256 `3969e3a12020d5f7d7cd71a80ba0a8f19833ba55d164188d03fd86d6e8eaa9b1`
- exact `98.000 s`
- exact `2352` frames
- `1280x720`, `24 fps`
- existing Scene 03 audio retained
- 29 media segments across 8 storyboard beats
- actual GIF shot assets generated from the existing still pool
- deterministic A/B slight-movement companions generated for still media
- no new image generation in this pass
- production/debug storyboard labels are not used as final picture media

The exact segment map is recorded in `ASSEMBLY05_MEDIA_PLAN.json`.

## Full-media continuation rule
The 29 Assembly05 segments are the current cut, not the full source-library ceiling. The eight hero frames are continuity anchors, not exclusive picture media.

`SCENE03_MEDIA_AUDIT.json` inventories the broader usable/promoted media currently visible in Drive and explicitly preserves promoted legacy assets even when their old filename still contains `REJECTED`. Truly rejected collage attempts remain excluded. Opaque `file_*.png` files remain fail-closed until matched to known provenance/semantic content rather than guessed into the edit.

## Main FX integration prepared
Scene 03 consumes current repository `main` through bootstrap. The current continuation pins main commit `0126b1c2978dc96810a02956a270feccdf02bdcf` and FX registry blob `64eaf9b7b681e1868532c9ed690fc31c88b23312` as execution authority.

`SCENE03_FX_EXECUTION_PLAN.json` maps each locked Scene 03 shot to approved main-FX resources only. It deliberately skips registry entries that are proof-required, conditional or unavailable unless a valid scene-local proof exists.

`render_scene03_assembly06_fullmedia_fx.py` is now the traceable Assembly06 renderer scaffold. It preserves the locked frame count, begins from Assembly05 coverage, adds eligible broader Scene 03 media, validates FX against current main, produces a coverage report, applies appropriate approved runtime/promoted effects, and remuxes the locked score/captions.

The new renderer commit passed both repository gates:
- AIVideoEdit Main System Verification — success
- AIVideoEdit Production Contract — success

No Assembly06 master has been promoted or accepted yet.

## Drive/audio state
The Scene 03 Drive folder contains the broader Generated Images pool, Reference Frames, recovery batches, generated rebuild candidates, prior effect/action passes, and the score/stems authority. The existing score analysis already records the required 48 kHz stereo master, exact edit range, structural markers and mix policy; no replacement WAV is required for this preparation pass.

## Exact next action
1. Restore/download the Scene 03 media workspace.
2. Run `render_scene03_assembly06_fullmedia_fx.py --dry-run` to produce the full-media coverage resolution report.
3. Resolve any required missing/provenance mismatches without guessing.
4. Render Assembly06 using the approved main-FX plan.
5. Compare Assembly06 against Assembly05 and Assembly02 for pacing, continuity, FX visibility and Scene 01 motion-language compliance.
6. Run final semantic/action, temporal, caption/audio and zero-drift QC before any master promotion.

## Remaining master blockers
- Assembly06 full-media resolution/render execution
- visual comparison against Assembly05/Assembly02
- final semantic/action and mode-aware QC
- current-user master acceptance

Do not collapse the scene back to one image per storyboard beat. Assembly02 remains the pre-production rollback authority; Assembly05 remains the current review candidate until a better candidate passes review.
