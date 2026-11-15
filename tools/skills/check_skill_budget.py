# check_skill_budget.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Checks that every SKILL.md holds no more words than the skill word budget.

Usage: python tools/skills/check_skill_budget.py [repository root] [--report] [--rule NAME]
"""

from __future__ import annotations

import sys
from collections.abc import Iterable, Iterator
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from checking.checker import Checker, Issue, run  # noqa: E402
from checking.ignored_paths import drop_ignored  # noqa: E402
from checking.source_file import SourceFile, read_files  # noqa: E402

import settings  # noqa: E402

#: The most words a SKILL.md body may hold, front matter left out.
K_WORD_BUDGET = 800
K_SKILL_FILE = "SKILL.md"
#: Folders whose skills belong to someone else and are not held to the budget.
K_FOREIGN_FOLDERS = ("third_party",)
K_FRONT_MATTER_MARK = "---"
#: Skills over the budget, each held to the count it had when the budget arrived; a ceiling only falls.
K_CEILINGS: dict[str, int] = getattr(settings, "K_SKILL_WORD_CEILINGS", {})


def _body(text: str) -> str:
    """Returns the text of a skill file without its front matter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != K_FRONT_MATTER_MARK:
        return text
    for number, line in enumerate(lines[1:], start=1):
        if line.strip() == K_FRONT_MATTER_MARK:
            return "\n".join(lines[number + 1:])
    return text


def _key(path: Path) -> str:
    """Returns the path of a skill file from the repository root that holds it, as K_CEILINGS names it."""
    resolved = path.resolve()
    for folder in resolved.parents:
        if (folder / ".git").exists():
            return resolved.relative_to(folder).as_posix()
    return path.as_posix()


def rule_word_budget(skill: SourceFile) -> Iterator[Issue]:
    """Yields an issue when a skill body holds more words than its ceiling, or K_WORD_BUDGET without one."""
    words = len(_body(skill.text).split())
    limit = K_CEILINGS.get(_key(skill.path), K_WORD_BUDGET)
    if words > limit:
        yield Issue(skill.path, 1, f"{words} words, limit {limit}; move detail to references/ or cut it")


def rule_ceiling_follows(skill: SourceFile) -> Iterator[Issue]:
    """Yields an issue when a skill has shrunk below its ceiling and the ceiling was not lowered."""
    ceiling = K_CEILINGS.get(_key(skill.path))
    if ceiling is None:
        return
    words = len(_body(skill.text).split())
    if words <= K_WORD_BUDGET:
        yield Issue(skill.path, 1, f"{words} words, within budget; remove its K_SKILL_WORD_CEILINGS entry")
    elif words < ceiling:
        yield Issue(skill.path, 1, f"{words} words, ceiling {ceiling}; lower K_SKILL_WORD_CEILINGS to {words}")


def _read_paths(root: Path) -> list[Path]:
    """Returns the SKILL.md files under one root, outside the foreign folders, that git does not ignore."""
    found = [
        path for path in sorted(root.rglob(K_SKILL_FILE))
        if not any(part in K_FOREIGN_FOLDERS for part in path.relative_to(root).parts)
    ]
    return drop_ignored(root, found)


def collect(paths: list[Path]) -> Iterable[SourceFile]:
    """Returns each skill file under the given roots, or each given skill file, as text."""
    found: list[Path] = []
    for path in paths:
        found.extend(_read_paths(path) if path.is_dir() else [path])
    return read_files(found, lambda _: True)


K_CHECKER = Checker(
    description="Checks that every SKILL.md stays within the skill word budget.",
    collect=collect,
    rules={
        "rule_word_budget": rule_word_budget,
        "rule_ceiling_follows": rule_ceiling_follows,
    },
)

if __name__ == "__main__":
    sys.exit(run(K_CHECKER))
