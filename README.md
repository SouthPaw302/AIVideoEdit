# AIVideoEdit

AI-native music-video production system for turning songs into directed long-form visual films.

## Start here

1. [`AGENT_HANDOFF.md`](AGENT_HANDOFF.md) — operating/recovery rules
2. [`PROJECT_INDEX.md`](PROJECT_INDEX.md) — current and historical song projects
3. [`CANONICAL_EFFECTS.md`](CANONICAL_EFFECTS.md) — reusable effects/loops/transitions entrypoint
4. [`general/reusable/CANONICAL_EFFECT_REGISTRY.md`](general/reusable/CANONICAL_EFFECT_REGISTRY.md) — accumulated production-technique library
5. [`docs/CANON_WORKFLOW.md`](docs/CANON_WORKFLOW.md) — production workflow

## Repository layout

```text
main
├── AGENT_HANDOFF.md
├── PROJECT_INDEX.md
├── REPOSITORY_INDEX.md
├── CANONICAL_EFFECTS.md
├── docs/                  # system workflow, architecture and visual language
├── general/
│   ├── PRODUCTION_SYSTEM_RULES.md
│   ├── ARCHIVE_INDEX.json
│   ├── SESSION_ASSET_RECOVERY.md
│   └── reusable/          # canonical cross-project effect/tool library
└── projects/              # project template only on main

song/<slug>                # actual per-video production branches
```

`main` is the persistent brain and reusable technology library. Each video is produced on `song/<slug>`. Large WAV/PNG/MP4 archives may live outside GitHub when appropriate, but GitHub preserves hashes, manifests, storage references, scripts, effect recipes, QC and recovery state.

## Current video projects

- **Irish Eyes** — active storyboard-linked shot-package/preview production.
- **Silver Coin** — V8 final complete / QC passed; canonical motion-quality reference and deepest implemented reusable-effects lineage.
- **IronFlame** — V1 rendered/delivered; exact final binary archive identity remains a recovery gap.
- **Leave It by the Door** — historical recovery/partial.
- **Sigh No More / Irish Eyes, Spanish Hair** — historical recovery/partial.

## Core production rule

Do not start a new video or effect from zero. Search the canonical reusable library first, build actual moving shot packages from the storyboard, QC the rendered result, and promote useful new techniques back to `main/general/reusable/`.
