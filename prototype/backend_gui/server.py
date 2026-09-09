#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import threading
import time
import uuid
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
RUNTIME = ROOT / ".runtime"
ASSET_ROOT = RUNTIME / "assets"
STATE_FILE = RUNTIME / "state.json"
MAX_UPLOAD = int(os.environ.get("AIVE_MAX_UPLOAD", str(2 * 1024 * 1024 * 1024)))

LOCK = threading.RLock()
STATE = {"jobs": [], "assets": []}


def load_state() -> None:
    RUNTIME.mkdir(parents=True, exist_ok=True)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    if STATE_FILE.is_file():
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                STATE["jobs"] = data.get("jobs", [])[-100:]
                STATE["assets"] = data.get("assets", [])[-100:]
        except Exception:
            pass


def save_state() -> None:
    with LOCK:
        tmp = STATE_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(STATE, indent=2), encoding="utf-8")
        tmp.replace(STATE_FILE)


def capability(name: str, command: list[str]) -> dict:
    found = shutil.which(command[0])
    if not found:
        return {"name": name, "available": False, "detail": "not found"}
    try:
        proc = subprocess.run(command, capture_output=True, text=True, timeout=3)
        text = (proc.stdout or proc.stderr).splitlines()
        detail = text[0] if text else found
        return {"name": name, "available": proc.returncode == 0, "detail": detail[:180]}
    except Exception as exc:
        return {"name": name, "available": False, "detail": str(exc)}


def capabilities() -> list[dict]:
    checks = [
        ("Python", ["python3", "--version"]),
        ("FFmpeg", ["ffmpeg", "-version"]),
        ("FFprobe", ["ffprobe", "-version"]),
        ("Git", ["git", "--version"]),
    ]
    return [capability(name, cmd) for name, cmd in checks]


def safe_name(name: str) -> str:
    name = Path(unquote(name or "upload.bin")).name
    clean = re.sub(r"[^A-Za-z0-9._ -]+", "_", name).strip(" .")
    return clean[:180] or "upload.bin"


def add_job(job_type: str, project: str, asset_id: str | None = None) -> dict:
    job = {
        "id": uuid.uuid4().hex[:10],
        "type": job_type,
        "project": project or "prototype",
        "asset_id": asset_id,
        "status": "queued",
        "created_at": time.time(),
        "result": None,
    }
    with LOCK:
        STATE["jobs"].append(job)
        STATE["jobs"] = STATE["jobs"][-100:]
        save_state()
    return job


def update_job(job_id: str, **changes) -> None:
    with LOCK:
        job = next((x for x in STATE["jobs"] if x["id"] == job_id), None)
        if job:
            job.update(changes)
            save_state()


def find_asset(asset_id: str) -> dict | None:
    return next((x for x in STATE["assets"] if x["id"] == asset_id), None)


def analyze_asset(job_id: str, asset_id: str) -> None:
    update_job(job_id, status="running", started_at=time.time())
    with LOCK:
        asset = find_asset(asset_id)
        if not asset:
            update_job(job_id, status="failed", result="asset not found", finished_at=time.time())
            return
        source = Path(asset["local_path"])
        asset["status"] = "analyzing"
        save_state()

    ffprobe = shutil.which("ffprobe")
    ffmpeg = shutil.which("ffmpeg")
    if not ffprobe or not ffmpeg:
        with LOCK:
            asset = find_asset(asset_id)
            if asset:
                asset["status"] = "failed"
                asset["error"] = "FFmpeg/FFprobe unavailable"
                save_state()
        update_job(job_id, status="failed", result="FFmpeg/FFprobe unavailable", finished_at=time.time())
        return

    try:
        probe = subprocess.run(
            [ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(source)],
            capture_output=True, text=True, timeout=30, check=True,
        )
        info = json.loads(probe.stdout)
        fmt = info.get("format", {})
        video = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
        audio = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), {})
        duration = float(fmt.get("duration") or video.get("duration") or 0)
        thumb = source.parent / "thumbnail.jpg"
        seek = min(max(duration * 0.15, 0.0), 2.0) if duration else 0.0
        subprocess.run(
            [ffmpeg, "-y", "-ss", f"{seek:.3f}", "-i", str(source), "-frames:v", "1", "-vf", "scale=640:-2", str(thumb)],
            capture_output=True, text=True, timeout=60, check=True,
        )
        metadata = {
            "duration_seconds": round(duration, 3),
            "format": fmt.get("format_name"),
            "size_bytes": int(fmt.get("size") or source.stat().st_size),
            "video_codec": video.get("codec_name"),
            "width": video.get("width"),
            "height": video.get("height"),
            "fps": video.get("avg_frame_rate"),
            "audio_codec": audio.get("codec_name"),
            "sample_rate": audio.get("sample_rate"),
            "channels": audio.get("channels"),
        }
        with LOCK:
            asset = find_asset(asset_id)
            if asset:
                asset["status"] = "ready"
                asset["metadata"] = metadata
                asset["thumbnail_url"] = f"/media/{asset_id}/thumbnail.jpg"
                save_state()
        summary = f"{metadata.get('width')}x{metadata.get('height')} · {metadata.get('duration_seconds')}s · {metadata.get('video_codec')}"
        update_job(job_id, status="complete", result=summary, finished_at=time.time())
    except Exception as exc:
        message = str(exc)[:400]
        with LOCK:
            asset = find_asset(asset_id)
            if asset:
                asset["status"] = "failed"
                asset["error"] = message
                save_state()
        update_job(job_id, status="failed", result=message, finished_at=time.time())


def run_ffmpeg_check(job_id: str) -> None:
    update_job(job_id, status="running", started_at=time.time())
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        update_job(job_id, status="failed", result="FFmpeg is not installed.", finished_at=time.time())
        return
    try:
        proc = subprocess.run([ffmpeg, "-version"], capture_output=True, text=True, timeout=5)
        result = (proc.stdout or proc.stderr).splitlines()[0]
        status = "complete" if proc.returncode == 0 else "failed"
    except Exception as exc:
        status, result = "failed", str(exc)
    update_job(job_id, status=status, result=result, finished_at=time.time())


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {fmt % args}")

    def translate_path(self, path: str) -> str:
        parsed = urlparse(path).path
        if parsed == "/":
            parsed = "/index.html"
        return str(STATIC / parsed.lstrip("/"))

    def send_json(self, payload, status=200):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def serve_runtime_file(self, asset_id: str, filename: str):
        target = ASSET_ROOT / asset_id / safe_name(filename)
        try:
            target = target.resolve()
            target.relative_to(ASSET_ROOT.resolve())
        except Exception:
            return self.send_error(403)
        if not target.is_file():
            return self.send_error(404)
        self.send_response(200)
        self.send_header("Content-Type", self.guess_type(str(target)))
        self.send_header("Content-Length", str(target.stat().st_size))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        with target.open("rb") as fh:
            shutil.copyfileobj(fh, self.wfile)

    def do_GET(self):
        path = urlparse(self.path).path
        if path.startswith("/media/"):
            parts = path.strip("/").split("/", 2)
            if len(parts) == 3:
                return self.serve_runtime_file(parts[1], parts[2])
        if path == "/api/health":
            return self.send_json({"ok": True, "service": "aivideoedit-prototype", "pid": os.getpid(), "workspace": str(RUNTIME)})
        if path == "/api/capabilities":
            return self.send_json({"capabilities": capabilities()})
        if path == "/api/jobs":
            with LOCK:
                return self.send_json({"jobs": list(reversed(STATE["jobs"][-25:]))})
        if path == "/api/assets":
            with LOCK:
                public = []
                for item in reversed(STATE["assets"][-25:]):
                    public.append({k: v for k, v in item.items() if k != "local_path"})
                return self.send_json({"assets": public})
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/api/assets":
            return self.receive_asset(parsed)
        if path == "/api/jobs":
            return self.receive_job()
        return self.send_json({"error": "not found"}, 404)

    def receive_asset(self, parsed):
        params = parse_qs(parsed.query)
        filename = safe_name((params.get("filename") or ["upload.bin"])[0])
        project = (params.get("project") or ["prototype"])[0][:120]
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return self.send_json({"error": "empty upload"}, 400)
        if length > MAX_UPLOAD:
            return self.send_json({"error": "upload too large", "max_bytes": MAX_UPLOAD}, 413)

        asset_id = uuid.uuid4().hex[:12]
        folder = ASSET_ROOT / asset_id
        folder.mkdir(parents=True, exist_ok=False)
        target = folder / filename
        remaining = length
        try:
            with target.open("wb") as fh:
                while remaining:
                    chunk = self.rfile.read(min(1024 * 1024, remaining))
                    if not chunk:
                        raise IOError("upload ended early")
                    fh.write(chunk)
                    remaining -= len(chunk)
        except Exception:
            shutil.rmtree(folder, ignore_errors=True)
            raise

        asset = {
            "id": asset_id,
            "project": project,
            "filename": filename,
            "size_bytes": target.stat().st_size,
            "status": "uploaded",
            "created_at": time.time(),
            "local_path": str(target),
            "metadata": None,
            "thumbnail_url": None,
        }
        with LOCK:
            STATE["assets"].append(asset)
            STATE["assets"] = STATE["assets"][-100:]
            save_state()
        job = add_job("analyze_media", project, asset_id)
        threading.Thread(target=analyze_asset, args=(job["id"], asset_id), daemon=True).start()
        return self.send_json({"asset": {k: v for k, v in asset.items() if k != "local_path"}, "job": job}, 202)

    def receive_job(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception:
            return self.send_json({"error": "invalid json"}, 400)
        job_type = data.get("type", "ffmpeg_check")
        job = add_job(job_type, data.get("project", "prototype"), data.get("asset_id"))
        if job_type == "ffmpeg_check":
            threading.Thread(target=run_ffmpeg_check, args=(job["id"],), daemon=True).start()
        elif job_type == "analyze_media" and job.get("asset_id"):
            threading.Thread(target=analyze_asset, args=(job["id"], job["asset_id"]), daemon=True).start()
        else:
            update_job(job["id"], status="failed", result=f"unknown job type: {job_type}", finished_at=time.time())
        return self.send_json(job, 202)


if __name__ == "__main__":
    load_state()
    host = os.environ.get("AIVE_HOST", "0.0.0.0")
    port = int(os.environ.get("AIVE_PORT", "8080"))
    print(f"AIVideoEdit prototype: http://127.0.0.1:{port}")
    print(f"Workspace: {RUNTIME}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()
