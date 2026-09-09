# Door Seconds continuation snapshot — 2026-09-09

This directory preserves an exact compressed snapshot of the current important text/code/QC continuation state for **The Door Between the Seconds / Pandora the Vampire**.

## Snapshot
Original archive: `door_seconds_text_snapshot_20260909.tar.gz`

Expected archive SHA-256:
`974b10f7db7c5ee73c20517adab538a6892c1329558b4839073dd5e4867e8769`

The archive was base64-encoded and split into four ordered repository-safe text chunks:

1. `chunk_00.b64`
2. `chunk_01.b64`
3. `chunk_02.b64`
4. `chunk_03.b64`

Chunk source SHA-256 values before repository upload:
- chunk_00: `12b28b66f371768c94fb4494d27fb20447de3f559063f99e36175dfa53a0f3fe`
- chunk_01: `37d64ca5bfb551dc3f0703ac87ac0034be008e623d76e00bf2f3692c211d5543`
- chunk_02: `649ff52172a6e44d8c1032b328f0463988785144187f2085f4e26741d5a416ca`
- chunk_03: `f7b47a4740ca0a3654459d66520de046008a6a72d1d4c7321fcef12e454151a7`

## Reconstruct
From this directory:

```bash
cat chunk_00.b64 chunk_01.b64 chunk_02.b64 chunk_03.b64 \
  | base64 -d > door_seconds_text_snapshot_20260909.tar.gz

sha256sum door_seconds_text_snapshot_20260909.tar.gz
# must equal:
# 974b10f7db7c5ee73c20517adab538a6892c1329558b4839073dd5e4867e8769

tar -xzf door_seconds_text_snapshot_20260909.tar.gz
```

## Included state
The archive contains the current important continuation records, including:
- `HANDOFF.md`
- `PROJECT_STATE.json`
- `QC.md`
- `RENDER_HISTORY.md`
- `MEDIA_PLAN.json`
- `SCRIPT.json`
- `SCRIPT.md`
- `SHOT_LIST.md`
- `STORYBOARD.md`
- `VISUAL_DNA.md`
- `STATUS.md`
- `FX_REQUIREMENTS.fx.json`
- `fx.lock.json`
- `CONTINUATION_ARTIFACTS.json`
- `proofs/current_gate/CAPABILITY_PROOF.json`
- `proofs/current_gate/SHOT_PROOF_QC.json`
- `production/build_pandora_final.py`
- `production/build_shot_packages_from_v2.py`
- patched 3-second and 5-second variety QC JSON records
- `production/final_pandora_v2_gate/RENDER_METADATA.json`

## Important status
This snapshot represents the **Pandora v3 framing/motion patch continuation state**. The patched 3-second and 5-second variety checks passed, but the complete current proof/QC chain still needs to be rerun after the latest renderer changes. Do not infer `FINAL_QC_PASSED` from the existence of this snapshot.

Large render/contact-sheet binaries are intentionally not embedded in this snapshot. Their local paths, sizes and SHA-256 hashes are recorded in `CONTINUATION_ARTIFACTS.json`; binary promotion should follow the repository storage contract rather than silently inflating git history.
