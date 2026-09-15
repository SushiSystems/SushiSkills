---
name: documentation
description: Use when creating, editing, moving or archiving any file under docs/ or a module README in a Sushi Systems repository, when recording a spec, plan, report, design decision, backlog item or changelog entry, or when unsure where a written fact belongs.
---

# Documentation

Documentation is split by what it records, and each kind has exactly one home. A fact in two
places is a fact that will disagree with itself. The failure this skill prevents is the soup:
many agents, each writing correct files in slightly different places, until nobody can find
the current truth.

## The tree

```
docs/
    README.md                     manual index; every document reachable from here
    CONTRIBUTING.md               what must be documented, how a change lands
    DOCUMENTATION_STYLE_GUIDE.md
    CLAUDE.md  AGENTS.md          the agent entry point (root files only point here)
    getting_started/  architecture/  guides/
    reference/
        CHANGELOG.md  GLOSSARY.md  KNOWN_ISSUES.md
    design/
        README.md                 topic -> design document map
        REMAINING_WORK.md         the single backlog
        <TOPIC>.md                live intent, each with a status line
    agent/
        <YYYY_MM_DD>_<WORK_NAME>/ one folder per piece of agent work
            SPEC.md  PLAN.md  REPORT.md
    archive/                      frozen; added to, never edited
<module>/README.md                the module's own facts, beside the code
```

No other folder under `docs/`. No other file names inside a work folder.

## Placement

Ask in order, stop at the first yes.

1. Is it a fact about one module? → that module's `README.md`.
2. Was it written by an agent while doing a piece of work? → that work's folder in `docs/agent/`.
3. Is it intent with an open phase? → `docs/design/<TOPIC>.md`.
4. Is it about work that is finished and untouched for 90 days? → `docs/archive/`.
5. Otherwise → the manual: `getting_started/`, `architecture/`, `guides/` or `reference/`.

## One topic, one design document

- `docs/design/README.md` maps every topic to exactly one document. Before writing, look the
  topic up there. If a document exists, extend it; never open a second one on the same topic.
- Every design document's second line is its status:
  `**Status:** Open — phase 2 of 4` or `**Status:** Shipped`.
- A design document above 1 500 lines is split into `<TOPIC>/` with a `README.md` and one file
  per phase, and the map is updated in the same commit.
- `REMAINING_WORK.md` is the only backlog. No TODO lists anywhere else.

## Agent work lifecycle

1. **Open.** One folder: `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/`. Before opening, check that no
   open folder already covers the work; if one does, continue it.
2. **Work.** The folder holds at most `SPEC.md`, `PLAN.md` and `REPORT.md`. Each is rewritten
   in place as the work moves. A second review round replaces the first `REPORT.md`; it is not
   a new file.
3. **Close.** The orchestrator, in one commit: writes the changelog line, updates the design
   status and `REMAINING_WORK.md`, updates the module READMEs and manual pages the work made
   false.
4. **Archive.** A work folder or a shipped design document with no commit for 90 days moves to
   `docs/archive/` as it is, keeping its path below `docs/`. `check_docs_layout.py` lists the
   candidates.

The manual is never archived; it is kept true.

## Who writes where

| Writer | May write |
| --- | --- |
| Agent doing one piece of work | Its own work folder; the README of a module it changed |
| Orchestrator (the session that dispatched the work) | Everything above, plus `design/`, the manual, `CHANGELOG.md`, `REMAINING_WORK.md` |
| Anyone | Nothing in `archive/` except moving a folder in |

## Changelog

One file, `docs/reference/CHANGELOG.md`, grouped by release, newest first.

```
# Changelog

## Unreleased

- 2026-09-15 — matter: Reserved the neighbour list at tick start (`neighbour_list.hpp`).
- 2026-09-14 — interop: Logged every refused share (`interop_share.cpp`, `ShareGate`).

## 0.3.0 — 2026-09-01

- 2026-08-28 — render: Fixed the star field's exposure (`star.vert`, `StarPass`).
```

| Part | Rule |
| --- | --- |
| Headings | `## Unreleased` on top, then `## <version> — <YYYY-MM-DD>` per release |
| Entry | `- <YYYY-MM-DD> — <scope>: <Past-tense verb> <what changed> (<where>).` |
| Scope | The commit scope, so one module's history is one search |
| Where | At most five backticked files or symbols |
| Order | Newest first inside each section |
| Length | At most 240 characters, one sentence, no nested bullet, never why |

A change that needs more than five places is more than one entry.

**Release.** When a version ships, `## Unreleased` is renamed to `## <version> — <date>` and a new
empty `## Unreleased` opens above it. The live file keeps `Unreleased` and the latest release;
every older release section moves, unchanged, to `docs/archive/changelog/<version>.md`.

## Names

- Files: `UPPER_SNAKE_CASE.md`. Work folders: `YYYY_MM_DD_UPPER_SNAKE_CASE`.
- Every link and cited path resolves. Example paths are in code spans, never live links.

## Same commit

A manual page that stops being true is a defect in the change that made it false. The code,
its module README, its design status and its changelog line land in one commit.

## Red flags

- "I will write a quick note in a new file so the next agent sees it." → the work folder.
- "This review deserves its own file." → replace `REPORT.md`.
- "This topic is slightly different from the existing design document." → extend it.
- "I will update the changelog at the end of the week." → it is part of the commit.
