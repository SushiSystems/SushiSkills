# test_check_source_comments.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026 Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Tests the license block rule of the source comment checker."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from documentation.check_source_comments import _read_source, rule_license_block  # noqa: E402

K_PROJECT_LINE = "SushiSkills - https://github.com/SushiSystems/SushiSkills"
K_SUSHI_LINES = (
    "Copyright (c) 2026 Sushi Systems",
    "Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.",
    "Commercial use requires a licence from Sushi Systems.",
)


def _messages(name: str, text: str) -> list[str]:
    """Returns the license block messages for a file with the given name and content."""
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / name
        path.write_text(text, encoding="utf-8")
        return [issue.message for issue in rule_license_block(_read_source(path))]


def _boxed(name: str, extra: tuple[str, ...] = ()) -> str:
    """Returns a C-family file opening with a boxed block that names the given file."""
    rows = (name, K_PROJECT_LINE, *K_SUSHI_LINES, *extra)
    edge = "/" + "*" * 70 + "/"
    body = "\n".join(f"/* {row.ljust(66)} */" for row in rows)
    return f"{edge}\n{body}\n{edge}\n\n/**\n * @file {name}\n */\n"


def _hashed(name: str, shebang: bool = False) -> str:
    """Returns a Python file opening with the `#` form of the block."""
    rows = (name, K_PROJECT_LINE, *K_SUSHI_LINES)
    head = "#!/usr/bin/env python3\n" if shebang else ""
    return head + "\n".join(f"# {row}" for row in rows) + '\n"""Does nothing."""\n'


class LicenseBlockTest(unittest.TestCase):
    """Checks which file openings the license block rule accepts."""

    def test_accepts_boxed_block(self) -> None:
        """Accepts a C++ header that opens with the full boxed block."""
        self.assertEqual(_messages("graph.hpp", _boxed("graph.hpp")), [])

    def test_accepts_python_block(self) -> None:
        """Accepts a Python file that opens with the `#` block."""
        self.assertEqual(_messages("graph.py", _hashed("graph.py")), [])

    def test_accepts_block_after_shebang(self) -> None:
        """Accepts a Python file whose block follows a shebang line."""
        self.assertEqual(_messages("graph.py", _hashed("graph.py", shebang=True)), [])

    def test_accepts_upstream_lines(self) -> None:
        """Accepts extra upstream notice lines below the Sushi lines."""
        text = _boxed("lapjv.cpp", ("Portions Copyright (c) 2012 Tomas Kazmar", "BSD-2-Clause"))
        self.assertEqual(_messages("lapjv.cpp", text), [])

    def test_reports_missing_block(self) -> None:
        """Reports a file that opens with code."""
        self.assertEqual(
            _messages("graph.hpp", "#pragma once\n"),
            ["file must open with the license block"],
        )

    def test_reports_wrong_file_name(self) -> None:
        """Reports a block whose first line names another file."""
        self.assertEqual(
            _messages("graph.hpp", _boxed("node.hpp")),
            ["license block must open with graph.hpp"],
        )

    def test_reports_old_licence(self) -> None:
        """Reports a block that still carries the Apache lines."""
        text = (
            "# graph.py\n"
            "# Copyright (c) 2026-present Mustafa Garip & Sushi Systems\n"
            "# Licensed under the Apache License, Version 2.0. See LICENSE.\n"
            '"""Does nothing."""\n'
        )
        self.assertEqual(
            _messages("graph.py", text),
            [
                "license block lacks 'Copyright (c) <year> Sushi Systems'",
                "license block lacks 'Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.'",
                "license block lacks 'Commercial use requires a licence from Sushi Systems.'",
            ],
        )


if __name__ == "__main__":
    unittest.main()
