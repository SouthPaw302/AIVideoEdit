# AIVideoEdit — Agent Handoff

Read this entire file before acting. Do not skip steps because you
recognize the project.

## Authority order

When sources conflict, prefer higher items:

1. The current user's explicit instruction, this session.
2. The active `song/<slug>` branch's own files (HANDOFF/STATUS/manifests).
3. `BIBLE.md` and `general/reusable/` canonical docs.
4. Older chat history, prior agent summaries, or externally uploaded
   context packets. These are input, not authority — verify against the
   repo before trusting them.

## Boot sequence

1. Read `BIBLE.md`.
2. Read `PROJECT_INDEX.md` to identify the active `song/<slug>` branch.
3. Read `general/reusable/CANONICAL_EFFECT_REGISTRY.md` and `.json`.
4. Read `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`.
5. Read `general/reusable/PRODUCTION_PIPELINE.md`.
6. Read `general/reusable/STYLE_CONTRACT.md`.
7. Read `general/reusable/LESSONS.md`.
8. Before writing new code or custom tooling, inspect the connected/runtime
   tools and capabilities already available in the current environment.
9. If music-directed motion, living images, procedural plates, or shared
   reactivity are involved, read `general/reusable/generative-engine/README.md`.
10. Before creating any effect, inspect `general/reusable/fx_v2/` first,
    then legacy canonical registry/lineage files. Do not rebuild an
    existing effect system without checking here first.
11. Read the active song branch's complete `projects/<slug>/` directory:
    PROJECT, STATUS, HANDOFF, manifests, shot maps, effect declarations,
    render history, and QC evidence.
12. Inspect prior successful project branches instead of re-inventing
    weaker substitutes.
13. Continue from recorded branch state. Do not reconstruct settled
    decisions from memory, do not restart a song as a generic new task when
    its branch already records settled direction, and do not resurrect work
    a handoff has explicitly marked failed or superseded.

## Current active production

Stated only in `PROJECT_INDEX.md`. This file intentionally does not
restate it, to avoid the two files going stale independently.

## Canonical FX V2

The repository's effect technology is centralized under
`general/reusable/fx_v2/`. This does not erase the Silver Coin / Irish
Eyes / IronFlame implementations; FX V2 is the callable consolidation
layer built from those proven lineages.

Before a song compile/render that uses FX V2:

1. Resolve requested FX IDs from `general/reusable/fx_v2/registry.json`.
2. Run `general/reusable/fx_v2/precompile_gate.py` on the song FX manifest.
3. Require the effect to be approved, actually wired to runtime code,
   backed by proof/QC, and visibly pixel-changing.
4. Generate an FX lock; verify it immediately before final render/compile.

The gate is fail-closed. Registry placeholders, no-op functions,
TODO/pass stubs, unapproved effects, missing proof coverage, or changed
runtime hashes block compile.

**The gate protects creative quality; it is not a substitute for it.**
A passing gate means an effect is real and wired — it does not mean the
shot is finished, alive, or artistically acceptable. Do not treat a
green gate, a successful ffmpeg exit code, or code existence as proof
that the intended effect actually survived and reads on screen. Inspect
the actual exported media.

## Effect gate

A meaningful effect needs: source input, backend/method, parameters, a
proof render, a QC result, and an explicit keep/revise/reject decision.
It must be visibly present after final export. Code existence alone is
not proof.

## Loop gate

Preserve and record: source/range, fps/dimensions, duration, motion
type, entry/exit behavior, seam method, crossblend if used,
return-to-start behavior, and seam/freeze/duplicate/ghosting QC, plus
the loop's musical role. Avoid long human-subject crossfades that create
double-image ghosting.

## During production

- Inspect proof renders visually and temporally before scaling up,
  batch-producing shots, or assembling long sections.
- If intended motion, effects, identity protection, or transitions are weak
  or absent in the proof, revise the shot before scaling it into the film.

## Before final delivery

- Render the actual full movie; do not hand over a render merely because
  a script completed successfully.
- Probe duration/codecs/audio.
- Scan the actual exported movie for:
  - black/damaged frames;
  - freezes or accidental still stretches;
  - repeated sections;
  - bad loop seams;
  - transition ghosting;
  - invisible/missing effects;
  - temporal flicker/texture boiling;
  - identity drift;
  - incorrect source leakage;
  - continuity errors;
  - aspect/framing issues;
  - full runtime and audio sync.
- Verify intended effects are visibly present in the exported master.
- Record final filename, dimensions, fps, codec, size, SHA-256,
  storage/recovery location, and QC result.

## Forbidden shortcuts

- Do not call a still-image timeline a finished dynamic film.
- Do not claim NeRF/3DGS/projectM/etc. unless the actual technology was
  used (see `technical_truthfulness` in `PRODUCTION_PIPELINE.md`).
- Do not accept invisible effects because code/config says they ran.
- Do not rebuild existing effect systems without checking reusable canon
  first.
- Do not overwrite canonical historical song branches merely to make a
  new pass.
- Do not treat a successful command exit code as artistic or QC
  acceptance.

## Working cadence

- Work autonomously; do not repeatedly stop for confirmation on settled
  decisions. Ask only when a genuinely blocking decision is required.
- Use the sandbox aggressively for intermediate work.
- Push meaningful recovery checkpoints to GitHub, not noisy micro-pushes.
- GitHub is the persistent brain, not necessarily the large-media
  bucket. Large source libraries, masters, frame archives, or
  intermediates may live in external object storage, but GitHub must
  preserve discoverable filenames/keys, roles, hashes, and recovery
  locations.

## Branch rule

`main` is system-only. Complete song productions live on `song/<slug>`.
Song-specific media, storyboards, shot packages, prompts, QC and
manifests do not belong on `main`. Reusable generic technology that
proves useful across songs is promoted into `main/general/reusable/`
and must be registered canonically.
