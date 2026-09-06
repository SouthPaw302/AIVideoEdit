#!/usr/bin/env python3
"""Stable launcher for the IronFlame V4 renderer.

The renderer loads FX2 lazily after it knows the repository root. This launcher keeps
that behavior while binding FXContext into the renderer module's global namespace so
module-level frame helpers can construct runtime contexts correctly.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from general.reusable.fx_v2.runtime import FXContext

renderer_path = Path(__file__).with_name("render_canon_motion_v4.py")
spec = importlib.util.spec_from_file_location("ironflame_canon_motion_v4", renderer_path)
if spec is None or spec.loader is None:
    raise RuntimeError(f"could not load renderer: {renderer_path}")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
renderer.FXContext = FXContext
renderer.main()
