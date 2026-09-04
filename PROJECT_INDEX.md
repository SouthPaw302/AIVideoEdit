# AIVideoEdit — Project Index

Each video has one canonical `song/<slug>` production branch. Cross-project effects and methods live on `main/general/reusable/`.

Before effects work, read `CANONICAL_EFFECTS.md` and the canonical effect registry.

## Active production

### Irish Eyes

- Branch: `song/irish-eyes`
- Project: `projects/irish-eyes/`
- Status: **active — storyboard-linked preview / shot-package production**
- Do **not** assemble the full movie yet.
- Accepted baseline: `IRISH_EYES_V4_REVIEW_MASTER.mp4`
- Baseline: 187.120 s, 720×1280, 30 fps, 5,611 frames
- SHA-256: `4ac2a1e3f8b4556d0a384029686cfdf246042c81fed6a9b38a0592fd74637614`
- Original workspace extracted all 5,611 frames to `/mnt/data/irish_eyes_v4_frames/` with `FRAME_MANIFEST.csv`.
- Brandi's real photographic identity is the reality anchor.
- Keep the entry shoreline footage with the boy; exclude the rejected busy beach/crowd/high-rise material.
- Build selected frames into actual source/alpha/layer/depth/FX/transition/loop/preview shot packages.
- Silver Coin final is the motion/quality benchmark, not the required art style.

Primary recovery file: `projects/irish-eyes/NEXT_AGENT_HANDOFF.md` on the song branch.

## Completed / delivered

### Silver Coin

- Branch: `song/silver-coin`
- Project: `projects/silver-coin/`
- Status: **V8 final complete / QC passed**
- Style: **Living Pre-Raphaelite Folk Romanticism**
- Final: `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`
- SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`
- Persistent Library ID: `libfile_acfb04300bd88191b67e23b2ad736870`

Silver Coin is the deepest completed reusable-effects lineage. Generic tools/methods have been promoted into `main/general/reusable/` and indexed canonically.

### IronFlame

- Branch: `song/ironflame`
- Project: `projects/ironflame/`
- Status: **V1 rendered and delivered; exact final MP4 archive identity still needs recovery**
- 12 scenes, 04:04.680, 1280×720 master plus 540p compact delivery
- Female recurring protagonist: **she is the IronFlame**.
- Exact delivered filename/hash/storage ID remains unknown and must not be invented.

IronFlame's reusable visual/effect language has been registered with conservative evidence statuses so the concepts survive without pretending every effect has been individually verified in the final binary.

## Historical recovery projects

### Leave It by the Door

- Branch: `song/leave-it-by-the-door`
- Status: **recovery / partial**
- Preserved lineage: living-image animation, warm tavern narrative treatment, lyric-timed living scenes, reusable pre-rendered scene/loop assembly.

### Sigh No More / Irish Eyes, Spanish Hair

- Branch: `song/sigh-no-more`
- Status: **recovery / partial; completed render not confirmed**
- Preserved direction: sequential generated cinema, wet-road/rain reflections, candlelight micro-loops, atmospheric fog, restrained ancestral-ghost transitions.

## Cross-project reusable system

Canonical reusable entrypoints:

- `CANONICAL_EFFECTS.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.json`
- `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`
- `general/reusable/EFFECT_PACKAGE_STANDARD.md`
- `general/reusable/REUSABLE_EFFECTS_POLICY.md`

A useful loop/effect/transition is not allowed to exist only in a chat, local preview directory or finished movie. Register it with source lineage, implementation/recipe, proof/QC and an honest validation status.

## Adding a new video

Create one branch: `song/<slug>`.

Minimum project package:

- `PROJECT.md`
- `STATUS.md`
- `LYRICS.md` when applicable
- `VISUAL_DNA.md`
- `EFFECTS_PLAN.md`
- `ASSET_MANIFEST.json`

Use the existing reusable library before inventing replacements. Checkpoint meaningful production state during work. Keep project-specific assets on the song branch; promote only reusable knowledge/tools to `main`.
