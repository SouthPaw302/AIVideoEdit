# AIVideoEdit

A reusable production system for creating **directed, dynamic long-form music films**.

The target is not a slideshow, a generic visualizer, or one source clip with weak effects. A finished production should feel like the song became a coherent visual world: changing shots, depth, internal motion, atmosphere, light, character continuity, transitions, recurring motifs, and music-directed behavior all working together.

Silver Coin V8 remains the primary quality/motion benchmark for this philosophy. Its specific art style is not mandatory for other songs.

---

## Start here

For a new agent/session, use the repository instead of reconstructing settled decisions from chat memory.

1. Read `AGENT_HANDOFF.md` — the canonical boot sequence.
2. Read `BIBLE.md` — system doctrine and production law.
3. Read `PROJECT_INDEX.md` — the only authority for the currently active production.
4. Read the reusable registries/pipeline files named by `AGENT_HANDOFF.md`.
5. Open the active `song/<slug>` branch and read the complete project handoff/status/manifests/QC before changing anything.

If this README and `PROJECT_INDEX.md` ever disagree about project state, `PROJECT_INDEX.md` is correct. Treat the mismatch as documentation drift and fix this file.

---

## Repository law

- `main` = production system, Bible, indexes, templates, and reusable cross-project technology.
- `song/<slug>` = one complete song/video production.
- Song-specific media references, storyboards, prompts, shot packages, manifests, QC, renders, decisions, and recovery information stay on the song branch.
- Only generic technology proven useful across projects returns to `main/general/reusable/`.
- Do not overwrite historical song branches merely to create a new pass.
- GitHub is the persistent brain, not necessarily the large-media bucket.

Large masters, source libraries, frame archives, and heavy intermediates may live in the active workspace/File Library/object storage, but the repository must preserve their identity: filename/object key, role, checksum when practical, and recovery location.

---

## Production standard

A production still is a **scene source**, not a finished shot.

Strong shots may combine:

- foreground / subject / midground / background separation
- authored depth or 2.5D parallax
- subject-safe hair, cloth, breathing, gesture, or prop micro-motion
- rain, smoke, fog, ash, embers, fire, reflections, water, dust, shadows
- practical-light movement and palette evolution
- music-directed camera amplitude and environmental intensity
- integrated visualizer or generative passages when the song calls for them
- match cuts, recursive/object transitions, light handoffs, pigment transitions, or other song-shaped edit grammar

The system should create enough real shot packages to cover a full song dynamically before treating timeline assembly as the main task.

### Motion must be visible

Subtle motion is valid; invisible motion is not.

When the user supplies motion/style references, measure them when useful (for example optical-flow density, cut cadence, or motion-region strength) and use those measurements as calibration evidence. Quantitative targets are **guides**, not substitutes for human visual review.

Do not increase global camera shake merely to make a metric larger. Prefer internal environmental motion, depth, cloth/hair behavior, light, atmosphere, reflections, and shot-specific transformation while protecting faces, hands, animals, instruments, and important props.

---

## Reuse before invention

Before creating a new effect, transition, spatial method, reactive analyzer, loop system, camera behavior, or QC utility, inspect existing reusable technology first.

Primary locations include:

- `general/reusable/fx_v2/`
- `general/reusable/generative-engine/`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.json`
- `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`
- `general/reusable/PRODUCTION_PIPELINE.md`
- successful prior song branches

Do not recreate weaker substitutes for technology that already survived a real production.

---

## FX V2 and evidence gates

Canonical reusable FX are consolidated under `general/reusable/fx_v2/`.

For production use:

1. declare the intended effect IDs in the song's FX manifest;
2. resolve them through `general/reusable/fx_v2/registry.json`;
3. run `precompile_gate.py`;
4. generate the FX lock;
5. verify that lock immediately before compile/render;
6. render proof/evidence;
7. inspect the **actual exported pixels**;
8. record keep / revise / reject.

The gate is fail-closed for missing, unapproved, unwired, changed, placeholder, or unproven effects.

A green FX gate proves that an implementation is real and wired. It does **not** prove that the shot is alive, that the effect is strong enough, that a transition is attractive, or that the film is artistically finished.

Successful code execution is evidence. **Visible survival in the exported movie is acceptance.**

---

## Technical truthfulness

Name techniques by what was actually rendered.

- **2.5D** = depth/layer-aware image-space motion.
- **NeRF** = an actual trained neural radiance field is rendered.
- **Hybrid NeRF** = a real radiance-field component is composited with other scene layers.
- **3DGS** = actual Gaussian-splat scene data/primitives are rendered.
- Gaussian-shaped overlays are not 3D Gaussian Splatting.
- Custom reactive fields are not projectM/MilkDrop unless those engines are actually used.

Never upgrade a claim because the output merely resembles a technology.

---

## QC law

A successful FFmpeg command or green CI job is **not** a finished video.

Before final delivery, inspect the actual exported movie for at least:

- exact runtime and audio sync
- codec / fps / dimensions / aspect
- black or damaged frames
- accidental freezes or still stretches
- repeated sections
- malformed transitions or ghosting
- invisible/missing intended effects
- temporal flicker / texture boiling
- identity drift or facial/body morphing
- hand/prop/animal deformation
- incorrect source leakage
- continuity and framing problems
- color / brightness discontinuities

Generate representative contact sheets and targeted temporal/transition proofs. Automated QC and human artistic review are both required for important masters.

Do not call a candidate `FINAL` merely because automated gates passed.

---

## Working cadence

- Work autonomously from settled project direction.
- Ask only when a genuinely blocking decision requires the user.
- Use the sandbox/workspace aggressively for intermediate work.
- Push **meaningful recovery checkpoints**, not noisy micro-pushes.
- Before a long render, preserve enough state that another agent can recover without rebuilding the phase.
- After material QC findings, preserve the decision and why it happened—not just the new script.
- Keep failed/superseded passes traceable when they contain useful evidence, but do not let them become the creative target.

---

## Tooling continuity notes

- Canonical reusable utility path: `general/reusable/tools/`.
- `general/reusable/embedded-tools/` was an earlier working name; do not create a second competing tree.
- Browser/WebGPU Gaussian-splat viewers such as `gsplat.js` or Luma's player are optional review/reference tools, not substitutes for genuine 3DGS production rendering.
- Optional review infrastructure should be created only when a real review-surface need exists; do not build infrastructure merely because it was once discussed.

---

## New song

Create `song/<slug>` from `main`, then start with `projects/PROJECT_TEMPLATE.md`.

Minimum durable project package normally includes:

- `PROJECT.md`
- `STATUS.md`
- `HANDOFF.md`
- `LYRICS.md` when applicable
- `VISUAL_DNA.md`
- `EFFECTS_PLAN.md`
- `ASSET_MANIFEST.json`
- shot/storyboard/timing records as the project matures
- render/QC history

The exact active branch and recovery entrypoint are always recorded in `PROJECT_INDEX.md` and the project branch itself.

---

## Final principle

> **The goal is not “AI pictures behind a song.”**
>
> **The goal is: the song became a visual world.**
