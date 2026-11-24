# test_remind_doctrine.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Tests the doctrine reminder writer on a sample doctrine and on the real skills."""

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

K_WITH_FRONT_MATTER = """---
name: sample
description: A sample.
---

# Title

Text.

"""


class TestParsing(unittest.TestCase):
    """The section, title, heading and body readers on sample text."""

    K_TEST_SIZE = "small"

    def test_section_stops_at_a_heading_of_the_same_level(self) -> None:
        lines = remind_doctrine.section(K_SAMPLE, "### Boundaries")
        self.assertNotIn("### Defaults", lines)
        self.assertIn("2. **Second.** Another rule.", lines)

    def test_titles_give_each_bold_title_without_its_full_stop(self) -> None:
        found = remind_doctrine.titles(remind_doctrine.section(K_SAMPLE, "### Boundaries"))
        self.assertEqual(found, ["First", "Second"])

    def test_titles_read_an_item_whose_rule_is_on_the_next_line(self) -> None:
        found = remind_doctrine.titles(remind_doctrine.section(K_SAMPLE, "### Defaults"))
        self.assertEqual(found, ["Third"])

    def test_headings_give_second_level_headings_only(self) -> None:
        self.assertEqual(remind_doctrine.headings("# One\n## Two\n### Three\n## Four\n"), ["Two", "Four"])

    def test_body_drops_front_matter_and_trailing_blank_lines(self) -> None:
        self.assertEqual(remind_doctrine.body(K_WITH_FRONT_MATTER), "# Title\n\nText.")

    def test_body_keeps_text_without_front_matter(self) -> None:
        self.assertEqual(remind_doctrine.body("# Title\n\nText.\n"), "# Title\n\nText.")


class TestReminders(unittest.TestCase):
    """The reminder texts read from the real skills, and the files the hooks print."""

    K_TEST_SIZE = "medium"

    def test_full_reminder_holds_each_source_file_verbatim(self) -> None:
        text = remind_doctrine.full_reminder()
        for path in remind_doctrine.K_SOURCES:
            self.assertIn(remind_doctrine.body(path.read_text(encoding="utf-8")), text, path.name)

    def test_full_reminder_names_the_path_of_each_source_file(self) -> None:
        text = remind_doctrine.full_reminder()
        for path in remind_doctrine.K_SOURCES:
            relative = path.relative_to(remind_doctrine.K_ROOT).as_posix()
            self.assertIn(f"=== {relative} ===", text)

    def test_full_reminder_keeps_the_not_when_line_of_each_default(self) -> None:
        text = remind_doctrine.full_reminder()
        self.assertEqual(text.count("**Not when:**"), 3)

    def test_short_reminder_is_one_line(self) -> None:
        text = remind_doctrine.short_reminder()
        self.assertEqual(len(text.splitlines()), 1)

    def test_short_reminder_names_every_boundary(self) -> None:
        text = remind_doctrine.short_reminder()
        skill = remind_doctrine.K_SKILL_FILE.read_text(encoding="utf-8")
        for title in remind_doctrine.titles(remind_doctrine.section(skill, "### Boundaries")):
            self.assertIn(title, text)

    def test_short_reminder_names_every_default(self) -> None:
        text = remind_doctrine.short_reminder()
        skill = remind_doctrine.K_SKILL_FILE.read_text(encoding="utf-8")
        for title in remind_doctrine.titles(remind_doctrine.section(skill, "### Defaults")):
            self.assertIn(title, text)

    def test_short_reminder_names_every_storage_rule_and_the_task_rule(self) -> None:
        text = remind_doctrine.short_reminder()
        storage = remind_doctrine.K_STORAGE_FILE.read_text(encoding="utf-8")
        for heading in remind_doctrine.headings(storage):
            self.assertIn(heading, text)
        self.assertIn(remind_doctrine.K_PROMPT_TASK_RULE, text)

    def test_the_files_the_hooks_print_match_the_skills(self) -> None:
        self.assertEqual(remind_doctrine.stale_files(), [])


if __name__ == "__main__":
    unittest.main()
