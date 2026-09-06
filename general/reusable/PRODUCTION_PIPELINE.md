# Production Pipeline

This ordered method applies to every `song/<slug>` branch and is enforced by `PRODUCTION_CONTRACT.json` + `production_guard.py`.

## 0 — Initialize authority/state
Create the branch-local template files. `SOURCE_AUTHORITY.json` allows current user inputs, current branch decisions, and current `main`; historical chats/unrelated branches are denied unless explicitly authorized.

## 1 — Ingest source material
Record hashes, roles, technical metadata, and recovery/storage pointers for supplied audio/video/images.

## 2 — Extract and analyze references
**Video present:**
- Short video (system default: <=30 s AND <=1800 frames): extract every frame.
- Larger video: meaningful sampling is allowed. Record sampling method, extracted count, frame/time ranges and scene/motion coverage.
- Analyze style, palette, motion language, composition, identity-bearing features, and useful frame/range mappings.

**Images present:** inspect/analyze all supplied images before deriving new media.

**No visual references:** do not generate original media yet. Build a proposed story/visual/media approach using the song/lyrics and `MEDIA_CAPABILITY_MATRIX`; show it to the user and record the resulting direction as established.

## 3 — Establish visual/media approach
Create/lock the production's visual DNA and `MEDIA_PLAN.json`. Choose deliberately among source footage, extracted frames, generated stills/support imagery, living paintings, layered composites, depth/2.5D, reactive/atmospheric plates, loops, transitions, real radiance fields, real 3DGS when valid, and conventional video.

## 4 — Lock storyboard and shot map
Only after reference analysis/approach is complete. Map narrative and musical beats to specific source frame/ranges or to the established original-media plan.

## 5 — Build shot packages
For each selected shot use:
`source/ alpha/ layers/ depth/ generated/ fx_assets/ transition/ loop/ preview/ notes/`.

## 6 — Animate/composite and prove
Reuse neutral canonical capabilities before inventing substitutes. Make short finished shot proofs. Inspect them visually. Protect identity. Internal motion first, camera second.

## 7 — Music-directed behavior
Prefer one preserved, smoothed, frame-aligned song analysis bus (RMS/onset/low/mid/high) when several systems need the same signals.

## 8 — Lock FX
Only accepted shot recipes enter the production FX manifest. Resolve callable effects from `fx_v2/registry.json`, declare real pixel-altering render inputs, run the fail-closed precompile gate, generate and verify `fx.lock.json` immediately before compile.

## 9 — Assemble
Only after enough finished shot packages/proofs exist. Never use infrastructure success as a substitute for creative completion.

## 10 — Render and QC
Inspect the actual full export for black/damaged frames, freezes, repetition, loop seams, ghosting, invisible/missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, compression and audio sync.

## 11 — Archive/promote
Preserve manifests, hashes, prompts/decisions, proof/QC records and storage pointers. Promote genuinely reusable methods to project-neutral `main/general/reusable/` only after proof/QC.
