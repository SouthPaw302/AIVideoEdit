# AIVideoEdit — System Index

Permanent-system index only. No active production names or unrelated song links belong here.

## Universal contract
- `AGENTS.md` — universal agent entry point.
- `general/reusable/PRODUCTION_CONTRACT.json` — machine-readable production state/rules.
- `general/reusable/tools/production_guard.py` — fail-closed production-stage validator.
- `general/reusable/MEDIA_CAPABILITY_MATRIX.json` / `.md` — media forms available to production.
- `projects/PROJECT_TEMPLATE.md` — required branch-local state/manifests.

## Doctrine
- `README.md`
- `AGENT_HANDOFF.md`
- `BIBLE.md`
- `general/reusable/PRODUCTION_PIPELINE.md`
- `general/reusable/STYLE_CONTRACT.md`

## Reusable capabilities
- `general/reusable/fx_v2/` — callable FX runtime/registry/proofs/gate; single runtime authority.
- `general/reusable/generative-engine/` — audio analysis, shared controls, reactive/spatial runtime.
- `general/reusable/painterly-motion/` — living/painterly motion and temporal QC.
- `general/reusable/memory-atmosphere/` — restoration/atmosphere treatments.
- `general/reusable/depth-parallax-25d/` — depth-assisted 2.5D motion.
- `general/reusable/tools/` — generic utilities.
- `general/reusable/SPATIAL_3DGS_SUPERSPLAT.md` — truthful 3DGS doctrine.

## Branch selection
New supplied audio master -> new `song/<slug>` from current `main`. Explicit request to continue a named existing branch -> continue it. Otherwise never infer continuation from historical names.
