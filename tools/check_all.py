# check_all.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Runs every checker and the checker tests over a repository; prints only what failed.

The shared checkers run first, then every other `tools/<area>/check_<what>.py` the repository
holds as its own.

Usage: python tools/check_all.py [root]
"""

from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))

import settings  # noqa: E402

K_TOOLS = Path(__file__).resolve().parent
#: How many checks run at once.
K_WORKERS = min(8, os.cpu_count() or 1)
K_EXTRA_TEST_FOLDERS: tuple[str, ...] = getattr(settings, "K_EXTRA_TEST_FOLDERS", ())
K_CHECKERS = (
    "documentation/check_source_comments.py",
    "documentation/check_docs_layout.py",
    "documentation/check_changelog.py",
    "documentation/check_backlog.py",
    "documentation/check_design_format.py",
    "documentation/check_design_topics.py",
    "documentation/check_module_install.py",
    "documentation/check_docs_truth.py",
    "documentation/check_docs_follow.py",
    "documentation/check_docs_facts.py",
    "layering/check_layering.py",
    "layering/check_agnostic.py",
    "commits/check_backlog_trailer.py",
    "testing/check_test_mirror.py",
    "testing/check_test_sizes.py",
    "testing/check_test_value.py",
    "testing/check_probes.py",
    "logs/check_logging.py",
    "ci/check_workflows.py",
)


@dataclass(frozen=True, slots=True)
class Check:
    """Holds one check: its name, the command that runs it and whether it is a test suite."""

    name: str
    command: tuple[str, ...]
    is_suite: bool


def own_checker_names(found: Sequence[str]) -> tuple[str, ...]:
    """Returns the names among the found paths that are checkers the shared list does not name."""
    return tuple(
        name for name in found
        if PurePosixPath(name).name.startswith("check_")
        and name not in K_CHECKERS
        and not name.startswith("tests/")
    )


def plan_checks(root: Path, tools: Path, interpreter: str, own: Sequence[str],
                suite_folders: Sequence[Path]) -> list[Check]:
    """Returns each check with its command: shared checkers, own ones, then test suites."""
    checks = [
        Check(name, (interpreter, str(tools / name), str(root)), False)
        for name in (*K_CHECKERS, *own)
    ]
    suites = [
        Check(_suite_name(root, tools, folder),
              (interpreter, "-m", "unittest", "discover", "-q", "-s", str(folder)), True)
        for folder in suite_folders
    ]
    return [*checks, *suites]


def report(checks: Sequence[Check], results: Sequence[tuple[int, str]]) -> tuple[list[str], int]:
    """Returns the lines to print for the failed checks, and the exit code."""
    failed = [check for check, (code, _) in zip(checks, results) if code != 0]
    lines = [f"== {check.name}\n{output}".rstrip()
             for check, (code, output) in zip(checks, results) if code != 0]
    checkers = sum(not check.is_suite for check in checks)
    lines.append(f"failed: {', '.join(check.name for check in failed)}" if failed
                 else f"clean: {checkers} checkers, tests")
    return lines, 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    """Runs every check, all at once, and returns 1 when any of them failed.

    The checks read the repository and write nothing, so they run side by side; their output
    is printed in the order they are listed.
    """
    arguments = sys.argv[1:] if argv is None else argv
    root = Path(arguments[0]) if arguments else Path.cwd()
    checks = plan_checks(root, K_TOOLS, sys.executable, own_checker_names(_read_found(K_TOOLS)),
                         _read_suite_folders(root))
    lines, code = report(checks, _run_all(checks))
    for line in lines:
        print(line)
    return code


def _suite_name(root: Path, tools: Path, folder: Path) -> str:
    """Returns the name of a test suite: `tests`, or `tests: <folder>` for another folder."""
    return "tests" if folder == tools / "tests" else f"tests: {folder.relative_to(root).as_posix()}"


def _read_found(tools: Path) -> list[str]:
    """Returns each check_*.py one folder below tools, relative to tools and in path order."""
    return [path.relative_to(tools).as_posix() for path in sorted(tools.glob("*/check_*.py"))]


def _read_suite_folders(root: Path) -> list[Path]:
    """Returns the test folders that exist: the tools' own, then the repository's extra ones."""
    candidates = [K_TOOLS / "tests", *(root / folder for folder in K_EXTRA_TEST_FOLDERS)]
    return [folder for folder in candidates if folder.is_dir()]


def _run_check(command: Sequence[str]) -> tuple[int, str]:
    """Runs one check and returns its exit code and everything it printed, read as UTF-8."""
    environment = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    completed = subprocess.run(list(command), capture_output=True, text=True, encoding="utf-8",
                               env=environment)
    return completed.returncode, f"{completed.stdout}{completed.stderr}"


def _run_all(checks: Sequence[Check]) -> list[tuple[int, str]]:
    """Runs every check on a thread pool and returns the results in the order of the checks."""
    with ThreadPoolExecutor(max_workers=K_WORKERS) as pool:
        return list(pool.map(lambda check: _run_check(check.command), checks))


if __name__ == "__main__":
    sys.exit(main())
