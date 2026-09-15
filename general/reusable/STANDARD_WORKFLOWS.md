# Standard Workflow Library

These are project-neutral production workflows available to every production. The resolver selects them from the active production mode and `MEDIA_PLAN.json` capabilities. Historical production names are not runtime identities and are intentionally absent.

Authority: `STANDARD_WORKFLOW_REGISTRY.json`. Resolver: `tools/workflow_resolver.py`. Guard: `tools/workflow_guard.py`.

Default workflows always preserve reversible project state, cache invalidation, deterministic resumable delivery, machine-readable QC, and professional audio post/QC. Conditional workflows cover reference-motion calibration, restoration, source-derived looping, living-scene assembly, generated cinema, 2.5D/NeRF/3DGS, compositing/mattes/rotoscoping/tracking/cleanup/stabilization, procedural FX, retiming and nested timelines.
