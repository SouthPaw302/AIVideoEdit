# AIVideoEdit

Canonical production system for dynamic long-form music films.

## Start here

1. Read `AGENT_HANDOFF.md` — this is the single boot sequence. Do not
   substitute your own reading order.
2. `AGENT_HANDOFF.md` will point you to `PROJECT_INDEX.md` for what is
   currently active, and to `BIBLE.md` for system doctrine.

## Repository law

- `main` = Bible, indexes, templates, reusable cross-project technology.
- `song/<slug>` = one complete song/video production, including all its
  source media references, storyboards, prompts, manifests, and QC.
- Do not store song productions on `main`.
- Promote only generic reusable methods back to `main/general/reusable/`.
- Current active production is stated in `PROJECT_INDEX.md`, nowhere else.
  If this README and `PROJECT_INDEX.md` ever disagree, `PROJECT_INDEX.md`
  is correct — treat the disagreement as a bug and fix this file.

## Tooling continuity notes

- The canonical reusable utility path is `general/reusable/tools/`.
  `general/reusable/embedded-tools/` was an earlier working name only;
  treat it as superseded and do not create both trees.
- Browser-loaded/WebGPU Gaussian-splat viewer references discussed during
  tooling research included `gsplat.js` and Luma's web player. They are
  optional browser-review/reference candidates, not required dependencies
  and not substitutes for truthful 3DGS production rendering.
- `.github/workflows/publish_review.yml` and `review/index.html` were
  discussed/offered as optional review infrastructure but were intentionally
  never built. Their absence is not missing work. Create them only if a
  concrete review-surface requirement appears later.
