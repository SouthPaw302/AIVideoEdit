# IronFlameNew FX Plan — Proof Stage

Do **not** treat this as the gate manifest yet. `FX_REQUIREMENTS.fx.json` remains uncompiled until actual renderer inputs and accepted shot recipes are known.

## Approved FX2 runtime candidates for first proofs
- `FX2-MOTION-002` — localized living flow
- `FX2-ATM-001` — advected smoke/haze where motivated
- `FX2-ATM-002` — rain plane for exterior / window scenes
- `FX2-LIGHT-001` — practical light breath
- `FX2-LIGHT-002` — moving light field
- `FX2-SURFACE-001` — temporal canvas/surface lock when appropriate

Use conservative strengths and prove visibility. Internal scene motion first; camera second.

## Spatial candidates
`FX2-MOTION-001`, `FX2-SPATIAL-001`, `FX2-SPATIAL-004`, NeRF and 3DGS paths are **not** automatically approved for production. For this film, create real/authored depth maps for selected hero stills and make truthful project proofs before claiming production spatial depth. No fake 3DGS/NeRF labels.

## Transition policy
No transition ID is locked yet. Current transition entries are proof-gated. The preferred *visual grammar* is motivated continuity through light, contour, reflection, rain, ribbon, hand contact, or architectural texture — never a portal/gate motif. A transition must be proven at its real duration before it enters the production manifest.

## Audio mapping
Use one preserved frame-aligned 24 fps control bus. Suggested mapping: low/rms → depth/light amplitude; mid → contour/ribbon density; high → small highlights/rain/dust; onset → brief motivated accents/cuts. Avoid generic strobing.
