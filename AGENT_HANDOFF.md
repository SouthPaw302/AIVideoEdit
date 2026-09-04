# AIVideoEdit — Agent Handoff

Read `BIBLE.md` first.

Then:

1. Read `PROJECT_INDEX.md`.
2. Identify the active `song/<slug>` branch.
3. Read that branch's complete `projects/<slug>/` directory, especially its handoff/status/manifest files.
4. Before creating effects, search `general/reusable/CANONICAL_EFFECT_REGISTRY.md` and inspect the existing reusable implementation.
5. Continue the production from the branch state; do not reconstruct settled decisions from memory.

## Branch rule

`main` is the system Bible only. Every complete song production belongs on its own `song/<slug>` branch. Song-specific media, storyboards, shot packages, prompts, QC and manifests do not belong on `main`.

Reusable generic technology that proves useful across songs belongs in `main/general/reusable/` and must be registered canonically.
