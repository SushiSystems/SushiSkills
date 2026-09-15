# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License, Version 2.0. See LICENSE.
"""Checks docs/reference/CHANGELOG.md against the changelog rules of the documentation skill.

Usage: python tools/documentation/check_changelog.py [repository root] [--report] [--rule NAME]
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.checker import Checker, Issue, run  # noqa: E402

K_CHANGELOG = Path("docs/reference/CHANGELOG.md")
K_LENGTH_CEILING = 240
K_CITED_PATH_CEILING = 3
K_ENTRY_SHAPE = re.compile(r"^- \d{4}-\d{2}-\d{2} — [A-Z][a-z]+ .+\.$")
K_SECOND_SENTENCE = re.compile(r"[.!?] +[A-Z]")
K_NESTED_BULLET = re.compile(r"^\s+[-*+] ")
K_CITED_PATH = re.compile(r"`[^`]+`")


@dataclass(frozen=True, slots=True)
class Entry:
    """Holds one bullet line of the changelog."""

    path: Path
    number: int
    text: str


def collect(paths: list[Path]) -> Iterable[Entry]:
    """Returns every bullet line, nested or not, of each repository's changelog."""
    entries: list[Entry] = []
    for root in paths:
        changelog = root if root.is_file() else root / K_CHANGELOG
        if not changelog.is_file():
            continue
        in_fence = False
        for index, line in enumerate(changelog.read_text(encoding="utf-8").splitlines()):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            elif not in_fence and re.match(r"^\s*[-*+] ", line):
                entries.append(Entry(changelog, index + 1, line.rstrip()))
    return entries


def _code_free(text: str) -> str:
    """Returns the entry with its backticked spans removed."""
    return K_CITED_PATH.sub("``", text)


def rule_entry_shape(entry: Entry) -> Iterator[Issue]:
    """Yields an issue when an entry is not `- date — Verb what, ending in a period`."""
    if not K_NESTED_BULLET.match(entry.text) and not K_ENTRY_SHAPE.match(entry.text):
        yield Issue(entry.path, entry.number, "entry must read '- YYYY-MM-DD — Verbed what (`where`).'")


def rule_length(entry: Entry) -> Iterator[Issue]:
    """Yields an issue when an entry is longer than the ceiling."""
    if len(entry.text) > K_LENGTH_CEILING:
        yield Issue(entry.path, entry.number, f"{len(entry.text)} characters, ceiling {K_LENGTH_CEILING}")


def rule_single_sentence(entry: Entry) -> Iterator[Issue]:
    """Yields an issue when an entry holds a second sentence."""
    if K_SECOND_SENTENCE.search(_code_free(entry.text)):
        yield Issue(entry.path, entry.number, "an entry is one sentence")


def rule_no_nesting(entry: Entry) -> Iterator[Issue]:
    """Yields an issue for each nested bullet."""
    if K_NESTED_BULLET.match(entry.text):
        yield Issue(entry.path, entry.number, "nested bullets are forbidden")


def rule_cited_paths(entry: Entry) -> Iterator[Issue]:
    """Yields an issue when an entry cites more places than one change touches."""
    count = len(K_CITED_PATH.findall(entry.text))
    if count > K_CITED_PATH_CEILING:
        yield Issue(entry.path, entry.number, f"cites {count} places; split into one line per change")


K_CHECKER = Checker(
    description="Checks the changelog against the documentation skill.",
    collect=collect,
    rules={
        "rule_entry_shape": rule_entry_shape,
        "rule_length": rule_length,
        "rule_single_sentence": rule_single_sentence,
        "rule_no_nesting": rule_no_nesting,
        "rule_cited_paths": rule_cited_paths,
    },
)

if __name__ == "__main__":
    sys.exit(run(K_CHECKER))
