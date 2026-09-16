# Scene 03 system authority

Scene 03 consumes the current `main` AIVideoEdit OS through bootstrap. Reusable FX and non-effect workflows are selected from current-main neutral registries according to this scene's `hybrid` production mode and declared media capabilities.

For the current Assembly06 preparation, the validated main authority is commit `0126b1c2978dc96810a02956a270feccdf02bdcf`; the current FX registry blob is `64eaf9b7b681e1868532c9ed690fc31c88b23312`.

Execution rules:
- reusable FX identities come from current-main `general/reusable/fx_v2/registry.json`;
- automatically execute only effects whose registry `gate_status` is `approved`;
- `proof_required` effects require a valid scene-local proof before use;
- `conditional` effects must satisfy their exact technology/geometry claim guard;
- `unavailable` effects are forbidden even if an older preset still references them;
- approved Scene 03 project-local FX may coexist with current-main FX but do not redefine or rename global FX identities;
- Scene 03 media selection remains project-local and must follow the full-media/zero-drift rules in `SCENE03_CONTINUATION_DIRECTIVE.md`, `SCENE03_MEDIA_AUDIT.json`, and `SCENE03_FX_EXECUTION_PLAN.json`.
