# IronFlame V3 — Shot Package Checkpoint

Branch: `song/ironflame-20260905-0216`

This checkpoint records V3 progress while the project is still in shot-package / proof-building stage. It is **not** a final-assembly checkpoint.

## Current V3 coverage

Completed HD narrative blocks:

- 00:00–00:42
- 00:42–01:35
- 01:35–02:02
- 02:02–02:47
- 02:47–03:30
- 03:30–04:04.680

All current V3 blocks are 1920x1080 at 24 fps with the canonical remastered song timing. The supplied vertical reference videos are not used as the framing backbone; AI-generated widescreen hero imagery is the film material, with the reference videos serving as visual/motion DNA.

## Current visual rules

- no blurred/mirrored portrait-video filler;
- no magic gate / portal / doorway-vortex transition language;
- transitions must arise from existing scene elements such as contour/ribbon/light/orb movement;
- hero stills must behave as living scenes rather than static slideshow images;
- music timing is authoritative: beat/onset/section/lyric timing controls edit and motion decisions;
- story continuity remains encounter -> recognition -> transformation -> separation -> reconnection -> integration -> resolution.

## Shot-proof QC status

Current exported blocks have been checked for:

- runtime and audio presence;
- 1920x1080 framing;
- 24 fps;
- black-frame events;
- >=1.5 s accidental freeze stretches;
- SHA-256 identity records.

The late blocks 02:02–02:47, 02:47–03:30, and 03:30–04:04.680 currently report no black events and no >=1.5 s freeze events at the selected shot-proof threshold.

## FX gate status

The repository FX V2 precompile gate remains a hard requirement when an effect/transition is promoted into the production compile path. We are not at final assembly yet.

Do not claim an effect is gate-approved merely because a shot proof rendered successfully. Production promotion requires the exact project FX manifest, approved registry status/proof coverage, generated `fx.lock.json`, and lock verification immediately before production compile according to `general/reusable/fx_v2/PRECOMPILE_FX_GATE.md`.

Current work remains shot-package/proof development. Custom shot behavior must preserve source/method/parameters/proof/QC/keep-revise-reject evidence before promotion.

## Persistence

Large V3 proof/master blocks and their QC/hash files are stored in ChatGPT Library under:

`/AIVideoEdit/IronFlame_V3_20260905/`

Do not assemble a final master merely because coverage now spans the song. Next work is artistic review of each package, effect/transition proof validation, revisions where needed, and only later production manifest/lock and full timeline assembly.
