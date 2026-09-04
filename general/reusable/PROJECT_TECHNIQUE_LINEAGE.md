# AIVideoEdit — Project Technique Lineage

This file preserves where reusable production ideas came from so future agents can recover the accumulated visual language without rereading every historical chat.

## Silver Coin

Status: completed V8 final / QC passed. This is the deepest implemented effect source currently available.

Canonical final reference:

- `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`
- SHA-256 `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`

Reusable implementation trees:

- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`

Major reusable contributions:

- painterly/live-image preparation and stable surface treatment;
- pseudo-depth and depth parallax;
- localized micro-warp / mesh breath;
- temporal canvas lock;
- advected atmosphere;
- motivated rain/embers;
- firelight breathing;
- wet reflection ripple / puddle shimmer;
- heat haze;
- depth-focus breathing;
- depth-gated and radial light shafts;
- localized metallic/specular glints;
- transient performance warps;
- chroma pigment transport;
- pigment/fog dissolves;
- object/coin portal transitions;
- narrative-ribbon reframing;
- reference-motion envelope calibration;
- compact CPU NeRF volume and hybrid neural-radiance-field spatial rendering;
- audio edit-map analysis and normalized audio-reactivity controls;
- temporal QC scanning;
- named V8 effect loops/presets: forest breath/hair/garland, coin glint, tavern firelight/smoke, fiddler impact, communal crowd sway, lightning/wet reflection, Gaussian-style light shafts, fog/pigment travel.

Important distinction: Silver Coin's implemented neural spatial path is a compact trained NeRF volume combined with image planes. 3D Gaussian Splatting is also a canonical repository technique, but should only be claimed when actual Gaussian scene data/rendering is used.

## Irish Eyes

Status: active production / preview and shot-package phase.

Validated reusable contributions:

- cinematic real-footage restoration using local luminance recovery, shadow lift, restrained warm balance, saturation recovery, bilateral cleanup, and subtle detail recovery;
- source-derived loop candidate search using frame/motion similarity with visual seam QC required;
- selective warm halation/bloom;
- water-region displacement/shimmer;
- measured song-RMS modulation of shimmer/halation;
- continuous soft-depth 2.5D parallax with protected subject, inpainted disocclusion plate, signed-distance alpha feathering, eased foreground transform, and loopable camera orbit;
- visible-memory treatment preset;
- full-frame extraction + storyboard-linked shot-package workflow.

Implementation/reference paths:

- `general/reusable/irish-eyes-tools/`
- `general/reusable/depth-parallax-25d/`
- `projects/irish-eyes/EFFECT_PROOF_01.md` on `song/irish-eyes`
- `projects/irish-eyes/EFFECT_PROOF_02_25D.md` on `song/irish-eyes`

Known failed patterns that remain useful as negative knowledge:

- long crossfades across real-motion loops can cause double-image ghosting;
- long full-body dream dissolves can create identity double exposure;
- hard foreground cutouts can create sticker/matte artifacts;
- a 2.5D insert can still fail if motion is too weak to read;
- full-runtime QC is required because isolated proofs can pass while timeline integration fails.

## IronFlame

Status: V1 rendered/delivered, but exact final binary identity and per-shot effect log were not fully recovered.

The 12-shot production plan preserves a rich effect language. Treat these as canonical project-direction / rendered-lineage techniques until exact per-effect proof is recovered:

- isolated rain planes;
- puddle ripple and weak ember pulse;
- threshold interior reflection and lamp flicker;
- forge tongs/blade micro-motion;
- furnace breathing;
- onset-driven sparks;
- smoke-hand / memory forms;
- ember cracks revealing faces/forms in architecture;
- lateral parallax and fog drift;
- cloak and wolf gait micro-loops;
- distant fire decay;
- steam/fog, grass/cloak motion and growing horizon gold;
- temporal painting with rotating architecture, suspended debris and pressure-synced scale;
- deep corridor push and long focus pull;
- locked-camera water/reflection motion with ash fall and ember-to-dawn transformation;
- radial forged waveform integrated into world geometry;
- transient ember bursts;
- curtain/dust movement and storm-blue to dawn-gold temporal grade;
- rack focus from symbolic mark to heroine with final heat pulse.

IronFlame's broader visualizer/transition vocabulary is also canonical as project direction:

- runic oscilloscope;
- radial frequency ring around an iron sigil;
- spectrum energy inside forge flame;
- waveform trails in smoke;
- particle tunnels between impossible spaces;
- feedback/plasma gravity-inversion transition;
- recursive match transitions such as raindrop→ember, ember→sun, doorway→corridor, railing→branches, smoke→storm, reflection→underground water, fire→lightning, and eye/glint→moon or forge light.

Source references:

- `general/branch-snapshots/ironflame/projects/ironflame/VISUAL_DNA.md`
- `general/branch-snapshots/ironflame/projects/ironflame/SHOT_LIST.md`
- `general/branch-snapshots/ironflame/projects/ironflame/RENDER_HISTORY.md`

## Leave It by the Door

Status: recovered / partial.

Historically supported reusable patterns:

- living-image animation;
- pre-rendered reusable scene/loop assembly;
- warm tavern narrative treatment;
- lyric-timed multi-image/living-scene experimentation.

Do not retroactively claim specific modern effects without recovering the original tests. Preserve this project mainly as lineage for the efficient scene/loop assembly philosophy.

Source reference:

- `general/branch-snapshots/leave-it-by-the-door/projects/leave-it-by-the-door/EFFECTS_PLAN.md`

## Sigh No More / Irish Eyes, Spanish Hair

Status: recovered / partial; sequential video prompt architecture was drafted, completed render not confirmed.

Canonical recovered direction, not validated implementation:

- sequential generated cinema / shot-to-shot video prompt architecture;
- wet-road and rain-reflection animation;
- candlelight micro-loops;
- atmospheric fog;
- restrained ancestral-ghost transitions;
- recurring rural/lake/mountain-road/old-house/wet-pavement visual continuity.

Source reference:

- `general/branch-snapshots/sigh-no-more/projects/sigh-no-more/EFFECTS_PLAN.md`

## Repository-wide AI Video Production System specification

The project file `AI_Video_Production_System_Master_Prompt.pdf` defines a broader capability target that should remain canonical architecture, not be confused with implemented effects.

System-capability lineage includes:

- nondestructive layered compositing;
- masks, mattes, alpha, keying, roto, planar/point/camera tracking;
- cleanup, object removal, stabilization and screen replacement;
- procedural, particle, lens, warp, distortion, glow, blur, sharpen, depth and light effects;
- reusable node/effect graphs and presets;
- nested timelines and retiming curves;
- one shared project state with reversible edits;
- proxy/cache/render invalidation strategy;
- deterministic/resumable delivery;
- machine-readable QC for black/flash/duplicate frames, clipping, loudness, color mismatch, missing media, sync, aspect, compression and render failures.

These are system requirements. They enter the visual effect library as implemented techniques only after real code/proof exists.

## Future mining rule

Whenever another historical video, file-library artifact, chat recovery, external-drive index, or old render is recovered:

1. identify any new loop/effect/transition/animation method;
2. add it to `CANONICAL_EFFECT_REGISTRY.json` and `.md`;
3. preserve source filename/hash/storage reference when available;
4. assign an evidence-based status;
5. promote generic implementation into `general/reusable/` when possible;
6. never discard a useful technique merely because the original song is finished.
