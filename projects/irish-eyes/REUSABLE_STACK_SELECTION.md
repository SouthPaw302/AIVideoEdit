# Irish Eyes — Reusable Stack Selection

Branch: `song/irish-eyes`

This file locks the repository-wide reusable technologies that must be considered during Irish Eyes preview/shot-package production before any final movie assembly.

## Current phase

Irish Eyes is in **preview / shot-package production mode**.

Do not assemble the full movie yet.

The goal is to prepare storyboard-linked production packages containing the actual ingredients for dynamic long-form YouTube footage: source frames, alpha plates, layers, depth/mattes, generated support media, effect assets, transitions, loops, and short proof/previews.

Do not preview generated images/contact sheets in chat unless the user explicitly asks.

## Canonical motion/quality reference

Use the actual delivered Silver Coin final as the practical quality and motion reference for Irish Eyes:

`Silver_Coin_V8_FINAL_YouTube_720p24.mp4`

Verified reference properties from the user-supplied live YouTube master copy:

- duration: 210.461333 s
- resolution: 1280x720
- frame rate: 24 fps
- video codec: H.264
- audio: AAC, 48 kHz stereo
- SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`

This hash matches the archived canonical Silver Coin delivery record.

The reference is important because its success comes from the combination of methods, not one isolated effect. It maintains coherent subjects and compositions while repeatedly changing depth, atmosphere, light, framing, pose, location, and visual energy. Motion is present inside the image without allowing the movie to collapse into a generic visualizer or simple zoom sequence.

For Irish Eyes, compare preview shots against the *behavior* of this final rather than copying its painterly art direction. The benchmark is:

- coherent visual identity throughout;
- meaningful internal movement;
- visible spatial/depth behavior;
- motivated environmental effects;
- transitions that feel authored rather than generic;
- changing compositions and scene energy across the runtime;
- recurring motifs that create continuity;
- effects that support the image rather than obscure it;
- enough finished shot variety that the eventual long-form edit feels alive.

## Mandatory repository-wide resources

### Silver Coin spatial/effect lineage

Inspect and reuse/adapt from:

- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`

Especially:

- `video_fx/tiny_nerf_volume.py` — compact trained neural radiance-field atmosphere/spatial volume;
- depth/pseudo-depth parallax;
- mesh breath / controlled micro-motion;
- advected atmosphere;
- wet reflection ripple;
- firelight/light breathing where motivated;
- localized heat haze;
- volumetric/light shafts;
- specular/glint tools;
- depth-focus breathing;
- temporal canvas lock where useful;
- pigment/optical dissolves where appropriate;
- object portal/match transitions where motivated;
- motion signature calibration;
- temporal QC.

Silver Coin proved that these techniques can be combined into a living, dimensional long-form sequence. Irish Eyes should reuse the underlying methods without inheriting Silver Coin's painterly art direction.

### 2.5D stack

Use:

- `general/reusable/depth-parallax-25d/`

For selected frames, separate Brandi/source subject, foreground, water/midground, skyline/background, sky, and optical elements where the source supports it.

### Irish Eyes local reusable tools

Use:

- `general/reusable/irish-eyes-tools/`

Including South Florida restoration, water/reflection shimmer, halation/bloom, and audio-reactive treatments already validated for this production lineage.

## Spatial technology choices

Use the strongest technically honest method for each selected shot:

1. 3D Gaussian Splatting / SuperSplat when adequate real multi-view source coverage and runtime support exist;
2. hybrid NeRF/spatial volume when learned atmosphere/light/depth response benefits the shot;
3. strong 2.5D depth-separated parallax when full 3D reconstruction is unnecessary or unreliable;
4. high-quality source-derived optical/compositing motion for shots that should remain primarily photographic.

Do not claim Gaussian or NeRF use unless the actual rendered proof contains it.

## Irish Eyes visual priorities

- preserve Brandi's real photographic identity;
- keep the shoreline boy entry footage approved by the user;
- exclude the rejected busy beach/crowd/high-rise material;
- create additional photoreal support media where the storyboard requires scenes not present in the source;
- maintain South Florida memory / water / light / humid atmosphere language;
- use visible dimensional motion, not only zooms;
- build seamless loops where useful;
- create purposeful transitions between storyboard moments;
- use music-reactive effects driven by `Irish eyes (Remastered).wav` when rendering begins;
- keep effects visible enough to matter;
- QC every proof before promotion into the final movie.

## Shot-package organization

For every selected storyboard/source frame that becomes a shot, prepare a recoverable package such as:

`projects/irish-eyes/shot_packages/<shot_id>/`

with applicable subfolders:

- `source/`
- `alpha/`
- `layers/`
- `depth/`
- `fx_assets/`
- `generated/`
- `transition/`
- `loop/`
- `preview/`
- `notes/`

Not every shot requires every folder, but each shot must contain enough organized material to be assembled later without rediscovering its intended effect/storyboard role.

## Final movie gate

Do not assemble the 3:07 final movie until enough storyboard-linked shot packages and preview clips exist to support a visually dynamic full runtime.
