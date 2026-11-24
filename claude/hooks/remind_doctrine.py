# remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Writes the doctrine reminders the Claude Code hooks print with `cat`, and checks them.

The session reminder prints the doctrine files verbatim; the prompt reminder is one line built from
their headings. Both files come from the skills; see `claude/README.md`.

Usage: python claude/hooks/remind_doctrine.py write|check
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

K_HOOKS_DIR = Path(__file__).resolve().parent
K_ROOT = K_HOOKS_DIR.parents[1]
K_SESSION_START_FILE = K_HOOKS_DIR / "session_start.txt"
K_PROMPT_SUBMIT_FILE = K_HOOKS_DIR / "prompt_submit.txt"
K_EXIT_CLEAN = 0
K_EXIT_STALE = 1
K_SKILLS_DIR = K_ROOT / "skills"
K_DOCTRINE_DIR = K_SKILLS_DIR / "sushiskills"
K_SKILL_FILE = K_DOCTRINE_DIR / "SKILL.md"
K_STORAGE_FILE = K_SKILLS_DIR / "storage-discipline" / "SKILL.md"
#: The files the session reminder prints in full, in the order the agent reads them.
K_SOURCES: tuple[Path, ...] = (
    K_SKILL_FILE,
    K_DOCTRINE_DIR / "references" / "solid.md",
    K_DOCTRINE_DIR / "references" / "skill-map.md",
    K_DOCTRINE_DIR / "references" / "excuses.md",
    K_STORAGE_FILE,
)
K_SESSION_HEADER = (
    "SushiSkills doctrine, printed verbatim from the files named below. Every rule holds as "
    "written; the 'Not when' line of a default is part of its rule."
)
K_PROMPT_TASK_RULE = "Load the skill the skill map names for this task before you work."
K_PROMPT_ESCALATION = "Unforeseen case: ask the owner in one line, recommending."
K_FRONT_MATTER_MARK = "---"
K_ITEM = re.compile(r"^\d+\. \*\*(?P<title>[^*]+)\*\*")


def section(text: str, heading: str) -> list[str]:
    """Returns the lines under a heading up to the next heading of the same or higher level."""
    lines = text.splitlines()
    level = heading.split(" ")[0]
    start = lines.index(heading) + 1
    end = start
    while end < len(lines):
        mark = lines[end].split(" ")[0]
        if mark.startswith("#") and len(mark) <= len(level):
            break
        end += 1
    return lines[start:end]


def titles(lines: list[str]) -> list[str]:
    """Returns the bold title of each numbered item, without its closing full stop."""
    found = (K_ITEM.match(line.strip()) for line in lines)
    return [match["title"].rstrip(".") for match in found if match]


def headings(text: str) -> list[str]:
    """Returns the text of each second-level heading."""
    return [line[3:].strip() for line in text.splitlines() if line.startswith("## ")]


def body(text: str) -> str:
    """Returns a file's text without its front matter and without trailing blank lines."""
    lines = text.splitlines()
    if lines and lines[0].strip() == K_FRONT_MATTER_MARK:
        for number, line in enumerate(lines[1:], start=1):
            if line.strip() == K_FRONT_MATTER_MARK:
                lines = lines[number + 1:]
                break
    return "\n".join(lines).strip()


def full_reminder() -> str:
    """Returns the header and each source file in full, each under a line naming its path."""
    parts = [K_SESSION_HEADER]
    for path in K_SOURCES:
        parts.append(f"=== {path.relative_to(K_ROOT).as_posix()} ===")
        parts.append(body(path.read_text(encoding="utf-8")))
    return "\n\n".join(parts)


def short_reminder() -> str:
    """Returns one line naming the boundaries, the defaults and the storage topics, and the task rule."""
    skill = K_SKILL_FILE.read_text(encoding="utf-8")
    boundaries = ", ".join(titles(section(skill, "### Boundaries")))
    defaults = ", ".join(titles(section(skill, "### Defaults")))
    storage = "; ".join(headings(K_STORAGE_FILE.read_text(encoding="utf-8")))
    return (
        f"SushiSkills boundaries hold without exception: {boundaries}. "
        f"Defaults hold unless their 'Not when' line applies: {defaults}. "
        f"Storage rules, in full at session start: {storage}. "
        f"{K_PROMPT_TASK_RULE} {K_PROMPT_ESCALATION}"
    )


def expected_files() -> dict[Path, str]:
    """Returns each reminder file with the text it must hold."""
    return {K_SESSION_START_FILE: full_reminder() + "\n", K_PROMPT_SUBMIT_FILE: short_reminder() + "\n"}


def stale_files() -> list[Path]:
    """Returns the reminder files whose text differs from what the skills give."""
    stale = []
    for path, text in expected_files().items():
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            stale.append(path)
    return stale


def write_files() -> None:
    """Writes every reminder file from the skills."""
    for path, text in expected_files().items():
        path.write_text(text, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    """Writes the reminder files, or checks them and names each stale one."""
    arguments = sys.argv[1:] if argv is None else argv
    if arguments == ["write"]:
        write_files()
        return K_EXIT_CLEAN
    if arguments != ["check"]:
        print("usage: remind_doctrine.py write|check", file=sys.stderr)
        return K_EXIT_STALE
    stale = stale_files()
    for path in stale:
        print(f"{path.name} is stale; run: python claude/hooks/remind_doctrine.py write", file=sys.stderr)
    return K_EXIT_STALE if stale else K_EXIT_CLEAN


if __name__ == "__main__":
    sys.exit(main())
