# AIVideoEdit Storage Architecture

## Rule
GitHub is the source of truth for code, manifests, prompts, metadata, checks, and reproducibility records.
Large generated media is external object storage.
GitHub Actions is compute/checking only and must use zero artifact/cache storage.

## External asset layout
Use any S3-compatible store, preferably Cloudflare R2 or Backblaze B2.

Recommended keys:

```
aivideoedit/
  projects/<project-slug>/source/
  projects/<project-slug>/frames/
  projects/<project-slug>/audio/
  projects/<project-slug>/renders/
  projects/<project-slug>/proofs/
  general/reference/
```

## Repo pointer manifests
For each external binary, commit a small JSON manifest containing:

- object key
- original filename
- byte size
- SHA-256
- MIME type
- public URL when applicable

`general/reusable/tools/object_store.py` creates these manifests while uploading files.

## Environment variables

```
AIVIDEO_OBJECT_ENDPOINT
AIVIDEO_OBJECT_ACCESS_KEY_ID
AIVIDEO_OBJECT_SECRET_ACCESS_KEY
AIVIDEO_OBJECT_BUCKET
AIVIDEO_OBJECT_REGION=auto
AIVIDEO_OBJECT_PUBLIC_BASE   # optional
```

## Upload example

```
python -m pip install boto3
python general/reusable/tools/object_store.py upload \
  output/final.mp4 \
  aivideoedit/projects/my-song/renders/final.mp4 \
  --manifest projects/my-song/assets/final.mp4.asset.json
```

## Download example

```
python general/reusable/tools/object_store.py download \
  aivideoedit/projects/my-song/renders/final.mp4 \
  output/final.mp4
```

## CI contract

Checks may generate temporary media on the runner for verification. Temporary files are discarded at the end of the job. They must not be uploaded through GitHub Actions artifacts or caches.

`general/reusable/tools/storage_guard.py` enforces this contract.
