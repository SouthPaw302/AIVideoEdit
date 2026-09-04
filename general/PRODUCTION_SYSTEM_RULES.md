# AIVideoEdit — System-Wide Production Rules

Canonical branch: `main`

These rules apply to every song/video project in this repository unless a project-specific directive explicitly overrides them.

## 1. Product definition

AIVideoEdit exists to create dynamic long-form music films for YouTube and related delivery surfaces. The target is not a slideshow, a generic visualizer, or a single source clip with barely visible effects.

Each song is developed as a directed visual story made from authored shots, loops, transitions, environmental extensions, dimensional motion, generated support footage, photographic source material, and music-driven effects.

## 2. Storyboard is a production map

A storyboard is not only a preview document. It is the production map for the actual movie.

For each selected storyboard frame or source frame that will become a scene, create a shot package containing the media needed to animate, transition, loop, composite, or extend that shot.

Do not require every source frame to become a shot. Select enough strong frames/scenes to give the final long-form movie continuous visual life and narrative coverage.

## 3. Shot-package / asset-first phase

Before assembling the final movie, build and organize the shot library.

A shot package may include, as appropriate:

- original/canonical source frame or clip;
- copied working frame;
- transparent RGBA/alpha subject plate;
- foreground, subject, midground, background, sky, water, architecture, or prop layers;
- masks, mattes, depth maps, segmentation, holdout masks, and occlusion maps;
- environmental extension plates;
- generated support images or footage that are intended for the real movie;
- reflection, fog, haze, rain, embers, light, bloom, prism, distortion, volumetric, or other FX assets;
- transition entry/exit elements;
- loop ingredients and seamless loop renders;
- short rendered preview/proof video showing the intended motion/effect;
- QC notes and storyboard/timeline placement metadata.

Do not assemble the final long-form movie until a useful bank of these shot packages exists and is organized in story order.

## 4. Preview-mode rule

When the user says the project is in preview/asset-production mode, create actual production media and short proof clips, but do not assemble the final movie.

Preview mode means "prepare the finished ingredients," not "show concept art in chat." Do not surface image/contact-sheet previews in chat unless the user asks to see them.

## 5. Mandatory reusable-stack preflight

Before inventing a new effect, every agent must inspect `main/general/reusable/` and the repository-wide catalogs.

At project start or recovery, explicitly inventory which existing techniques are relevant to the song and record the selected ones in the project effects plan.

Existing reusable technology must be preferred over recreating weaker substitutes from scratch.

At minimum, agents must check for:

- 2.5D/depth-parallax tools;
- spatial/NeRF/3DGS techniques;
- camera/motion signatures;
- atmosphere, smoke, fog, rain, ember, water, reflection, bloom, prism, heat-haze and light-shaft effects;
- temporal painting and living-image tools;
- audio-reactive drivers and edit maps;
- transition engines and object portals;
- seamless loop builders;
- temporal/video QC tools.

## 6. Silver Coin spatial/effect lineage is reusable

Silver Coin is a canonical proof project for reusable dimensional and living-image techniques.

Its promoted reusable stack includes:

- `general/reusable/silver-coin-tools/video_fx/tiny_nerf_volume.py` — compact trained neural radiance-field volume;
- hybrid neural-radiance-field spatial compositing;
- pseudo-depth/depth parallax;
- mesh breath and micro-motion;
- advected atmosphere;
- wet reflection ripple;
- firelight breathing;
- localized heat haze;
- motivated volumetric/light shafts;
- silver/specular glints;
- performance transient warps;
- depth-focus breathing;
- temporal canvas lock;
- pigment dissolve;
- object/coin portal transitions;
- motion-signature calibration;
- temporal QC.

These techniques are not Silver Coin-only. Future projects should reuse, adapt, or combine them when the song and footage benefit from them.

## 7. Gaussian splatting / NeRF / 2.5D distinction

Do not blur these terms.

- **3D Gaussian Splatting (3DGS)**: scene reconstruction/rendering using oriented translucent Gaussian primitives; use when adequate source views and runtime support exist.
- **NeRF**: trained neural radiance field; use when an actual neural field is trained and rendered.
- **Hybrid neural-radiance-field spatial rendering**: Silver Coin's proven approach, where a trained radiance-field volume supplies learned atmosphere/light/depth response while detailed imagery remains in image/depth layers.
- **2.5D parallax**: layered/depth-aware image-space camera motion; use when full 3D reconstruction is unnecessary or unsupported.

Never claim a technique was used merely because it was discussed. The rendered result must contain the technique and pass QC.

## 8. Effects must be visible

An effect is not implemented until it is visible in a rendered proof and survives into the exported file.

Do not dial an approved effect down until it is functionally invisible. Subtlety is allowed; absence is not.

For important effects preserve:

- source input;
- implementation/backend;
- parameters/preset;
- rendered proof;
- QC result;
- keep/revise/reject decision.

## 9. Concepts may not disappear

If a project produces a useful visual concept, renderer, transition, motion method, shader, scene graph pattern, or QC method, it must not remain only in chat or only on the song branch.

Promote the generic method to `main/general/reusable/` and add it to the relevant global catalog/index. Keep only song-specific parameters and assets in the song project.

Agents recovering a project must search the reusable library and catalogs before concluding an older concept is unavailable.

## 10. Source-first, generated-support second

Use real source media aggressively when it provides identity, motion, environment, or continuity. Extract and reuse frames, frame windows, masks, loops, retimes, depth layers, and environmental information.

Generated media is also allowed and encouraged when the storyboard requires scenes, environments, transitions, or supporting visuals that do not exist in the real source.

Generated material must be made for a concrete movie purpose, not as decorative concept art.

## 11. Long-form motion density

The final movie should feel continuously alive. Not every frame needs a unique effect, but enough shot packages must contain real movement that long static stretches do not dominate.

Possible motion sources include:

- original footage;
- frame-derived loops;
- optical-flow/interpolated motion;
- 2.5D camera travel;
- Gaussian/NeRF spatial travel where viable;
- moving water/clouds/reflections;
- atmospheric volumes;
- hair/cloth/foliage micro-motion;
- practical-light changes;
- transition motion;
- music-reactive environmental behavior;
- generated support footage.

## 12. Music-directed behavior

Use the song as the control signal. Audio analysis may drive motion density, scene timing, cut points, atmosphere, light, reflections, glints, transient accents, and transition timing.

Do not default to generic spectrum overlays unless the visual language explicitly calls for them.

## 13. Organize before assembly

Shot packages must be named and arranged so the final assembler can follow the storyboard without rediscovering what each asset is.

Recommended structure:

`projects/<slug>/shot_packages/<shot_id>/`

with subfolders such as `source/`, `alpha/`, `layers/`, `depth/`, `fx_assets/`, `generated/`, `transition/`, `loop/`, `preview/`, and `notes/`.

The exact structure may vary, but storyboard placement, source identity, approval status, and preview/proof location must be recoverable.

## 14. Final assembly is a later gate

Do not rush into a full-song render merely because a few assets exist.

The final timeline is assembled only after enough storyboard-linked shot packages, loops, transitions, and effects have passed preview/QC to support the movie's full runtime.

## 15. Final-video QC

Before delivery, scan the actual exported video for:

- black or damaged frames;
- freezes or accidental still stretches;
- repeated sections/loops with visible seams;
- missing or invisible effects;
- incorrect source-footage leakage;
- identity drift;
- temporal flicker/texture boiling;
- transition failures;
- continuity problems;
- audio sync and full runtime.

A successful render command is not a QC pass.

## 16. Persistence

Meaningful production decisions, shot-package manifests, approved previews, effect settings, reusable methods, QC findings, and final render manifests must be checkpointed to GitHub continuously so a new agent can recover the production without relying on chat memory.
