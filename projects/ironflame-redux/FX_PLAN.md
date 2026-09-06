# IronFlameRedux FX Plan

Status: **creative families selected from storyboard; production FX manifest not yet locked.**

Only registry-approved effects may enter a production `.fx.json` manifest without first completing the repo's proof/promotion requirements. The board requests several effect families; this plan separates usable canon from blocked candidates.

## Approved canonical FX suitable for Redux proofs
- `FX2-MOTION-002` — localized_living_flow: localized internal scene motion.
- `FX2-ATM-001` — advected_smoke: forge/battle/ruin atmosphere.
- `FX2-ATM-002` — rain_plane: selected exterior weather.
- `FX2-FIRE-001` — living_flame: forge, practical fire, chorus ignition.
- `FX2-FIRE-002` — embers: forge/battle/legacy particle layer.
- `FX2-LIGHT-001` — practical_light_breath: fire/candle/forge-driven illumination.
- `FX2-LIGHT-002` — moving_light_field: subtle motivated light movement.
- `FX2-SURFACE-001` — temporal_canvas_lock: only when the shot's surface treatment benefits and identity detail remains intact.

These IDs are candidates, not blanket permissions. Each shot manifest must request only what is visibly needed.

## Storyboard-requested families currently blocked from production use
- `FX2-SPATIAL-001` hybrid_25d — `proof_required`.
- `FX2-SPATIAL-004` streaming_living_parallax — `proof_required`.
- `FX2-LIGHT-003` localized_glint — `proof_required`.
- `FX2-LIGHT-004` temporal_palette_migration — `proof_required`.
- `FX2-ATM-003` rain_glass — `proof_required`.
- `FX2-TRANS-001..005` — transition entries remain `proof_required` in the current registry.

Do not silently substitute an unapproved look-alike and claim the blocked ID. If a blocked technique becomes necessary, prove/promote it according to repo law before production use, or use a separately authored non-FX compositing/camera method whose technical identity is documented truthfully and passes shot QC.

## Spatial truthfulness
The storyboard wants parallax/depth. Do not call 2D Gaussian overlays 3DGS, and do not call image-space parallax NeRF. Real 3DGS is conditional and requires genuine splat geometry plus a PASS preflight. For the first Redux proofs, prioritize source/layer construction and identity-safe motion; choose the final spatial path only after the source imagery exists and can be tested.

## Audio-reactive mapping
Once the Redux master is received, derive one preserved 24 fps control bus and map it approximately as follows:
- low/bass -> `living_flame` intensity and glow;
- mids -> spark/ember density;
- highs/transients -> brief highlight/ember accents and cut emphasis;
- vocal/melodic focus -> depth/focus/light attention;
- sustained/reverb energy -> smoke/fog density.

Do not reuse historical IronFlame control data unless the user explicitly makes that audio/control source part of Redux.

## First proof stack
Start with four representative short proofs rather than full assembly:
1. forge shot: motion + flame + embers + practical light + smoke;
2. heroine close-up: localized motion + practical/moving light with identity QC;
3. iron-blue exterior: localized motion + rain/smoke + moving light;
4. dawn/ruin: localized motion + atmosphere + restrained light.

For every real render: declare exact `render_inputs`, run `precompile_gate.py`, generate schema-v2 `fx.lock.json`, verify the lock immediately before compile, then inspect the exported pixels. Gate PASS is not artistic approval.
