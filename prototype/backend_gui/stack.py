#!/usr/bin/env python3
"""AIVideoEdit alpha stack runtime.

Layers a bounded worker queue, project-wide orchestration and optional external
storage mirroring on top of the stable alpha server without changing the
existing server/API contract.
"""
from __future__ import annotations

import os
import queue
import shutil
import threading
from http.server import ThreadingHTTPServer
from urllib.parse import urlparse

import server as base
import storage

WORKER_COUNT = max(1, int(os.environ.get("AIVE_WORKERS", "2")))
JOB_QUEUE: queue.Queue[dict] = queue.Queue()


def sync_project_job(job: dict) -> None:
    project_id = job["project"]
    base.update_job(job["id"], status="running", started_at=base.now(), progress=5)
    with base.LOCK:
        assets = [dict(a) for a in base.STATE["assets"] if a.get("project") == project_id]

    def progress(index: int, total: int, name: str) -> None:
        pct = 10 if total <= 0 else min(95, 10 + int(index / total * 85))
        base.update_job(job["id"], progress=pct, result=f"Uploading {name} · {index}/{total}")

    try:
        manifest = storage.sync_project(project_id, assets, base.PROJECT_ROOT, progress=progress)
        base.update_job(
            job["id"], status="complete", progress=100,
            result=f"External sync complete · {len(manifest['objects'])} objects",
            finished_at=base.now(),
        )
    except Exception as exc:
        base.update_job(
            job["id"], status="failed", progress=100,
            result=str(exc)[:600], finished_at=base.now(),
        )


def execute_job(job: dict) -> None:
    handlers = {
        "ffmpeg_check": lambda: base.run_ffmpeg_check(job["id"]),
        "analyze_media": lambda: base.analyze_asset(job["id"], job["asset_id"]),
        "make_proxy": lambda: base.make_proxy(job["id"], job["asset_id"]),
        "extract_review_frames": lambda: base.extract_review_frames(job["id"], job["asset_id"]),
        "qc_media": lambda: base.qc_asset(job["id"], job["asset_id"]),
        "sync_project": lambda: sync_project_job(job),
    }
    fn = handlers.get(job.get("type"))
    if not fn:
        base.update_job(
            job["id"], status="failed", progress=100,
            result=f"unknown job type: {job.get('type')}", finished_at=base.now(),
        )
        return
    try:
        fn()
    except Exception as exc:
        base.update_job(
            job["id"], status="failed", progress=100,
            result=str(exc)[:600], finished_at=base.now(),
        )


def worker_loop(index: int) -> None:
    while True:
        job = JOB_QUEUE.get()
        try:
            execute_job(job)
        finally:
            JOB_QUEUE.task_done()


def dispatch_job(job: dict) -> None:
    JOB_QUEUE.put(job)


def start_workers() -> None:
    for index in range(WORKER_COUNT):
        threading.Thread(
            target=worker_loop,
            args=(index,),
            name=f"aive-worker-{index + 1}",
            daemon=True,
        ).start()


def system_snapshot() -> dict:
    usage = shutil.disk_usage(base.RUNTIME)
    with base.LOCK:
        running = sum(1 for j in base.STATE["jobs"] if j.get("status") == "running")
        queued = sum(1 for j in base.STATE["jobs"] if j.get("status") == "queued")
        stored_bytes = sum(
            int(a.get("size_bytes") or 0) + int(a.get("proxy_size_bytes") or 0)
            for a in base.STATE["assets"]
        )
        projects = len(base.STATE["projects"])
        assets = len(base.STATE["assets"])
    return {
        "workers": WORKER_COUNT,
        "queue_depth": JOB_QUEUE.qsize(),
        "running_jobs": running,
        "queued_jobs": queued,
        "projects": projects,
        "assets": assets,
        "stored_bytes": stored_bytes,
        "disk": {"total": usage.total, "used": usage.used, "free": usage.free},
        "storage": storage.status(),
    }


def prepare_project(project_id: str) -> list[dict]:
    created: list[dict] = []
    with base.LOCK:
        assets = [
            dict(a) for a in base.STATE["assets"]
            if a.get("project") == project_id and a.get("status") == "ready"
        ]
    for asset in assets:
        metadata = asset.get("metadata") or {}
        if metadata.get("video_codec"):
            if not asset.get("proxy_url"):
                created.append(base.add_job("make_proxy", project_id, asset["id"]))
            if not asset.get("review_frames"):
                created.append(base.add_job("extract_review_frames", project_id, asset["id"]))
        if (asset.get("qc") or {}).get("status") != "pass":
            created.append(base.add_job("qc_media", project_id, asset["id"]))
    for job in created:
        dispatch_job(job)
    return created


class StackHandler(base.Handler):
    server_version = "AIVideoEditAlphaStack/0.3"

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/system":
            return self.send_json(system_snapshot())
        if path == "/api/storage":
            return self.send_json(storage.status())
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path.startswith("/api/projects/") and path.endswith("/prepare"):
            parts = path.strip("/").split("/")
            project_id = parts[2]
            if not base.find_project(project_id):
                return self.send_json({"error": "project not found"}, 404)
            jobs = prepare_project(project_id)
            return self.send_json({"jobs": jobs, "count": len(jobs)}, 202)
        if path.startswith("/api/projects/") and path.endswith("/sync"):
            parts = path.strip("/").split("/")
            project_id = parts[2]
            if not base.find_project(project_id):
                return self.send_json({"error": "project not found"}, 404)
            if not storage.status().get("configured"):
                return self.send_json({"error": "external storage is not configured", "storage": storage.status()}, 409)
            job = base.add_job("sync_project", project_id, None)
            dispatch_job(job)
            return self.send_json(job, 202)
        return super().do_POST()


if __name__ == "__main__":
    base.load_state()
    # Replace the stable server's thread-per-job dispatch with the bounded queue.
    base.dispatch_job = dispatch_job
    start_workers()
    host = os.environ.get("AIVE_HOST", "0.0.0.0")
    port = int(os.environ.get("AIVE_PORT", "8080"))
    print(f"AIVideoEdit Alpha Stack: http://127.0.0.1:{port}")
    print(f"LAN bind: {host}:{port}")
    print(f"Workspace: {base.RUNTIME}")
    print(f"Workers: {WORKER_COUNT}")
    print(f"Storage: {storage.status()['detail']}")
    ThreadingHTTPServer((host, port), StackHandler).serve_forever()
