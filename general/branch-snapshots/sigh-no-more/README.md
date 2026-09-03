# AIVideoEdit

AI-native music-video production pipeline for turning songs into directed visual films.

## New agent / new chat

**Start here:** [`AGENT_HANDOFF.md`](AGENT_HANDOFF.md)

That file is the canonical recovery entrypoint for the entire project. It explains the system, storage model, tool/connector philosophy, production workflow, and how to recover active song projects without relying on chat history.

Then read:
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

Large media assets (WAV/MP3/PNG/MP4) may live in the active production workspace or external object storage; this repo stores the reproducible workflow, scripts, manifests, asset references, and shot decisions.

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

## Active flagship project

`projects/ironflame/` — canonical rebuild of **IronFlame**, centered on a female mythic protagonist: **she is the IronFlame**.

Every active song project should contain enough written state in its project directory to survive a new chat or agent handoff.