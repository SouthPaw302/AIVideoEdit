# AIVideoEdit — Canonical Reusable Production Library

This directory is the permanent front door for reusable loops, effects, transitions, motion methods, spatial techniques, QC tools, and production patterns created across AIVideoEdit music-video projects.

## Mandatory recovery order

Before inventing a new effect or building a new song:

1. read `CANONICAL_EFFECT_REGISTRY.md`;
2. read `CANONICAL_EFFECT_REGISTRY.json` when machine-readable detail is useful;
3. read `PROJECT_TECHNIQUE_LINEAGE.md` to see which project created or validated each technique;
4. read `EFFECT_PACKAGE_STANDARD.md` before creating a new reusable loop/effect;
5. inspect the implementation path and proof/QC source listed for any effect you intend to reuse;
6. inspect `generative-engine/` before building a new song-level audio-reactive analyzer or living-image runtime;
7. only then create a new effect when the existing library cannot satisfy the shot.

## Status language

Every registered technique is canonical as a **record**, but its validation status matters:

- `render_proven` — a rendered proof exists and passed recorded QC;
- `final_lineage` — implementation belongs to a completed/final production lineage;
- `rendered_project_unverified_per_effect` — the project rendered, but a complete per-effect final log was not recovered;
- `recovered_pattern` — a historical production pattern is documented, but the original effect binary/code is incomplete;
- `project_direction` — a designed effect/loop language preserved from a project, not proven as an implementation;
- `system_capability` — part of the larger production-system specification, not automatically implemented.

Never upgrade an effect's status without evidence.

## Current canonical implementation trees

- `generative-engine/` — shared music-reactive control bus plus streaming reference renderers for organic reactive fields and continuous living-image parallax. Song-specific mappings remain proof-gated.
- `silver-coin-tools/` — deepest reusable CPU effect/audio/QC stack; includes hybrid painterly motion, audio reactivity, temporal QC, and compact NeRF volume rendering.
- `silver-coin-docs/` — method catalog, motion calibration, visual style catalog, architecture and workflow references.
- `depth-parallax-25d/` — continuous soft-depth 2.5D parallax renderer validated during Irish Eyes.
- `irish-eyes-tools/` — real-footage restoration, halation/bloom, water shimmer, and visible memory treatment.

## Source projects currently mined

- Silver Coin
- IronFlame
- Irish Eyes
- Leave It by the Door
- Sigh No More / Irish Eyes, Spanish Hair
- repository-wide AI Video Production System specification

When another historical video or recovered project is found, mine it into the registry before starting new work.

## Core rule

A good effect must not die with a chat, branch, preview folder, or single song. If it was useful enough to keep, it belongs in this library with a stable name, provenance, validation status, implementation/reference path, parameters or recipe, and proof/QC record.
