# AIVideoEdit — Canonical Effect Registry

This is the human-readable registry of reusable loops, effects, transitions, spatial methods, animation patterns, audio-reactive systems, and QC methods recovered or created across the Video Creation project.

Every item below is canonical as a discoverable record. **Status determines whether it is proven, final-lineage, recovered, or only designed.**

## A. Silver Coin — implemented reusable stack

### Spatial / dimensional

- `SC-SPATIAL-001` — **Pseudo-depth field** — `final_lineage` — non-metric depth proxy for parallax, atmosphere and focus. Implementation: `silver-coin-tools/video_fx/painterly_cpu_fx.py`.
- `SC-SPATIAL-002` — **Depth parallax** — `final_lineage` — per-pixel depth-dependent camera displacement. Same implementation path.
- `SC-SPATIAL-003` — **Compact NeRF volume** — `render_proven` — actual compact MLP radiance/density field with Fourier features and ray volume rendering. Implementation: `silver-coin-tools/video_fx/tiny_nerf_volume.py`.
- `SC-SPATIAL-004` — **Hybrid neural-radiance-field spatial rendering** — `render_proven` — NeRF atmosphere/light volume composited with image planes; documented in `silver-coin-docs/EFFECTS_METHOD_CATALOG.md` and Silver Coin `NERF_V4_QC.json`.

### Living-image motion

- `SC-MOTION-001` — **Localized micro-warp** — `final_lineage` — low-frequency depth-gated cloth/crowd/foliage/hair motion.
- `SC-MOTION-002` — **Mesh breath** — `final_lineage` — coherent sub-pixel interior motion with pinned edges.
- `SC-MOTION-003` — **Temporal canvas lock** — `final_lineage` — shot-fixed pigment/weave field preventing crawling texture.
- `SC-MOTION-004` — **Depth-focus breath** — `final_lineage` — gentle pseudo-depth rack focus.
- `SC-MOTION-005` — **Performance transient warp** — `final_lineage` — regional impulse warp for bow strokes, drum hits, hand strikes and similar transients.
- `SC-MOTION-006` — **Reference-motion envelope calibration** — `render_proven` — optical-flow measurement of style references used to bound animation intensity.
- `SC-MOTION-007` — **Narrative-ribbon camera travel** — `render_proven` — move focal windows across a continuous multi-character panorama instead of fragmenting it into close crops.

### Atmosphere / light / optical

- `SC-FX-001` — **Advected atmosphere** — `final_lineage` — stable moving fog/smoke from advected low-frequency density fields.
- `SC-FX-002` — **Motivated rain / embers** — `final_lineage` — deterministic scene-motivated particles.
- `SC-FX-003` — **Firelight breath** — `final_lineage` — low-amplitude warm temporal luminance modulation.
- `SC-FX-004` — **Wet reflection ripple** — `final_lineage` — mirrored lower-frame color memory with refractive puddle/road motion.
- `SC-FX-005` — **Puddle shimmer** — `final_lineage` — lighter lower-frame refractive motion.
- `SC-FX-006` — **Heat haze** — `final_lineage` — localized refractive shimmer near motivated hot sources.
- `SC-FX-007` — **Depth-gated volumetric light shafts** — `final_lineage` — light fan/ray volumes gated by pseudo-depth.
- `SC-FX-008` — **Candle/window radial shafts** — `final_lineage` — lighter radial warm shaft variant.
- `SC-FX-009` — **Localized specular glint** — `final_lineage` — bounded metallic sweep for coin, buckle, glass, instrument hardware, etc.

### Transitions / reframing

- `SC-TRANS-001` — **Chroma pigment transport** — `final_lineage` — incoming scene chroma arrives before luminance/geometry.
- `SC-TRANS-002` — **Pigment dissolve** — `final_lineage` — stable low-frequency mask with soft bloom, designed to read as wet pigment mixing.
- `SC-TRANS-003` — **Fog/pigment travel** — `final_lineage` — pigment dissolve extended with traveling fog/light.
- `SC-TRANS-004` — **Object / coin portal** — `render_proven` — recurring object expands into a reflective portal/match cut.
- `SC-EDIT-001` — **Edge-contamination reframe** — `render_proven` — crop/recompose contaminated storyboard edges rather than large synthetic inpainting.

### Audio / QC

- `SC-AUDIO-001` — **Audio edit map** — `render_proven` — signal-derived section candidates, beat/transient/energy/high-value sync points. Implementation: `silver-coin-tools/audio/analyze_edit_map.py`.
- `SC-AUDIO-002` — **Normalized reactivity controls** — `render_proven` — 20 Hz controls for energy, transient, brightness, low, mid and high bands. Implementation: `silver-coin-tools/audio/build_reactivity.py`.
- `SC-QC-001` — **Temporal QC scanner** — `render_proven` — frame-difference, optical-flow and sharpness outlier detection with absolute floors and expected edit windows.

### Silver Coin V8 named effect-loop presets

All implemented in `silver-coin-tools/video_fx/render_silver_coin_v8_effect_pack.py`:

- `SC-LOOP-001` — **Forest breath / hair / garland** — `final_lineage` — masked foliage/hair motion, motivated warm shafts, breathing camera.
- `SC-LOOP-002` — **Coin glint** — `final_lineage` — localized sweep and pulsing ring around the coin.
- `SC-LOOP-003` — **Tavern firelight / smoke** — `final_lineage` — garland micro-motion, multi-source firelight, flame pulse, advected smoke, breathing camera.
- `SC-LOOP-004` — **Fiddler impact** — `final_lineage` — bow-region warp, beat impact camera, localized spark/glint accents.
- `SC-LOOP-005` — **Communal crowd sway** — `final_lineage` — opposing crowd transforms around protected central subject, pulse-driven warmth and camera motion.
- `SC-LOOP-006` — **Lightning / wet reflection** — `final_lineage` — brief lightning bolts/sky flash, reflected road flash, wet-road distortion and camera drift.
- `SC-LOOP-007` — **Gaussian-style light shafts** — `final_lineage` — moving Gaussian light volumes with haze and camera travel; visual Gaussian field effect, not a 3DGS reconstruction.
- `SC-LOOP-008` — **Fog / pigment travel** — `final_lineage` — traveling low-frequency dissolve, fog bloom, localized warm light and camera motion.

## B. Irish Eyes — source-footage and 2.5D stack

- `IE-RESTORE-001` — **Cinematic real-footage restoration** — `render_proven` — LAB/CLAHE luminance recovery, shadow lift, warm balance, saturation recovery, bilateral cleanup and subtle unsharp recovery. Proof: `projects/irish-eyes/EFFECT_PROOF_01.md`.
- `IE-LOOP-001` — **Source-derived motion loop candidate** — `experimental` — frame/motion endpoint search + short source-only crossblend; requires visual seam QC before approval.
- `IE-FX-001` — **Selective warm halation / bloom** — `render_proven` — high-luminance motivated bloom.
- `IE-FX-002` — **Water-region displacement / shimmer** — `render_proven` — localized water motion preserving subject identity.
- `IE-AUDIO-001` — **RMS-driven memory modulation** — `render_proven` — measured song RMS modulates water shimmer and halation with smoothing/bounds.
- `IE-SPATIAL-001` — **Continuous soft-depth 2.5D** — `render_proven` — continuous depth-field background remap plus protected/eased foreground plane; implementation: `depth-parallax-25d/depth_parallax_25d.py`.
- `IE-SPATIAL-002` — **Inpainted disocclusion plate + signed-distance alpha feather** — `render_proven` — protects subject edges during camera travel and fills newly revealed background conservatively.
- `IE-CAMERA-001` — **Loopable eased orbit path** — `render_proven` — camera path returns smoothly to its start for reusable 2.5D passages.
- `IE-FX-003` — **Visible Memory FX preset** — `render_proven` — stronger, intentionally visible memory treatment preserved under `irish-eyes-tools/VISIBLE_MEMORY_FX_PRESET.md`.
- `IE-QC-001` — **Identity-safe loop/2.5D QC rules** — `render_proven` — no hard sticker edges, no double-exposure identity ghosting, no invisible motion, no assumption that endpoint similarity equals seam quality.

## C. IronFlame — canonical mythic effect language

IronFlame V1 rendered, but its complete per-shot effect log is missing. Items therefore remain `rendered_project_unverified_per_effect` or `project_direction` until the exact final is recovered and scanned.

### Shot-motion lineage

- `IF-MOTION-001` — isolated rain planes + puddle ripple + weak ember pulse — `rendered_project_unverified_per_effect`.
- `IF-MOTION-002` — threshold reflection + lamp flicker — `rendered_project_unverified_per_effect`.
- `IF-MOTION-003` — forge tongs/blade micro-motion + furnace breathing + onset sparks — `rendered_project_unverified_per_effect`.
- `IF-MOTION-004` — smoke-hand memory forms — `project_direction`.
- `IF-MOTION-005` — ember-crack light reveals in walls/architecture — `project_direction`.
- `IF-MOTION-006` — lateral parallax + fog drift + cloak/wolf gait micro-loops + distant fire decay — `rendered_project_unverified_per_effect`.
- `IF-MOTION-007` — steam/fog + grass/cloak movement + horizon-gold growth — `rendered_project_unverified_per_effect`.
- `IF-TEMPORAL-001` — rotating architecture + suspended debris + pressure-synced scale temporal painting — `rendered_project_unverified_per_effect`.
- `IF-CAMERA-001` — deep corridor push + long focus pull + distant figure definition gain — `rendered_project_unverified_per_effect`.
- `IF-TEMPORAL-002` — locked water/reflection + ash fall + ember-to-dawn transformation — `rendered_project_unverified_per_effect`.
- `IF-VIS-001` — radial forged waveform integrated into world geometry + transient ember bursts — `rendered_project_unverified_per_effect`.
- `IF-GRADE-001` — storm-blue to dawn-gold temporal grade — `rendered_project_unverified_per_effect`.
- `IF-CAMERA-002` — symbolic mark→heroine rack focus + final heat pulse — `rendered_project_unverified_per_effect`.

### Integrated visualizer language

- `IF-VIS-002` — runic oscilloscope — `project_direction`.
- `IF-VIS-003` — radial frequency ring around iron sigil — `project_direction`.
- `IF-VIS-004` — spectrum energy inside forge flame — `project_direction`.
- `IF-VIS-005` — waveform trails in smoke — `project_direction`.
- `IF-VIS-006` — particle tunnel between impossible spaces — `project_direction`.
- `IF-VIS-007` — feedback/plasma gravity-inversion passage — `project_direction`.

### Recursive transition vocabulary

Registered as `project_direction`:

- `IF-TRANS-001` raindrop→ember
- `IF-TRANS-002` ember→sun
- `IF-TRANS-003` doorway→corridor
- `IF-TRANS-004` iron railing→tree branches
- `IF-TRANS-005` smoke→storm clouds
- `IF-TRANS-006` reflection→underground water
- `IF-TRANS-007` fire→lightning
- `IF-TRANS-008` eye/glint→moon or forge light

Source: `general/branch-snapshots/ironflame/projects/ironflame/VISUAL_DNA.md` and `SHOT_LIST.md`.

## D. Leave It by the Door — recovered historical patterns

- `LD-LOOP-001` — **Living-image animation** — `recovered_pattern`.
- `LD-LOOP-002` — **Pre-rendered reusable scene/loop assembly** — `recovered_pattern` — important production philosophy: build reusable moving scene units before long-form assembly.
- `LD-EDIT-001` — **Lyric-timed multi-image / living-scene construction** — `recovered_pattern`.
- `LD-LOOK-001` — **Warm tavern narrative treatment** — `recovered_pattern`.

Do not assign modern effect implementations retroactively without evidence.

## E. Sigh No More / Irish Eyes, Spanish Hair — recovered direction

All are canonical records but remain `project_direction` / recovery hypotheses until original prompts/tests are verified:

- `SNM-CINEMA-001` — sequential generated cinema / shot-to-shot prompt architecture.
- `SNM-FX-001` — wet-road / rain-reflection animation.
- `SNM-LOOP-001` — candlelight micro-loop.
- `SNM-FX-002` — atmospheric fog.
- `SNM-TRANS-001` — restrained ancestral-ghost transition.

## F. Repository-wide spatial technologies

- `SYS-SPATIAL-001` — **3D Gaussian Splatting / SuperSplat** — `system_capability` — canonical option for actual multi-view 3D Gaussian scene rendering. Do not claim it unless actual splat data/rendering exists.
- `SYS-SPATIAL-002` — **NeRF** — implemented in compact form through Silver Coin; larger captured-scene NeRF remains hardware/source dependent.
- `SYS-SPATIAL-003` — **2.5D scene graphs** — implemented through Silver Coin and Irish Eyes; separate background/midground/subject/foreground/atmosphere/reflections/lights and drive true depth differential.

## G. Broader AI Video Production System capabilities

These are `system_capability` entries from the project-wide production-system specification. They are architectural requirements until a concrete implementation/proof is registered:

- `SYS-COMP-001` layered nondestructive compositing;
- `SYS-COMP-002` masks, mattes, alpha channels and keying;
- `SYS-COMP-003` rotoscoping;
- `SYS-TRACK-001` planar, point and camera tracking;
- `SYS-CLEAN-001` cleanup/object removal/screen replacement;
- `SYS-MOTION-001` stabilization with natural-camera-energy preservation;
- `SYS-FX-001` procedural and particle effects;
- `SYS-FX-002` lens effects, warps and distortion;
- `SYS-FX-003` glow, blur, sharpen and depth/light operations;
- `SYS-EDIT-001` speed changes and retiming curves;
- `SYS-EDIT-002` compound clips and nested timelines;
- `SYS-STATE-001` nondestructive reversible project state and version branching;
- `SYS-PERF-001` proxy/cache/render invalidation;
- `SYS-RENDER-001` deterministic, resumable render/delivery;
- `SYS-QC-001` machine-readable black/flash/duplicate-frame, color, sync, aspect, compression and render-failure QC;
- `SYS-AUDIO-001` audio clipping/loudness/distortion QC and professional post chain architecture.

## Required use in future videos

Before a new shot/effect is invented, search this registry by visual need. Reuse or adapt existing methods first. A project may combine techniques from different songs; the original art direction does not travel with the implementation unless explicitly chosen.

Example: Irish Eyes may reuse Silver Coin's light-volume, wet-reflection, NeRF, motion-calibration and temporal-QC methods without becoming a Pre-Raphaelite painting.

Whenever a new technique is created, update both this file and `CANONICAL_EFFECT_REGISTRY.json` before the production chat ends or moves to another major phase.
