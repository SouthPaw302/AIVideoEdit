# AIVideoEdit Scene Runtime Contract

This contract adds a deterministic browser-renderable scene format to AIVideoEdit. It is subordinate to `PRIME_DIRECTIVE.md`, `DOCTRINE_LIVING_SCENE.md`, `PRODUCTION_CONTRACT.json`, narrative/style contracts, branch policy, and project state. It does **not** replace agent boot, director logic, storyboard approval, asset provenance, continuity rules, or GitHub workflow guards.

## Purpose

Use browser-renderable compositions when a production benefits from deterministic 2D/2.5D motion, typography, overlays, particles, SVG/canvas/WebGL effects, local video layers, or reusable transparent renders. The director still decides what the shot is; this runtime only makes the approved shot reproducible.

## Composition root

Every renderable composition must expose one root element with:

- `data-composition-id`: stable project/shot identifier.
- `data-start="0"`.
- `data-duration`: finite seconds.
- `data-fps`: `24`, `30`, or `60`.
- `data-width` and `data-height`.

Timed visible elements use a stable `id`, `class="clip"`, `data-start`, and `data-duration`. Track indices are organizational metadata and must not become semantic scene authority.

## Seek-safe animation

Render-critical animation must be a pure function of composition time.

- Create paused timelines (`gsap.timeline({ paused: true })`).
- Register the scene timeline under `window.__timelines[compositionId]`.
- Initialize with `timeline.seek(0)`; never depend on `timeline.play()` for exported motion.
- No `Date.now()`, wall-clock timers, unseeded `Math.random()`, request races, or event-driven timeline construction.
- Finite repeats only.
- Network media is forbidden for final render. Freeze assets locally before QC/render.
- If procedural noise is needed, use a fixed project seed recorded in project state or the shot manifest.

These rules complement Zero-Drift: determinism does not authorize new motion, geometry, characters, props, camera axes, or environment changes.

## Media ownership

The composition may reference only local staged assets or explicitly approved generated media. Source files remain governed by AIVideoEdit media/storage manifests. Rendering does not make an asset canonical.

## Audio timing

When a production uses `audiomap.json`, that file is the canonical machine timing map for its recorded source SHA-256. A production must not silently replace beat/energy timing with a second analyzer. Sparse or weakly rhythmic music should be paced by phrase/energy anchors rather than blindly hard-cutting on an estimated beat grid.

## QC

A render candidate should pass, in order:

1. Existing AIVideoEdit production/narrative/branch guards.
2. Scene structural/runtime/layout/motion/contrast checks.
3. Snapshot inspection at scene starts, strongest audio moments, hard stops/silences where relevant, and the tail frame.
4. Existing mode-aware, continuity, drift, and export QC.

A scene-runtime QC pass cannot override an AIVideoEdit production guard failure.

## Output

Default delivery is H.264/AAC MP4. Transparent intermediate layers may be MOV/ProRes 4444, VP9 WebM alpha, or RGBA PNG sequence. Final format remains a project/director decision.

## Implementation boundary

The initial runtime uses maintained open-source rendering components behind AIVideoEdit wrappers. Their package/API names are implementation details, not workflow identities. AIVideoEdit commands, contracts, project state, and branches remain the public operational surface.
