# remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Claude Code hook that repeats the sushiskills doctrine as additional context.

In full at session start and every K_TOOL_INTERVAL tool calls, as one line on every prompt.

Usage: python claude/hooks/remind_doctrine.py   (hook input as JSON on stdin)
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

#: Tool calls between two full reminders.
K_TOOL_INTERVAL = 25
K_SKILL_DIR = Path(__file__).resolve().parents[2] / "skills" / "sushiskills"
K_SKILL_FILE = K_SKILL_DIR / "SKILL.md"
K_FLAGS_FILE = K_SKILL_DIR / "references" / "red-flags.md"
K_COUNTER_DIR = Path(tempfile.gettempdir()) / "sushiskills-remind"
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


def tool_call_due(session: str) -> bool:
    """Counts a tool call for the session and tells whether a full reminder is due."""
    K_COUNTER_DIR.mkdir(exist_ok=True)
    counter = K_COUNTER_DIR / f"{re.sub(r'[^A-Za-z0-9_-]', '_', session)}.txt"
    try:
        count = int(counter.read_text(encoding="utf-8")) + 1
    except (OSError, ValueError):
        count = 1
    counter.write_text(str(count), encoding="utf-8")
    return count % K_TOOL_INTERVAL == 0


def reminder_for(event: dict) -> str | None:
    """Returns the reminder a hook event gets, or None when it gets none."""
    name = event.get("hook_event_name", "")
    if name == "SessionStart":
        return full_reminder()
    if name == "UserPromptSubmit":
        return short_reminder()
    if name == "PostToolUse" and tool_call_due(event.get("session_id", "unknown")):
        return full_reminder()
    return None


def main() -> int:
    """Reads the hook event from stdin and prints the hook output."""
    event = json.load(sys.stdin)
    text = reminder_for(event)
    if text:
        output = {"hookEventName": event["hook_event_name"], "additionalContext": text}
        print(json.dumps({"hookSpecificOutput": output}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
