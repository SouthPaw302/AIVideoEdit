from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ActionPolicy:
    change_tags: tuple[str, ...]
    canon_sensitive: bool = False
    requires_canonical_guard: bool = True


_POLICIES: dict[str, ActionPolicy] = {
    "production.sync_assets": ActionPolicy(("source_media", "asset_manifest", "reference_manifest")),
    "production.analyze": ActionPolicy(("analysis", "music", "references")),
    "production.set_music_context": ActionPolicy(("music", "lyrics", "genre")),
    "approach.set_capabilities": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "approach.set_routes": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "approach.select_route": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "storyboard.set": ActionPolicy(("storyboard", "script"), canon_sensitive=True),
    "storyboard.lock": ActionPolicy(("storyboard", "script"), canon_sensitive=True),
    "shots.build_packages": ActionPolicy(("shots",), canon_sensitive=True),
    "generated.request": ActionPolicy(("generated_media",)),
    "generated.register": ActionPolicy(("generated_media",)),
    "generated.accept": ActionPolicy(("generated_media", "accepted_media"), canon_sensitive=True),
    "generated.reject": ActionPolicy(("generated_media", "accepted_media"), canon_sensitive=True),
    "proofs.record": ActionPolicy(("proofs",)),
    "proofs.accept": ActionPolicy(("proofs", "accepted_media"), canon_sensitive=True),
    "proofs.finalize": ActionPolicy(("proofs", "accepted_media"), canon_sensitive=True),
    "proofs.reject": ActionPolicy(("proofs", "accepted_media"), canon_sensitive=True),
    "fx.set_requirements": ActionPolicy(("fx", "transitions")),
    "fx.lock": ActionPolicy(("fx", "transitions")),
    "assembly.run": ActionPolicy(("assembly",)),
    "final_qc.run_technical": ActionPolicy(("final_qc",)),
    "final_qc.accept_creative": ActionPolicy(("final_qc",)),
    "final_qc.reject": ActionPolicy(("final_qc",)),
    "archive.build": ActionPolicy(("archive",)),
    "production.advance": ActionPolicy(("stage",)),
}


def policy_for(action: str) -> ActionPolicy:
    action = str(action or "").strip()
    if action in _POLICIES:
        return _POLICIES[action]
    return ActionPolicy((f"tool:{action or 'unknown'}",), canon_sensitive=True)
