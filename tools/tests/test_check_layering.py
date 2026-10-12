# test_check_layering.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Tests the upward include rule of tools/layering/check_layering.py on a tree built on disk."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from layering.check_layering import ModuleTree, _discover, rule_upward_includes  # noqa: E402

K_TIERS = ("foundation", "domain")


def _tree(root: Path, include_line: str) -> ModuleTree:
    """Returns a two-tier tree whose foundation module holds one header with the given include."""
    low = root / "modules" / "foundation" / "blas" / "include" / "Project" / "blas"
    high = root / "modules" / "domain" / "geometry" / "include" / "Project" / "geometry"
    low.mkdir(parents=True)
    high.mkdir(parents=True)
    (low / "backend.hpp").write_text(include_line + "\n", encoding="utf-8")
    (high / "mesh.hpp").write_text("\n", encoding="utf-8")
    return ModuleTree(root, _discover(root), K_TIERS)


class RuleUpwardIncludesTest(unittest.TestCase):
    """Covers the rule that a module includes nothing from a higher tier."""

    def test_reports_an_include_of_a_higher_module(self) -> None:
        """Checks that a header of this repository's higher tier is a finding."""
        with tempfile.TemporaryDirectory() as folder:
            tree = _tree(Path(folder), "#include <Project/geometry/mesh.hpp>")
            self.assertEqual(len(list(rule_upward_includes(tree))), 1)

    def test_ignores_another_project_with_a_module_of_the_same_name(self) -> None:
        """Checks that a dependency's header is not taken for this repository's module."""
        with tempfile.TemporaryDirectory() as folder:
            tree = _tree(Path(folder), "#include <Other/geometry/mesh.hpp>")
            self.assertEqual(list(rule_upward_includes(tree)), [])


if __name__ == "__main__":
    unittest.main()
