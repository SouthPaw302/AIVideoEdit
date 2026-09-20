# AIVideoEdit Project & Branch Catalog

This is the non-destructive catalog for music/video production families. Branch-local project state remains authoritative.

## Drive

Google Drive is available to every AIVideoEdit production for source media, generated assets, proofs, backups, and final renders.

Canonical Drive root: AIVideoEdit (`1DZa50G2MVy9ER3b-ff4tpCQpzSqpHr1E`)

- `00 System`
- `10 Productions`
- `20 Shared Assets`
- `30 Delivery Masters`
- `90 Archive`
- `99 Inbox`

## Production families

### Silver Coin
- original: `song/silver-coin`
- alternate/current rework: `song/silver-coin-alternate`
- project: `projects/silver-coin/`
- Drive production folder: `10 Productions/Silver Coin`
- Drive folder ID: `1ROTZHvmBb71snAsBXXU6YImyXWT0ikEV`
- preserved original assets are inside that folder:
  - `01 Source Audio`
  - `02 Canonical References`
  - `03 Hero Paintings`
  - `04 V8 Effect Assets`
  - `05 Section Renders`
  - `06 QC & Contact Sheets`
  - `07 Final Masters`
  - `08 Manifests & Repo Records`
  - `09 Archive Snapshots`

### Midnight Tribal Pulse
- `song/midnight-tribal-pulse`
- Drive: `10 Productions/Midnight Tribal Pulse`

### Celtic
- `song/celtic`
- Drive: `10 Productions/Celtic`

### Leave It by the Door
- `song/leave-it-by-the-door`

### IronFlame family
Retained for recovery; do not delete or merge by inference:
- `song/ironflame`
- `song/ironflame-20260905-0216`
- `song/ironflame-cleanroom-20260917`
- `song/ironflame-redux`
- `song/ironflamenew`
- `work/ironflame-claude-implementation-20260906`
- Drive: `10 Productions/IronFlame - Cleanroom Backup 2026-09-17`

### Caspian family
- `song/caspian-the-day-the-silence-sang`
- `song/caspian-cleanroom-20260917`

### Irish Eyes
- `song/irish-eyes`
- `archive/video/irish-eyes`

### American Empire family
- `movie/american-empire-act1`
- `project/american-empire-act1/main`
- `project/american-empire-act1/scene-01`
- `project/american-empire-act1/scene-02`
- `project/american-empire-act1/scene-03`
- `song/american-empire-act1-scene1`
- `song/american-empire-act1-scene2`
- `song/american-empire-act1-scene3`
- `sync/american-empire-scene01-main`

### Other song branches
- `song/a-thousand-doors`
- `song/sigh-no-more`
- `song/the-door-between-the-seconds`
- `song/tribal-house-remastered`

## Non-production branches
Branches under `system/`, `integration/`, `feat/`, `fx/`, `promote/`, `prototype/`, `ops/`, `snapshot/`, `tmp/`, `chore/`, and `fix/` are infrastructure/tooling branches, not separate song projects.

## Organization rules
1. One production family gets one folder under Drive `10 Productions`.
2. Branch-local `STORAGE_MANIFEST.json` points to that folder.
3. Finished delivery masters may additionally live in `30 Delivery Masters`.
4. Cross-project reusable media belongs in `20 Shared Assets`.
5. Superseded snapshots and abandoned packages go to `90 Archive`.
6. Unsorted incoming media goes to `99 Inbox`.
7. Duplicate/legacy Git branches remain intact until explicitly reviewed.
