# test_check_skill_budget.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Tests the rule of tools/skills/check_skill_budget.py on skill text held in memory."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sushicore.tools.checking.source_file import SourceFile  # noqa: E402
import skills.check_skill_budget as budget  # noqa: E402
from skills.check_skill_budget import K_WORD_BUDGET, Skill, rule_ceiling_follows, rule_word_budget  # noqa: E402

K_SKILL = Path("skills/x/SKILL.md")
K_FRONT_MATTER = "---\nname: x\ndescription: " + "word " * 50 + "\n---\n"


def _issues(text: str) -> list[str]:
    """Returns the message of each issue the budget rule yields for a skill text."""
    return [issue.message for issue in rule_word_budget(Skill(SourceFile(K_SKILL, text), K_SKILL.as_posix()))]


class WordBudgetTest(unittest.TestCase):
    """Covers a body at the budget, a body over it, and front matter left out of the count."""
    K_TEST_SIZE = "small"

    def test_passes_a_body_at_the_budget(self) -> None:
        self.assertEqual(_issues(K_FRONT_MATTER + "word " * K_WORD_BUDGET), [])

    def test_reports_a_body_over_the_budget(self) -> None:
        issues = _issues("word " * (K_WORD_BUDGET + 1))
        self.assertEqual(len(issues), 1)
        self.assertTrue(issues[0].startswith(f"{K_WORD_BUDGET + 1} words"))

    def test_leaves_front_matter_out_of_the_count(self) -> None:
        self.assertEqual(_issues(K_FRONT_MATTER + "word " * (K_WORD_BUDGET - 10)), [])


class CeilingTest(unittest.TestCase):
    """Covers a skill held to its ceiling, one grown past it, and one shrunk under it."""
    K_TEST_SIZE = "small"

    def setUp(self) -> None:
        self._saved = dict(budget.K_CEILINGS)
        budget.K_CEILINGS.clear()
        budget.K_CEILINGS[K_SKILL.as_posix()] = K_WORD_BUDGET + 100

    def tearDown(self) -> None:
        budget.K_CEILINGS.clear()
        budget.K_CEILINGS.update(self._saved)

    def _follows(self, words: int) -> list[str]:
        """Returns the message of each issue the ceiling rule yields for a body of this many words."""
        return [issue.message for issue in rule_ceiling_follows(Skill(SourceFile(K_SKILL, "word " * words), K_SKILL.as_posix()))]

    def test_passes_a_skill_at_its_ceiling(self) -> None:
        self.assertEqual(_issues("word " * (K_WORD_BUDGET + 100)), [])
        self.assertEqual(self._follows(K_WORD_BUDGET + 100), [])

    def test_reports_a_skill_grown_past_its_ceiling(self) -> None:
        self.assertEqual(len(_issues("word " * (K_WORD_BUDGET + 101))), 1)

    def test_asks_to_lower_the_ceiling_of_a_shrunk_skill(self) -> None:
        self.assertIn(f"lower K_SKILL_WORD_CEILINGS to {K_WORD_BUDGET + 50}", self._follows(K_WORD_BUDGET + 50)[0])

    def test_asks_to_remove_the_ceiling_of_a_skill_within_budget(self) -> None:
        self.assertIn("remove its K_SKILL_WORD_CEILINGS entry", self._follows(K_WORD_BUDGET)[0])


class CollectTest(unittest.TestCase):
    """Covers the key collect reads from the repository that holds a skill, whatever the working directory."""
    K_TEST_SIZE = "medium"

    def test_keys_a_skill_by_its_path_from_the_repository_root(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".git").mkdir()
            skill = root / "skills" / "x" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text("word", encoding="utf-8")
            self.assertEqual([found.key for found in budget.collect([root / "skills"])], ["skills/x/SKILL.md"])


if __name__ == "__main__":
    unittest.main()
