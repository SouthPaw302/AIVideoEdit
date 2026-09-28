#!/usr/bin/env python3
"""Upload/download large project assets to any S3-compatible object store.

Designed for Cloudflare R2, Backblaze B2 S3, Wasabi, MinIO, or AWS S3.
The repository stores only small JSON pointer manifests; media stays external.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def client():
    try:
        import boto3
    except ImportError as exc:
        raise SystemExit("Install boto3: python -m pip install boto3") from exc

    endpoint = os.environ["AIVIDEO_OBJECT_ENDPOINT"]
    key = os.environ["AIVIDEO_OBJECT_ACCESS_KEY_ID"]
    secret = os.environ["AIVIDEO_OBJECT_SECRET_ACCESS_KEY"]
    region = os.getenv("AIVIDEO_OBJECT_REGION", "auto")
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        region_name=region,
    )


def upload(src: Path, object_key: str, manifest: Path | None) -> None:
    bucket = os.environ["AIVIDEO_OBJECT_BUCKET"]
    c = client()
    content_type = mimetypes.guess_type(src.name)[0] or "application/octet-stream"
    c.upload_file(str(src), bucket, object_key, ExtraArgs={"ContentType": content_type})
    public_base = os.getenv("AIVIDEO_OBJECT_PUBLIC_BASE", "").rstrip("/")
    record = {
        "schema": "aivideoedit.external-asset.v1",
        "bucket": bucket,
        "key": object_key,
        "filename": src.name,
        "size": src.stat().st_size,
        "sha256": sha256_file(src),
        "content_type": content_type,
        "url": f"{public_base}/{object_key}" if public_base else None,
    }
    text = json.dumps(record, indent=2) + "\n"
    if manifest:
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(text, encoding="utf-8")
    print(text, end="")


def download(object_key: str, dest: Path) -> None:
    bucket = os.environ["AIVIDEO_OBJECT_BUCKET"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    client().download_file(bucket, object_key, str(dest))
    print(dest)


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    up = sub.add_parser("upload")
    up.add_argument("src", type=Path)
    up.add_argument("key")
    up.add_argument("--manifest", type=Path)
    down = sub.add_parser("download")
    down.add_argument("key")
    down.add_argument("dest", type=Path)
    a = p.parse_args()
    if a.cmd == "upload":
        upload(a.src, a.key, a.manifest)
    else:
        download(a.key, a.dest)


if __name__ == "__main__":
    main()
