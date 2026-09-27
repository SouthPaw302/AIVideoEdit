from __future__ import annotations

import argparse
import json
import os
import tempfile
import urllib.request
from pathlib import Path

from .registry import ModelRegistry, inferred_repo_root


def provision(model_id: str, *, force: bool = False) -> dict:
    registry = ModelRegistry.load_default()
    record = registry.require(model_id)
    if record.get("runtime") != "onnxruntime":
        raise ValueError(f"model is not externally provisioned ONNX: {model_id}")

    # The registry already supports an explicit AIVIDEOEDIT_REPO_ROOT override
    # and otherwise infers the checkout from this module, so provisioning works
    # in both Compose and ordinary local clones.
    repo_root = inferred_repo_root()
    if not repo_root.is_dir():
        raise RuntimeError("AIVideoEdit repository root is unavailable")
    destination = registry.model_path(record)
    if destination is None:
        raise RuntimeError("model registry has no cache path")

    if destination.is_file() and not force:
        ok, reason = registry.verify_model_file(record, destination)
        if ok:
            return {"status": "READY", "model": model_id, "path": str(destination), "verification": reason}
        raise RuntimeError("existing model failed verification; use --force to replace it: " + reason)

    url = str(record.get("download_url") or "")
    if not url.startswith("https://"):
        raise RuntimeError("approved HTTPS download URL is missing")
    destination.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False, suffix=".partial") as tmp:
        tmp_path = Path(tmp.name)
        request = urllib.request.Request(url, headers={"User-Agent": "AIVideoEdit-RuntimeV2/0.3"})
        with urllib.request.urlopen(request, timeout=120) as response:
            while True:
                block = response.read(1024 * 1024)
                if not block:
                    break
                tmp.write(block)
    try:
        ok, reason = registry.verify_model_file(record, tmp_path)
        if not ok:
            raise RuntimeError("downloaded model failed pinned-source verification: " + reason)
        tmp_path.replace(destination)
    finally:
        tmp_path.unlink(missing_ok=True)

    receipt = {
        "schema": "aivideoedit.model-provision.v1",
        "model": model_id,
        "path": str(destination),
        "source_repository": record.get("source_repository"),
        "source_commit": record.get("source_commit"),
        "source_git_blob_sha1": record.get("source_git_blob_sha1"),
        "source_size_bytes": record.get("source_size_bytes"),
        "verification": reason,
    }
    destination.with_suffix(destination.suffix + ".receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return {"status": "PROVISIONED", **receipt}


def main() -> int:
    ap = argparse.ArgumentParser(description="Provision an approved Runtime V2 model outside git history")
    ap.add_argument("model_id")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    print(json.dumps(provision(args.model_id, force=args.force), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
