# Rules unification

**Status:** Shipped — implemented and reviewed on 2026-10-05; see `REPORT.md`.

Programme 1 of 5 in the estate refactor. The estate audit of 2026-10-05
(`docs/agent/2026_10_05_ESTATE_AUDIT/REPORT.md`) found that this repository states several rules
twice with different text, and that its header template and dependency table still assume
Apache-2.0. Every other repository is measured against these rules, so they are made single and
current before programmes 2 to 5 (licence, CLI, documentation and layout, code) touch anything else.

## Goal

After this work, each rule has one home, the checkers enforce what the skills say, the header
template carries the new licence, and this repository passes its own checkers.

## Owner decisions this spec rests on

All taken on 2026-10-05.

| # | Decision |
| --- | --- |
| D1 | Shared repositories move to PolyForm Noncommercial 1.0.0. Companies buy a commercial licence. |
| D2 | `sushiengine` and `sushiweb` are closed: all rights reserved. |
| D3 | `sushihub` and `sushicore` take the non-commercial licence too; the commercial agreement grants customers their use. |
| D4 | The single licensor and copyright holder is Sushi Systems. |
| D5 | Agent work lives in `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/` with `SPEC.md`, `PLAN.md`, `REPORT.md`. |
| D6 | There is no `docs/modules/`. A module's facts live in its own `README.md`. |
| D7 | The dispatch block lives in `claude/CLAUDE.md`: today's six lines plus the file-set line. |
| D8 | The licence header stays a boxed block, in the shape shown under "Header template". |

## Precondition

The working tree holds uncommitted rule changes that are already live on this machine through
symlinks: `README.md`, `claude/CLAUDE.md`, `docs/reference/CHANGELOG.md`,
`skills/sushiskills/SKILL.md` and the untracked `skills/storage-discipline/`. Met: the owner
approved and they were committed as they were on 2026-10-05 (`7fef7ae` after the history rebuild). The `claude:`
changelog entry for the delegation change is still owed and lands with the first task.

## Design

### 1. One home per rule

`claude/CLAUDE.md` is loaded into every session; a skill is loaded on demand. A rule stated in
both has already drifted four times (docs tree, placement order, changelog entry shape, dispatch
block). The split after this work:

| Rule | Home | The other file |
| --- | --- | --- |
| Documentation tree, placement, changelog shape | `skills/documentation/SKILL.md` | CLAUDE.md names the skill and keeps only the first-entry rule (measure, report, get approval) |
| Source comment rules | `skills/source-comments/SKILL.md` | CLAUDE.md names the skill |
| Dispatch block, model and effort per dispatch, report evidence rule | `claude/CLAUDE.md` | `multi-agent-work` cites CLAUDE.md and drops its own block and its model table |
| Planning: hierarchy first, inline or waves | `skills/multi-agent-work/SKILL.md` | CLAUDE.md names the skill |
| Language, quality, honesty | `claude/CLAUDE.md` | unchanged |

The owner left this choice to the engineer on 2026-10-05. CLAUDE.md sections that restate a
skill shrink to a citation plus the rules the skill lacks, because a second copy is what drifted.

### 2. Dispatch block

The block in CLAUDE.md gains one line, placed fourth, and the later lines move down:

```
4. Write only to the files listed below and to the work folder under docs/agent/.
```

The block is then seven lines. The evidence rule that reads "1, 2, 5 and 6" becomes
"1, 2, 6 and 7". `multi-agent-work` keeps roles, planning, report acceptance and the shared
working tree rules, and says where the block is.

### 3. Documentation skill and checker

- The tree in `documentation` is the one in D5 and D6; it already is. CLAUDE.md stops restating it.
- Placement keeps the skill's order and its 90-day archive rule, which `K_ARCHIVE_AFTER_DAYS` implements.
- `sushiskills/SKILL.md` gains the mapping for the vendored superpowers skills: a superpowers
  spec or plan is written as `SPEC.md` or `PLAN.md` in the work folder, never under
  `docs/superpowers/`.
- `check_docs_layout.py` gains two rules, one function and one table row each:
  `rule_required_entries` (the required documents exist; folders appear with content) and `rule_reachable_from_index`
  (every live document is linked from `docs/README.md`, directly or through an index it links).
- `tools/README.md` states the checkers' real coverage; its list of unbuilt checks moves to
  `docs/design/REMAINING_WORK.md`.

### 4. Header template

`source-comments` replaces the Apache block with three variants of one shape. The first line is
the file name, the second the project and its URL.

Non-commercial repositories:

```cpp
/****************************************************************/
/* graph.hpp                                                    */
/* SushiRuntime - https://github.com/SushiSystems/SushiRuntime  */
/* Copyright (c) 2026 Sushi Systems                             */
/* Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.    */
/* Commercial use requires a licence from Sushi Systems.        */
/****************************************************************/
```

Closed repositories (`sushiengine`, `sushiweb`) replace the two licence lines with:

```cpp
/* All rights reserved. No licence is granted.                  */
```

Python, shell and CMake files use the same lines with `#` and no box:

```python
# graph.py
# SushiRuntime - https://github.com/SushiSystems/SushiRuntime
# Copyright (c) 2026 Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
```

Rules that go with the block:

- The year is the year the file was first written and is never updated.
- The holder is `Sushi Systems` and nothing else. `@author` still names a person.
- A file ported from third-party code keeps the upstream copyright line and licence name inside
  the block, below the Sushi lines.
- `check_source_comments.py` gains `rule_license_block`: the file opens with the block, the
  first line is the file name, and the copyright and licence lines are present. The expected
  lines are `K_` constants at the top of the checker, the one per-repository setting the
  `project-tools` contract allows; a closed repository changes those constants and nothing else.

### 5. Dependencies skill

- The licence table gains a row: "Sushi Systems repositories, under their own licence: Accepted".
  The non-commercial row keeps rejecting third-party code.
- A new section, "Ported code": code translated or adapted from a third-party source keeps its
  upstream notice in the file header and in `NOTICE.md`; the owner cannot relicense that part.
- A new section, "Notices": `NOTICE.md` at the repository root lists every third-party
  component, ported file and redistributed binary with its licence and source.

### 6. Layout, CI and versioning skills

- `repository-layout`: the root list gains `NOTICE.md` and `COMMERCIAL.md`. A skills repository
  has `skills/` and `claude/` at its root in place of `modules/`; this is stated as a second
  root shape, not as an exception.
- `continuous-integration`: the push workflow is `ci.yml`, the name three repositories already
  use and no repository contradicts. A repository without a project CLI runs the checkers
  directly; this is the only allowed direct call.
- `versioning-and-release`: a repository without a build manifest takes its version from the
  latest `## vX.Y.Z` changelog heading, and the tag must match it.

### 7. This repository made to follow its own rules

- `LICENSE` becomes the unmodified PolyForm Noncommercial 1.0.0 text, fetched from
  polyformproject.org, followed by `Required Notice: Copyright (c) 2026 Sushi Systems`.
  `COMMERCIAL.md` says how a company obtains a licence. `README.md` says "source-available, free
  for non-commercial use" and never "open source".
- The 20 commits already on the public remote stay Apache-2.0. The changelog and README name
  the first version under the new licence. `third_party/superpowers` stays MIT.
- The six files under `tools/` take the new Python header.
- `skills/humanizer` and `skills/marketing-copy` are compared against the Wikipedia (CC BY-SA 4.0)
  and GOV.UK (OGL 3.0) sources they cite. Copied passages are rewritten; `NOTICE.md` credits the
  sources either way.
- The documentation skeleton is built: `docs/README.md`, `CONTRIBUTING.md`,
  `DOCUMENTATION_STYLE_GUIDE.md`, `getting_started/`, `reference/GLOSSARY.md`,
  `reference/KNOWN_ISSUES.md`, `design/README.md`, `design/REMAINING_WORK.md`. The install
  instructions move from the root README to `getting_started/`, which names one installation
  method. `skills/README.md` and `claude/README.md` take the facts about those folders.
- Root `AGENTS.md` and `CLAUDE.md` name the skills this repository follows.
- `.github/workflows/ci.yml` runs the four checkers on Windows and Linux.

## Not in this programme

- Any file outside `D:/Projects/sushiskills`. The sibling repositories copy the new `tools/` and
  rewrite their headers in programme 2, and move their agent documents in programme 4.
- The text of the commercial licence agreement. It is a legal document; `COMMERCIAL.md` only
  points at how to ask for one.
- Pushing. Every commit stays local until the owner pushes.

## Acceptance

1. `python tools/documentation/check_docs_layout.py`, `check_changelog.py`,
   `check_source_comments.py` and `python tools/layering/check_layering.py` exit 0 over this
   repository.
2. The dispatch block appears in exactly one tracked file outside `third_party/` and `docs/archive/`.
3. No tracked file outside `third_party/`, `docs/archive/` and `docs/agent/` contains "Apache",
   except the sentence that says earlier versions stay Apache-2.0.
4. `docs/README.md` reaches every live document, proven by `rule_reachable_from_index`.
5. The installed skills under `~/.claude/skills` still resolve, since they are symlinks into this tree.

## Open risk

PolyForm Noncommercial does not define "noncommercial", has no governing-law clause, and Turkish
law (FSEK art. 52) asks for written form on contracts over economic rights. A lawyer should
confirm the public licence and draft the commercial agreement before the first sale. This does
not block the repository work.
