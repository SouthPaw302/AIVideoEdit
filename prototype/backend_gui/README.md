# AIVideoEdit Backend GUI — Alpha

A single-user browser-controlled production backend. GitHub remains source control; runtime media and processing live on the backend machine.

## Alpha stack

Browser GUI -> Python standard-library API -> persistent local job/state layer -> FFmpeg/FFprobe workers -> local media workspace -> QC

No Python web framework or database server is required.

## Run

```bash
python3 prototype/backend_gui/server.py
```

Open `http://127.0.0.1:8080` on the host, or `http://<host-lan-ip>:8080` from another device on the same network. The server binds to `0.0.0.0` by default.

Environment overrides:

- `AIVE_HOST` (default `0.0.0.0`)
- `AIVE_PORT` (default `8080`)
- `AIVE_RUNTIME` (default `prototype/backend_gui/.runtime`)
- `AIVE_MAX_UPLOAD` (default 2 GiB)

## Alpha features

- multiple persistent projects
- direct browser media ingest
- restart-safe project/asset/job state
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
- LAN-ready GUI
- runtime media excluded from Git

## API

- `GET /api/health`
- `GET /api/capabilities`
- `GET /api/projects`
- `POST /api/projects`
- `GET /api/assets?project=<id>`
- `POST /api/assets?filename=<name>&project=<id>` (raw body)
- `GET /api/assets/<id>`
- `DELETE /api/assets/<id>`
- `GET /api/jobs?project=<id>`
- `POST /api/jobs`
- `GET /api/projects/<id>/manifest`
- `GET /media/<asset-id>/<relative-path>`

Worker job types: `ffmpeg_check`, `analyze_media`, `make_proxy`, `extract_review_frames`, `qc_media`.

## Verified alpha proof

The alpha was exercised end-to-end in the development sandbox with a generated H.264/AAC MP4. The backend successfully created a project, ingested and hashed the source, probed metadata, generated a thumbnail, built a playable H.264/AAC proxy, extracted six review frames, served byte-range video requests with HTTP 206, passed decode/integrity QC, and generated a project manifest.

## Deliberately deferred after alpha

- remote object storage adapter (R2/B2/S3)
- authentication/TLS for exposure outside a trusted LAN
- browser-side WebCodecs/WebGPU workers
- AI inference workers
- multi-user scheduling/permissions
- production database/queue service

Those can layer onto the alpha without changing the core project/asset/job model.
