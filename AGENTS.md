# AIVideoEdit Universal Agent Contract

This applies to **every agent, model, automation, connector, local process, and human-operated workflow** that works in this repository.

## Mandatory first action — bootstrap the OS
Before reading project history, generating media, changing production state, selecting FX, rendering, or inspecting unrelated branches:

```bash
python bootstrap.py boot --repo-root <repo>
```

If the repository is not present in the sandbox, `bootstrap.py install --workspace <path>` can install `main`, then `boot` must run.

A session is not production-capable until bootstrap prints `AIVideoEdit OS BOOTSTRAP: PASS`.

Bootstrap materializes the **entire exact current `main` commit** into `.aivideoedit/os/`, runs the current-main production guard against the active working branch, then writes:
- `.aivideoedit/session.json` — session attestation
- `.aivideoedit/SECOND_BRAIN.md` — generated current-session branch context

Read `SOUL.md` from the bootstrapped OS and the generated `SECOND_BRAIN.md` after bootstrap.

## Authority
1. Current explicit user instruction.
2. Active `song/<slug>` branch state/manifests.
3. Current-main AIVideoEdit OS loaded by bootstrap.

Nothing else is automatically authoritative. Historical chats, summaries, unrelated production branches, old visual DNA/storyboards, prior generated media, and project-specific provenance are prohibited as production inputs unless the current user explicitly authorizes them.

## Runtime law
- Do not bypass bootstrap by manually copying rules into a sandbox.
- Do not use a stale branch copy of the guard when the bootstrapped current-main guard differs.
- Before stage-changing work, run the guard from the bootstrapped OS:
  `python .aivideoedit/os/general/reusable/tools/production_guard.py --branch <current-branch>`
- If the session attestation is missing, branch-mismatched, or its critical OS hashes changed, the guard must fail.
- Start every new agent/session with a fresh bootstrap, even when reusing the same sandbox.

## Non-negotiable sequence
Source ingest -> reference extraction/analysis -> visual/media approach -> storyboard -> shot packages -> short finished proofs -> FX lock -> assembly -> actual-export QC -> archive.

Short reference videos are fully extracted. Long references use recorded meaningful sampling. If there is no usable visual reference, no original media may be generated until the story/visual/media approach has been shown to the user and recorded as established.

A storyboard is never a substitute for shot production. A successful command is never artistic QC. Effects must be visible and traceable. Technology names must be truthful.
