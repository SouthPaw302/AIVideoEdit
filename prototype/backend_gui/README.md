# AIVideoEdit Backend GUI Prototype

This branch proves the smallest useful version of the proposed architecture:

Browser GUI -> backend API -> media worker -> local workspace -> future object storage

GitHub remains source control and project history. Runtime media is stored under `.runtime/`, ignored by Git, and the prototype does not use GitHub Actions artifacts or caches.

## Run

From the repository root:

```bash
python3 prototype/backend_gui/server.py
```

Then open:

```text
http://127.0.0.1:8080
```

The server binds to `0.0.0.0` by default, so another device on the same LAN can use the machine's LAN IP. No Python web framework is required; the server uses only the Python standard library.

## What it currently proves

- one browser GUI can control the backend
- the backend reports installed Python, FFmpeg, FFprobe, and Git capabilities
- media can upload directly from the browser into backend storage
- upload bytes are streamed to disk instead of being held as a GitHub artifact
- job and asset state persist locally across page refreshes/restarts
- FFprobe extracts real media metadata
- FFmpeg generates a preview thumbnail
- background worker jobs execute outside GitHub Actions
- runtime files are explicitly excluded from Git

## Prototype API

- `GET /api/health`
- `GET /api/capabilities`
- `GET /api/jobs`
- `POST /api/jobs`
- `GET /api/assets`
- `POST /api/assets?filename=<name>&project=<project>`
- `GET /media/<asset-id>/thumbnail.jpg`

## Sandbox proof

The prototype was executed in the development sandbox with FFmpeg 7.1.5. A generated H.264/AAC MP4 was uploaded through `/api/assets`; the backend stored it, detected 320x180 video, 2.0 second duration, H.264 video and AAC audio, generated a JPEG thumbnail, and completed the analysis job successfully.

## Next milestones

- S3-compatible object storage adapter (Cloudflare R2/B2/S3)
- project directories/manifests instead of a single asset list
- actual render commands and progress reporting
- OpenCV worker operations
- authentication before exposure beyond a trusted LAN
