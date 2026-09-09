#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
import subprocess
import threading
import time
import uuid
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
JOBS = []
LOCK = threading.Lock()


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


def run_job(job_id: str) -> None:
    with LOCK:
        job = next(x for x in JOBS if x["id"] == job_id)
        job["status"] = "running"
        job["started_at"] = time.time()

    # Prototype worker: prove that the backend can execute local media tooling.
    ffmpeg = shutil.which("ffmpeg")
    result = ""
    status = "complete"
    if ffmpeg:
        try:
            proc = subprocess.run([ffmpeg, "-version"], capture_output=True, text=True, timeout=5)
            result = (proc.stdout or proc.stderr).splitlines()[0]
            if proc.returncode != 0:
                status = "failed"
        except Exception as exc:
            status = "failed"
            result = str(exc)
    else:
        status = "failed"
        result = "FFmpeg is not installed on this server yet."

    with LOCK:
        job = next(x for x in JOBS if x["id"] == job_id)
        job["status"] = status
        job["result"] = result
        job["finished_at"] = time.time()


class Handler(SimpleHTTPRequestHandler):
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

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self.send_json({"ok": True, "service": "aivideoedit-prototype", "pid": os.getpid()})
        if path == "/api/capabilities":
            return self.send_json({"capabilities": capabilities()})
        if path == "/api/jobs":
            with LOCK:
                return self.send_json({"jobs": list(reversed(JOBS[-25:]))})
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/jobs":
            return self.send_json({"error": "not found"}, 404)
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception:
            return self.send_json({"error": "invalid json"}, 400)

        job = {
            "id": uuid.uuid4().hex[:10],
            "type": data.get("type", "ffmpeg_check"),
            "project": data.get("project", "prototype"),
            "status": "queued",
            "created_at": time.time(),
            "result": None,
        }
        with LOCK:
            JOBS.append(job)
        threading.Thread(target=run_job, args=(job["id"],), daemon=True).start()
        return self.send_json(job, 202)


if __name__ == "__main__":
    host = os.environ.get("AIVE_HOST", "0.0.0.0")
    port = int(os.environ.get("AIVE_PORT", "8080"))
    print(f"AIVideoEdit prototype: http://127.0.0.1:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()
