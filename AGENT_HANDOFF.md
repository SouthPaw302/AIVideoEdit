# AIVideoEdit — Agent Handoff

## First action in every new session
Run:

```bash
python bootstrap.py boot --repo-root <repo>
```

Do not continue a handoff, inspect production history, generate media, change state, select FX, or render before bootstrap passes. After PASS, read bootstrapped `SOUL.md` and `.aivideoedit/SECOND_BRAIN.md`.

## Authority
1. Current explicit user instruction.
2. Active `song/<slug>` branch `PROJECT_STATE.json`, `SOURCE_AUTHORITY.json`, STATUS/HANDOFF/manifests.
3. Current-main AIVideoEdit OS loaded into `.aivideoedit/os/`.

Historical chats/summaries, unrelated branches, old production imagery, and provenance are not automatic authority. Use them only when the current user explicitly authorizes them.

## Runtime
Before advancing state, run:
`python .aivideoedit/os/general/reusable/tools/production_guard.py --branch <current-branch>`

Do not substitute a stale branch-local guard for the bootstrapped current-main guard. Inspect connected/runtime tools and relevant project-neutral reusable capabilities before inventing substitutes. Resolve callable FX only through the bootstrapped current-main `general/reusable/fx_v2/registry.json`.

## Film rule
Build real shot packages, not slides. Inspect short finished motion proofs before scaling. Internal scene motion first, camera second. Use measured song controls when music-reactivity is intended. Protect identity. Never accept invisible effects or command success as QC.

## Final QC
Inspect the actual exported media for damaged/black frames, freezes, repetition, loop seams, ghosting, missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, and audio sync. Record specs/SHA/storage/QC.
