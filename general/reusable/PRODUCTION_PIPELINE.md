# Production Pipeline

This is the ordered method for turning a song into a finished, visibly
animated music film. It applies on every `song/<slug>` branch.

## Step 0 — Determine reference availability

Before anything else, decide which path applies for this production.

**Branch A — reference video/images exist.**
1. Extract frames from the reference at a meaningful sampling rate.
2. Analyze visual style, motion language, palette, and (if a human
   subject is present) identity-bearing features that must be preserved.
3. Analyze the lyrics and the song's beat/structure to define narrative
   beats and musical cues.
4. Derive the shot library and storyboard from the source material,
   mapping narrative beats to specific extracted frames/ranges.

**Branch B — no reference video/images exist.**
1. Derive the visual DNA from the lyrics, genre, and mood alone: define
   setting, era, palette, lighting philosophy, and (if there is a
   protagonist) an identity sheet describing them consistently.
2. Generate original key stills via the generative engine at a locked
   spec (resolution, aspect ratio, character/identity sheet) — see
   `general/reusable/generative-engine/README.md`.
3. Lock the identity/style decisions before proceeding; do not
   regenerate a subject's face/identity between shots once locked.
4. Rejoin the pipeline at the same point Branch A does: build the shot
   library and storyboard, now from your own generated stills instead
   of source footage.

Both branches converge here onward. A missing reference is not a reason
to build a weaker or more static film — treat generated stills exactly
like extracted frames: raw scene material to be brought to life, not a
long static image.

## Step 1 — Lock storyboard and shot map

The storyboard is a production map. Every selected frame/still must
become a real shot package — a storyboard is not itself a deliverable.

## Step 2 — Build the asset/shot library

For each shot, use the standard layout:

```
projects/<slug>/shot_packages/<shot_id>/
  source/      alpha/      layers/      depth/
  generated/   fx_assets/  transition/  loop/
  preview/     notes/
```

Preview mode means producing genuine production ingredients and short
proof renders — not prematurely assembling the full movie.

## Step 3 — Create real animated/composited shot packages

Reuse before inventing. Read, in order, before building any new effect:

1. `general/reusable/CANONICAL_EFFECT_REGISTRY.md` / `.json`
2. `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`
3. `general/reusable/generative-engine/`
4. `general/reusable/fx_v2/`

Reusable technology available in this repo includes: 2.5D/depth
parallax; compact NeRF / hybrid radiance-field rendering where
technically truthful; 3D Gaussian Splatting (only when actual splat
data exists — see `technical_truthfulness` below); mesh/micro-motion and
living-image motion; fog/smoke/rain/embers/heat-haze atmosphere;
water/wet-road reflections; halation/bloom/light shafts/glints;
transient/performance warps; audio-reactive controls; a shared
frame-aligned reactive control bus; organic generative visual plates;
pigment/object/recursive transitions; an integrated visualizer
language; and temporal QC.

Major reusable trees: `general/reusable/fx_v2/`,
`general/reusable/generative-engine/`, `general/reusable/depth-parallax-25d/`,
`general/reusable/silver-coin-tools/`, `general/reusable/silver-coin-docs/`,
`general/reusable/irish-eyes-tools/`.

### Technical truthfulness

- 2.5D means depth/layer-aware image-space motion.
- NeRF means an actual trained neural radiance field.
- Hybrid NeRF means a trained radiance-field component composited with
  image/depth layers.
- 3DGS means actual Gaussian-splat scene primitives/data are rendered.
- Do not rename a look-alike effect as a technology that was not
  actually used.

Protect identity-bearing human subjects from morphing, anatomy drift,
waxy faces, or obvious matte artifacts, whether the subject came from
source footage (Branch A) or a locked identity sheet (Branch B).

## Step 4 — Add music-directed behavior and transitions

The song can drive: shot timing, cut/transient accents, motion density,
atmosphere, reflection strength, light/glint behavior, camera amplitude,
and transition timing. Preferred architecture: analyze the song once
into a preserved, smoothed, frame-aligned control bus (RMS/onset/
low/mid/high) when multiple systems need the same signals, rather than
re-deriving audio analysis per effect.

## Step 5 — Assemble

Only assemble once enough finished shot packages exist. Do not confuse
verification infrastructure (the FX gate, precompile checks) with the
creative production itself.

## Step 6 — Render and QC the complete movie

See the final-QC checklist in `AGENT_HANDOFF.md`.

## Step 7 — Archive

Preserve recovery docs, manifests, hashes, QC, prompts, decisions, and
external-storage pointers. Promote genuinely reusable methods back to
`general/reusable/` — but only after they've proven useful, not
pre-emptively.
