# Project Index

This file tracks productions inside AIVideoEdit. Each project must be recoverable from GitHub without relying on chat history, and every reusable technique must be recoverable without knowing which song first created it.

## Canonical cross-project effect library

Before creating new motion/effects for any project, read:

- `CANONICAL_EFFECTS.md`
- `general/reusable/README.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.json`
- `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`
- `general/reusable/EFFECT_PACKAGE_STANDARD.md`
- `general/reusable/REUSABLE_EFFECTS_POLICY.md`

The registry currently preserves **101 named effect/loop/transition/spatial/QC/system records** mined from the Video Creation project. A record's validation status must be respected; discoverable does not automatically mean render-proven.

## General archive

Known historical Video Creation branches are consolidated on `main` under `general/`, with Git-tree snapshots in `general/branch-snapshots/` and machine-readable recovery state in `general/ARCHIVE_INDEX.json`.

Point-in-time backup branches:

- `archive/video/ironflame`
- `archive/video/silver-coin`
- `archive/video/leave-it-by-the-door`
- `archive/video/sigh-no-more`

## Active / completed productions

### Irish Eyes

Branch: `song/irish-eyes`  
Project path: `projects/irish-eyes/`

Status: **ACTIVE — preview / storyboard-linked shot-package production**

Current rule: **do not assemble the full movie yet.** Build organized, reusable moving-shot packages first.

Accepted baseline:

- `IRISH_EYES_V4_REVIEW_MASTER.mp4`
- 187.120000 s
- 720x1280 portrait
- 30 fps
- 5,611 frames
- SHA-256 `4ac2a1e3f8b4556d0a384029686cfdf246042c81fed6a9b38a0592fd74637614`

The originating workspace extracted all 5,611 frames to `/mnt/data/irish_eyes_v4_frames/` with `FRAME_MANIFEST.csv`; GitHub records that verified working set rather than storing more than 5 GiB of individual PNGs.

Binding visual continuity:

- Brandi's real photographic identity is the reality anchor;
- keep the entry shoreline footage with the boy;
- exclude the rejected busy beach/crowd/high-rise footage;
- storyboard is a production guide/artifact but should not be previewed in chat unless requested;
- selected storyboard/source frames become actual shot packages with source, alpha, layers, depth/mattes, generated/support media, FX assets, transitions, loops, previews, and notes as appropriate;
- use the accumulated canonical effects library and the Silver Coin final as the motion/quality benchmark without copying Silver Coin's painterly art direction.

Validated reusable contributions already promoted/indexed:

- real-footage restoration;
- selective warm halation/bloom;
- audio-reactive water shimmer;
- RMS-driven visible-memory modulation;
- continuous soft-depth 2.5D parallax;
- inpainted disocclusion + soft-alpha strategy;
- loopable eased camera orbit;
- identity-safe temporal/loop QC.

Primary recovery file: `projects/irish-eyes/NEXT_AGENT_HANDOFF.md`.

### Silver Coin

Branch: `song/silver-coin`  
Archive branch: `archive/video/silver-coin`  
General snapshot: `general/branch-snapshots/silver-coin/`  
Project path: `projects/silver-coin/`

Status: **V8 FINAL COMPLETE / QC PASSED**

Canonical style: **Living Pre-Raphaelite Folk Romanticism**

Final master:

- `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`
- SHA-256 `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`
- Persistent Library ID `libfile_acfb04300bd88191b67e23b2ad736870`

Silver Coin is currently the deepest validated reusable-effects source in the repository. Its tools/docs are exposed at:

- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`

Its canonical contributions include pseudo-depth/parallax, mesh breath, temporal canvas lock, advected atmosphere, rain/embers, firelight, wet reflections, heat haze, depth focus, volumetric/radial light shafts, glints, transient performance warps, pigment transitions, object portals, narrative ribbon, motion calibration, compact NeRF/hybrid neural-radiance-field rendering, audio reactivity, temporal QC, and eight named V8 effect-loop presets.

The actual Silver Coin final is the benchmark for the production principle: coherent visual identity plus continuous authored change in composition, depth, atmosphere, light, subject motion, and transitions—not a static slideshow or generic visualizer.

### IronFlame

Branch: `song/ironflame`  
Archive branch: `archive/video/ironflame`  
General snapshot: `general/branch-snapshots/ironflame/`  
Project path: `projects/ironflame/`

Status: **V1 rendered and delivered / exact final MP4 archive identity still needs recovery**

Core canon:

- female mythic protagonist; she **is** the IronFlame;
- dark folk / mythic fantasy / haunted but resolute;
- ember orange → iron blue → ash gray → dawn gold;
- living scenes, not slideshow frames;
- micro-animation, parallax, particles, audio-reactive light/FX, temporal paintings and integrated visualizer language.

Known delivered result: 12 scenes, 04:04.680, 1280x720 master plus 540p compact delivery. Exact final filenames/hashes/storage IDs remain a documented gap.

IronFlame's reusable concepts are preserved in the canonical registry with evidence-based status rather than being lost: rain/reflection treatments, forge motion, furnace breath, onset sparks, fog/cloak/wolf micro-loops, temporal architecture/gravity effects, integrated waveform/oscilloscope/spectrum/plasma language, and recursive object/environment transitions.

A 1536x1024 storyboard visible in the 2026-09-03 runtime is fingerprinted in `general/SESSION_ASSET_RECOVERY.md` as SHA-256 `27cbb1a5b7ac00f65f23ea3f57477781adbd725e6a8a2a8b18513ea8bd8bdc4b`.

## Recovered / partial song projects

### Leave It by the Door

Branch: `song/leave-it-by-the-door`  
Archive branch: `archive/video/leave-it-by-the-door`  
General snapshot: `general/branch-snapshots/leave-it-by-the-door/`

Status: **Recovery / partial**

Canonical recovered patterns:

- living-image animation;
- reusable pre-rendered scene/loop assembly;
- lyric-timed multi-image/living-scene construction;
- warm tavern narrative treatment.

Do not retroactively assign modern implementations without evidence, but do preserve the workflow lineage.

### Sigh No More / Irish Eyes, Spanish Hair

Branch: `song/sigh-no-more`  
Archive branch: `archive/video/sigh-no-more`  
General snapshot: `general/branch-snapshots/sigh-no-more/`

Status: **Recovery / partial**

Canonical recovered direction:

- sequential generated-cinema / shot-to-shot prompt architecture;
- wet-road/rain-reflection animation;
- candlelight micro-loops;
- atmospheric fog;
- restrained ancestral-ghost transitions.

A completed render has not been confirmed, so these remain direction/recovery records until proof is recovered.

## Repository-wide production-system lineage

The File Library project specification `AI_Video_Production_System_Master_Prompt.pdf` defines broader canonical architecture including nondestructive layered compositing, masks/mattes/alpha/keying, roto/tracking, cleanup, stabilization, screen replacement, particles/procedural/lens/warp/glow/depth/light effects, retiming, nested timelines, shared reversible project state, deterministic rendering, caching/proxy behavior, and machine-readable QC.

These are preserved as `system_capability` records in the canonical registry until concrete implementations/proofs are registered.

## Historical/reference techniques now canonicalized

The accumulated registry covers, among other things:

- living-cover / living-image animation;
- source-derived and synthesized micro-loops;
- pre-rendered scene/loop assembly;
- painterly motion transfer;
- music-directed living imagery;
- 2.5D scene graphs and continuous depth parallax;
- compact NeRF / hybrid radiance-field atmosphere;
- 3D Gaussian Splatting / SuperSplat as a distinct system option when actual splat data exists;
- Gaussian-shaped volumetric light fields;
- water/wet-road reflection effects;
- fog/smoke/steam/ash/rain/ember systems;
- heat haze, bloom, halation, glints and light shafts;
- audio-reactive parameters;
- pigment/object/recursive transitions;
- integrated visualizer language;
- motion calibration and temporal QC.

## Adding or continuing a project

Create/use `song/<slug>` and `projects/<slug>/` with at minimum:

- `PROJECT.md`
- `STATUS.md`
- `LYRICS.md` if applicable
- `VISUAL_DNA.md`
- `EFFECTS_PLAN.md`
- `ASSET_MANIFEST.json`

Before inventing new effects, search the canonical effect registry. During production, checkpoint meaningful assets/decisions. Whenever a new useful effect/loop/transition is created or recovered:

1. give it a stable canonical ID/name;
2. preserve implementation or exact recipe/reference;
3. record its source project and validation status;
4. preserve proof/QC/failure knowledge;
5. update both canonical registry files;
6. promote generic implementation into `general/reusable/` when practical.

At a major milestone/final state, update this index, project status/manifests, archive/snapshot records as appropriate, and the canonical effects registry. A useful technique is not allowed to exist only in chat history or a finished video.