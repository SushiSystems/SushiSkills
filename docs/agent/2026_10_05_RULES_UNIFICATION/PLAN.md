# Rules Unification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every Sushi rule one home, move the header template and this repository to the new licence, and make this repository pass its own checkers.

**Architecture:** Rule text moves so that `claude/CLAUDE.md` and each skill never restate each other. Three checker rules are added as one function and one table row each, with unit tests under `tools/tests/`. The repository then takes its own licence, notices and documentation skeleton.

**Tech Stack:** Markdown, Python 3.11 standard library (`unittest`, `tempfile`), GitHub Actions.

**Spec:** `docs/agent/2026_10_05_RULES_UNIFICATION/SPEC.md`

## Global Constraints

- Work only inside `D:/Projects/sushiskills`. No sibling repository is touched.
- Nothing under `third_party/` or `docs/archive/` is edited.
- Licence: PolyForm Noncommercial 1.0.0. Holder: `Sushi Systems`. Never write "open source"; write "source-available, free for non-commercial use".
- Header lines, verbatim: `Copyright (c) 2026 Sushi Systems`, `Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.`, `Commercial use requires a licence from Sushi Systems.`
- Checkers: Python 3.11, standard library only, one function per rule, one table row per rule, `K_` constants for settings, no side effects.
- Every prose change goes through the `humanizer` skill. Every commit follows the `commits` skill, staged by path, and carries its changelog line in `docs/reference/CHANGELOG.md` (one line, scope first, at most 240 characters, never why).
- No push. Commits stay local until the owner pushes.
- Skills under `~/.claude/skills` are symlinks into this tree, so every edit is live the moment it is saved. A half-edited rule is live too: finish a file before leaving it.

## Review Focus

1. A Python file that opens with a `#!` shebang: the license block follows the shebang and `rule_license_block` accepts it. Test in Task 2.
2. A file ported from third-party code carries extra upstream lines inside the block: the rule accepts extra lines and still demands the Sushi lines. Test in Task 2.
3. A link with an anchor (`GUIDE.md#install`) in `docs/README.md`: the target counts as reached. Test in Task 4.
4. A document under `docs/agent/` that the index does not link: no finding, work folders are exempt. Test in Task 4.
5. A repository with no `docs/README.md`: `rule_reachable_from_index` stays silent and `rule_required_entries` reports the missing index once. Test in Task 4.

## File structure

| File | Responsibility after this plan |
| --- | --- |
| `claude/CLAUDE.md` | Language, quality, honesty, the dispatch block, model and effort; names skills for the rest |
| `skills/multi-agent-work/SKILL.md` | Roles, planning, report acceptance; cites the dispatch block |
| `skills/documentation/SKILL.md` | The docs tree, placement, changelog; states the reachability exemption |
| `skills/source-comments/SKILL.md` | The license block in three variants and its rules |
| `skills/dependencies/SKILL.md` | Licence table with the first-party row, ported code, notices |
| `skills/repository-layout/SKILL.md` | Root entries including `NOTICE.md`, `COMMERCIAL.md`; the skills-repository root shape |
| `skills/continuous-integration/SKILL.md` | `ci.yml` and `release.yml`; the no-CLI case |
| `skills/versioning-and-release/SKILL.md` | The version source for a repository without a manifest |
| `skills/sushiskills/SKILL.md` | The superpowers mapping |
| `tools/documentation/check_source_comments.py` | Gains `rule_license_block` |
| `tools/documentation/check_docs_layout.py` | Gains `rule_required_entries`, `rule_reachable_from_index` |
| `tools/tests/test_check_source_comments.py`, `tools/tests/test_check_docs_layout.py` | Unit tests for the three rules |
| `LICENSE`, `COMMERCIAL.md`, `NOTICE.md`, `README.md`, `AGENTS.md`, `CLAUDE.md` | The repository's own front door and licence |
| `docs/**` | The documentation skeleton |
| `.github/workflows/ci.yml` | Runs the checkers and the tests on Windows and Linux |

---

### Task 1: One home per rule

**Files:**
- Modify: `claude/CLAUDE.md` (sections "Documentation architecture", "Source comments", "Delegation", "Planning")
- Modify: `skills/multi-agent-work/SKILL.md` (sections "Dispatch", "Choosing a model")
- Modify: `skills/documentation/SKILL.md` (the tree comment for `README.md`)
- Modify: `skills/sushiskills/SKILL.md` (new section after "The bricks")
- Modify: `docs/reference/CHANGELOG.md`

**Interfaces:**
- Produces: the seven-line dispatch block in `claude/CLAUDE.md`, which every later dispatch copies.

- [ ] **Step 1: Replace the "Documentation architecture" section of `claude/CLAUDE.md`** with:

```markdown
## Documentation architecture

Every repository, whatever its size, carries the documentation tree the `documentation` skill
defines, so that what exists, what is done, what is left and what is planned can be read from
the tree. Load that skill before writing or moving anything under `docs/` or a module README.
It holds the tree, the placement questions and the changelog entry shape;
`tools/documentation/check_docs_layout.py` and `check_changelog.py` enforce it.

A manual page that stops being true is a defect in the change that made it false. The
documentation update is part of the same commit as the code; a change without its README,
design status or changelog entry is not finished.

On first entering a repository that lacks this shape: measure it, report the gaps, and get
approval before building the skeleton. The build-out is its own task.
```

- [ ] **Step 2: Replace the "Source comments" section** with:

```markdown
## Source comments

A comment says what a thing does, in Doxygen form, and nothing else. Load the `source-comments`
skill before writing or reviewing a comment, a file header or a license block. It holds the
license block, the `@file` block, the tag table and what is forbidden in source;
`tools/documentation/check_source_comments.py` enforces it.
```

- [ ] **Step 3: In "Delegation"**, change "the same six lines" to "the same seven lines", insert the new fourth line and renumber the rest:

```markdown
4. Write only to the files listed below and to the work folder under `docs/agent/`.
5. Report what was done and what was not. Paste the output of every verification you claim.
6. Before reporting, syntax-check what you wrote without building: C++ through
   `compile_commands.json` with `clang -fsyntax-only`, GLSL through `shader_compiler.exe`.
   Paste the command and its output.
7. Write scratch only to the scratchpad, never binaries or copies, under 100 MB; delete what you
   made and report the scratchpad size (`storage-discipline` skill).
```

Change "without evidence of 1, 2, 5 and 6" to "without evidence of 1, 2, 6 and 7".

- [ ] **Step 4: Replace the "Planning" section** with:

```markdown
## Planning

The `multi-agent-work` skill holds the planning rules: hierarchy first, one acceptance criterion
and one build per task. I choose how a plan runs, inline or in waves; ask me.
```

- [ ] **Step 5: In `skills/multi-agent-work/SKILL.md`, replace the "Dispatch" section body up to "Then:"** with:

```markdown
Every dispatch opens with the dispatch block, verbatim, whatever the task. The block lives in
the owner's global instructions, `claude/CLAUDE.md` in SushiSkills, section "Delegation", and
nowhere else; copy it from there.
```

Keep the "Then: the task, its file list, ..." paragraph and the paragraph after it. Replace the "Choosing a model" section body with:

```markdown
The model and the effort for each kind of dispatch are set in the same "Delegation" section.
Both are set on every dispatch, never inherited by default.
```

- [ ] **Step 6: In `skills/documentation/SKILL.md`**, change the tree comment on `README.md` to `manual index; every document outside agent/ reachable from here`.

- [ ] **Step 7: In `skills/sushiskills/SKILL.md`**, add after the bricks table:

```markdown
## Third-party skills

The vendored superpowers skills name their own paths. In a Sushi repository a superpowers spec
is `SPEC.md` and a superpowers plan is `PLAN.md` in the work folder
`docs/agent/<YYYY_MM_DD>_<WORK_NAME>/`. Nothing is written under `docs/superpowers/`.
```

- [ ] **Step 8: Add changelog lines** under `## Unreleased`, newest first:

```markdown
- 2026-10-05 — claude: Reduced the documentation, source comment and planning sections to citations of their skills and added the file-set line to the dispatch block (`claude/CLAUDE.md`).
- 2026-10-05 — multi-agent-work: Removed the second dispatch block and the model table in favour of the global instructions (`skills/multi-agent-work/SKILL.md`).
- 2026-10-05 — sushiskills: Mapped superpowers specs and plans onto the work folder (`skills/sushiskills/SKILL.md`).
- 2026-10-03 — claude: Added the scratch rule as the sixth dispatch line and to the report evidence rule (`claude/CLAUDE.md`).
```

- [ ] **Step 9: Verify**

Run: `grep -rn "SOLID, without exception" --include=*.md . | grep -v third_party | grep -v docs/agent | grep -v docs/archive`
Expected: lines from `claude/CLAUDE.md` (the Quality section and dispatch line 1) and `skills/sushiskills/SKILL.md` (the doctrine) only. No line in `skills/multi-agent-work/`.

Run: `python tools/documentation/check_changelog.py .`
Expected: no output, exit 0.

- [ ] **Step 10: Commit**

```bash
git add claude/CLAUDE.md skills/multi-agent-work/SKILL.md skills/documentation/SKILL.md skills/sushiskills/SKILL.md docs/reference/CHANGELOG.md
git commit -m "refactor(claude): keep each rule in one file"
```

---

### Task 2: License block template and its checker rule

**Files:**
- Modify: `skills/source-comments/SKILL.md` (section "File opening", section "Python")
- Modify: `tools/documentation/check_source_comments.py`
- Create: `tools/tests/test_check_source_comments.py`
- Modify: `tools/common/__init__.py`, `tools/common/checker.py`, `tools/documentation/check_changelog.py`, `tools/documentation/check_docs_layout.py`, `tools/documentation/check_source_comments.py`, `tools/layering/check_layering.py` (the header lines)
- Modify: `tools/README.md`, `docs/reference/CHANGELOG.md`

**Interfaces:**
- Produces: `rule_license_block(source: SourceFile) -> Iterator[Issue]`, constants `K_COPYRIGHT_LINE`, `K_LICENSE_LINES`.

- [ ] **Step 1: Write the failing tests** in `tools/tests/test_check_source_comments.py`:

```python
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
    rows = (name, "SushiSkills - https://github.com/SushiSystems/SushiSkills", *K_SUSHI_LINES, *extra)
    edge = "/" + "*" * 70 + "/"
    body = "\n".join(f"/* {row.ljust(66)} */" for row in rows)
    return f"{edge}\n{body}\n{edge}\n\n/**\n * @file {name}\n */\n"


def _hashed(name: str, shebang: bool = False) -> str:
    """Returns a Python file opening with the `#` form of the block."""
    rows = (name, "SushiSkills - https://github.com/SushiSystems/SushiSkills", *K_SUSHI_LINES)
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
        self.assertEqual(_messages("graph.hpp", "#pragma once\n"), ["file must open with the license block"])

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
```

- [ ] **Step 2: Run the tests and see them fail**

Run: `python -m unittest discover -s tools/tests -t tools -v`
Expected: `ImportError: cannot import name 'rule_license_block'`.

- [ ] **Step 3: Implement the rule** in `tools/documentation/check_source_comments.py`. Add below `K_LICENSE_LINE`:

```python
K_COPYRIGHT_LINE = re.compile(r"^Copyright \(c\) \d{4} Sushi Systems$")
K_LICENSE_LINES = (
    "Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.",
    "Commercial use requires a licence from Sushi Systems.",
)
```

Change `_license_end_python` so a shebang counts as part of the leading run (it already does, since a shebang starts with `#`; no edit). Add before `rule_file_header`:

```python
def _license_texts(source: SourceFile) -> list[str]:
    """Returns the license block's lines without comment markers, box edges or a shebang."""
    texts: list[str] = []
    for line in source.lines[:source.body_start]:
        stripped = line.strip()
        if source.is_python and stripped.startswith("#!"):
            continue
        text = stripped[1:].strip() if source.is_python else stripped[2:-2].strip()
        if text and set(text) != {"*"}:
            texts.append(text)
    return texts


def rule_license_block(source: SourceFile) -> Iterator[Issue]:
    """Yields an issue when the file does not open with the repository's license block."""
    texts = _license_texts(source)
    if not texts:
        yield Issue(source.path, 1, "file must open with the license block")
        return
    if texts[0] != source.path.name:
        yield Issue(source.path, 1, f"license block must open with {source.path.name}")
    if not any(K_COPYRIGHT_LINE.match(text) for text in texts):
        yield Issue(source.path, 1, "license block lacks 'Copyright (c) <year> Sushi Systems'")
    for expected in K_LICENSE_LINES:
        if expected not in texts:
            yield Issue(source.path, 1, f"license block lacks '{expected}'")
```

Add the first row of the rule table: `"rule_license_block": rule_license_block,`.

- [ ] **Step 4: Run the tests and see them pass**

Run: `python -m unittest discover -s tools/tests -t tools -v`
Expected: 7 tests, `OK`.

- [ ] **Step 5: Give the six tool files the new header.** Replace the two leading lines of each with five lines; for `tools/common/checker.py`:

```python
# checker.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026 Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
```

The first line is each file's own name: `__init__.py`, `checker.py`, `check_changelog.py`, `check_docs_layout.py`, `check_source_comments.py`, `check_layering.py`.

- [ ] **Step 6: Rewrite "File opening" in `skills/source-comments/SKILL.md`.** Replace the code block's boxed part with the block from the spec, section 4, non-commercial variant, followed by the unchanged `@file` block. Replace the two bullets below it with:

```markdown
- The first line of the license block is the file name; the second is the project and its URL.
- The holder is `Sushi Systems`. The year is the year the file was first written and is never
  updated.
- A closed repository replaces the two licence lines with
  `All rights reserved. No licence is granted.`
- A file ported from third-party code keeps the upstream copyright line and licence name inside
  the block, below the Sushi lines. See `dependencies`.
- `@file` repeats the file name; `@brief` is one sentence starting with a verb; `@author` names
  a person. No `@date`, no version, no history.
```

In the "Python" section, add after the first sentence: "The license block is the same five lines, each behind `#`, with no box; a shebang, when present, comes first." and show the Python block from the spec.

- [ ] **Step 7: Update `tools/README.md`**: in the `check_source_comments.py` row, put "license block, " before "file header". Under "Per-repository settings" add: "`K_COPYRIGHT_LINE` and `K_LICENSE_LINES` in `check_source_comments.py` hold the repository's licence lines; a closed repository sets `K_LICENSE_LINES` to `("All rights reserved. No licence is granted.",)`." Add a row for `tests/`: "Unit tests for the checker rules; run `python -m unittest discover -s tools/tests -t tools`".

- [ ] **Step 8: Verify and commit**

Run: `python tools/documentation/check_source_comments.py tools`
Expected: no output, exit 0.

Changelog line: `- 2026-10-05 — source-comments: Replaced the Apache license block with the PolyForm Noncommercial block and added the rule that checks it (`skills/source-comments/SKILL.md`, `check_source_comments.py`, `rule_license_block`).`

```bash
git add skills/source-comments/SKILL.md tools docs/reference/CHANGELOG.md
git commit -m "feat(source-comments)!: move the license block to PolyForm Noncommercial"
```

---

### Task 3: The repository's own licence, notices and the dependency rules

**Files:**
- Replace: `LICENSE`
- Create: `COMMERCIAL.md`, `NOTICE.md`
- Modify: `README.md` (section "Licence")
- Modify: `skills/dependencies/SKILL.md`, `skills/repository-layout/SKILL.md`
- Modify: `docs/reference/CHANGELOG.md`

- [ ] **Step 1: Fetch the licence text**

Run: `curl -fsSL https://raw.githubusercontent.com/polyformproject/polyform-licenses/1.0.0/PolyForm-Noncommercial-1.0.0.md -o LICENSE`
Then read the file and confirm it opens with `# PolyForm Noncommercial License 1.0.0` and contains `https://polyformproject.org/licenses/noncommercial/1.0.0`. If the URL fails, stop and report; do not type the licence from memory.

Append to `LICENSE`, after one blank line:

```
Required Notice: Copyright (c) 2026 Sushi Systems (https://github.com/SushiSystems)
```

- [ ] **Step 2: Write `COMMERCIAL.md`**:

```markdown
# Commercial use

SushiSkills is source-available under the PolyForm Noncommercial License 1.0.0 (`LICENSE`).
Personal use, study, research, and use by educational, charitable and public bodies are free.

Any commercial purpose needs a separate licence from Sushi Systems. That includes use inside a
company, use in paid client work, and use in a product or service that is sold. To ask for one,
write to mustafagarip@sushisystems.io with what you want to build and who will use it.
```

- [ ] **Step 3: Write `NOTICE.md`** listing: `third_party/superpowers` (MIT, upstream URL and version copied from `third_party/superpowers/README.md`); the sources `skills/humanizer` and `skills/marketing-copy` cite (Wikipedia "Signs of AI writing", CC BY-SA 4.0; GOV.UK content, Open Government Licence v3.0), each with its URL from `skills/humanizer/research/generic_english_sources.md`; and the sentence "Versions up to and including commit `ef442df` were published under Apache-2.0 and remain available under it."

- [ ] **Step 4: Replace the licence section of `README.md`** with:

```markdown
## Licence

Source-available, free for non-commercial use, under the PolyForm Noncommercial License 1.0.0;
see `LICENSE`. Commercial use needs a licence from Sushi Systems; see `COMMERCIAL.md`.
Third-party material keeps its own licence; see `NOTICE.md`. Versions up to commit `ef442df`
were published under Apache-2.0 and stay under it.
```

- [ ] **Step 5: `skills/dependencies/SKILL.md`**: add a table row after the MIT row, `| A Sushi Systems repository, under its own licence | Accepted |`, and change the non-commercial row to `| Third-party non-commercial, source-available, field-of-use limits | Rejected |`. Add two sections before "Where it comes from":

```markdown
## Ported code

Code translated or adapted from a third-party source is that source's work, whatever language
it ends up in. The file keeps the upstream copyright line and licence name in its license
block, and `NOTICE.md` lists it. The owner's licence covers the changes, not the original.

## Notices

`NOTICE.md` at the repository root lists every third-party component, every ported file and
every redistributed binary: its name, source URL, version, licence and where it sits in the
tree. A component that is not listed is not shipped.
```

- [ ] **Step 6: `skills/repository-layout/SKILL.md`**: in the root listing put `NOTICE.md  COMMERCIAL.md` after `LICENSE`, add table rows `| NOTICE.md | Third-party components, ported files and redistributed binaries; see dependencies |` and `| COMMERCIAL.md | How a company obtains a commercial licence |`, and add after the table:

```markdown
A repository that holds skills and no code has `skills/` and `claude/` in place of `cmake/`,
`cli/`, `modules/`, `tests/` and `applications/`. Each skill folder is a module.
```

- [ ] **Step 7: Verify and commit**

Run: `grep -rIl "Apache" . --exclude-dir=.git --exclude-dir=third_party --exclude-dir=archive --exclude-dir=agent`
Expected: `README.md`, `NOTICE.md`, `skills/dependencies/SKILL.md` (the accepted-licences row) and the changelog only.

Changelog lines:
`- 2026-10-05 — licence: Moved the repository from Apache-2.0 to PolyForm Noncommercial 1.0.0 (`LICENSE`, `COMMERCIAL.md`, `NOTICE.md`, `README.md`).`
`- 2026-10-05 — dependencies: Accepted first-party repositories and added the ported code and notices rules (`skills/dependencies/SKILL.md`, `skills/repository-layout/SKILL.md`).`

```bash
git add LICENSE COMMERCIAL.md NOTICE.md README.md skills/dependencies/SKILL.md skills/repository-layout/SKILL.md docs/reference/CHANGELOG.md
git commit -m "chore(licence)!: move to PolyForm Noncommercial 1.0.0"
```

---

### Task 4: Required documents and reachability rules

**Files:**
- Modify: `tools/documentation/check_docs_layout.py`
- Create: `tools/tests/test_check_docs_layout.py`
- Modify: `tools/README.md`, `skills/project-tools/SKILL.md`, `docs/reference/CHANGELOG.md`

**Interfaces:**
- Produces: `rule_required_entries(repository: Repository) -> Iterator[Issue]`, `rule_reachable_from_index(repository: Repository) -> Iterator[Issue]`, helper `_relative_links(path: Path) -> Iterator[tuple[int, str]]`, constant `K_REQUIRED_ENTRIES`.

- [ ] **Step 1: Write the failing tests** in `tools/tests/test_check_docs_layout.py`:

```python
# test_check_docs_layout.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026 Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Tests the required-entry and reachability rules of the docs layout checker."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from documentation.check_docs_layout import (  # noqa: E402
    K_REQUIRED_ENTRIES,
    Repository,
    rule_reachable_from_index,
    rule_required_entries,
)


def _repository(folder: str, files: dict[str, str]) -> Repository:
    """Returns a repository whose docs/ tree holds the given files."""
    root = Path(folder)
    for name, text in files.items():
        path = root / "docs" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return Repository(root)


def _names(issues) -> list[str]:
    """Returns the docs-relative path of each issue."""
    return [issue.path.as_posix().split("/docs/", 1)[1] for issue in issues]


class RequiredEntriesTest(unittest.TestCase):
    """Checks that each required document is demanded."""

    def test_reports_every_missing_document(self) -> None:
        """Reports all required documents for a docs/ tree that holds none."""
        with tempfile.TemporaryDirectory() as folder:
            repository = _repository(folder, {"guides/X.md": "# X\n"})
            self.assertEqual(_names(rule_required_entries(repository)), list(K_REQUIRED_ENTRIES))

    def test_accepts_a_complete_tree(self) -> None:
        """Reports nothing when every required document exists."""
        with tempfile.TemporaryDirectory() as folder:
            repository = _repository(folder, {name: "# T\n" for name in K_REQUIRED_ENTRIES})
            self.assertEqual(list(rule_required_entries(repository)), [])


class ReachabilityTest(unittest.TestCase):
    """Checks which documents count as reached from the index."""

    def test_follows_links_through_an_index(self) -> None:
        """Reaches a document linked from an index the root index links, anchor included."""
        files = {
            "README.md": "# Manual\n[design](design/README.md)\n[guide](guides/GUIDE.md#install)\n",
            "design/README.md": "# Design\n[topic](TOPIC.md)\n",
            "design/TOPIC.md": "# Topic\n",
            "guides/GUIDE.md": "# Guide\n",
        }
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(list(rule_reachable_from_index(_repository(folder, files))), [])

    def test_reports_an_orphan(self) -> None:
        """Reports a document no index links."""
        files = {"README.md": "# Manual\n", "guides/ORPHAN.md": "# Orphan\n"}
        with tempfile.TemporaryDirectory() as folder:
            issues = rule_reachable_from_index(_repository(folder, files))
            self.assertEqual(_names(issues), ["guides/ORPHAN.md"])

    def test_ignores_links_in_code(self) -> None:
        """Does not count a link inside a fence or a code span as reaching its target."""
        files = {
            "README.md": "# Manual\n`[a](guides/A.md)`\n```\n[b](guides/B.md)\n```\n",
            "guides/A.md": "# A\n",
            "guides/B.md": "# B\n",
        }
        with tempfile.TemporaryDirectory() as folder:
            issues = rule_reachable_from_index(_repository(folder, files))
            self.assertEqual(_names(issues), ["guides/A.md", "guides/B.md"])

    def test_exempts_work_folders_and_archive(self) -> None:
        """Reports nothing for unlinked documents under agent/ and archive/."""
        files = {
            "README.md": "# Manual\n",
            "agent/2026_10_05_WORK/SPEC.md": "# Spec\n",
            "archive/OLD.md": "# Old\n",
        }
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(list(rule_reachable_from_index(_repository(folder, files))), [])

    def test_is_silent_without_an_index(self) -> None:
        """Reports nothing when docs/README.md is absent; the required-entry rule owns that."""
        with tempfile.TemporaryDirectory() as folder:
            repository = _repository(folder, {"guides/X.md": "# X\n"})
            self.assertEqual(list(rule_reachable_from_index(repository)), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run and see the failure**

Run: `python -m unittest discover -s tools/tests -t tools -v`
Expected: `ImportError: cannot import name 'K_REQUIRED_ENTRIES'`.

- [ ] **Step 3: Implement.** Add below `K_DESIGN_INDEXES`:

```python
K_REQUIRED_ENTRIES = (
    "README.md", "CONTRIBUTING.md", "DOCUMENTATION_STYLE_GUIDE.md",
    "reference/CHANGELOG.md", "reference/GLOSSARY.md", "reference/KNOWN_ISSUES.md",
    "design/README.md", "design/REMAINING_WORK.md",
)
```

Add before `rule_docs_entries`:

```python
def _relative_links(path: Path) -> Iterator[tuple[int, str]]:
    """Yields the line number and anchor-free target of each relative link outside code."""
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for target in K_LINK.findall(K_CODE_SPAN.sub("", line)):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            yield number, target.split("#", 1)[0]


def _reachable(index: Path) -> set[Path]:
    """Returns every Markdown file reachable from an index through relative links."""
    reached: set[Path] = set()
    pending = [index.resolve()]
    while pending:
        path = pending.pop()
        if path in reached or not path.is_file():
            continue
        reached.add(path)
        for _, target in _relative_links(path):
            linked = (path.parent / target).resolve()
            if linked.suffix == ".md":
                pending.append(linked)
    return reached
```

Replace the body of `rule_links` with:

```python
    for path in repository.live_documents():
        for number, target in _relative_links(path):
            if not (path.parent / target).exists():
                yield Issue(path, number, f"link target does not exist: {target}")
```

Add after `rule_links`:

```python
def rule_required_entries(repository: Repository) -> Iterator[Issue]:
    """Yields an issue for each required document missing from docs/."""
    for name in K_REQUIRED_ENTRIES:
        if not (repository.docs / name).is_file():
            yield Issue(repository.docs / name, 1, "required document is missing")


def rule_reachable_from_index(repository: Repository) -> Iterator[Issue]:
    """Yields an issue for each live document outside agent/ that docs/README.md does not reach."""
    index = repository.docs / "README.md"
    if not index.is_file():
        return
    reached = _reachable(index)
    agent = repository.docs / "agent"
    for path in repository.live_documents():
        if agent not in path.parents and path.resolve() not in reached:
            yield Issue(path, 1, "not reachable from docs/README.md")
```

Register both in the rule table: `"rule_required_entries"` after `"rule_docs_entries"`, `"rule_reachable_from_index"` after `"rule_links"`.

- [ ] **Step 4: Run and see the pass**

Run: `python -m unittest discover -s tools/tests -t tools -v`
Expected: 14 tests, `OK`.

- [ ] **Step 5: Update the two descriptions.** In `tools/README.md`, the `check_docs_layout.py` row becomes: "`docs/` entries, required documents, document names, work folders, status lines, design ceiling, links under `docs/`, reachability from `docs/README.md`, READMEs under `modules/<tier>/`, archive candidates". Delete the "Not checked" section (its items move to the backlog in Task 6). In `skills/project-tools/SKILL.md`, the `check_docs_layout.py` row becomes: "The tree, required documents, names, work folder contents, status lines, broken links, reachability from the index and 90-day archive candidates from `documentation`".

- [ ] **Step 6: Verify and commit**

Run: `python tools/documentation/check_source_comments.py tools`
Expected: no output, exit 0.

Changelog line: `- 2026-10-05 — tools: Added the required-document and reachability rules to the docs layout checker (`check_docs_layout.py`, `rule_required_entries`, `rule_reachable_from_index`).`

```bash
git add tools skills/project-tools/SKILL.md docs/reference/CHANGELOG.md
git commit -m "feat(tools): require the manual's documents and their reachability"
```

---

### Task 5: CI and versioning rules

**Files:**
- Modify: `skills/continuous-integration/SKILL.md`, `skills/versioning-and-release/SKILL.md`, `docs/reference/CHANGELOG.md`

- [ ] **Step 1:** In `skills/continuous-integration/SKILL.md`, "Shape" item 2 becomes: "One workflow file per trigger under the forge's workflow folder: `ci.yml` for pushes and pull requests, `release.yml` for tags." Add after item 1: "A repository without a project CLI calls the checkers and its unit tests directly; that is the only direct call allowed."

- [ ] **Step 2:** In `skills/versioning-and-release/SKILL.md`, add a row to the version-source table: `| No build manifest (a skills or documentation repository) | The latest `## vX.Y.Z` heading in `docs/reference/CHANGELOG.md`; the tag carries the same number |`. Read the table first and match its column order.

- [ ] **Step 3: Commit** with changelog line `- 2026-10-05 — continuous-integration: Named the push workflow `ci.yml`, allowed direct checker calls without a CLI and gave manifest-free repositories a version source (`skills/continuous-integration/SKILL.md`, `skills/versioning-and-release/SKILL.md`).`

```bash
git add skills/continuous-integration/SKILL.md skills/versioning-and-release/SKILL.md docs/reference/CHANGELOG.md
git commit -m "docs(continuous-integration): name the push workflow ci.yml"
```

---

### Task 6: This repository's documentation skeleton and front door

**Files:**
- Create: `docs/README.md`, `docs/CONTRIBUTING.md`, `docs/DOCUMENTATION_STYLE_GUIDE.md`, `docs/getting_started/INSTALL.md`, `docs/reference/GLOSSARY.md`, `docs/reference/KNOWN_ISSUES.md`, `docs/design/README.md`, `docs/design/REMAINING_WORK.md`
- Create: `skills/README.md`, `claude/README.md`, `AGENTS.md`, `CLAUDE.md`
- Modify: `README.md`, `docs/reference/CHANGELOG.md`

Each document is written through `humanizer`, in English, and holds exactly these facts:

- [ ] **Step 1: `docs/README.md`**: one line on what the manual is, then a link list reaching every other live document: `CONTRIBUTING.md`, `DOCUMENTATION_STYLE_GUIDE.md`, `getting_started/INSTALL.md`, `reference/CHANGELOG.md`, `reference/GLOSSARY.md`, `reference/KNOWN_ISSUES.md`, `design/README.md`, `design/REMAINING_WORK.md`.
- [ ] **Step 2: `docs/CONTRIBUTING.md`**: how a rule changes (the text now under "Changing a rule" in the root README, moved here): the rule is fixed in its skill first, the checker follows in the same commit, the changelog line names the skill as scope, sibling repositories copy `tools/` again. Inbound contributions need a signed contributor agreement before they are merged, because the outbound licence is non-commercial and Sushi Systems sells commercial licences.
- [ ] **Step 3: `docs/DOCUMENTATION_STYLE_GUIDE.md`**: names `humanizer` as the prose rule and `documentation` as the placement rule, and states the SKILL.md front-matter contract (`name`, `description` starting "Use when").
- [ ] **Step 4: `docs/getting_started/INSTALL.md`**: the install text now in the root README, with one method per tool: symlink each folder under `skills/` into `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (other agents); import `claude/CLAUDE.md` from `~/.claude/CLAUDE.md` with the `@` line. State that a symlinked install runs the working tree, so uncommitted edits are live.
- [ ] **Step 5: `docs/reference/GLOSSARY.md`**: brick, skill, work folder, dispatch block, orchestrator, worker, checker, tier. One sentence each, taken from the skills that define them.
- [ ] **Step 6: `docs/reference/KNOWN_ISSUES.md`**: the archived v0.1.0 changelog has six entries for fourteen commits and omits the initial skill set and the TypeScript skill; local tags `v0.1.0` and `v0.1.1` were never pushed.
- [ ] **Step 7: `docs/design/README.md`**: the topic map; it has no topics yet and says so in one line. `docs/design/REMAINING_WORK.md`: the four unbuilt checks removed from `tools/README.md` in Task 4, plus "cited paths in backticks are not resolved by `rule_links`" and "`rule_module_readmes` covers `modules/<tier>/` only".
- [ ] **Step 8: `skills/README.md`**: the skill table now in the root README, the front-matter contract, and that `humanizer` and `marketing-copy` carry language files and `research/`. `claude/README.md`: what `CLAUDE.md` is, the import line, the per-OS path of the importing file.
- [ ] **Step 9: Root `AGENTS.md` and `CLAUDE.md`**, same text in both: this repository follows `sushiskills`, `documentation`, `humanizer`, `commits`, `python-code-style`, `source-comments`, `project-tools`; its checkers run with `python tools/<area>/check_<what>.py .`; its tests with `python -m unittest discover -s tools/tests -t tools`.
- [ ] **Step 10: Shrink the root `README.md`** to: what SushiSkills is, a pointer to `skills/README.md` for the table, a link to `docs/README.md`, the third-party section, the licence section from Task 3.
- [ ] **Step 11: Verify**

Run: `python tools/documentation/check_docs_layout.py .`
Expected: no output, exit 0. Paste the output.
Run: `ls ~/.claude/skills | wc -l` and `ls ~/.claude/skills/humanizer/SKILL.md`
Expected: 24 and the path, proving the symlinks still resolve.

- [ ] **Step 12: Commit** with changelog line `- 2026-10-05 — docs: Built the documentation skeleton and moved install and rule-change text out of the front door (`docs/README.md`, `docs/getting_started/INSTALL.md`, `skills/README.md`, `AGENTS.md`).`

```bash
git add docs README.md AGENTS.md CLAUDE.md skills/README.md claude/README.md
git commit -m "docs: build the documentation skeleton"
```

---

### Task 7: Humanizer and marketing-copy sources

**Files:**
- Modify (only if copied passages are found): `skills/humanizer/*.md`, `skills/marketing-copy/*.md`
- Modify: `NOTICE.md`, `docs/agent/2026_10_05_RULES_UNIFICATION/REPORT.md`

- [ ] **Step 1:** Fetch the two sources named in `skills/humanizer/research/generic_english_sources.md` (the Wikipedia "Signs of AI writing" page and the GOV.UK style guide's "words to avoid" list). Compare them with `skills/humanizer/generic_english.md`, `plain_english.md` and `skills/marketing-copy/english.md`: look for sentences of eight or more consecutive words in common, and for lists whose order and membership match a source list.
- [ ] **Step 2:** Rewrite each copied sentence in the repository's own words. A list of single words stays; it is recorded in `NOTICE.md` as "word list informed by" with the source and its licence.
- [ ] **Step 3:** Write the result into `REPORT.md`: the files compared, each match found with both texts, and what was done. If nothing was copied, the report says so with the comparison method.
- [ ] **Step 4: Commit** `docs(humanizer): credit the sources of the word lists`, with a changelog line only if a skill file changed.

---

### Task 8: CI and close

**Files:**
- Create: `.github/workflows/ci.yml`
- Modify: `docs/reference/CHANGELOG.md`, `docs/agent/2026_10_05_RULES_UNIFICATION/SPEC.md` (status line), `REPORT.md`

- [ ] **Step 1: Write `.github/workflows/ci.yml`**:

```yaml
name: ci

on:
  push:
  pull_request:

jobs:
  checkers:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: python tools/documentation/check_source_comments.py .
        run: python tools/documentation/check_source_comments.py .
      - name: python tools/documentation/check_docs_layout.py .
        run: python tools/documentation/check_docs_layout.py .
      - name: python tools/documentation/check_changelog.py .
        run: python tools/documentation/check_changelog.py .
      - name: python tools/layering/check_layering.py .
        run: python tools/layering/check_layering.py .
      - name: python -m unittest discover -s tools/tests -t tools
        run: python -m unittest discover -s tools/tests -t tools
```

`fetch-depth: 0` is there because `rule_archive_candidates` reads commit dates.

- [ ] **Step 2: Run the spec's five acceptance checks** and paste each command with its output into `REPORT.md`:

```bash
python tools/documentation/check_source_comments.py . ; echo exit $?
python tools/documentation/check_docs_layout.py . ; echo exit $?
python tools/documentation/check_changelog.py . ; echo exit $?
python tools/layering/check_layering.py . ; echo exit $?
python -m unittest discover -s tools/tests -t tools
grep -rln "re-attachable without touching" --include=*.md . | grep -v -e third_party -e docs/archive -e docs/agent
grep -rIl "Apache" . --exclude-dir=.git --exclude-dir=third_party --exclude-dir=archive --exclude-dir=agent
ls ~/.claude/skills | wc -l
```

Expected: four `exit 0`, 14 tests `OK`, the dispatch grep prints `claude/CLAUDE.md` and `skills/sushiskills/SKILL.md` only, the Apache grep prints the files Task 3 names, and 24 skills.

- [ ] **Step 3:** Set the spec's status line to `**Status:** Shipped`, write `REPORT.md` (what was done, what was not, the pasted output), add the changelog line `- 2026-10-05 — ci: Added the workflow that runs the four checkers and the checker tests on Windows and Linux (`.github/workflows/ci.yml`).`

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/ci.yml docs/reference/CHANGELOG.md docs/agent/2026_10_05_RULES_UNIFICATION docs/agent/2026_10_05_ESTATE_AUDIT
git commit -m "build(ci): run the checkers and their tests on push"
```

## Execution mode

The tasks share `docs/reference/CHANGELOG.md` and several of them edit the same skills, so no two
can run in one wave. Inline is the fitting mode: one session, hierarchy order, eight commits,
followed by one independent review of the whole branch.
