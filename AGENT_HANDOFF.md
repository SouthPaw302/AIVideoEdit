# AIVideoEdit — Agent Handoff

## Authority
1. Current explicit user instruction.
2. If already on a `song/<slug>` branch, that branch's STATUS/HANDOFF/manifests.
3. `BIBLE.md`, `SYSTEM_INDEX.md`, and `general/reusable/`.
4. Older chats/summaries/provenance.

## Boot
1. Read `BIBLE.md`.
2. Read `SYSTEM_INDEX.md`.
3. Read `general/reusable/fx_v2/registry.json` and `PRECOMPILE_FX_GATE.md`.
4. Read `general/reusable/PRODUCTION_PIPELINE.md` and `STYLE_CONTRACT.md`.
5. Inspect connected/runtime tools before new code.
6. Inspect relevant `general/reusable/` capabilities before inventing substitutes.

## Branch trigger
A newly supplied music/audio master intended for video production creates a fresh `song/<slug>` from `main` before production work begins. Do not search `main` for an active project and do not infer continuation from historical names. Only an explicit user instruction to continue a named existing branch overrides this.

## Project-neutral promotion
Production-created technology is proven on its branch, then generalized: remove production media/paths/constants/story assumptions/names, assign capability IDs/names, create project-neutral proof/QC, promote to `main/general/reusable/`, and register canonically. Origin is provenance, never capability identity.

## FX rule
Resolve callable FX from `general/reusable/fx_v2/registry.json`; run the fail-closed precompile gate; generate and verify the lock immediately before render; inspect the actual exported media. Gate success proves implementation/evidence integrity, not artistic success.

## Film rule
Build real shot packages, not slides. Inspect short proofs before scaling. Use measured song controls when music-reactivity is intended. Protect identity. Never accept invisible effects or command success as QC.

## Final QC
Inspect the actual export for black/damaged frames, freezes, repetition, loop seams, ghosting, missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, and audio sync. Record specs/SHA/storage/QC.
