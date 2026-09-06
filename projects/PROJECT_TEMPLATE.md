# Production Branch Template

Use only on `song/<slug>`. A new supplied audio master creates a fresh branch from current `main` unless the user explicitly names an existing branch to continue.

## Required branch-local package
- `PROJECT.md`
- `STATUS.md`
- `HANDOFF.md`
- `PROJECT_STATE.json`
- `SOURCE_AUTHORITY.json`
- `REFERENCE_MANIFEST.json`
- `MEDIA_PLAN.json`
- `ASSET_MANIFEST.json`
- `LYRICS.md` when applicable
- `VISUAL_DNA.md`
- `SHOT_LIST.md`
- FX plan/manifest and later `fx.lock.json`
- `RENDER_HISTORY.md`
- `QC.md`
- `shot_packages/`

The machine stage is recorded in `PROJECT_STATE.json` and validated by `general/reusable/tools/production_guard.py`. Do not manually claim a later state unless its required evidence exists.

Historical chats/branches/media are excluded by default in `SOURCE_AUTHORITY.json`. Explicit user authorization is required to add any such source.
