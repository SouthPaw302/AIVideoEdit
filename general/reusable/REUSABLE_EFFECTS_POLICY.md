# AIVideoEdit — Reusable Effects Policy

Canonical branch: `main`

This policy governs effects, shaders, render passes, transitions, loop builders, analysis tools, compositors, presets, and other reusable production technology created during individual song projects.

## Purpose

Song branches are laboratories. `main/general/reusable/` is the shared effect library for the entire AIVideoEdit stack.

A useful effect created for one song must not disappear with that branch or remain documented only in a project-specific notes file.

## Mandatory reuse preflight

Before creating a new effect, renderer, transition, loop method, spatial treatment, or QC utility, the active agent must inspect `main/general/reusable/` and the repository-wide effect/style catalogs.

The agent must determine whether an existing implementation already solves the problem well enough to reuse or adapt.

Do not recreate a weaker substitute simply because an earlier effect was developed in another song.

For every recovered/new production, explicitly check at least:

- `general/reusable/depth-parallax-25d/`
- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`
- project-appropriate reusable tools such as `general/reusable/irish-eyes-tools/`
- the repository-wide visual/effect catalogs and system production rules.

Record the selected reusable methods in the song project's effects plan.

## Silver Coin canonical reusable lineage

Silver Coin is a canonical proof project for dimensional/living-image effects. Its promoted reusable resources include:

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
- pigment dissolve;
- object/coin portal transitions;
- reference-motion signature analysis;
- temporal QC;
- music-directed living-painting render tools.

These are not Silver Coin-only. They must be considered for reuse by later projects whenever aesthetically and technically appropriate.

3D Gaussian Splatting is a separate spatial technology from the Silver Coin tiny-NeRF implementation. It remains a repository-wide option when adequate source views and runtime support exist.

## Promotion workflow

1. Develop the effect inside the song branch using real production material.
2. Render a proof clip or representative before/after frames.
3. QC the effect for visible function, temporal stability, performance, and failure modes.
4. Separate project-specific parameters from generic implementation.
5. Promote the generic implementation and documentation to `main/general/reusable/`.
6. Keep song-specific presets/configuration in the song project.
7. Record which production first validated the reusable effect.
8. Add or update a repository-wide catalog/index entry so future agents can discover it.

## Required package contents

Every promoted reusable effect should include, as applicable:

- implementation code or shader;
- README describing purpose and visual behavior;
- required inputs and dependencies;
- adjustable parameters and safe ranges;
- example invocation/configuration;
- render/backend requirements;
- known limitations and fallback behavior;
- proof/QC notes;
- source project that first validated it.

## Render-proof requirement

An effect is not reusable merely because code exists. It must have successfully rendered in a real production test.

Do not promote placeholder code, pseudo-effects, unverified shaders, or techniques that were only described in planning documents.

A production may not claim a reusable technique merely because the code was available. The actual proof/final render must visibly contain that technique.

## Visibility requirement

Approved effects must survive into the output with enough strength to be visually meaningful.

Subtle is acceptable. Functionally invisible is not.

If the effect cannot be seen in a representative rendered proof or in sampled final-output frames, treat it as absent and revise it.

## Source-derived effects

Reusable tooling for frame extraction, seamless loop generation, optical-flow retiming, frame interpolation, depth separation, stabilization, photographic enhancement, compositing, color treatment, and temporal QC is encouraged.

The generic tool belongs here; source footage and identity-specific data remain within the project or approved binary archive.

## PlayCanvas / 3D stack

Reusable PlayCanvas assets may include:

- compose shaders;
- custom render passes;
- CameraFrame/post-processing presets;
- audio-reactive parameter drivers;
- depth/parallax scene utilities;
- Gaussian-splat scene helpers;
- camera path and temporal-stability utilities;
- water, reflection, atmosphere, bloom, diffusion, lens, and optical effects.

SuperSplat/3DGS-specific helpers should remain independent of a single song's splat asset wherever possible.

## Spatial-rendering naming rule

Keep spatial techniques technically honest and discoverable:

- **3DGS / Gaussian splatting** only when Gaussian primitives/reconstruction are actually used;
- **NeRF** only when an actual trained neural radiance field is rendered;
- **hybrid neural-radiance-field spatial rendering** when a trained radiance-field component is composited with image/depth layers;
- **2.5D parallax** for layered/depth-aware image-space motion.

Never relabel a simple zoom, pseudo-depth warp, fog overlay, or generic particle system as Gaussian or NeRF rendering.

## Naming

Prefer descriptive technology names rather than song names for reusable implementations. Song-specific presets may retain song labels.

Example:

- reusable: `water_reflection_audio_driver`
- project preset: `irish_eyes_water_reflection_v1.json`

## Branch rule

The repository currently uses `main` as its canonical/default branch. For project instructions that refer to the "master branch," interpret that as `main` unless the repository's canonical branch is intentionally renamed.

## Anti-loss rule

A reusable method is considered at risk of being lost if it exists only in:

- chat history;
- a project handoff;
- a song-specific notes file;
- an unindexed branch path;
- a large archive with no discoverable manifest.

Before ending a production phase, ensure important techniques are promoted or at minimum indexed from `main` with their exact path, proof project, and status.

## First production under this rule

`Irish Eyes` (`song/irish-eyes`) is the first project explicitly governed by this strengthened promotion/reuse policy. Any new effect developed and validated there should be promoted here for future AIVideoEdit productions.
