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
- `MUSIC_ANALYSIS.json`
- `STORAGE_MANIFEST.json` after remote media storage is initialized
- `LYRICS.md` when lyrics are present
- `VISUAL_DNA.md`
- `SHOT_LIST.md`
- `SCRIPT.md`
- `SCRIPT.json`
- FX plan/manifest and later `fx.lock.json`
- `RENDER_HISTORY.md`
- `QC.md`
- `shot_packages/`

The machine stage is recorded in `PROJECT_STATE.json` and validated by both `general/reusable/tools/production_guard.py` and `general/reusable/tools/narrative_guard.py`. Do not manually claim a later state unless its required evidence exists.

Historical chats/branches/media are excluded by default in `SOURCE_AUTHORITY.json`. Explicit user authorization is required to add any such source.

## MUSIC_ANALYSIS requirement
Before `REFERENCES_ANALYZED`, resolve lyrics status, genre authority, and the musical section/cue map.

Minimum shape:

```json
{
  "schema": "aivideoedit.music-analysis.v1",
  "analysis_complete": true,
  "lyrics": {
    "status": "instrumental",
    "source": "audio_analysis",
    "text_file": null
  },
  "genre": {
    "status": "user_confirmed",
    "label": "Reggae Dubstep Mix",
    "source": "current_user_instruction",
    "confidence": 1.0,
    "user_declaration": "This is a Reggae Dubstep Mix"
  },
  "rhythm": {
    "tempo_status": "measured",
    "tempo_bpm": 76.0,
    "pulse_description": "half-time bass pulse with syncopated offbeat accents",
    "meter_or_groove": "4/4 reggae-derived offbeat groove with dubstep half-time weight"
  },
  "sections": [
    {
      "id": "A",
      "start_seconds": 0.0,
      "end_seconds": 20.0,
      "energy": "low/building",
      "musical_cues": ["filtered intro", "first bass entrance"],
      "narrative_function": "establish world and first dramatic question"
    },
    {
      "id": "B",
      "start_seconds": 20.0,
      "end_seconds": 40.0,
      "energy": "rising",
      "musical_cues": ["full groove", "widening bass"],
      "narrative_function": "commit protagonist to the journey"
    }
  ]
}
```

If the agent cannot identify the genre confidently, it must ask the current user before approach/story lock. A user-confirmed genre must preserve the user's declaration.

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

The real gate requires at least three materially distinct options. `status` may be `selected` or `hybrid`; a hybrid records every selected option number plus the user's modification.

## SCRIPT requirement
After the storyboard/shot map is locked and before shot packages are built, create a readable `SCRIPT.md` and a machine-readable `SCRIPT.json`.

Minimum machine shape:

```json
{
  "schema": "aivideoedit.video-script.v1",
  "locked": true,
  "based_on_storyboard": true,
  "target_fps": 24,
  "duration_seconds": 180.64,
  "total_frames": 4335,
  "basis": ["storyboard", "music_analysis"],
  "entries": [
    {
      "shot_id": "S01",
      "start_frame": 0,
      "end_frame": 383,
      "story_action": "The protagonist encounters the first threshold.",
      "visual_media": "Generated cinematic hero environment + locked protagonist identity.",
      "animation_behavior": "Localized environmental motion, depth-aware camera approach, practical light movement.",
      "music_cues": ["intro pulse", "first harmonic swell"],
      "lyric_cue": null,
      "transition": "camera crosses the threshold"
    }
  ]
}
```

Frame ranges must be contiguous from frame `0` through `total_frames - 1`. When lyrics are present, add `"lyrics"` to `basis` and map lyric cues into the relevant entries.

## Shot-package media evidence
Every `shot_packages/Sxx/package.json` must include non-empty `media_evidence` with actual asset locators and hashes. Example:

```json
{
  "shot": "S01",
  "media_evidence": [
    {
      "kind": "generated_image",
      "path": "generated/S01_hero.png",
      "sha256": "<sha256>",
      "status": "generated"
    }
  ]
}
```

A metadata-only shot package is invalid. If generated-media capabilities are selected, `ASSET_MANIFEST.json` must also contain generated visual asset entries, using `origin: "generated"` or a generated kind/role.

Large media may be stored in the song's GitHub Release through `general/reusable/storage/github_release_storage.py`. The branch-local `STORAGE_MANIFEST.json` remains the authoritative index of those remote assets.
