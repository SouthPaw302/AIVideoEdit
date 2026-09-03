# General Video Creation Archive

Created 2026-09-03 to make the ChatGPT Video Creation project recoverable from `main` even when a production chat, workspace, or active song branch is unavailable.

## Canonical video branches

- `song/ironflame`
- `song/silver-coin`
- `song/leave-it-by-the-door`
- `song/sigh-no-more`

## Archive branches

Point-in-time recovery branches created from the current production tips:

- `archive/video/ironflame` -> `06ba8f00d784b474b86e9093595e03180337607f`
- `archive/video/silver-coin` -> `45367f11c72b631bab1181f39a162046a8c6e10c`
- `archive/video/leave-it-by-the-door` -> `93761c0e604c94668bf57b9003ccb9c0040d2bf8`
- `archive/video/sigh-no-more` -> `3e6fe5d5fcc5057f595ee6b449f72b598b5015c2`

## Complete branch snapshots on main

`general/branch-snapshots/` contains Git-tree snapshots of the complete tracked contents of each production branch. These snapshots preserve every Git-tracked file reachable from that branch tip, including project documentation, manifests, scripts, images, reference media, QC material, effect recipes, and other committed resources. Git reuses existing blobs rather than re-uploading duplicate binary data.

- `general/branch-snapshots/ironflame/`
- `general/branch-snapshots/silver-coin/`
- `general/branch-snapshots/leave-it-by-the-door/`
- `general/branch-snapshots/sigh-no-more/`

## Reusable effects/resources

Silver Coin contains the most developed reusable effects stack currently in the repository. Its complete branch snapshot includes the `tools/` tree and effect/motion method documentation, including painterly motion, music-directed living-painting, temporal QC, narrative ribbon, Gaussian/volumetric methods, tiny-NeRF volume work, 2.5D/depth methods, and the V8 effect-pack renderer.

For convenience, `general/reusable/silver-coin-tools/` and `general/reusable/silver-coin-docs/` directly preserve those trees as reusable resources.

## Final-output status

### Silver Coin

Current canonical final: `Silver_Coin_V8_FINAL_YouTube_720p24.mp4`.

Recorded on the production branch as QC passed, 210.461333 s, 1280x720/24 fps H.264 with 48 kHz stereo AAC, 155,101,031 bytes, SHA-256 `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`, persistent Library ID `libfile_acfb04300bd88191b67e23b2ad736870`.

The final master and the >1 GB runtime/effect archive are referenced by the GitHub manifests but are larger than GitHub's ordinary single-file limit and were stored in persistent Library/archive storage. Their hashes and recovery records remain in the Silver Coin snapshot.

### Ironflame

V1 is recorded as rendered and delivered (12 scenes, 04:04.680, 1280x720 master plus 540p compact delivery), but the exact final MP4 binary/storage identifier remains a documented archive gap. Do not invent a replacement filename or hash.

A storyboard image is present in the active 2026-09-03 session as `Ironflame: A Mythic Visual Storyboard.png`, 1536x1024, 2,423,152 bytes, SHA-256 `27cbb1a5b7ac00f65f23ea3f57477781adbd725e6a8a2a8b18513ea8bd8bdc4b`. The connector available in this session cannot stream that local binary into GitHub directly; its fingerprint is preserved in `general/SESSION_ASSET_RECOVERY.md` so it can be matched exactly if re-ingested.

### Leave It by the Door

Recovery/partial project. Warm tavern narrative and living-scene experiments are preserved; exact historical source/output binaries were not recovered.

### Sigh No More / Irish Eyes, Spanish Hair

Recovery/partial project. Sequential video-prompt architecture and visual direction are preserved; no completed render has been confirmed.

## Recovery rule

For a future production agent: start at this file, then read the relevant `general/branch-snapshots/<video>/` snapshot and the canonical `song/<video>` branch. New meaningful work must still be checkpointed to the song branch during production, and important reusable methods should also be indexed here.