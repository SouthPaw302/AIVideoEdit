# AIVideoEdit

Canonical production system for dynamic long-form music films.

**Start:** read `AGENT_HANDOFF.md`.

## Repository law
- `main` is system-only: doctrine, templates, reusable capabilities, proofs, QC, and system indexes.
- `main` does not identify, rank, or link to active/completed song productions.
- Every production lives on its own `song/<slug>` branch.
- A newly supplied music/audio master for video work (MP3/WAV/FLAC/M4A/AAC/etc.) creates a new `song/<slug>` branch from `main` before production begins, unless the user explicitly says to continue a named existing branch.
- Song media, story, prompts, shot packages, status, manifests, renders, and QC stay on that production branch.
- Reusable discoveries return to `main` only after generic extraction, project-neutral naming/path cleanup, proof/QC, and canonical registration.
- Song/project names must not become reusable effect IDs, folder names, preset names, examples, or discovery paths. Origin may remain only as optional provenance.

## System entry points
- `BIBLE.md`
- `SYSTEM_INDEX.md`
- `general/reusable/fx_v2/registry.json`
- `general/reusable/generative-engine/`
- `general/reusable/painterly-motion/`
- `general/reusable/memory-atmosphere/`
- `general/reusable/depth-parallax-25d/`
- `general/reusable/tools/`
