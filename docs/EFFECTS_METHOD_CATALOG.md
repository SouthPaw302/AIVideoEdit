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

### Localized micro-warp / mesh breath

Apply low-frequency, sub-pixel mesh motion. One variant is depth-gated; another pins frame edges while letting the interior breathe. Both are designed to suggest breathing, cloth movement, crowd sway, leaves, and hair without high-frequency texture boiling.

Use for: living-painting motion where a full character animation model is unavailable.

### Temporal canvas lock

Generate one deterministic woven/pigment field per scene and reuse the same field on every frame. This restores a stable canvas/pigment micro-surface after remapping/compositing and prevents frame-randomized grain from crawling.

### Advected atmosphere

Create a low-frequency density field once, then advect/remap it over time instead of generating new random noise each frame. Tint and depth-gate it as fog, smoke, steam, or mist.

Benefit: atmospheric motion stays coherent and does not crawl like regenerated noise.

### Depth-gated volumetric light shafts

Generate soft radial/fan light volumes from a motivated source such as a tavern window, hearth, lantern, or dawn sun. Gate visibility using pseudo-depth so the light reads as occupying space instead of being painted uniformly over subjects.

### Motivated radial candle/window shafts

A lighter-weight variant generates soft warm radial shafts around a known source location. It is useful when depth gating is unnecessary or the source image already strongly establishes room depth.

### Motivated particle fields

Use deterministic particles only when justified by the scene:

- exterior: rain, occasional wet-air points
- tavern/hearth: embers and ash
- workshop/forge: sparks

Avoid decorative magical particles with no physical source.

### Firelight breath

Combine multiple low-amplitude temporal sine components to modulate warm luminance around hearth/candle scenes. The amplitude is intentionally small to avoid visible flicker artifacts.

### Heat haze

Apply a restrained refractive warp only within the region affected by hot candles/hearths. Avoid global wavy distortion. Use low amplitude and blend the warped result back into the original frame.

### Puddle reflection shimmer / wet reflection ripple

Animate the lower exterior frame with restrained refractive displacement. The stronger variant builds a faint mirrored color memory from image content immediately above the road line and ripples it before blending it into the wet ground.

### Depth focus breath

Use the pseudo-depth field to move a shallow focus zone slowly through a portrait/subject shot. The background blur contribution stays low; this is an emotional emphasis tool, not a simulated DSLR rack-focus showcase.

### Localized specular glint

Sweep a small specular highlight across a bounded metallic region such as a coin, buckle, blade, glass rim, or instrument fitting. It must not brighten the whole frame.

Silver Coin implementation: the glint is centered only on the coin/hat area.

### Performance transient warp

Apply a small impulse-shaped regional warp to a performance ROI. It can suggest bow strokes, drum hits, hand strikes, foot stamps, or other transients. When real audio is available, drive the impulse from the transient envelope instead of a fixed cycle.

Silver Coin implementation: the fiddler bow region receives a tiny transient warp.

### Chroma pigment transport

During a transition, move the LAB chroma channels toward the incoming scene before fully replacing luminance/geometry. This allows a cold exterior painting to begin warming into tavern amber before the scene itself changes.

### Pigment dissolve

Use a stable low-frequency field as a soft threshold mask, with a short mid-transition bloom. The result resembles wet pigment mixing more than a digital crossfade.

### Object portal / match-cut portal

Expand a circular mask from a real recurring object and reveal the next scene through it. Optional narrow optical glints can be added along the ring.

Silver Coin implementation: the coin becomes a reflective portal rather than a generic magical vortex.

### Edge-contamination reframe

When storyboard titles or labels touch an image edge, reframe/crop the contaminated strip and restore composition instead of asking an inpainting algorithm to invent a large replacement region. This is safer for moving footage because no synthetic repair texture can shimmer later.

The same rule applies to lyric/caption contamination along the bottom edge: crop/recompose when it preserves the shot better than generative repair.

### Painterly upscale

Lanczos enlargement + restrained bilateral smoothing + low-amplitude unsharp recovery. Avoid aggressive AI-style sharpening that converts painted faces and cloth into plastic photo texture.

## Compact CPU neural radiance field

`tools/video_fx/tiny_nerf_volume.py` implements a genuine compact MLP:

`(x, y, z, view_x, view_y, view_z) -> (density, red, green, blue)`

It uses Fourier positional features, a small hidden layer, deterministic training samples, validation samples, and volume rendering along rays. The learned field is designed as atmospheric/light volume, not as a photogrammetric reconstruction of the detailed subject image.

Each production use should record:

- family/config
- seed
- training sample count
- step count
- train loss
- validation loss
- rendered volume resolution/sample count
- composite opacity

## Hybrid neural-radiance-field integration

A compact CPU NeRF may supply learned volumetric density/color and view-dependent atmosphere while detailed subjects remain painted multi-plane imagery. Pseudo-depth methods in this catalog can drive compositing masks, occlusion, and camera motion around that neural field.

Allowed description: **hybrid neural-radiance-field spatial rendering** when an actual trained radiance-field component is present.

Do not describe pseudo-depth, parallax, or noise volumes alone as a NeRF.

## Silver Coin V3/V4 production findings

- Large storyboard label remnants are better removed by reframing than inpainting.
- Bottom lyric/caption contamination in recovered panels can also be removed by deterministic crop/recomposition.
- Rain reads well over the cold labor/village scenes but should not leak deeply into the tavern interior.
- Tavern embers should remain sparse and physically tied to hearth/firelight.
- Low-frequency mesh motion is safer than frame-randomized deformation for the Living Pre-Raphaelite surface.
- Temporal canvas lock helps restore stable painted material after multiple warps/composites.
- Depth-gated or motivated light volume increases perceived space without breaking the oil-painting material.
- Heat haze should stay localized and lower amplitude than ordinary fantasy-video implementations.
- Performance transient warp works best on a restricted ROI and should eventually be driven by the actual audio transient envelope.
- The silver-coin portal should remain brief; the coin is a narrative match-cut device, not a permanent fantasy effect.
- V4 successfully combined 21 cleaned narrative frames with trained NeRF volumes and the CPU motion/effects stack.

## Local audio edit-map method

`tools/audio/analyze_edit_map.py` derives signal-based section candidates, beat times, transient peaks, energy peaks, brightness, and high-value sync points. It intentionally does not auto-label Verse/Chorus/Bridge; semantic labels require listening/lyric verification.

This edit map should drive:

- cut/transition placement
- performance transient effects
- foot-stamp/crowd motion intensity
- coin glints
- firelight/camera response
- section-scale palette and scene-family changes

## Future method candidates

- optical-flow assisted interpolation between closely matched generated keyframes
- semantic masks for faces/hands/instruments to keep those regions more rigid than cloth/background motion
- multi-plane depth cards with foreground segmentation and explicit occlusion ordering
- learned depth maps when a reliable local model is available
- true Gaussian splatting or full NeRF reconstruction when an appropriate GPU/runtime and source views exist
- palette-consistent grain/brush restoration after heavy compositing
- temporal artifact detector for face/hand/instrument drift
- automatic QC contact-sheet generation with frame-risk scoring

Update this file whenever a method becomes reproducible enough that another agent should be able to discover and reuse it.