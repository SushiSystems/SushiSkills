# ignored_paths.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Drops the paths git ignores, so a checker reads only what the repository owns."""

from __future__ import annotations

import subprocess
from pathlib import Path

K_EXIT_SOME_IGNORED = 0
K_EXIT_NONE_IGNORED = 1


def drop_ignored(root: Path, paths: list[Path]) -> list[Path]:
    """Returns the paths git does not ignore below root; all of them outside a repository."""
    if not paths:
        return paths
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "check-ignore", "-z", "--stdin"],
            input="\0".join(str(path.resolve()) for path in paths) + "\0",
            capture_output=True, text=True, encoding="utf-8",
        )
    except OSError:
        return paths
    if completed.returncode not in (K_EXIT_SOME_IGNORED, K_EXIT_NONE_IGNORED):
        return paths
    ignored = {Path(entry).resolve() for entry in completed.stdout.split("\0") if entry}
    return [path for path in paths if path.resolve() not in ignored]
