# AIVideoEdit — Reusable Effects Policy

Canonical branch: `main`

This policy governs effects, shaders, render passes, transitions, loop builders, analysis tools, compositors, presets, spatial renderers, and other reusable production technology created or recovered during individual song projects.

## Purpose

Song branches are laboratories. `main/general/reusable/` is the shared effect library for the entire AIVideoEdit stack.

A useful effect created for one song must not disappear with that branch, chat, local workspace, preview folder, or finished video.

The canonical discovery layer is:

- `CANONICAL_EFFECTS.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.json`
- `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`
- `general/reusable/EFFECT_PACKAGE_STANDARD.md`

## Mandatory reuse preflight

Before creating a new effect, renderer, transition, loop method, spatial treatment, audio-reactive behavior, or QC utility, the active agent must:

1. search the canonical effect registry for the visual/technical need;
2. inspect the registered implementation/reference and provenance;
3. respect the registered validation status;
4. determine whether an existing implementation already solves the problem well enough to reuse or adapt;
5. record the chosen reusable method IDs in the active project's effect/shot plan when practical.

Do not recreate a weaker substitute simply because an earlier effect was developed in another song.

At minimum inspect project-appropriate resources under:

- `general/reusable/depth-parallax-25d/`
- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`
- `general/reusable/irish-eyes-tools/`
- the canonical registry and lineage files.

Art direction does not automatically travel with implementation. A photographic project may reuse Silver Coin's motion, light, NeRF, audio-reactivity or QC methods without inheriting Silver Coin's painterly look.

## Canonical status model

A technique can be canonical as a record without being proven. Use these statuses honestly:

- `render_proven` — a representative render exists and passed recorded QC;
- `final_lineage` — the implementation belongs to a completed/final production lineage;
- `rendered_project_unverified_per_effect` — the project rendered, but exact per-effect final verification was not recovered;
- `recovered_pattern` — historical method/workflow is supported by recovery evidence, implementation/proof incomplete;
- `project_direction` — designed visual/effect language, not proven as implementation;
- `experimental` — test/implementation exists but has not passed its acceptance gate;
- `system_capability` — canonical architecture/technology option, not automatically implemented.

Never upgrade a status merely because a technique sounds plausible or resembles something visible in a final video.

## Silver Coin canonical reusable lineage

Silver Coin is a canonical proof/final-lineage project for dimensional/living-image effects. Its promoted reusable resources include:

- `general/reusable/silver-coin-tools/video_fx/tiny_nerf_volume.py` — compact trained neural-radiance-field volume;
- depth/pseudo-depth parallax;
- mesh breath / micro-motion;
- advected atmosphere;
- wet reflection ripple;
- firelight breath;
- localized heat haze;
- motivated volumetric/light shafts;
- silver/specular glints;
- performance transient warps;
- depth-focus breathing;
- temporal canvas lock;
- pigment/chroma transitions;
- object/coin portal transitions;
- reference-motion signature analysis;
- temporal QC;
- audio edit maps and normalized reactivity controls;
- music-directed living-image render tools;
- eight named V8 effect-loop presets recorded in the canonical registry.

These are not Silver Coin-only. They must be considered for reuse by later projects whenever aesthetically and technically appropriate.

3D Gaussian Splatting is a separate spatial technology from the Silver Coin tiny-NeRF implementation and from Gaussian-shaped light fields. It remains a repository-wide option only when actual Gaussian splat data/rendering is used.

## Promotion / registration workflow

For genuinely new reusable technology:

1. develop the effect inside the active song/project using real production material;
2. assign a stable canonical ID and descriptive name;
3. render a proof clip or representative before/after frames where applicable;
4. QC visible function, temporal stability, identity/edge integrity, performance, seam behavior and failure modes;
5. separate project-specific parameters from generic implementation;
6. promote generic implementation/documentation to `main/general/reusable/` when practical;
7. keep song-specific presets/configuration in the project branch;
8. record which project/shot first validated or recovered it;
9. add/update both `CANONICAL_EFFECT_REGISTRY.md` and `.json`;
10. update `PROJECT_TECHNIQUE_LINEAGE.md` when the technique materially expands the system.

Follow `EFFECT_PACKAGE_STANDARD.md` for required metadata.

## Required package contents

Every promoted reusable effect should preserve, as applicable:

- implementation code, shader, node graph, preset or exact recipe;
- canonical ID/name and category;
- purpose and visual behavior;
- source project/shot and validation status;
- required inputs/dependencies;
- masks, mattes, alpha, depth, tracking or ROI requirements;
- deterministic seeds if applicable;
- adjustable parameters and safe ranges;
- audio-control mapping if reactive;
- example invocation/configuration;
- duration/FPS/aspect constraints where relevant;
- loop entry/exit or transition behavior;
- render/backend requirements;
- known limitations and fallback behavior;
- proof/QC references and checksums when available;
- license/provenance for third-party effect assets;
- version/change history.

## Render-proof requirement

Code or planning alone does not make a technique render-proven.

Do not mark placeholder code, pseudo-effects, unverified shaders, or planning concepts as `render_proven`.

A production may not claim a technique merely because its code was available. The actual proof/final render must visibly contain that technique.

## Visibility requirement

Approved effects must survive into output with enough strength to be visually meaningful.

Subtle is acceptable. Functionally invisible is not.

If the effect cannot be seen in a representative rendered proof or sampled final-output frames, treat it as absent and revise it.

## Loop requirements

A reusable loop must preserve source/range, FPS/dimensions, duration, real/synthesized/generated/hybrid motion type, entry/exit behavior, seam method, crossblend duration if any, return-to-start behavior, seam QC, freeze/duplicate/ghosting QC, and intended musical role.

Mathematical endpoint similarity is not visual seam acceptance.

Avoid long crossfades that create double-image ghosting. Identity-bearing human footage requires especially strict seam and double-exposure review.

## Transition requirements

Transitions should record outgoing/incoming sources, duration, mask/object/depth logic, midpoint behavior, exposure/color continuity, identity protection, and reversibility where relevant.

Long full-body dissolves that create identity double exposure normally fail. Prefer motivated object, reflection, pigment, atmospheric, spatial, lens or geometry transitions where appropriate.

## Source-derived effects

Reusable tooling for frame extraction, source-derived loop generation, optical-flow retiming, frame interpolation, depth separation, stabilization, photographic enhancement, compositing, color treatment, alpha/matte creation, and temporal QC is encouraged.

Generic tooling belongs here; source footage and identity-specific data remain within the project or approved binary archive.

## PlayCanvas / 3D stack

Reusable PlayCanvas/3D resources may include:

- compose shaders;
- custom render passes;
- CameraFrame/post-processing presets;
- audio-reactive parameter drivers;
- depth/parallax scene utilities;
- Gaussian-splat scene helpers;
- camera path and temporal-stability utilities;
- water, reflection, atmosphere, bloom, diffusion, lens and optical effects.

SuperSplat/3DGS-specific helpers should remain independent of a single song's splat asset wherever possible.

## Spatial-rendering naming rule

Keep spatial techniques technically honest and discoverable:

- **3DGS / Gaussian splatting** only when Gaussian primitives/reconstruction are actually used;
- **NeRF** only when an actual trained neural radiance field is rendered;
- **hybrid neural-radiance-field spatial rendering** when a trained radiance-field component is composited with image/depth layers;
- **2.5D parallax** for layered/depth-aware image-space motion;
- **Gaussian light field/shaft** may describe a Gaussian-shaped optical field, but it must not be confused with 3D Gaussian Splatting.

Never relabel a simple zoom, pseudo-depth warp, fog overlay, or generic particle system as Gaussian-splat or NeRF rendering.

## Naming

Prefer descriptive technology names rather than song names for generic implementations. Song-specific presets may retain song labels.

Example:

- reusable: `water_reflection_audio_driver`
- project preset: `irish_eyes_water_reflection_v1.json`

Stable canonical registry IDs may retain project lineage prefixes such as `SC-`, `IE-`, or `IF-`; the reusable implementation itself should still use a descriptive generic name when practical.

## Recovery mining rule

When historical chats, File Library assets, old branches, local drives, object storage, or final renders reveal a previously unregistered technique:

1. preserve it immediately as a canonical record;
2. attach evidence/source references;
3. assign the most conservative truthful validation status;
4. recover implementation, presets, previews and checksums when possible;
5. do not discard the idea merely because the original code/binary is temporarily unavailable.

This allows the system to remember excellent concepts without pretending they were already proven.

## Branch rule

The repository currently uses `main` as its canonical/default branch. For project instructions that refer to the "master branch," interpret that as `main` unless the repository's canonical branch is intentionally renamed.

## Anti-loss rule

A reusable method is considered at risk of being lost if it exists only in:

- chat history;
- a project handoff;
- a song-specific notes file;
- an unindexed branch path;
- an unregistered local preview/effect directory;
- a large archive with no discoverable manifest;
- a final video with no recorded implementation lineage.

Before ending a production phase, ensure important techniques are promoted or at minimum registered from `main` with exact source/project path, validation status and proof/implementation references.

## Current governed production

`Irish Eyes` (`song/irish-eyes`) is the first active project explicitly governed by the strengthened registry/package policy. Any new effect developed, recovered, rejected for reusable reasons, or validated there must feed back into the canonical library for future AIVideoEdit productions.
