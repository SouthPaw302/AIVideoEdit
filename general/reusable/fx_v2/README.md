# AIVideoEdit Canonical FX V2

Canonical location: `main/general/reusable/fx_v2/`

## Purpose

Unify the strongest proven AIVideoEdit effects behind one stable callable runtime while keeping song-specific timing, ROIs, mappings, and story decisions on song branches.

## Core rule

**Internal scene motion first. Camera motion second.**

The viewer should read a living image, not a still being shaken or zoomed.

## Runtime layers

1. `audio` — shared frame-aligned reactive controls from `general/reusable/generative-engine/`.
2. `surface` — stable canvas/pigment, local contrast, identity protection.
3. `motion` — depth parallax, cloth/hair/crowd breath, water/foliage flow.
4. `environment` — rain, rain glass, fog/smoke, spray, embers, fire.
5. `light` — firelight, moving practical light, shafts, glints, temporal palette migration.
6. `visualizer` — generated compositing plates consuming the shared control bus.
7. `transition` — pigment, fog/light, reflection, doorway/depth, object portal, perceptual gates.
8. `spatial` — honest 2.5D, NeRF atmosphere, and real 3DGS/SuperSplat integration when source geometry supports it.

## Stable IDs

Effects are addressed by stable IDs from `registry.json`. A song manifest calls IDs plus parameters; it does not copy implementation code.

For music-directed projects, prefer a single preserved `FX2-AUDIO-001` analysis pass and map its smoothed controls into several effects rather than independently re-analyzing the song inside every renderer.

The historical IDs in `generative-engine/registry_entries.json` are aliases only; the callable registry remains this directory's `registry.json`.

## Hard precompile gate

A project may not compile merely because an FX ID exists in JSON.

`precompile_gate.py` schema v2 verifies:

- production approval state;
- runtime wiring or real adapter implementation files;
- stub/placeholder rejection;
- human-approved proof records;
- proof-binary bytes when an addressable artifact is recorded;
- deterministic sample-output hashes plus pixel/temporal/global-shift smoke metrics for runtime effects;
- explicit hashed PASS preflight for conditional/external technology;
- exact production `render_inputs` that can alter the pixels.

The generated lock includes a complete evidence fingerprint. Lock verification reruns the live checks immediately before compile. Schema-v1 locks are obsolete and must be regenerated.

See `PRECOMPILE_FX_GATE.md`.

## Promotion gate

No effect is promoted merely because code exists. Candidates require deterministic implementation, representative rendered proof, native project cadence, measurable motion/pixel behavior where appropriate, visual QC, documented limitations, and truthful technology naming.

Adapter/external effects promoted to ordinary `approved` status additionally require byte-verifiable proof artifact evidence. Conditional technologies remain conditional and require project-specific preflight evidence.

## Design rules

- eliminate global shake as a default motion source;
- analyze song reactivity once and preserve a common control bus;
- cache static masks/fields once per shot;
- stream full-song procedural renders rather than buffering every frame in RAM;
- use loop-safe phase functions and advected fields instead of per-frame random noise;
- protect faces/hands/instruments from broad warps;
- support explicit ROIs/masks for fire, smoke, water, glass and reflective surfaces;
- separate flame geometry from firelight illumination;
- make transitions physically motivated by visible scene elements;
- expose song-agnostic presets instead of hard-coded song paths;
- keep real 3DGS clearly separate from 2D Gaussian light fields; see `../SPATIAL_3DGS_SUPERSPLAT.md`;
- keep custom reactive fields distinct from projectM/MilkDrop unless those actual engines are used.

## Historical lineage

FX V2 consolidates reusable implementation lineage from Silver Coin, Irish Eyes, IronFlame, Leave It by the Door, the shared Generative Engine, and genuine SuperSplat/3DGS workflows when real splat geometry exists. Historical integration branches remain provenance only; `main` is the current source of truth.
