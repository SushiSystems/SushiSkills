# remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Writes the doctrine reminders the Claude Code hooks print with `cat`, and checks them.

Both files come from `skills/sushiskills/SKILL.md` and its red flags; see `claude/README.md`.

Usage: python claude/hooks/remind_doctrine.py write|check
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

K_HOOKS_DIR = Path(__file__).resolve().parent
K_SESSION_START_FILE = K_HOOKS_DIR / "session_start.txt"
K_PROMPT_SUBMIT_FILE = K_HOOKS_DIR / "prompt_submit.txt"
K_EXIT_CLEAN = 0
K_EXIT_STALE = 1
K_SKILL_DIR = Path(__file__).resolve().parents[2] / "skills" / "sushiskills"
K_SKILL_FILE = K_SKILL_DIR / "SKILL.md"
K_FLAGS_FILE = K_SKILL_DIR / "references" / "red-flags.md"
K_ITEM = re.compile(r"^\d+\. \*\*(?P<title>[^*]+)\*\*\s*(?P<rest>.*)$")


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


def items(lines: list[str]) -> list[tuple[str, str]]:
    """Returns each numbered item as its bold title and its first sentence."""
    found: list[tuple[str, list[str]]] = []
    for line in lines:
        match = K_ITEM.match(line.strip())
        if match:
            found.append((match["title"].rstrip("."), [match["rest"]]))
        elif found and line.startswith("   ") and line.strip():
            found[-1][1].append(line.strip())
    result = []
    for title, parts in found:
        body = " ".join(parts).replace("**Rule:**", "").strip()
        result.append((title, body.split(". ")[0].rstrip(".") + "."))
    return result


def full_reminder() -> str:
    """Returns the boundaries, the defaults and the red flags, read from the skill."""
    text = K_SKILL_FILE.read_text(encoding="utf-8")
    out = ["SushiSkills doctrine reminder. Boundaries hold without exception:"]
    out += [f"- {title}: {first}" for title, first in items(section(text, "### Boundaries"))]
    out.append("Defaults hold unless their own 'not when' line applies, read as written:")
    out += [f"- {title}: {first}" for title, first in items(section(text, "### Defaults"))]
    out.append("A case no rule foresaw is the owner's call. Red flags, stop if you think one:")
    flags = K_FLAGS_FILE.read_text(encoding="utf-8").splitlines()
    out += [line for line in flags if line.startswith("- ")]
    return "\n".join(out)


def short_reminder() -> str:
    """Returns one line naming the boundaries."""
    text = K_SKILL_FILE.read_text(encoding="utf-8")
    names = ", ".join(title for title, _ in items(section(text, "### Boundaries")))
    return f"SushiSkills boundaries hold without exception: {names}. Unforeseen case: ask the owner."


def expected_files() -> dict[Path, str]:
    """Returns each reminder file with the text it must hold."""
    return {K_SESSION_START_FILE: full_reminder() + "\n", K_PROMPT_SUBMIT_FILE: short_reminder() + "\n"}


def stale_files() -> list[Path]:
    """Returns the reminder files whose text differs from what the skill gives."""
    stale = []
    for path, text in expected_files().items():
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            stale.append(path)
    return stale


def write_files() -> None:
    """Writes every reminder file from the skill."""
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
