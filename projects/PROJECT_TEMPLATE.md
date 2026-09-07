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
- `STORAGE_MANIFEST.json` after remote media storage is initialized
- `LYRICS.md` when applicable
- `VISUAL_DNA.md`
- `SHOT_LIST.md`
- FX plan/manifest and later `fx.lock.json`
- `RENDER_HISTORY.md`
- `QC.md`
- `shot_packages/`

The machine stage is recorded in `PROJECT_STATE.json` and validated by `general/reusable/tools/production_guard.py`. Do not manually claim a later state unless its required evidence exists.

Historical chats/branches/media are excluded by default in `SOURCE_AUTHORITY.json`. Explicit user authorization is required to add any such source.

## No-reference MEDIA_PLAN requirement
When `REFERENCE_MANIFEST.json` contains no usable reference videos and no reference images, `MEDIA_PLAN.json` must contain a locked `visual_direction_gate` before `APPROACH_ESTABLISHED`.

Minimum shape:

```json
{
  "user_approach_established": true,
  "visual_direction_gate": {
    "required": true,
    "presented_in_chat": true,
    "options": [
      {
        "number": 1,
        "name": "Route name",
        "story_approach": "Distinct narrative interpretation",
        "rendering_route": "Distinct artistic/media treatment",
        "storyboard": [
          {"number": 1, "description": "Opening beat/frame"},
          {"number": 2, "description": "Development beat/frame"},
          {"number": 3, "description": "Climactic beat/frame"}
        ]
      }
    ],
    "user_selection": {
      "status": "selected",
      "selected_option_numbers": [1],
      "recorded_user_instruction": "User's explicit current-chat selection or modification"
    },
    "locked": true
  }
}
```

The real gate requires at least three materially distinct options. `status` may be `selected` or `hybrid`; a hybrid records every selected option number plus the user's modification. Concept/storyboard previews used only to choose a route are decision artifacts, not production assets.

Large media may be stored in the song's GitHub Release through `general/reusable/storage/github_release_storage.py`. The branch-local `STORAGE_MANIFEST.json` remains the authoritative index of those remote assets.
