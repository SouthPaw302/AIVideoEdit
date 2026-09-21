# Silver Coin Test 2 — Handoff

This branch is intentionally isolated from all previous Silver Coin production branches.

Boot order:

1. Run `python bootstrap.py boot --repo-root <repo>`.
2. Read the bootstrapped current-main authority files.
3. Use only the two assets recorded in `ASSET_MANIFEST.json`.
4. Run `render_test2.py` and verify `TEST2_RENDER_REPORT.json`.
