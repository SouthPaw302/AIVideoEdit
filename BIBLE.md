# AIVideoEdit — Bible

Permanent operating system for dynamic long-form music films.

## Branch and authority law
`main` is system-only. Every production lives on `song/<slug>`. A new audio master starts a fresh song branch from current `main` unless the user explicitly names an existing branch. Production authority is current user instruction -> active song-branch state -> current main. Historical projects/chats are opt-in only.

## Target
Make a directed long-form visual film, not a slideshow, generic visualizer, or one weak repeated clip. The song should become a continuously authored visual world through shots, depth, atmosphere, light, internal motion, environment, composition, transitions, and recurring motifs.

## Hard production order
Initialize -> ingest sources -> extract/analyze references -> establish visual/media approach -> lock storyboard/shot map -> build shot library -> animate/composite -> accept short proofs -> lock FX -> assemble -> render -> inspect actual export -> archive.

`general/reusable/tools/production_guard.py` is the fail-closed stage authority.

## Reference law
- Short reference video: extract every frame.
- Long/large reference video: meaningful sampling is allowed, but policy, sample count, frame ranges/scene coverage, and analysis must be recorded.
- Supplied images: inspect/analyze them before deriving new media.
- No visual references: the production enters the **Visual Direction Selection Gate**. Before generating production media, the agent must present at least three materially distinct numbered artistic-rendering routes in chat. Each route must contain a named story interpretation, rendering/media treatment, and a numbered mini-storyboard of at least three beats/frames. The user must explicitly select one route, select a hybrid by option number, or modify a route. The presented options and current-user selection must be recorded in `MEDIA_PLAN.json` and locked before production proceeds.
- Concept/storyboard previews created only for the Visual Direction Selection Gate are allowed as decision artifacts; they are not production assets unless the selected direction explicitly adopts them.
- Historical styles/preferences and agent taste cannot substitute for a current no-reference selection.

## Shot-package law
Every selected scene becomes a genuine branch-local shot package with source, masks/alpha, layers, depth where needed, generated support, FX assets, transitions/loops, proof preview, notes, and QC. Preview means a short finished proof, not premature assembly.

## Reuse and media law
Before inventing technology, inspect `SYSTEM_INDEX.md`, `MEDIA_CAPABILITY_MATRIX.json`, `fx_v2/registry.json`, the generative engine, and relevant neutral capability folders. The production media plan must deliberately select suitable media forms instead of defaulting to stills + zoom.

## Technical truthfulness
2.5D means depth/layer image-space motion. NeRF means an actual trained radiance field. 3DGS means actual Gaussian-splat scene primitives. A Gaussian light/noise field is not 3DGS. A custom reactive field is not projectM/MilkDrop unless that engine is actually used.

## Proof/QC law
Code existence is not proof. Preserve implementation/backend, parameters, proof render, QC, and keep/revise/reject decision. Effects must be visible in proof and survive export. Callable FX must pass the canonical gate/lock. Final acceptance requires inspection of the actual complete export.

## Persistence
GitHub is the persistent brain; large binaries may live externally if branch manifests preserve identity/hash/role/recovery location.

## Final principle
The goal is not “AI pictures behind a song.” The goal is: **the song became a visual world.**
