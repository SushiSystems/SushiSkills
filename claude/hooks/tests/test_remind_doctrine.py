# test_remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Tests the doctrine reminder writer on a sample doctrine and on the real skill."""

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


class TestReminders(unittest.TestCase):
    """The reminder texts read from the real skill, and the files the hooks print."""

    K_TEST_SIZE = "medium"

    def test_full_reminder_holds_every_boundary_and_flag(self) -> None:
        text = remind_doctrine.full_reminder()
        self.assertIn("- SOLID:", text)
        self.assertIn("- Act on the known step:", text)
        self.assertIn("written before reading the files", text)

    def test_short_reminder_is_one_line(self) -> None:
        text = remind_doctrine.short_reminder()
        self.assertEqual(len(text.splitlines()), 1)
        self.assertIn("The owner decides the boundaries", text)

    def test_the_files_the_hooks_print_match_the_skill(self) -> None:
        self.assertEqual(remind_doctrine.stale_files(), [])


if __name__ == "__main__":
    unittest.main()
