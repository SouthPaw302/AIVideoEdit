# AIVideoEdit Studio — Alpha Stack

A single-user browser-controlled production workstation. GitHub remains source control; runtime media, processing, QC and optional external media mirroring live on the workstation/backend machine.

## Stack

Browser Studio -> Python standard-library API -> bounded worker queue -> FFmpeg/FFprobe workers -> persistent local workspace -> QC -> optional external object-storage mirror

No Python web framework or database server is required.

## Recommended run

Windows: double-click `prototype/backend_gui/start_windows.bat`.

Termux:

```bash
cd AIVideoEdit/prototype/backend_gui
bash start_termux.sh
```

Manual:

```bash
python prototype/backend_gui/stack.py
```

Open `http://127.0.0.1:8080` on the host, or `http://<host-lan-ip>:8080` from another device on the same network. The stack binds to `0.0.0.0` by default.

`server.py` remains the stable bare-alpha fallback. `stack.py` is the full alpha runtime and layers queued workers, project-wide orchestration and storage telemetry on top of it.

Environment overrides:

- `AIVE_HOST` (default `0.0.0.0`)
- `AIVE_PORT` (default `8080`)
- `AIVE_RUNTIME` (default `prototype/backend_gui/.runtime`)
- `AIVE_MAX_UPLOAD` (default 2 GiB)
- `AIVE_WORKERS` (default `2`)
- `AIVE_RCLONE_REMOTE` (optional; e.g. an rclone remote/path for R2, B2 or S3-compatible storage)

## Alpha features

- multiple persistent projects
- direct browser media ingest
- restart-safe project/asset/job state
- bounded configurable worker queue
- project-wide Prepare action that queues missing proxy/review/QC work
- SHA-256 asset identity
- FFprobe metadata inspection
- thumbnail generation
- byte-range media serving for browser playback
- 720p H.264/AAC proxy generation
- six-point review-frame extraction
- decode/integrity QC gate
- asset deletion with derivative cleanup
- project-scoped job history
- project manifest API
- storage/disk/queue telemetry
- optional external project mirror through rclone
- LAN-ready GUI
- Windows and Termux launchers
- runtime media excluded from Git

## API additions in `stack.py`

Base alpha API remains available, plus:

- `GET /api/system`
- `GET /api/storage`
- `POST /api/projects/<id>/prepare`
- `POST /api/projects/<id>/sync`

Base API includes projects, assets, jobs, manifests and `/media/...` byte-range serving.

Worker job types include `ffmpeg_check`, `analyze_media`, `make_proxy`, `extract_review_frames`, `qc_media`, and `sync_project` when external storage is configured.

## External storage

Local media remains authoritative during alpha. External storage is an optional mirror.

Install and configure `rclone`, then set `AIVE_RCLONE_REMOTE` to the desired remote prefix. Example shape:

```text
AIVE_RCLONE_REMOTE=r2:aivideoedit
```

When configured, Studio exposes **Back up project**. The stack mirrors source files, proxies, thumbnails, review frames and an external-storage manifest. No credentials are stored in Git or browser JavaScript.

## Verified alpha proof

The media path was exercised end-to-end in the development sandbox with H.264/AAC media: ingest, SHA-256, metadata probe, thumbnail, H.264/AAC proxy, six review frames, HTTP 206 playback, decode/integrity QC and project manifest all completed successfully. The queued runtime was separately exercised with three project preparation jobs submitted together; proxy, review-frame extraction and QC all completed successfully through two bounded workers.

## Still deferred

- authentication/TLS for exposure outside a trusted LAN
- browser-side WebCodecs/WebGPU workers
- AI inference workers
- multi-user scheduling/permissions
- production database/service-bus replacement for the alpha state layer

Those can layer onto the current project/asset/job model without changing the Studio workflow.
