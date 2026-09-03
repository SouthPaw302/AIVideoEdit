# AIVideoEdit — Effects & Rendering Method Catalog

This file is a persistent reference for effects that have been implemented, tested, or deliberately rejected in production. It complements `VISUAL_STYLE_CATALOG.md`: the style catalog describes visual languages; this catalog describes reproducible motion, spatial, transition, lighting, and compositing methods.

## Design rules

1. Prefer effects that preserve subject identity and painterly surface stability.
2. Every effect should have a motivated visual role; avoid random particles or constant motion.
3. CPU-safe implementations are valuable because they can run in a recovery environment without GPU dependencies.
4. Distinguish true neural methods from approximations. Never describe pseudo-depth or image warping as a full 3D reconstruction.
5. Save deterministic seeds and configuration with renders.
6. QC still frames and transitions before committing a full-song render.

## Implemented CPU methods

### Pseudo-depth parallax

Derive a stable non-metric depth proxy from vertical perspective, local luminance contrast, edge salience, and saturation. Use the field to drive per-pixel camera displacement.

Use for: gentle camera travel through still paintings, foreground/background separation, layered occlusion.

Do not claim: monocular metric depth or reconstructed 3D geometry.

### Localized micro-warp

Apply low-frequency, sub-pixel mesh motion gated by the depth proxy. Designed to suggest breathing, cloth movement, crowd sway, leaves, and hair without high-frequency texture boiling.

Use for: living-painting motion where a full character animation model is unavailable.

### Advected atmosphere

Create a low-frequency density field once, then advect/remap it over time instead of generating new random noise each frame. Tint and depth-gate it as fog, smoke, steam, or mist.

Benefit: atmospheric motion stays coherent and does not crawl like regenerated noise.

### Depth-gated volumetric light shafts

Generate soft radial/fan light volumes from a motivated source such as a tavern window, hearth, lantern, or dawn sun. Gate visibility using pseudo-depth so the light reads as occupying space instead of being painted uniformly over subjects.

### Motivated particle fields

Use deterministic particles only when justified by the scene:

- exterior: rain, occasional wet-air points
- tavern/hearth: embers and ash
- workshop/forge: sparks

Avoid decorative magical particles with no physical source.

### Firelight breath

Combine multiple low-amplitude temporal sine components to modulate warm luminance around hearth/candle scenes. The amplitude is intentionally small to avoid visible flicker artifacts.

### Puddle reflection shimmer

Warp only the lower exterior frame with low-amplitude horizontal displacement, blending the warped result back through a vertical mask. Useful for wet roads and reflected lantern/sunset light.

### Chroma pigment transport

During a transition, move the LAB chroma channels toward the incoming scene before fully replacing luminance/geometry. This allows a cold exterior painting to begin warming into tavern amber before the scene itself changes.

### Pigment dissolve

Use a stable low-frequency field as a soft threshold mask, with a short mid-transition bloom. The result resembles wet pigment mixing more than a digital crossfade.

### Object portal / match-cut portal

Expand a circular mask from a real recurring object and reveal the next scene through it. Optional narrow optical glints can be added along the ring.

Silver Coin implementation: the coin becomes a reflective portal rather than a generic magical vortex.

### Edge-contamination reframe

When storyboard titles or labels touch an image edge, reframe/crop the contaminated strip and restore composition instead of asking an inpainting algorithm to invent a large replacement region. This is safer for moving footage because no synthetic repair texture can shimmer later.

### Painterly upscale

Lanczos enlargement + restrained bilateral smoothing + low-amplitude unsharp recovery. Avoid aggressive AI-style sharpening that converts painted faces and cloth into plastic photo texture.

## Hybrid neural-radiance-field integration

A compact CPU NeRF may supply learned volumetric density/color and view-dependent atmosphere while detailed subjects remain painted multi-plane imagery. Pseudo-depth methods in this catalog can drive compositing masks, occlusion, and camera motion around that neural field.

Allowed description: **hybrid neural-radiance-field spatial rendering** when an actual trained radiance-field component is present.

Do not describe pseudo-depth, parallax, or noise volumes alone as a NeRF.

## Silver Coin V3/V3.1 production findings

- Large storyboard label remnants are better removed by reframing than inpainting.
- Rain reads well over the cold labor/village scenes but should not leak deeply into the tavern interior.
- Tavern embers should remain sparse and physically tied to hearth/firelight.
- Low-frequency mesh motion is safer than frame-randomized deformation for the Living Pre-Raphaelite surface.
- Depth-gated light volume increases perceived space without breaking the oil-painting material.
- The silver-coin portal should remain brief; the coin is a narrative match-cut device, not a permanent fantasy effect.

## Future method candidates

- audio-derived transient envelopes mapped to bow strokes, foot stamps, coin glints, and light response
- optical-flow assisted interpolation between closely matched generated keyframes
- semantic masks for faces/hands/instruments to keep those regions more rigid than cloth/background motion
- multi-plane depth cards with foreground segmentation and explicit occlusion ordering
- learned depth maps when a reliable local model is available
- true Gaussian splatting or full NeRF reconstruction when an appropriate GPU/runtime and source views exist
- palette-consistent grain/brush restoration after heavy compositing
- temporal artifact detector for face/hand/instrument drift

Update this file whenever a method becomes reproducible enough that another agent should be able to discover and reuse it.