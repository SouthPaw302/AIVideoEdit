# AIVideoEdit

AI-native music-video production pipeline for turning songs into directed visual films.

## New agent / new chat

**Start here:** [`AGENT_HANDOFF.md`](AGENT_HANDOFF.md)

That file is the canonical recovery entrypoint for the entire project. It explains the system, storage model, tool/connector philosophy, production workflow, and how to recover active song projects without relying on chat history.

Then read:
- [`general/README.md`](general/README.md) — consolidated video/effects/resource archive on `main`
- [`PROJECT_INDEX.md`](PROJECT_INDEX.md)
- [`REPOSITORY_INDEX.md`](REPOSITORY_INDEX.md)
- [`CHAT_RECOVERY_LOG.md`](CHAT_RECOVERY_LOG.md)
- [`docs/CANON_WORKFLOW.md`](docs/CANON_WORKFLOW.md)
- [`docs/CONTINUOUS_CHECKPOINT_POLICY.md`](docs/CONTINUOUS_CHECKPOINT_POLICY.md)
- [`docs/VISUAL_STYLE_CATALOG.md`](docs/VISUAL_STYLE_CATALOG.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/STORAGE_AND_CONNECTORS.md`](docs/STORAGE_AND_CONNECTORS.md)

This repository is the canonical source for:

- song-to-visual direction
- visual DNA and storyboard manifests
- visual style and rendering-method catalog
- AI image artifact QC
- 2.5D / parallax animation
- looping environmental motion
- audio-reactive cinematography
- hybrid visualizers
- FFmpeg/Python assembly
- tool / MCP / connector interfaces
- project status and handoff context
- final render validation

`general/branch-snapshots/` preserves complete Git-tree snapshots of every known Video Creation production branch, while `general/reusable/` preserves reusable effect/tool trees. Archive branches under `archive/video/*` provide additional point-in-time recovery refs.

Large media assets (WAV/MP3/PNG/MP4) may also live in persistent Library or external object storage when they exceed GitHub's ordinary file limits; the repo preserves hashes, manifests, storage references, representative media, scripts, effects, QC, and exact recovery state.

## Canon workflow

1. Listen & Decode
2. Define Visual DNA
3. Concept / Style Tests
4. Asset Creation
5. Artifact Scan & Repair
6. Animation & Layering
7. Sync & React
8. Edit / Transition Design
9. Final Grade & Render
10. Validation & Archive

See `docs/CANON_WORKFLOW.md`.

## Video projects

- **IronFlame** — V1 delivered; final MP4 archive identity remains an explicit recovery gap.
- **Silver Coin** — V8 final complete / QC passed; full production/effect state preserved on `song/silver-coin` and in the general branch snapshot.
- **Leave It by the Door** — recovery/partial project.
- **Sigh No More / Irish Eyes, Spanish Hair** — recovery/partial project.

Every active song project should contain enough written and referenced state in its project directory to survive a new chat or agent handoff.