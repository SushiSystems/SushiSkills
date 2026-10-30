# test_apply_settings.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Tests how the Sushi settings and the CLAUDE.md block are added to a repository on disk."""

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


class ApplySettingsTest(unittest.TestCase):
    """Builds a repository with a settings file and a manifest for each test."""

    def setUp(self) -> None:
        self._folder = tempfile.TemporaryDirectory()
        self.root = Path(self._folder.name)
        (self.root / "tools").mkdir()
        (self.root / "tools" / "settings.py").write_text(K_SETTINGS, encoding="utf-8")
        (self.root / "sushi-module.toml").write_text('[module]\nname = "x"\nalias = "sx"\n', encoding="utf-8")

    def tearDown(self) -> None:
        self._folder.cleanup()

    def _settings(self) -> str:
        return (self.root / "tools" / "settings.py").read_text(encoding="utf-8")

    def test_appends_every_constant_the_file_lacks_and_keeps_the_rest(self) -> None:
        added = apply_settings.apply_to_settings(self.root)
        text = self._settings()
        self.assertTrue(text.startswith(K_SETTINGS))
        self.assertIn("K_TOOLING_PACKAGE", added)
        self.assertIn("K_MODULE_MANIFEST", added)
        self.assertNotIn("K_LICENSE_HOLDER", added)
        self.assertEqual(text.count("K_LICENSE_HOLDER"), 1)
        self.assertIn('K_MODULE_MANIFEST = \'sushi-module.toml\'', text)

    def test_the_result_is_a_python_file_with_the_values_intact(self) -> None:
        apply_settings.apply_to_settings(self.root)
        namespace: dict[str, object] = {}
        exec(compile(self._settings(), "settings.py", "exec"), namespace)  # noqa: S102
        self.assertEqual(namespace["K_TOOLING_PACKAGE"], "sushicore")
        self.assertEqual(namespace["K_MODULE_HEADINGS"], ("## Standalone", "## With SushiHub"))
        self.assertIn("SUSHISTACK_HOME", namespace["K_MODULE_WORKSPACE_READ"])
        self.assertTrue(namespace["K_CLOSED"])

    def test_a_second_run_adds_nothing(self) -> None:
        apply_settings.apply_to_settings(self.root)
        self.assertEqual(apply_settings.apply_to_settings(self.root), [])

    def test_the_claude_block_gets_the_alias_and_is_written_once(self) -> None:
        (self.root / "CLAUDE.md").write_text("# Project\n", encoding="utf-8")
        self.assertTrue(apply_settings.apply_to_claude(self.root, "sx"))
        text = (self.root / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("`sx backlog next`", text)
        self.assertNotIn("<alias>", text)
        self.assertTrue(text.startswith("# Project\n"))
        self.assertFalse(apply_settings.apply_to_claude(self.root, "sx"))

    def test_a_repository_without_a_claude_file_gets_one(self) -> None:
        self.assertTrue(apply_settings.apply_to_claude(self.root, "sx"))
        self.assertTrue((self.root / "CLAUDE.md").is_file())

    def test_the_alias_comes_from_the_manifest(self) -> None:
        self.assertEqual(apply_settings.alias_of(self.root), "sx")
        (self.root / "sushi-module.toml").unlink()
        self.assertIsNone(apply_settings.alias_of(self.root))

    def test_the_command_needs_an_alias_and_a_settings_file(self) -> None:
        (self.root / "sushi-module.toml").unlink()
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(apply_settings.main([str(self.root)]), 2)
            self.assertEqual(apply_settings.main([str(self.root / "tools")]), 2)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(apply_settings.main([str(self.root), "--alias", "sx"]), 0)


if __name__ == "__main__":
    unittest.main()
