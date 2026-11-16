# test_remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Tests the doctrine reminder hook on a sample doctrine and on the real skill."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import remind_doctrine  # noqa: E402

K_SAMPLE = """# Doctrine

### Boundaries

1. **First.** One rule. Its detail
   runs on.
2. **Second.** Another rule.

### Defaults

1. **Third.**
   **Rule:** a default rule. More.

## Next
"""


class TestParsing(unittest.TestCase):
    """The section and item readers on a sample doctrine."""

    K_TEST_SIZE = "small"

    def test_section_stops_at_a_heading_of_the_same_level(self) -> None:
        lines = remind_doctrine.section(K_SAMPLE, "### Boundaries")
        self.assertNotIn("### Defaults", lines)
        self.assertIn("2. **Second.** Another rule.", lines)

    def test_items_give_title_and_first_sentence(self) -> None:
        found = remind_doctrine.items(remind_doctrine.section(K_SAMPLE, "### Boundaries"))
        self.assertEqual(found, [("First", "One rule."), ("Second", "Another rule.")])

    def test_items_drop_the_rule_label(self) -> None:
        found = remind_doctrine.items(remind_doctrine.section(K_SAMPLE, "### Defaults"))
        self.assertEqual(found, [("Third", "a default rule.")])


class TestEvents(unittest.TestCase):
    """The reminder each hook event gets, read from the real skill."""

    K_TEST_SIZE = "medium"

    def test_session_start_gets_every_boundary_and_flag(self) -> None:
        text = remind_doctrine.reminder_for({"hook_event_name": "SessionStart"})
        self.assertIn("- SOLID:", text)
        self.assertIn("- Act on the known step:", text)
        self.assertIn("written before reading the files", text)

    def test_prompt_gets_one_line(self) -> None:
        text = remind_doctrine.reminder_for({"hook_event_name": "UserPromptSubmit"})
        self.assertEqual(len(text.splitlines()), 1)
        self.assertIn("The owner decides the boundaries", text)

    def test_tool_use_gets_a_reminder_only_on_the_interval(self) -> None:
        event = {"hook_event_name": "PostToolUse", "session_id": f"test-{id(self)}"}
        answers = [remind_doctrine.reminder_for(event) for _ in range(remind_doctrine.K_TOOL_INTERVAL)]
        self.assertEqual(sum(answer is not None for answer in answers), 1)
        self.assertIsNotNone(answers[-1])

    def test_other_events_get_nothing(self) -> None:
        self.assertIsNone(remind_doctrine.reminder_for({"hook_event_name": "Stop"}))


if __name__ == "__main__":
    unittest.main()
