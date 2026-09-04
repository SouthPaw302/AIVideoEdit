# AIVideoEdit — Repository Index

Durable map of the Video Creation repository after the 2026-09-03 cleanup.

## Canonical entrypoints

| Path | Role |
|---|---|
| `AGENT_HANDOFF.md` | Primary agent recovery/operating instructions |
| `PROJECT_INDEX.md` | Song project registry and current status |
| `CANONICAL_EFFECTS.md` | Reusable-effects recovery entrypoint |
| `docs/` | Workflow, architecture, visual-style and storage rules |
| `general/PRODUCTION_SYSTEM_RULES.md` | Binding cross-project production rules |
| `general/reusable/` | Canonical effect, loop, transition, spatial and QC library |
| `general/ARCHIVE_INDEX.json` | Historical branch/output recovery metadata |
| `general/SESSION_ASSET_RECOVERY.md` | Fingerprints for important unarchived binaries |
| `CHAT_RECOVERY_LOG.md` | Historical project-recovery evidence and known gaps |

## Canonical production branches

- `main` — system canon, indexes, reusable technology and recovery metadata
- `song/irish-eyes` — active Irish Eyes production
- `song/silver-coin` — completed Silver Coin V8 production
- `song/ironflame` — IronFlame V1 production/recovery
- `song/leave-it-by-the-door` — historical recovery
- `song/sigh-no-more` — historical recovery

The normal operating model is one song branch per video. Do not make additional QC/temp branches unless a real branch is needed; short-lived tests belong in the project workspace and should be checkpointed into the song branch when meaningful.

## Main-tree layout

```text
/
├── AGENT_HANDOFF.md
├── README.md
├── PROJECT_INDEX.md
├── REPOSITORY_INDEX.md
├── CANONICAL_EFFECTS.md
├── CHAT_RECOVERY_LOG.md
├── docs/
├── general/
│   ├── PRODUCTION_SYSTEM_RULES.md
│   ├── ARCHIVE_INDEX.json
│   ├── SESSION_ASSET_RECOVERY.md
│   └── reusable/
└── projects/
    └── PROJECT_TEMPLATE.md
```

Per-song project directories, assets, manifests, render/QC history and shot packages live on their `song/<slug>` branches rather than being copied back into `main` wholesale.

## Reusable library

`general/reusable/` is the permanent cross-project technology layer. Key components:

- `CANONICAL_EFFECT_REGISTRY.md` / `.json`
- `PROJECT_TECHNIQUE_LINEAGE.md`
- `EFFECT_PACKAGE_STANDARD.md`
- `REUSABLE_EFFECTS_POLICY.md`
- `silver-coin-tools/`
- `silver-coin-docs/` — only Silver-Coin-specific method documentation after cleanup
- `depth-parallax-25d/`
- `irish-eyes-tools/`

The registry currently preserves 101 named records with evidence-based statuses rather than forcing every recovered idea to appear render-proven.

## Cleanup state

Removed from `main`:

- `general/branch-snapshots/` — redundant whole-branch mirrors
- duplicate generic documentation formerly copied under `general/reusable/silver-coin-docs/`

Recovery protection:

- exact pre-cleanup main state: `archive/pre-cleanup-20260903`
- canonical song branches and their complete Git history remain intact
- historical archive refs remain recorded in `general/ARCHIVE_INDEX.json`

The branch-snapshot mirrors were navigational duplicates; removing them from `main` did not erase the underlying commits or canonical song branches.

## Large-media rule

Do not bloat `main` with gigabytes of frame sequences or final masters simply to call them archived. Preserve practical-size reference/proof assets in GitHub and record large binaries by filename, SHA-256, technical metadata and durable Library/object-storage reference.

## Recovery sequence

1. Read `AGENT_HANDOFF.md`.
2. Read `PROJECT_INDEX.md` and identify the active `song/<slug>` branch.
3. Read `CANONICAL_EFFECTS.md` and the reusable registry before inventing new visual technology.
4. Read the active branch's `projects/<slug>/` directory and current handoff/status files.
5. Resolve large source/final media from manifests and storage references.
6. Continue from recorded state; do not reconstruct settled decisions from chat memory.

## Anti-clutter rule

Keep `main` small and authoritative. Promote reusable implementations and knowledge, not entire production trees. Keep song-specific assets and history on their song branch. Avoid duplicate docs, duplicate branch mirrors, and temporary branch names that outlive their task.
