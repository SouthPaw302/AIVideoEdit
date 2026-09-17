# AIVideoEdit Scene Runtime

Optional deterministic rendering/QC support for AIVideoEdit productions. This directory is deliberately isolated from `bootstrap.py` and existing GitHub Actions. Installing its Node dependencies does not alter the repository's Python environment or agent boot sequence.

## Requirements

- Node.js 22+
- FFmpeg + ffprobe on PATH
- Chrome/Chromium is managed by the rendering dependency

Install once in this directory:

```bash
npm install
node runtime_doctor.mjs
```

## Render

```bash
node render_scene.mjs /path/to/composition.html /path/to/output.mp4 --fps 30 --quality standard
```

Transparent editor intermediate:

```bash
node render_scene.mjs /path/to/composition.html /path/to/overlay.mov --transparent --format mov
```

The renderer also supports `webm`, `gif`, `png-sequence`, and `hls` where the underlying engine supports them.

## Scene QC + snapshots

For a browser-composition project accepted by the runtime checker:

```bash
node scene_qc.mjs /path/to/composition-project
```

This is an **additional** quality check. Existing AIVideoEdit production, narrative, branch, drift, continuity, and export guards remain authoritative.

## Local browser animation assets

Do not rely on CDNs in final renders. Stage pinned local copies into a composition project:

```bash
node stage_runtime_assets.mjs /path/to/composition-project
```

Then reference:

```html
<script src="vendor/aivideoedit-gsap.min.js"></script>
<script src="vendor/aivideoedit-shader-transitions.js"></script>
```

The available experimental transition names are in `effects_catalog.json`. They are not automatically promoted into the canonical effect library.

## Audio-driven timing

The companion analyzer is one directory up:

```bash
python ../tools/audio_map.py song.wav -o /path/to/project/audiomap.json --print
```

Once created for a source SHA-256, that `audiomap.json` is the production's canonical machine timing analysis unless the source file changes.

## Operational boundary

- No modification of agent boot.
- No modification of existing GitHub Actions.
- No automatic effect promotion.
- No replacement of `PRIME_DIRECTIVE.md`, project state, storyboard, narrative contracts, or Zero-Drift.
- Rendering and QC are tools called by the existing director/agent workflow.

## Third-party implementation dependencies

The initial adapter uses open-source packages from `heygen-com/hyperframes` behind AIVideoEdit-native entry points. The main upstream work is Apache-2.0; its shader-transition package is MIT. Package names remain visible here for license/dependency transparency but are not AIVideoEdit workflow or product names. See `THIRD_PARTY_NOTICES.md`.
