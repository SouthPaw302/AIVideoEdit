# AIVideoEdit Backend GUI Prototype

This branch proves the smallest useful version of the proposed architecture:

Browser GUI -> local/backend API -> worker -> temporary disk -> future object storage

GitHub remains source control and project history. The prototype does not use GitHub Actions artifacts or caches.

## Run

From the repository root:

```bash
python3 prototype/backend_gui/server.py
```

Then open:

```text
http://127.0.0.1:8080
```

No Python framework is required. The server uses only the Python standard library.

## What it currently proves

- one browser GUI can control the backend
- the backend reports installed runtime capabilities
- jobs can be submitted through an API
- a background worker thread can execute a local FFmpeg task
- job state is visible in the GUI
- execution happens on the server instead of GitHub Actions

## Prototype API

- `GET /api/health`
- `GET /api/capabilities`
- `GET /api/jobs`
- `POST /api/jobs`

Example job body:

```json
{
  "type": "ffmpeg_check",
  "project": "prototype/backend-gui"
}
```

## Intentionally not added yet

- database
- authentication
- persistent queue
- object storage credentials
- upload/download media pipeline
- real render commands
- OpenCV worker
- AI inference worker
- deployment automation

Those belong after the basic architecture is proven on a real machine.
