# AIVideoEdit Repository and Recovery Index

This is the durable index for the ChatGPT **Video Creation** project. It maps the system, projects, branches, styles, archives, recoverable assets, and reusable production technology so a future agent can resume without relying on chat history.

## Canon entrypoints

| Path | Purpose |
|---|---|
| `AGENT_HANDOFF.md` | Primary operating instructions for every new agent/chat |
| `README.md` | Short repository orientation |
| `CANONICAL_EFFECTS.md` | Root recovery entrypoint for all reusable loops/effects/transitions |
| `general/README.md` | Consolidated archive of all known Video Creation branches, reusable effects/resources, and binary recovery gaps |
| `general/ARCHIVE_INDEX.json` | Machine-readable branch tips, tree SHAs, final-output hashes and archive state |
| `general/SESSION_ASSET_RECOVERY.md` | Fingerprints for session-visible binaries not yet streamable into GitHub |
| `general/reusable/README.md` | Front door for reusable production technology |
| `general/reusable/CANONICAL_EFFECT_REGISTRY.md` | Human-readable canonical registry of cross-project effects/loops/techniques |
| `general/reusable/CANONICAL_EFFECT_REGISTRY.json` | Machine-readable canonical effect registry |
| `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md` | Provenance and status of techniques by project |
| `general/reusable/EFFECT_PACKAGE_STANDARD.md` | Required packaging/QC metadata for every reusable effect/loop |
| `general/reusable/REUSABLE_EFFECTS_POLICY.md` | Promotion and reuse policy |
| `REPOSITORY_INDEX.md` | Complete recovery map and branch registry |
| `PROJECT_INDEX.md` | Active and reference production registry |
| `CHAT_RECOVERY_LOG.md` | Durable summary of recovered Video Creation conversations and remaining gaps |
| `docs/CANON_WORKFLOW.md` | Ten-phase music-video production workflow |
| `docs/CONTINUOUS_CHECKPOINT_POLICY.md` | Mandatory in-progress GitHub save points and asset/effect traceability |
| `docs/VISUAL_STYLE_CATALOG.md` | Named rendering, animation, narrative, visualizer, and transition languages |
| `docs/ARCHITECTURE.md` | Direction, asset, QC, animation, edit, render, and archive layers |
| `docs/STORAGE_AND_CONNECTORS.md` | GitHub/workspace/object-storage roles and connector rules |
| `projects/PROJECT_TEMPLATE.md` | Required structure for every new song |

## Branch registry

| Branch | Scope | Current role |
|---|---|---|
| `main` | Repository-wide canon, merged records, reusable effect registry, and `general/` archive | Default recovery branch |
| `song/irish-eyes` | Irish Eyes production | Active preview/shot-package production; V4 Brandi-based baseline and 5,611-frame extraction recorded |
| `song/ironflame` | IronFlame production | V1 delivered; exact final MP4 archive references still need recovery |
| `song/silver-coin` | Silver Coin production | V8 final complete / QC passed |
| `song/leave-it-by-the-door` | Historical project recovery | Warm tavern/living-scene evidence; missing source/output details recorded |
| `song/sigh-no-more` | Draft project recovery | Veo/Sora prompt architecture preserved; no completed render confirmed |
| `archive/video/ironflame` | Point-in-time IronFlame backup | Frozen recovery ref from current production tip at archive time |
| `archive/video/silver-coin` | Point-in-time Silver Coin backup | V8 final production tip at archive time |
| `archive/video/leave-it-by-the-door` | Point-in-time recovery backup | Preserves recovery project state |
| `archive/video/sigh-no-more` | Point-in-time recovery backup | Preserves recovery project state |

New songs should normally use `song/<slug>`. After meaningful production milestones, update the active song branch and preserve important reusable work in the canonical effect registry/general reusable tree.

## General archive layout

`general/branch-snapshots/` contains complete Git-tree snapshots of the tracked contents of historical production branches. These snapshots reuse Git blobs rather than duplicating media bytes, while keeping committed assets reachable from `main`.

- `general/branch-snapshots/ironflame/`
- `general/branch-snapshots/silver-coin/`
- `general/branch-snapshots/leave-it-by-the-door/`
- `general/branch-snapshots/sigh-no-more/`

`general/reusable/` is now the canonical cross-project technology library, not merely a Silver Coin mirror.

Current implementation trees include:

- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`
- `general/reusable/depth-parallax-25d/`
- `general/reusable/irish-eyes-tools/`

The canonical registry currently contains **101 named records** covering implemented/proven effects, final-lineage loops, recovered patterns, project directions, and broader system capabilities.

Important accumulated techniques include painterly/living motion, temporal surface lock, pseudo-depth, 2.5D, compact NeRF, Gaussian-style light volumes, true 3DGS as a system option, atmospheric fields, wet reflections, firelight, heat haze, glints, audio reactivity, integrated visualizers, recursive transitions, source-derived loop logic, frame-level shot packaging, narrative ribbon, and temporal QC.

## Project registry

### Irish Eyes

- Active branch: `song/irish-eyes`
- Project path: `projects/irish-eyes/`
- Current production mode: **preview / storyboard-linked shot-package production; do not assemble full movie yet**
- Accepted visual baseline: `IRISH_EYES_V4_REVIEW_MASTER.mp4`
- Baseline duration: 187.120000 s
- Baseline: 720x1280 portrait, 30 fps, 5,611 frames
- Baseline SHA-256: `4ac2a1e3f8b4556d0a384029686cfdf246042c81fed6a9b38a0592fd74637614`
- Full extracted working set recorded at `/mnt/data/irish_eyes_v4_frames/` with `FRAME_MANIFEST.csv` in the originating workspace; GitHub preserves its verified count/path rather than 5+ GiB of PNG binaries.
- Identity anchor: Brandi's real photographic source footage.
- Keep the entry shoreline footage with the boy; exclude the rejected busy beach/crowd/high-rise material.
- Reusable validated contributions: real-footage restoration, warm halation, water shimmer, RMS-driven memory modulation, continuous soft-depth 2.5D, inpainted disocclusion/soft alpha strategy, loopable orbit path, identity-safe temporal QC.
- Mandatory cross-project reference: Silver Coin final motion/quality standard and the entire canonical effect registry.

### IronFlame

- Active branch: `song/ironflame`
- Archive branch: `archive/video/ironflame`
- General snapshot: `general/branch-snapshots/ironflame/`
- Project path: `projects/ironflame/`
- Status source: `projects/ironflame/STATUS.md`
- Core files: `PROJECT.md`, `LYRICS.md`, `VISUAL_DNA.md`, `SHOT_LIST.md`, `PROMPTS.md`, `QC.md`, `ASSET_MANIFEST.json`, `AUDIO_RECOVERY.md`
- Assets include analysis, source/reference imagery, production images, QC material, and lossless-audio recovery parts.
- Critical canon: the IronFlame is a woman; the canonical film is rebuilt from scratch.
- V1 was rendered as a 12-scene, 04:04.680 film: 1280 x 720 master (58.9 MB reported) plus a 540p delivery (21.9 MB reported).
- The exact delivered MP4 binaries/storage IDs remain an explicit archive gap.
- Session-visible storyboard fingerprint: SHA-256 `27cbb1a5b7ac00f65f23ea3f57477781adbd725e6a8a2a8b18513ea8bd8bdc4b`; see `general/SESSION_ASSET_RECOVERY.md`.
- IronFlame's rain/forge/fog/temporal-painting/visualizer/recursive-transition language is preserved in the canonical effect registry with evidence-based status rather than being lost with the project.

### Silver Coin

- Active branch: `song/silver-coin`
- Archive branch: `archive/video/silver-coin`
- General snapshot: `general/branch-snapshots/silver-coin/`
- Project path: `projects/silver-coin/`
- Canonical style: **Living Pre-Raphaelite Folk Romanticism**
- Current final: **V8 complete / QC passed**
- Final master identity: `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`
- Final SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`
- Persistent Library ID: `libfile_acfb04300bd88191b67e23b2ad736870`
- Final master is >100 MB, so GitHub stores its exact recovery metadata/hashes while the large binary remains in persistent archive storage.
- The branch snapshot preserves all Git-tracked references, scripts, effect recipes, QC, timing maps, manifests and representative media.
- Silver Coin is currently the deepest implemented reusable stack and supplied eight named V8 effect-loop presets now registered canonically.

### Leave It by the Door

- Branch: `song/leave-it-by-the-door`
- Archive: `archive/video/leave-it-by-the-door`
- Snapshot: `general/branch-snapshots/leave-it-by-the-door/`
- Status: recovery / partial.
- Canonical recovered production patterns: living-image animation, warm tavern narrative treatment, lyric-timed living-scene experiments, and pre-rendered reusable scene/loop assembly.

### Sigh No More / Irish Eyes, Spanish Hair

- Branch: `song/sigh-no-more`
- Archive: `archive/video/sigh-no-more`
- Snapshot: `general/branch-snapshots/sigh-no-more/`
- Status: recovery / partial; completed render not confirmed.
- Canonical recovered direction: sequential generated cinema, wet-road/rain reflection, candlelight micro-loops, atmospheric fog and restrained ancestral-ghost transitions.

## Silver Coin durable source references

### Canonical audio

- Filename: `Silver Coin  (Remastered).wav`
- SHA-256: `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`
- Format: 48 kHz, stereo, 16-bit PCM WAV
- Duration: 207.440 seconds
- Full source is identified in the project manifest and persistent archive state.

### Supplied visual-style clips

1. `imagine-d04b484c.mp4`
   - SHA-256: `8f14739f3eb4f7e7dcc639dfe9fab398623f4a7b5c31ce8b2c0131fab89e6c9c`
   - 560 x 560, 24 fps, 6.041667 seconds
2. `imagine-5558fc80.mp4`
   - SHA-256: `162b3c5cf6c41cc1b85800a1e6111a94df3e3dd829935521aa8c90de15e51803`
   - 560 x 560, 24 fps, 6.041667 seconds

The originals define the canonical look and motion. GitHub reference copies/previews are recovery aids, not generation masters.

## Production and chat discipline

- One major music-video production per fresh chat when practical.
- One song branch per production.
- GitHub is the persistent brain; large masters may remain in Library/workspace/object storage when they exceed normal GitHub file limits.
- Store practical critical images, previews, masks, references, scripts and effect tests in GitHub.
- Update `STATUS.md`, manifests and QC records after meaningful work and before handing off.
- Record rejections as well as approvals so later agents do not repeat failed directions.
- Preserve shot ratings, timing decisions, prompts, continuity rules, hashes, archive references, and effect recipes.
- Keep `general/`, the canonical effect registry, and archive refs current whenever a production reaches a durable milestone or final state.
- Before inventing a new visual technique, search `CANONICAL_EFFECTS.md` / `general/reusable/CANONICAL_EFFECT_REGISTRY.md` first.

## What “indexed” means

A recoverable project records:

1. branch and project path;
2. canonical source filenames and hashes;
3. available storage or Library references;
4. named visual style and precise visual DNA;
5. representative reference still/motion preview when practical;
6. current state, completed work, rejected directions, and exact next action;
7. shot/timing/QC/effect data as production matures;
8. general archive snapshot and point-in-time archive branch when a major milestone is reached;
9. every reusable effect/loop/transition exported to the canonical registry with validation status and implementation/proof path.

## Mandatory recovery sequence

1. Start on `main` and read `AGENT_HANDOFF.md`.
2. Read `CANONICAL_EFFECTS.md`, `general/reusable/README.md`, and the canonical effect registry.
3. Read `general/README.md`, this file, and `PROJECT_INDEX.md`.
4. Check `general/ARCHIVE_INDEX.json` for archived branch tips and large-binary recovery identifiers.
5. Identify the active song branch.
6. Read the complete active project directory and its corresponding snapshot/handoff material.
7. Resolve original media through `ASSET_MANIFEST.json` and any persistent Library/object-storage references.
8. Continue from `STATUS.md` / the current handoff; do not reconstruct settled decisions from memory.
9. Reuse or adapt existing canonical effects before inventing new ones, and promote any new reusable technique back into `general/reusable/`.
