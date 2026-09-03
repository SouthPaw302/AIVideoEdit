# Silver Coin — Effects & Motion Methods

**Branch:** `song/silver-coin`  
**Current renderer family:** CPU painterly sequence + hybrid NeRF-compatible spatial compositing

## Purpose

Silver Coin is the first project in this repository to formalize a reusable CPU-first living-painting effects stack around the selected Living Pre-Raphaelite Folk Romanticism visual language.

The goal is not to make still images visibly wobble. The goal is to create coherent camera travel, air, weather, firelight, cloth/crowd motion, wet surfaces, and object-driven transitions while keeping the hand-painted surface stable.

## V3/V3.1 stack

### 1. Edge-contamination reframe

Recovered storyboard keyframes contained fragments of section titles at the left edge. Early V2 inpainting left residual letters and risked invented texture. V3.1 instead crops/reframes the contaminated edge before 16:9 composition.

QC result: **approved**. No visible storyboard label remains in the cleaned keyframe contact sheet.

### 2. Painterly upscale

Lanczos enlargement + restrained bilateral filtering + low-amplitude unsharp recovery.

Goal: retain brush/pigment texture without producing photographic/plastic faces.

### 3. Pseudo-depth field

A non-metric depth proxy is derived from frame position, local contrast, edges, and saturation. It drives camera displacement and masks atmosphere/light.

This is a compositing utility, not a claim of reconstructed 3D geometry.

### 4. Depth parallax

Per-pixel remapping uses the depth proxy to produce gentle camera motion and relative foreground/background displacement.

Exterior motion amplitude is slightly higher than tavern motion.

### 5. Localized micro-warp

Low-frequency displacement is strongest in mid/near image regions and weak in the distant background. It gives cloth, crowds, foliage, and hair a living quality without random high-frequency deformation.

### 6. Advected atmosphere

Fog/smoke density is generated as a stable low-frequency field and moved over time by advection. The field is depth-gated and tinted by scene family.

Scene roles:

- village: cool mist / wet air
- threshold: mixed cool mist and warm leakage
- tavern: smoke / dust / steam
- coin: restrained haze only
- dawn: soft afterglow atmosphere

### 7. Depth-gated light volume

Soft source-driven fan/radial light is masked by depth and low-frequency density so candle/window/hearth illumination feels volumetric rather than overlaid.

### 8. Motivated particles

Particles are physical, not decorative:

- rain in exterior labor/village shots
- embers in firelit tavern shots
- only weak crossover at the threshold

Deep tavern interiors should not receive rain.

### 9. Firelight breath

Very small multi-frequency brightness/warmth modulation keeps firelit scenes alive while avoiding obvious digital flicker.

### 10. Puddle reflection shimmer

Only the lower exterior portion of the image receives restrained horizontal refractive displacement, suggesting wet road and reflected light.

### 11. Chroma pigment transport

Before a conventional scene replacement becomes obvious, LAB chroma begins drifting toward the incoming painting. This supports the project's cold-road -> warm-tavern palette journey.

### 12. Pigment dissolve

A stable low-frequency threshold field with a brief soft bloom creates a wet-paint transition rather than a standard crossfade.

### 13. Silver-coin portal

The recurring coin opens a circular reflected view into the next shot. The edge receives a narrow silver optical glint. It is intentionally not a fantasy vortex.

Use only around the merchant/coin narrative beat or another explicit coin match cut.

## V3 QC history

### V2

Working motion preview proved parallax, atmosphere, rain/embers, firelight, pigment dissolve, and the coin portal. Residual storyboard letters remained visible in several scenes.

### V3 initial QC

Added localized micro-warp, light volumes, wet-ground shimmer, and chroma transport. Motion/lighting direction passed, but edge title cleanup was still insufficient.

### V3.1 cleanup

Increased edge reframe on contaminated source panels. Cleaned 16:9 keyframes were visually checked and section-title fragments were removed without inpainting.

## Reusable repo implementation

- `tools/video_fx/painterly_cpu_fx.py`
- `tools/video_fx/render_painterly_sequence.py`
- `docs/EFFECTS_METHOD_CATALOG.md`
- `projects/silver-coin/render-config-v3.json`

## Next production improvements

1. Build the real audio edit map from the canonical WAV instead of equal-duration preview scenes.
2. Add transient envelopes for foot stamps, fiddle bow accents, coin glints, and transition timing.
3. Separate face/hands/instrument masks from cloth/background motion so identity-critical regions stay more rigid.
4. Expand beyond the ten recovered storyboard panels with additional clean production stills or locally created composites.
5. Add the compact trained CPU radiance-field layer described in `NERF_PLAN.md` to the approved atmospheric families.
6. Assemble a full-song 16:9 draft, inspect artifact frames, then repair and re-render.

## File needed from the user only when necessary

The canonical WAV is already indexed in the project manifest/Library. If the runtime cannot obtain its actual bytes when full-song audio analysis begins, ask the user to attach `Silver Coin  (Remastered).wav` to the active production chat. Do not ask for it before it becomes the blocking dependency.
