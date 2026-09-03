# Storage, Tools, Connectors, and Recovery

The user created AIVideoEdit specifically so work can survive ChatGPT context/session boundaries. This document defines what belongs where and how a new agent should recover.

## GitHub: persistent source of truth

Repository: `SouthPaw302/AIVideoEdit`

Store:
- handoff/context files
- project status
- lyrics and visual DNA
- shot lists and manifests
- prompts
- code/scripts
- tool schemas/config
- QC notes
- references to large assets

Do not assume chat history is available. Important decisions must be written here.

## ChatGPT project/workspace: active production

Use the active execution environment for large/temporary production material:
- WAV/MP3 source audio
- PNG/JPG source frames
- masks
- depth images
- contact sheets
- micro-loops
- intermediate MP4/WebM
- final renders in progress

Workspace paths such as `/mnt/data/...` are useful during a session but should be considered potentially ephemeral across future chats unless the project environment guarantees persistence.

Therefore every active project's `STATUS.md` should name important assets and, when possible, record external/archive references.

## Object storage: long-term large media

Preferred future archive for:
- source masters
- high-resolution generated image sets
- final high-bitrate video masters
- alternate cuts
- intermediate scene renders worth preserving
- reusable FX packs

Cloudflare R2 / S3-compatible object storage is a preferred design target.

### Important connector rule

Do not claim Cloudflare/R2 or any other external service is connected unless the current environment actually exposes a legitimate connector/tool or authenticated workflow.

If unavailable:
1. keep working locally/project-side;
2. define the expected storage interface;
3. persist metadata/references in GitHub;
4. integrate later without redesigning the creative pipeline.

## MCP / plugin / connector philosophy

AIVideoEdit should use legitimate available tools rather than hard-code itself to one execution environment.

Candidate integrations include:
- GitHub
- image generation/editing
- web research
- object storage
- media-processing services
- video-generation systems
- transcription/audio-analysis systems
- MCP servers exposing render or archive tools
- project/workspace file tools

When an integration is useful but unavailable, define an adapter contract rather than pretending it exists.

## Suggested object-storage manifest fields

Future project manifests can track media with fields such as:

```json
{
  "id": "ironflame-source-audio",
  "type": "audio",
  "filename": "Ironflame (Remastered) (1).mp3",
  "storage": "workspace|r2|s3|github-release|other",
  "uri": null,
  "sha256": null,
  "notes": "Canonical remastered source"
}
```

Hashes are strongly recommended once assets are archived, especially for source audio and final masters.

## Recovery requirement

A new agent should be able to reconstruct the current state by reading:

1. `/AGENT_HANDOFF.md`
2. `/PROJECT_INDEX.md`
3. `/docs/*`
4. `/projects/<active-project>/*`

If those files are stale, update them before ending the session.