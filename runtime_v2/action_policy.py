from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ActionPolicy:
    change_tags: tuple[str, ...]
    canon_sensitive: bool = False
    requires_canonical_guard: bool = True


_POLICIES: dict[str, ActionPolicy] = {
    # Content/source mutations: enforced against active refinement/recut scope.
    "production.sync_assets": ActionPolicy(("source_media", "asset_manifest", "reference_manifest")),
    "production.set_music_context": ActionPolicy(("music", "lyrics", "genre")),
    "approach.set_capabilities": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "approach.set_routes": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "approach.select_route": ActionPolicy(("visual_approach",), canon_sensitive=True),
    "storyboard.set": ActionPolicy(("storyboard", "script"), canon_sensitive=True),
    "storyboard.lock": ActionPolicy(("storyboard", "script"), canon_sensitive=True),
    "shots.build_packages": ActionPolicy(("shots",), canon_sensitive=True),
    "generated.request": ActionPolicy(("generated_media",), canon_sensitive=True),
    "generated.register": ActionPolicy(("generated_media",), canon_sensitive=True),
    "generated.accept": ActionPolicy(("generated_media", "accepted_media"), canon_sensitive=True),
    "generated.reject": ActionPolicy(("generated_media", "accepted_media"), canon_sensitive=True),
    "fx.set_requirements": ActionPolicy(("fx", "transitions"), canon_sensitive=True),
    "operating.lock_canon": ActionPolicy(("canon", "accepted_baseline"), canon_sensitive=True),

    # Control/evidence mutations still require fresh attestation and canonical
    # guards, but they do not themselves alter the bounded creative scope.
    "production.analyze": ActionPolicy(()),
    "proofs.record": ActionPolicy(()),
    "proofs.accept": ActionPolicy(()),
    "proofs.finalize": ActionPolicy(()),
    "proofs.reject": ActionPolicy(()),
    "fx.lock": ActionPolicy(()),
    "assembly.run": ActionPolicy(()),
    "final_qc.run_technical": ActionPolicy(()),
    "final_qc.accept_creative": ActionPolicy(()),
    "final_qc.reject": ActionPolicy(()),
    "archive.build": ActionPolicy(()),
    "production.advance": ActionPolicy(()),
    "operating.configure_v2": ActionPolicy(()),
    "operating.update_next_action": ActionPolicy(()),
    "operating.set_refinement": ActionPolicy(()),
}


def policy_for(action: str) -> ActionPolicy:
    action = str(action or "").strip()
    if action in _POLICIES:
        return _POLICIES[action]
    return ActionPolicy((f"tool:{action or 'unknown'}",), canon_sensitive=True)
