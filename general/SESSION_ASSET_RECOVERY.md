# Session Asset Recovery

Date: 2026-09-03

This file records binary assets visible in the active ChatGPT runtime that are not already proven to be present as GitHub blobs.

## Ironflame storyboard

- Runtime filename: `Ironflame: A Mythic Visual Storyboard.png`
- Runtime path: `/mnt/data/Ironflame: A Mythic Visual Storyboard.png`
- Dimensions: 1536 x 1024
- Size: 2,423,152 bytes
- SHA-256: `27cbb1a5b7ac00f65f23ea3f57477781adbd725e6a8a2a8b18513ea8bd8bdc4b`
- GitHub code search at archive time did not find this storyboard by name/title.
- Status: fingerprint preserved; local binary upload was not possible through the current GitHub connector because it accepts blob content rather than a mounted-file handle.

If the file is later re-ingested, verify the SHA-256 before marking it recovered and place it under the Ironflame project assets plus this general archive.

## Known large binary archives

Silver Coin V8 and its runtime/effect archive are durably identified by project manifests and persistent Library references in the Silver Coin production snapshot. The final master is >100 MB and therefore exceeds GitHub's ordinary single-file limit. Preserve GitHub manifests/hashes plus persistent storage references; if a future Git-LFS/object-storage workflow is added, mirror the large binaries there without changing their canonical hashes.
