# General Video Creation Archive

`general/` stores repository-wide production rules, archive metadata, session asset fingerprints, and the reusable effect/tool library.

## Read first

- `PRODUCTION_SYSTEM_RULES.md` — system-wide production behavior
- `reusable/README.md` — reusable-library entrypoint
- `reusable/CANONICAL_EFFECT_REGISTRY.md` — human-readable effect/loop/transition registry
- `reusable/CANONICAL_EFFECT_REGISTRY.json` — machine-readable registry
- `ARCHIVE_INDEX.json` — historical branch/output recovery metadata
- `SESSION_ASSET_RECOVERY.md` — fingerprints for important binaries not yet durably stored in GitHub

## Reusable implementations

Current core implementation trees:

- `reusable/silver-coin-tools/`
- `reusable/silver-coin-docs/` — Silver-Coin-specific method documents only
- `reusable/depth-parallax-25d/`
- `reusable/irish-eyes-tools/`

Silver Coin remains the deepest completed reusable-effects lineage, while Irish Eyes is actively contributing photographic restoration, water/halation treatment and continuous soft-depth 2.5D methods.

## Historical recovery

Per-video production state belongs on the canonical `song/<slug>` branches. Historical point-in-time branch refs are recorded in `ARCHIVE_INDEX.json` where still useful.

The former `general/branch-snapshots/` mirror was removed from `main` on 2026-09-03 because it duplicated entire branch trees and made normal repository navigation noisy. The exact pre-cleanup state remains recoverable at `archive/pre-cleanup-20260903`.

## Large media

GitHub is the production brain, not necessarily the large-media bucket. Large masters/source libraries may live in ChatGPT Library/workspace or external object storage, but manifests must preserve filenames, hashes, dimensions/duration, storage references, approval/QC state and enough information to recover them.
