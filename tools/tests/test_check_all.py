# test_check_all.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Tests which checks tools/check_all.py plans and how it reports them, pure and on disk."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from check_all import (  # noqa: E402
    K_CHECKERS,
    Check,
    _read_found,
    _run_check,
    own_checker_names,
    plan_checks,
    report,
)

K_ROOT = Path("repo")
K_TOOLS = K_ROOT / "tools"


class OwnCheckerNamesTest(unittest.TestCase):
    """Covers which of the found paths are own checkers that the shared list does not name."""

    K_TEST_SIZE = "small"

    def test_names_a_checker_the_shared_list_does_not_name(self) -> None:
        found = [*K_CHECKERS, "layering/check_package_layers.py"]
        self.assertEqual(own_checker_names(found), ("layering/check_package_layers.py",))

    def test_drops_a_test_helper_and_a_checker_under_tests(self) -> None:
        found = ["layering/helper.py", "tests/check_fake.py", "layering/check_package_layers.py"]
        self.assertEqual(own_checker_names(found), ("layering/check_package_layers.py",))


class PlanChecksTest(unittest.TestCase):
    """Covers the order of the checks, their commands and the names of the test suites."""

    K_TEST_SIZE = "small"

    def test_shared_checkers_run_first_then_own_then_suites(self) -> None:
        plan = plan_checks(K_ROOT, K_TOOLS, "py", ["layering/check_x.py"], [K_TOOLS / "tests"])
        names = [check.name for check in plan]
        self.assertEqual(names, [*K_CHECKERS, "layering/check_x.py", "tests"])

    def test_each_checker_runs_with_the_interpreter_and_the_root(self) -> None:
        plan = plan_checks(K_ROOT, K_TOOLS, "py", [], [])
        self.assertEqual(plan[0].command, ("py", str(K_TOOLS / K_CHECKERS[0]), str(K_ROOT)))

    def test_suite_runs_unittest_discover_on_its_folder(self) -> None:
        plan = plan_checks(K_ROOT, K_TOOLS, "py", [], [K_ROOT / "gui" / "tests"])
        self.assertEqual(plan[-1], Check("tests: gui/tests",
                                         ("py", "-m", "unittest", "discover", "-q", "-s",
                                          str(K_ROOT / "gui" / "tests")), True))

    def test_no_folder_that_exists_means_no_suite(self) -> None:
        plan = plan_checks(K_ROOT, K_TOOLS, "py", [], [])
        self.assertFalse(any(check.is_suite for check in plan))


class ReportTest(unittest.TestCase):
    """Covers the lines and the exit code for a clean run, a failed run and several failures."""

    K_TEST_SIZE = "small"

    def test_clean_run_counts_checkers_not_suites_and_exits_zero(self) -> None:
        checks = [Check("a", (), False), Check("b", (), False), Check("tests", (), True)]
        results = [(0, ""), (0, ""), (0, "")]
        self.assertEqual(report(checks, results), (["clean: 2 checkers, tests"], 0))

    def test_failed_check_prints_its_trimmed_output_and_is_named(self) -> None:
        checks = [Check("a", (), False), Check("b", (), False)]
        self.assertEqual(report(checks, [(0, "ok\n"), (1, "finding\n\n")]),
                         (["== b\nfinding", "failed: b"], 1))

    def test_several_failures_keep_the_order_of_the_checks(self) -> None:
        checks = [Check("a", (), False), Check("b", (), False), Check("c", (), False)]
        lines, code = report(checks, [(2, "one"), (0, ""), (1, "three")])
        self.assertEqual((lines, code), (["== a\none", "== c\nthree", "failed: a, c"], 1))


class ShellTest(unittest.TestCase):
    """Covers the disk and process edges: own checkers found on disk, and a check's output."""

    K_TEST_SIZE = "medium"

    def test_finds_a_checker_the_shared_list_does_not_name(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            tools = Path(folder)
            for name in (*K_CHECKERS, "layering/check_package_layers.py", "tests/check_fake.py",
                         "layering/helper.py"):
                (tools / name).parent.mkdir(parents=True, exist_ok=True)
                (tools / name).write_text("\n", encoding="utf-8")
            own = own_checker_names(_read_found(tools))
            self.assertEqual(own, ("layering/check_package_layers.py",))


    def test_reads_a_non_ascii_finding(self) -> None:
        """Reads an em dash a checker prints, whatever the console's code page."""
        script = "print('Open — phase 1'); raise SystemExit(1)"
        code, output = _run_check([sys.executable, "-c", script])
        self.assertEqual((code, output.strip()), (1, "Open — phase 1"))


if __name__ == "__main__":
    unittest.main()
