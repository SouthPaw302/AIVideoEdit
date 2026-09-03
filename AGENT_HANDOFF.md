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

Large binary media should normally live in the active ChatGPT project/workspace or external object storage and be referenced by manifest.

---

## 3. Recovery order for a new agent

1. Read `AGENT_HANDOFF.md` (this file).
2. Read `README.md`.
3. Read `REPOSITORY_INDEX.md`.
4. Read `PROJECT_INDEX.md`.
5. Read `docs/CANON_WORKFLOW.md`.
6. Read `docs/VISUAL_STYLE_CATALOG.md`.
7. Read `docs/ARCHITECTURE.md`.
8. Read `docs/STORAGE_AND_CONNECTORS.md`.
9. Resolve the active song branch from `PROJECT_INDEX.md`.
10. On that branch, read everything in `projects/<slug>/`, especially `PROJECT.md`, `STATUS.md`, `VISUAL_DNA.md`, and `ASSET_MANIFEST.json`.
11. Inspect the current repo/branch state before modifying anything.
12. Use only legitimately available tools and continue production without repeatedly asking for minor decisions already settled in the project files.

---

## 3A. Branch, chat, and indexing discipline

- Use one production branch per song: `song/<slug>`.
- Prefer one fresh production chat per video so media generation and rendering do not overload a single conversation.
- Search `REPOSITORY_INDEX.md` and `PROJECT_INDEX.md` before beginning or recovering work.
- Keep global workflow and style vocabulary discoverable from `main`; keep active song decisions and assets on the song branch until intentionally merged.
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

Motion QC must also check temporal flicker, texture boiling, unstable edges, morphing props, black frames, and sync.

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

See `PROJECT_INDEX.md`.

Current flagship/canonical production:

### IronFlame
Directory: `projects/ironflame/`

This is the first project intended to exercise the full canon workflow.

Critical creative rule:

> **The IronFlame is a woman. She is the recurring mythic protagonist.**

Critical production rule:

> **The new canonical IronFlame film must be rebuilt from scratch. Do not reuse prior IronFlame MP4 renders, their frames, scene timing, transitions, or loops.**

Read the project directory before touching production.

---

## 9. Creative authority

The user has explicitly given the system/director latitude to make strong creative choices. Do not stop for every minor decision. Use the song, lyrics, project files, and established visual DNA to keep moving toward a finished film.

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

This is how the project survives chat/context boundaries.