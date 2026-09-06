# AIVideoEdit

Canonical production system for dynamic long-form music films.

**Universal start:** read `AGENTS.md`, then run the production guard. No agent, model, connector, local script, or human automation receives a separate production authority.

## Repository law
- `main` is system-only: doctrine, contracts, templates, reusable capabilities, proofs, QC, and system indexes.
- Every production lives on its own `song/<slug>` branch.
- A new supplied audio master creates a new `song/<slug>` from current `main` unless the user explicitly names an existing branch to continue.
- Production media/story/prompts/status/manifests/renders/QC stay on that branch.
- Reusable discoveries return to `main` only after project-neutral extraction, proof/QC, and canonical registration.
- Historical chats, unrelated song branches, prior storyboards, prior art direction, and production media are **not production authority** unless the current user explicitly authorizes them.

## Hard contract
- `general/reusable/PRODUCTION_CONTRACT.json`
- `general/reusable/tools/production_guard.py`
- `general/reusable/MEDIA_CAPABILITY_MATRIX.json`
- `general/reusable/fx_v2/registry.json`

The written docs explain the system; the guard determines whether a production may advance.
