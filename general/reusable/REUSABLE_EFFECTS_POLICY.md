# AIVideoEdit — Reusable Effects Policy

Canonical branch: `main`

This policy governs effects, shaders, render passes, transitions, loop builders, analysis tools, compositors, presets, and other reusable production technology created during individual song projects.

## Purpose

Song branches are laboratories. `main/general/reusable/` is the shared effect library for the entire AIVideoEdit stack.

A useful effect created for one song must not disappear with that branch or remain documented only in a project-specific notes file.

## Promotion workflow

1. Develop the effect inside the song branch using real production material.
2. Render a proof clip or representative before/after frames.
3. QC the effect for visible function, temporal stability, performance, and failure modes.
4. Separate project-specific parameters from generic implementation.
5. Promote the generic implementation and documentation to `main/general/reusable/`.
6. Keep song-specific presets/configuration in the song project.
7. Record which production first validated the reusable effect.

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

## Naming

Prefer descriptive technology names rather than song names for reusable implementations. Song-specific presets may retain song labels.

Example:

- reusable: `water_reflection_audio_driver`
- project preset: `irish_eyes_water_reflection_v1.json`

## Branch rule

The repository currently uses `main` as its canonical/default branch. For project instructions that refer to the "master branch," interpret that as `main` unless the repository's canonical branch is intentionally renamed.

## First production under this rule

`Irish Eyes` (`song/irish-eyes`) is the first project explicitly governed by this promotion policy. Any new effect developed and validated there should be promoted here for future AIVideoEdit productions.
