# AIVideoEdit — Canon Agent Handoff

**Repository:** `SouthPaw302/AIVideoEdit`  
**Default branch:** `main`  
**Purpose:** Persistent source of truth for an AI-native music-video production system.

This file is the **primary recovery entrypoint for any new ChatGPT/agent session**. If the user points a new agent to this repository, read this file first, then follow the linked project files.

---

## 1. What this project is

AIVideoEdit is not a single-song project and not a slideshow generator. It is a reusable production framework for turning songs into directed visual films using whatever visual language the song calls for.

Core principle:

> **Each song will speak to you and tell you what it wants to be.**

The system may combine:
- cinematic living paintings
- narrative AI imagery
- traditional video / stock-like footage
- painterly animation
- graphic-novel / collage animation
- 2.5D parallax
- procedural particles and environmental FX
- audio-reactive cinematography
- WMP-era / oscilloscope / spectrum / plasma visualizers
- recursive dream transitions
- temporal paintings
- hybrid techniques

Do not force every song into the same look.

---

## 2. Repo role

GitHub is the **persistent brain**, not the large-media bucket.

Store here:
- workflow documentation
- visual DNA
- lyrics / shot plans / project status
- prompts and style decisions
- reusable render scripts
- QC rules
- manifests
- tool/connector interfaces
- storage references
- production decisions
- the canonical cross-project effect/loop/transition registry

Large binary media should normally live in the active ChatGPT project/workspace or external object storage and be referenced by manifest.

---

## 3. Recovery order for a new agent

1. Read `AGENT_HANDOFF.md` (this file).
2. Read `README.md`.
3. Read `REPOSITORY_INDEX.md`.
4. Read `CHAT_RECOVERY_LOG.md`.
5. Read `PROJECT_INDEX.md`.
6. Read `CANONICAL_EFFECTS.md`.
7. Read `general/reusable/README.md`.
8. Read `general/reusable/CANONICAL_EFFECT_REGISTRY.md`.
9. Read `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`.
10. Read `general/reusable/EFFECT_PACKAGE_STANDARD.md` and `general/reusable/REUSABLE_EFFECTS_POLICY.md`.
11. Read `docs/CANON_WORKFLOW.md`.
12. Read `docs/CONTINUOUS_CHECKPOINT_POLICY.md`.
13. Read `docs/VISUAL_STYLE_CATALOG.md`.
14. Read `docs/ARCHITECTURE.md`.
15. Read `docs/STORAGE_AND_CONNECTORS.md`.
16. Resolve the active song branch from `PROJECT_INDEX.md`.
17. On that branch, read everything in `projects/<slug>/`, especially `PROJECT.md`, `STATUS.md`, `VISUAL_DNA.md`, `EFFECTS_PLAN.md`, `DECISIONS.md`, `ASSET_MANIFEST.json`, and any current handoff/production-rules files.
18. Inspect the current repo/branch state before modifying anything.
19. Use only legitimately available tools and continue production without repeatedly asking for minor decisions already settled in the project files.

---

## 3A. Branch, chat, and indexing discipline

- Use one production branch per song: `song/<slug>`.
- Prefer one fresh production chat per video so media generation and rendering do not overload a single conversation.
- Search `REPOSITORY_INDEX.md`, `PROJECT_INDEX.md`, and the canonical effect registry before beginning or recovering work.
- Keep global workflow, style vocabulary, and reusable production technology discoverable from `main`; keep active song decisions and assets on the song branch until intentionally merged.
- Every project must preserve its branch, project path, canonical source filenames, cryptographic hashes when available, style lock, reference assets, current status, and exact next action.
- Before changing chats or agents, update `STATUS.md` and `ASSET_MANIFEST.json`.

When a user supplies a new visual-style reference:

1. give the style a durable descriptive name;
2. describe surface, palette, lighting, motion, camera, continuity, and failure modes;
3. add it to `docs/VISUAL_STYLE_CATALOG.md`;
4. lock the project-specific interpretation in `projects/<slug>/VISUAL_DNA.md`;
5. preserve small representative still/motion previews in GitHub when practical;
6. record original media filenames, hashes, and external or Library references in the manifest.

---

## 3B. Continuous GitHub checkpoint policy

GitHub updates happen **during production**, not only at the end of a chat. This protects the project from freezes, context/cache limits, failed renders, and agent handoffs.

Checkpoint the active song branch after:

- a source audio or reference asset is received and fingerprinted;
- a style, story, character, palette, or effects decision is approved;
- audio/lyric/structure analysis is completed;
- each meaningful image batch is generated, reviewed, approved, rejected, or repaired;
- an effect or motion test is created and evaluated;
- a shot list, prompt set, timing map, or scene graph changes;
- an intermediate segment or full render is produced;
- QC finds or resolves a material issue;
- an asset is moved to Library/object storage;
- any long operation after which losing the chat would cause duplicated work.

Before starting another major generation/render batch, confirm the previous phase is represented by committed status, manifest, decisions, prompts, and previews.

Generated images and effects must be traceable:

- record prompt/version, intended shot, hash, dimensions, storage path/ID, approval state, and QC notes;
- commit practical-size canonical images, contact sheets, masks, previews, scripts, and effect tests to the song branch;
- when originals are too large, preserve a representative preview plus hash and durable external reference;
- select effects from `docs/VISUAL_STYLE_CATALOG.md` and `general/reusable/CANONICAL_EFFECT_REGISTRY.md`, then lock their actual project use in `EFFECTS_PLAN.md`;
- never leave a critical approval or rejection only in chat.

See `docs/CONTINUOUS_CHECKPOINT_POLICY.md`.

---

## 3C. Mandatory reusable-effects preflight

AIVideoEdit has accumulated reusable visual technology across multiple productions. **Do not start from zero.**

Before creating a new loop, transition, animation, atmosphere treatment, spatial effect, audio-reactive behavior, or QC method:

1. search `general/reusable/CANONICAL_EFFECT_REGISTRY.md` / `.json` for the visual need;
2. inspect the existing implementation/reference path;
3. respect the entry's validation status;
4. adapt the existing technique when it fits rather than recreating it under a new song-specific name;
5. keep the current song's art direction separate from the reusable implementation;
6. when a genuinely new reusable method is created, register it before the production moves on.

The current registry contains the accumulated lineage of Silver Coin, IronFlame, Irish Eyes, Leave It by the Door, Sigh No More / Irish Eyes Spanish Hair, and the wider AI Video Production System design.

Important examples already preserved include:

- Silver Coin's pseudo-depth, mesh breath, advected atmosphere, wet reflections, firelight, heat haze, light shafts, glints, transient warps, pigment transitions, object portal, narrative ribbon, audio reactivity, temporal QC, compact NeRF, and eight named V8 effect-loop presets;
- Irish Eyes' real-footage restoration, halation, water shimmer, source-loop method, continuous soft-depth 2.5D and identity-safe QC;
- IronFlame's rain/forge/fog/temporal-painting/integrated-visualizer/recursive-transition language;
- Leave It by the Door's pre-rendered reusable scene/loop assembly pattern;
- Sigh No More's sequential generated-cinema, wet-road, candlelight and ancestral-transition direction.

A reusable effect must not die with a chat, branch, local directory, or finished song. Follow `general/reusable/EFFECT_PACKAGE_STANDARD.md`.

---

## 4. Canon production workflow

The detailed workflow is in `docs/CANON_WORKFLOW.md`.

High-level phases:

1. Listen & Decode
2. Visual DNA
3. Concept / Style Tests
4. Asset Creation
5. Artifact Scan & Repair
6. Animation & Layering
7. Audio Sync & Reactivity
8. Edit / Transition Design
9. Final Grade & Render
10. Validation & Archive

A production still should become a **mini scene graph**, not just a slow zoom.

Possible independent layers:
- background
- midground
- character
- foreground
- rain / windows
- fog / smoke / steam
- fire / practical lights
- dust / embers / ash
- reflections
- shadows
- visualizer FX
- camera/depth transforms

---

## 5. AI image artifact QC is mandatory

Before expensive animation/rendering, inspect for:
- bad hands/fingers
- malformed eyes/faces
- broken instruments/weapons/props
- duplicated objects
- impossible architecture/perspective
- nonsense text
- bad reflections
- character/costume continuity drift
- unstable regions likely to flicker under warping

Fix selectively. Do **not** regenerate a whole set because of one defect. Crop, mask, edit, darken, blur, cover with atmosphere, or replace only the failing shot.

Motion QC must also check temporal flicker, texture boiling, unstable edges, morphing props, black frames, sync, freezes, duplicate passages, loop seams, and transition ghosting.

---

## 6. Tool philosophy

Use whatever tools are actually available in the current system, including when appropriate:
- image generation/editing
- Python / FFmpeg / image-processing tools
- GitHub connector
- web research
- MCP/plugin-style tools
- project/workspace files
- external storage connectors
- Cloudflare/R2/S3-compatible storage if a legitimate connector or credentialed tool is available

If a desired connector is unavailable:
- do not fake it
- define the interface/config expected
- document the dependency
- use a local/project substitute
- keep the workflow ready to plug the connector in later

The long-term system should evolve reusable modules such as:
- `song_analyzer`
- `visual_dna_builder`
- `shot_planner`
- `artifact_scanner`
- `character_consistency_checker`
- `depth_map_builder`
- `parallax_scene_builder`
- `micro_loop_builder`
- `particle_engine`
- `audio_envelope_extractor`
- `visualizer_engine`
- `transition_engine`
- `scene_renderer`
- `timeline_builder`
- `final_assembler`
- `qc_renderer`
- `publisher`
- `archive_manager`

Exact implementation names may change; preserve the capabilities.

---

## 7. Storage model

Three-tier model:

### GitHub
Persistent text/code/metadata source of truth.

### ChatGPT project/workspace
Active production area for audio, generated images, temporary layers, loops, intermediate segments, contact sheets, and active renders.

### Object/cloud storage
Preferred long-term home for large masters, source image libraries, alternate cuts, reusable FX packs, and archives. Cloudflare R2/S3-compatible storage is a target, but must not be claimed as connected until it actually is.

See `docs/STORAGE_AND_CONNECTORS.md`.

---

## 8. Active projects

See `PROJECT_INDEX.md` for current production status. Do not assume the historically first flagship project is the currently active song.

### IronFlame historical canon

Directory: `projects/ironflame/` on its song branch/snapshot.

Critical creative rule:

> **The IronFlame is a woman. She is the recurring mythic protagonist.**

Critical production rule from the canon rebuild:

> **The new canonical IronFlame film must be rebuilt from scratch. Do not reuse prior IronFlame MP4 renders, their frames, scene timing, transitions, or loops as production sources.**

The techniques learned from IronFlame may still be preserved and reused through the canonical effect registry; the old rendered IronFlame media itself is excluded as a source for that rebuild.

---

## 9. Creative authority

The user has explicitly given the system/director latitude to make strong creative choices. Do not stop for every minor decision. Use the song, lyrics, project files, established visual DNA, and reusable effect library to keep moving toward a finished film.

The target feeling is:

> **“This song became a visual world.”**

Not:

> “Someone put AI pictures behind a song.”

---

## 10. Handoff discipline

Every active production should maintain at minimum:

- `projects/<slug>/PROJECT.md` — immutable-ish concept and rules
- `projects/<slug>/STATUS.md` — current production state and next actions
- `projects/<slug>/LYRICS.md` when lyrics matter
- `projects/<slug>/VISUAL_DNA.md` for detailed direction
- manifests or shot lists as the project matures

Before ending a long session or moving to a new agent, update `STATUS.md` with:
- what was completed
- what was rejected
- current assets and their locations/references
- exact next action
- any technical failures/workarounds
- decisions that must not be lost

Also update the canonical effect registry whenever a reusable production technique is created, materially improved, rejected for a reusable reason, or recovered from historical work.

This is how the project survives chat/context boundaries.