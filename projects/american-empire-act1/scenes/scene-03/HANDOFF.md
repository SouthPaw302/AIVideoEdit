# Scene 03 Production Handoff

## Authority

Work only on `project/american-empire-act1/scene-03`. Repository `main` remains the AIVideoEdit OS and reusable-FX authority; `project/american-empire-act1/main` is the film integration branch.

Read before continuing:
- `SCENE03_CONTINUATION_DIRECTIVE.md`
- `SCENE03_CONTINUATION_ARCHITECTURE.json`
- `SCENE03_ZERO_DRIFT_PROMPT_PACK.json`
- `SCENE03_FX_EXECUTION_PLAN.json`
- `SCENE03_MEDIA_AUDIT.json`
- `STATUS.md`
- `PROJECT_STATE.json`
- `ASSEMBLY05_MEDIA_PLAN.json`
- locked `SCRIPT.json`
- `STORYBOARD_LOCKED.md`
- `VISUAL_DNA.md`
- project `MOTION_LANGUAGE.md`
- `PRIME_DIRECTIVE.md`
- `general/reusable/ZERO_DRIFT_DIRECTOR_DIRECTIVE.md`
- current-main `general/reusable/fx_v2/registry.json`

## Resume state

Scene 03 is assembled at exactly 98.000 seconds / 2352 frames / 24 fps / 1280x720.

Current review candidate:

`Scene03_ASSEMBLY05_MULTIIMAGE_GIF_FX_REVIEW_COMPACT.mp4`

SHA-256 `3969e3a12020d5f7d7cd71a80ba0a8f19833ba55d164188d03fd86d6e8eaa9b1`

Assembly02 remains the immutable approved pre-production rollback/reference for feel, Claire continuity, Paris/city design, shot order and score timing. It is not the current resume candidate.

## Full-media rule

The eight Scene 03 heroes are continuity/composition anchors, **not the complete source library and not an editorial cap**.

Continue from the full approved/promoted Scene 03 media pool. Assembly05 currently uses 29 clean media segments across the eight locked storyboard beats, but those 29 segments are not a maximum. Inventory and use non-hero stills, approved/promoted variations, matched-angle companions, actual GIF assets, source-derived continuity media, canonical recovery assets and valid project-local FX where they improve the scene and pass continuity/QC.

Do not silently omit approved/promoted assets merely because they are not heroes. Map each approved/promoted asset to a beat/shot role or record a concrete reason it is not used.

Filename text alone is not lifecycle authority. Some legacy files retain `REJECTED` in their filename but were subsequently promoted by explicit user approval and are marked approved in `ASSET_MANIFEST.json`; those are usable. Genuinely rejected collage/drift media remains excluded unless explicitly promoted by the current user.

`SCENE03_MEDIA_AUDIT.json` records the current Drive inventory. Opaque `file_*.png` media must be semantically matched to canonical provenance before final use rather than guessed into a beat.

## Main FX rule

Use the reusable FX resources from current repository `main`, not a hero-only local effect recipe. The current authority pin for this continuation is main commit `0126b1c2978dc96810a02956a270feccdf02bdcf` and FX registry blob `64eaf9b7b681e1868532c9ed690fc31c88b23312`.

`SCENE03_FX_EXECUTION_PLAN.json` compiles Scene 03 against approved current-main FX only, including appropriate use of canvas lock, practical/source-driven light, rain, atmospheric depth, restrained pseudo-depth, wet-road/reflection effects and approved promoted effect adapters. Existing proved project-local micro-motion and matched-angle assets remain valid source coverage.

Do not auto-use `proof_required`, `conditional` or `unavailable` FX. In particular, do not blindly apply the stale unavailable effect referenced by the older coherent-storm preset. Fail closed or produce a scene-local proof first.

## Execution implementation

`render_scene03_assembly06_fullmedia_fx.py` is the traceable Assembly06 execution scaffold. It:
- preserves exactly 2352 frames / 98.000 s;
- starts from Assembly05 coverage but adds eligible full-media audit coverage;
- resolves `S3_GEN_` aliases and approved hero/GIF companions;
- validates every requested reusable FX ID against the current-main registry;
- applies only `gate_status=approved` FX automatically;
- keeps exterior rain out of identified interior coverage;
- generates a coverage report documenting resolved, missing, deduplicated and excluded media;
- muxes the locked score and captions after picture render.

Use `--dry-run` first against the restored media workspace to verify coverage before rendering picture.

## Current motion implementation

Maintain source-locked, bounded movement. Existing matched-angle pairs, GIF assets, registered diegetic FX and clean multi-image coverage may be used where compatible with the locked world. Do not redraw Claire, props, architecture or scene topology to manufacture motion.

Use Scene 01 as the motion-language baseline: world/character/weather/light/depth motion before camera motion.

## Next phase

Run the Assembly06 full-media resolver against the restored Scene 03 media workspace, inspect its coverage report, then render the main-FX picture pass. Compare against Assembly05 and Assembly02. Keep only improvements that preserve canon and the Scene 01 motion language.

After picture review, run final semantic/action QC, temporal continuity QC, zero-drift QC, caption/sound-boundary checks and terminal-frame QC.

Do not promote to accepted master without current-user approval.

## Non-negotiable

- Preserve Claire identity, anatomy, dark wavy hair, phone, approved essential and wardrobe continuity.
- Preserve the eight locked storyboard beat functions and exact 98-second score/frame map.
- Preserve locked dialogue wording.
- Preserve Paris apartment/corridor/elevator/lobby/street geography and storm logic.
- Use the full approved/promoted Scene 03 media pool, not only eight heroes.
- Use approved current-main FX resources where semantically appropriate; do not apply every effect indiscriminately.
- Do not collapse back to one image per storyboard beat.
- No fake handheld, global wobble, oscillating crop, endless zoom, identity drift or topology mutation.
- Keep weather/light/system effects physically registered.
- Drive uploads remain checkpoint/final-handoff storage, not constant scratch synchronization.
