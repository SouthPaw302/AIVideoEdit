# AIVideoEdit — Agent Handoff

## Authority
1. Current explicit user instruction.
2. Active `song/<slug>` branch `PROJECT_STATE.json`, `SOURCE_AUTHORITY.json`, STATUS/HANDOFF/manifests.
3. `AGENTS.md`, `BIBLE.md`, `SYSTEM_INDEX.md`, `general/reusable/PRODUCTION_CONTRACT.json`, and current `general/reusable/`.

Historical chats/summaries, unrelated branches, old production imagery, and provenance are **not automatic authority**. Use them only when the current user explicitly authorizes them.

## Boot
1. Read `AGENTS.md` and `PRODUCTION_CONTRACT.json`.
2. Read `SYSTEM_INDEX.md` and `MEDIA_CAPABILITY_MATRIX.json`.
3. Read the active branch state/manifests if on `song/<slug>`.
4. Run `production_guard.py` before advancing state.
5. Inspect connected/runtime tools and relevant project-neutral reusable capabilities before inventing substitutes.
6. Resolve callable FX only through `general/reusable/fx_v2/registry.json`.

## Film rule
Build real shot packages, not slides. Inspect short finished proofs before scaling. Internal scene motion first, camera second. Use measured song controls when music-reactivity is intended. Protect identity. Never accept invisible effects or command success as QC.

## Final QC
Inspect the actual exported media for damaged/black frames, freezes, repetition, loop seams, ghosting, missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, and audio sync. Record specs/SHA/storage/QC.
