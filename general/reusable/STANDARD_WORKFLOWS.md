# Standard Workflow Library

These are project-neutral production workflows available to every production. The resolver selects them from the active production mode and `MEDIA_PLAN.json` capabilities. Historical production names are not runtime identities and are intentionally absent.

Authority: `STANDARD_WORKFLOW_REGISTRY.json`. Resolver: `tools/workflow_resolver.py`. Guard: `tools/workflow_guard.py`.

Default workflows always preserve reversible project state, cache invalidation, deterministic resumable delivery, machine-readable QC, and professional audio post/QC. Conditional workflows cover reference-motion calibration, restoration, source-derived looping, living-scene assembly, generated cinema, 2.5D/NeRF/3DGS, compositing/mattes/rotoscoping/tracking/cleanup/stabilization, procedural FX, retiming and nested timelines.


FX resolution is a default workflow. Before scene-level FX requirements are authored, agents should run the accepted batch/scene/still semantics through `fx_v2/fx_resolver.py` or the harness `harness.fx_resolve` tool. The result is advisory for creative judgment but authoritative for registry discovery: agents must not skip the current canonical library and invent project-local substitutes merely because they did not look.
