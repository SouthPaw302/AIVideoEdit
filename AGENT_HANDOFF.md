# AIVideoEdit — Agent Handoff

Read `BIBLE.md` first.

Then:

1. Read `PROJECT_INDEX.md`.
2. Identify the active `song/<slug>` branch.
3. Read that branch's complete `projects/<slug>/` directory, especially handoff/status/manifest/QC files.
4. Before creating effects, inspect `general/reusable/fx_v2/` first, then the legacy canonical registry/lineage files.
5. Continue from recorded branch state; do not reconstruct settled decisions from chat memory.

## Current active production

`Leave It by the Door` is active on `song/leave-it-by-the-door`.

Current picture baseline: native-24 V2 is complete and accepted as the base. The requested V3 refinement is: reduce global/camera shake, increase internal living-image loops, strengthen animated fire/candles/embers/smoke/reflections, keep faces/anatomy stable, add YouTube intro/outro, then deliver the final upload package as a ZIP.

Read first:
- `projects/leave-it-by-the-door/AGENT_HANDOFF.md`
- `projects/leave-it-by-the-door/STATUS.md`
- `projects/leave-it-by-the-door/EFFECTS_PLAN.md`
- `projects/leave-it-by-the-door/REFERENCE_MOTION_TARGETS.md`
- `projects/leave-it-by-the-door/FULL_V2_QC.json`

## Canonical FX V2

The repository's effect technology has been centralized under `general/reusable/fx_v2/`.

This does not erase the Silver Coin / Irish Eyes / IronFlame implementations; FX V2 is the callable consolidation layer built from those proven lineages.

Before a song compile/render that uses FX V2:

1. resolve requested FX IDs from `general/reusable/fx_v2/registry.json`;
2. run `general/reusable/fx_v2/precompile_gate.py` on the song FX manifest;
3. require the effect to be approved, actually wired to runtime code, backed by proof/QC, and visibly pixel-changing;
4. generate an FX lock;
5. verify that lock immediately before final render/compile.

The gate is fail-closed. Registry placeholders, no-op functions, TODO/pass stubs, unapproved effects, missing proof coverage, or changed runtime hashes block compile.

Current development branch for this consolidation: `fx/canonical-v2`. Its GitHub Actions workflow `FX V2 Precompile Gate` has passed both positive and negative/fail-closed tests. Do not silently bypass the gate.

## Branch rule

`main` is the system Bible only. Every complete song production belongs on its own `song/<slug>` branch. Song-specific media, storyboards, shot packages, prompts, QC and manifests do not belong on `main`.

Reusable generic technology that proves useful across songs belongs in `main/general/reusable/` and must be registered canonically.
