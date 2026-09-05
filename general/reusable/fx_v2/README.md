# AIVideoEdit Canonical FX V2

Branch: `fx/canonical-v2`

## Purpose

Unify the strongest proven AIVideoEdit effects from Silver Coin, Irish Eyes, IronFlame and Leave It by the Door behind one stable callable runtime.

The old repository has excellent effects, but they are fragmented across song renderers and overlapping helper modules. V2 makes the effects reusable by ID and keeps song-specific timing/ROIs in project manifests.

## Core rule

**Internal scene motion first. Camera motion second.**

The viewer should read a living image, not a still being shaken or zoomed.

## Runtime layers

1. `surface` — stable canvas/pigment, local contrast, identity protection.
2. `motion` — depth parallax, cloth/hair/crowd breath, water/foliage flow.
3. `environment` — rain, rain glass, fog/smoke, spray, embers, fire.
4. `light` — firelight, moving practical light, shafts, glints, temporal palette migration.
5. `transition` — pigment, fog/light, reflection, doorway/depth, object portal, perceptual gates.
6. `spatial` — honest 2.5D, NeRF atmosphere, and real 3DGS/SuperSplat integration when source geometry supports it.

## IDs

Effects are addressed by stable IDs from `registry.json`. A song manifest calls IDs plus parameters; it does not copy implementation code.

Example:

```json
{
  "effects": [
    {"id": "FX2-FIRE-001", "roi": [0.05,0.38,0.46,0.98], "strength": 0.9},
    {"id": "FX2-ATM-001", "roi": [0.0,0.0,0.58,0.78], "strength": 0.5},
    {"id": "FX2-MOTION-002", "roi": [0.0,0.0,1.0,1.0], "strength": 0.7}
  ]
}
```

## Hard precompile gate

A project may not compile merely because an FX ID exists in JSON.

Before a production render, run `precompile_gate.py`. It verifies that every requested effect:

- is explicitly production-approved in the canonical registry;
- is wired into the actual runtime path;
- is not a placeholder/stub/no-op;
- has a rendered proof/checksum and KEEP/APPROVED/PASS visual QC;
- produces measurable pixel change and temporal behavior where expected;
- does not smuggle excessive whole-frame shake into non-camera effects.

The gate writes an `fx.lock.json` containing hashes of the manifest, registry, runtime implementation and proof records. The lock must be verified again immediately before compile. Any change invalidates it.

See `PRECOMPILE_FX_GATE.md`.

## Promotion gate

No effect is promoted to `main` merely because code exists. Each candidate requires:

- deterministic implementation;
- 3–10 second rendered proof;
- native final cadence (24/30 fps as project requires);
- before/after or motion metrics;
- black/freeze/loop-seam scan;
- visual QC: KEEP / REVISE / REJECT;
- documented limitations.

Until that happens its `gate_status` remains `proof_required`, which makes the precompile gate fail if a song attempts to use it.

## Design improvements over V1

- eliminate global shake as a default motion source;
- cache static masks/fields once per shot;
- use loop-safe phase functions and advected fields instead of per-frame random noise;
- protect faces/hands/instruments from broad warps;
- support explicit ROIs/masks for fire, smoke, water, glass and reflective surfaces;
- separate flame geometry from firelight illumination;
- make transitions physically motivated by visible scene elements;
- expose song-agnostic presets instead of hard-coded song paths;
- keep real 3DGS clearly separate from 2D Gaussian light fields.

## Source lineage being consolidated

- Silver Coin V8 effect packs and music-directed living painting tools;
- Irish Eyes Magic Gate perceptual/reflection/water/glass transition families;
- IronFlame recursive transition and temporal-painting concepts;
- Leave It by the Door native-24 localized weather/fire/identity-safe motion renderer;
- SuperSplat for genuine Gaussian-splat scene editing/rendering only when valid splat geometry exists.
