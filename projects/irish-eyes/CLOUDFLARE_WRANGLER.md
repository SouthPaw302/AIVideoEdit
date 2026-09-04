# Irish Eyes — Cloudflare Wrangler Tooling

Branch: `song/irish-eyes`

Cloudflare Wrangler is part of the production preflight for Irish Eyes when available and authenticated.

## Role

Wrangler is infrastructure/storage tooling, not the artistic renderer. Use it to support the production system where it provides a concrete advantage.

Primary candidate uses:

- Cloudflare R2 for large source media, extracted-frame archives, generated support packs, proof renders, intermediate segments and final masters that should not bloat GitHub;
- Workers for lightweight asset/index APIs, signed-link helpers, metadata endpoints or other small production utilities when needed;
- Pages/Workers-hosted review/index interfaces when a browsable proof library would materially improve QC/review;
- KV, D1, Queues or other Cloudflare services only when a specific production dependency warrants them.

## Preflight rule

Before writing new custom infrastructure or storage code:

1. check whether Wrangler is available in the active runtime;
2. check whether it is authenticated/authorized without exposing credentials;
3. inspect existing Cloudflare configuration/resources before creating anything new;
4. prefer existing buckets/services over duplicate infrastructure when appropriate;
5. use the simplest service that solves the production need;
6. record object/service identifiers and recovery metadata in the Irish Eyes manifests.

## Media persistence rule

For any important media placed in R2 or another external object store, preserve in GitHub:

- original filename;
- object key/path;
- production role;
- source shot/frame when applicable;
- size when known;
- SHA-256 or equivalent checksum when practical;
- creation/version date;
- proof/QC status;
- recovery/public-review reference if appropriate.

GitHub remains the persistent brain/index. R2 can be the persistent large-binary layer.

## Security rule

Do not commit Cloudflare API tokens, account secrets, access keys, signed URLs with long-lived credentials, or other secrets into GitHub.

## Current runtime check — 2026-09-04

The current ChatGPT container did not expose a `wrangler` executable on `PATH`. A direct `npx wrangler` availability probe did not complete in the runtime, so this session must not claim that Wrangler is currently authenticated or usable locally.

This does **not** remove Wrangler from the project toolchain. It remains a first-class capability to check whenever the active runtime/connector exposes it.

## Current Irish Eyes priority

Do not delay the frame-selection and shot-package pass merely to create Cloudflare infrastructure. Use Wrangler/R2 when the first large persistent asset batch, proof library, or recovery problem justifies it.
