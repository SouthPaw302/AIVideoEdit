# FX V2 Precompile Gate

## Why this exists

An effect name in a manifest is not evidence that the effect is actually present in the render path. AIVideoEdit now treats FX verification as a hard compile dependency.

Production render order is:

1. project declares exact FX IDs in a project `.fx.json` manifest;
2. `precompile_gate.py` resolves every ID against `registry.json`;
3. the gate verifies the real runtime wiring/implementation, rejects stubs/placeholders, checks approved proof/QC records, and runs pixel-level smoke tests;
4. the gate writes `fx.lock.json` with hashes of the project manifest, registry, runtime implementation and proof records;
5. immediately before the real render starts, the renderer verifies the lock again;
6. any changed code, registry or manifest invalidates the lock and blocks compile until the gate is rerun.

## Fail-closed rules

The gate fails when any requested effect:

- does not exist in the canonical registry;
- is `proof_required`, experimental, rejected, or otherwise not `approved`;
- exists in the registry but is not routed through the real runtime dispatcher;
- resolves to an empty method, `pass`, `NotImplementedError`, TODO/FIXME/placeholder code;
- lacks a rendered proof record covering that exact FX ID;
- lacks a valid proof binary checksum;
- lacks KEEP / APPROVED / PASS visual QC;
- uses a proof below 24 fps, under 24 frames, or below 320x180;
- produces effectively no pixel change in the runtime smoke test;
- is supposed to animate but does not change over time;
- causes excessive whole-frame translation when it is not a camera/spatial effect;
- is a transition that does not preserve the outgoing/incoming endpoints or visibly evolve between them.

## What this does not pretend to automate

Pixel metrics cannot decide whether an effect is artistically beautiful. Human visual QC is therefore mandatory before `gate_status` can become `approved`. The automated gate catches fake wiring, no-op implementations, placeholders, missing proofs, stale locks, and obviously broken temporal behavior. The proof/QC decision is the artistic gate.

## Production command

```bash
python general/reusable/fx_v2/precompile_gate.py \
  --manifest projects/<song>/FX_REQUIREMENTS.fx.json \
  --lock-out projects/<song>/fx.lock.json
```

Then immediately before compile:

```bash
python general/reusable/fx_v2/precompile_gate.py \
  --manifest projects/<song>/FX_REQUIREMENTS.fx.json \
  --verify-lock projects/<song>/fx.lock.json
```

A non-zero exit code means **do not render**.

## Approval states

- `approved` — may compile after the gate passes.
- `proof_required` — implementation may exist, but production use is blocked until a proof passes visual and technical QC.
- `conditional` — external/spatial technology such as real SuperSplat/3DGS. It requires explicit project opt-in plus a separate technology-specific spatial preflight. It is never silently substituted with a 2D imitation.

## Current proof policy

A single rendered proof may cover multiple effects only when the proof record explicitly lists every effect and the visual inspection confirms each one is genuinely visible. If an individual effect cannot be distinguished in the proof, it does not deserve `approved` status.

## Camera rule

Ordinary environment/light/surface effects are checked for unintended global translation. The FX layer must not smuggle camera shake into a scene under another effect name. Camera movement belongs to explicit camera/spatial logic and must be independently QC'd.
