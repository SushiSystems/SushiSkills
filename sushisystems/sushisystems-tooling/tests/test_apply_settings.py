# test_apply_settings.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
"""Tests how the Sushi settings and the CLAUDE.md block are added to a repository."""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import apply_settings  # noqa: E402

K_SETTINGS = 'K_CLOSED = True\nK_LICENSE_HOLDER = "Kept Holder"\n'
K_MANIFEST = '[module]\nname = "x"\nalias = "sx"\n'
K_COMMANDS = (("sx", "`sx backlog next`"), (None, "`python -m sushicore.backlog next`"))


class MissingSettingsTest(unittest.TestCase):
    """Covers the decision on which constants a settings text lacks."""

    K_TEST_SIZE = "small"

    def test_a_text_that_holds_every_missing_constant_lacks_none(self) -> None:
        body = "".join(f"{name} = {value!r}\n" for name, value in apply_settings.missing_settings(K_SETTINGS))
        self.assertEqual(apply_settings.missing_settings(K_SETTINGS + body), [])


class ApplySettingsTest(unittest.TestCase):
    """Builds a repository with a settings file and a manifest for each test."""

    K_TEST_SIZE = "medium"

    def setUp(self) -> None:
        self._folder = tempfile.TemporaryDirectory()
        self.root = Path(self._folder.name)
        (self.root / "tools").mkdir()
        (self.root / "tools" / "settings.py").write_text(K_SETTINGS, encoding="utf-8")
        (self.root / "sushi-module.toml").write_text(K_MANIFEST, encoding="utf-8")

    def tearDown(self) -> None:
        self._folder.cleanup()

    def _settings(self) -> str:
        return (self.root / "tools" / "settings.py").read_text(encoding="utf-8")

    def _claude(self) -> str:
        return (self.root / "CLAUDE.md").read_text(encoding="utf-8")

    def test_the_missing_constants_are_appended(self) -> None:
        apply_settings.apply_to_settings(self.root)
        self.assertIn("K_MODULE_MANIFEST = 'sushi-module.toml'", self._settings())

    def test_the_existing_lines_stay_first(self) -> None:
        apply_settings.apply_to_settings(self.root)
        self.assertTrue(self._settings().startswith(K_SETTINGS))

    def test_a_defined_constant_is_not_added(self) -> None:
        self.assertNotIn("K_LICENSE_HOLDER", apply_settings.apply_to_settings(self.root))

    def test_the_result_is_a_python_file_with_the_values_intact(self) -> None:
        apply_settings.apply_to_settings(self.root)
        namespace: dict[str, object] = {}
        exec(compile(self._settings(), "settings.py", "exec"), namespace)  # noqa: S102
        self.assertEqual(namespace["K_TOOLING_PACKAGE"], "sushicore")
        self.assertEqual(namespace["K_MODULE_HEADINGS"], ("## Standalone", "## With SushiHub"))
        self.assertIn("SUSHISTACK_HOME", namespace["K_MODULE_WORKSPACE_READ"])
        self.assertTrue(namespace["K_CLOSED"])

    def test_the_block_goes_after_the_existing_text(self) -> None:
        (self.root / "CLAUDE.md").write_text("# Project\n", encoding="utf-8")
        apply_settings.apply_to_claude(self.root, "sx")
        self.assertTrue(self._claude().startswith("# Project\n"))

    def test_a_file_that_holds_the_block_is_not_written(self) -> None:
        (self.root / "CLAUDE.md").write_text("# Project\n\n## Backlog and design\n", encoding="utf-8")
        self.assertFalse(apply_settings.apply_to_claude(self.root, "sx"))

    def test_a_repository_without_a_claude_file_gets_one_with_its_commands(self) -> None:
        for alias, command in K_COMMANDS:
            with self.subTest(alias=alias):
                (self.root / "CLAUDE.md").unlink(missing_ok=True)
                self.assertTrue(apply_settings.apply_to_claude(self.root, alias))
                self.assertIn(command, self._claude())

    def test_the_alias_comes_from_the_manifest(self) -> None:
        self.assertEqual(apply_settings.alias_of(self.root), "sx")

    def test_no_manifest_gives_no_alias(self) -> None:
        (self.root / "sushi-module.toml").unlink()
        self.assertIsNone(apply_settings.alias_of(self.root))

    def test_the_command_refuses_a_root_without_settings(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(apply_settings.main([str(self.root / "tools")]), 2)

    def test_the_command_applies_to_a_root_with_settings(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(apply_settings.main([str(self.root)]), 0)


class ClaudeBlockTest(unittest.TestCase):
    """Covers the block read from the template for a CLI alias or for none."""

    K_TEST_SIZE = "medium"

    def test_the_alias_replaces_every_placeholder(self) -> None:
        for alias, command in K_COMMANDS:
            with self.subTest(alias=alias):
                block = apply_settings.claude_block(alias)
                self.assertIn(command, block)
                self.assertNotIn("<alias>", block)


if __name__ == "__main__":
    unittest.main()
