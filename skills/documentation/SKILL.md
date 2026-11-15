---
name: documentation
description: Use when creating, editing, moving or archiving any file under docs/ or a module README in a repository, when adding, renaming or removing a public name, a signature, a header path, a CLI command or a behaviour a page may describe, when recording a spec, plan, report, design decision, backlog item or changelog entry, or when unsure where a written fact belongs.
---

# Documentation

Documentation is split by what it records, and each kind has exactly one home. A fact in two
places is a fact that will disagree with itself.

## The tree

Folders, required files and names under `docs/`: `references/tree.md`, read before
adding anything under `docs/`. `tools/documentation/check_docs_layout.py` enforces them.

## Placement

Ask in order, stop at the first yes.

1. Is it a fact about one module? → that module's `README.md`.
2. Was it written by an agent while doing a piece of work? → that work's folder in `docs/agent/`.
3. Is it work to be done, or a defect a reader can meet? → the backlog, through `backlog add`.
4. Is it intent with an open phase? → the topic that owns its module, `design owner <path>`:
   `docs/design/<TOPIC>/`, as a page or a phase. A new topic only through `design new`.
5. Is it about work that is finished? → nowhere: it is deleted when its decisions are in the topic;
   version history keeps it.
6. Otherwise → the manual: `getting_started/`, `architecture/`, `guides/` or `reference/`.

## The root README

The front page: each line answers a cold reader's question, everything else links into `docs/`.
Its sections and what stays off it: `references/root-readme.md`.

## Read before

| Task | File in this folder |
| --- | --- |
| Opening or extending a design document, opening or closing a work folder under `docs/agent/` | `AGENT_WORK.md` |
| Writing or reshaping a design document: its sections, status line and phase table | `DESIGN_FORMAT.md` |
| Writing a changelog entry or moving a release section | `CHANGELOG_FORMAT.md` |
| Reading, writing or closing an entry of the backlog in `docs/backlog/` | `BACKLOG_FORMAT.md` |
| A checker finding, a page over its ceiling, a source example, a `Describes:` line, a fact marker, the red flags | `references/manual.md` |
| What is left or next, what a module is meant to be or who owns it, a defect found, work finished, a decision made | The `backlog` and `design` skills: the answer comes from the repository's commands |

## Keeping the manual true

A manual page that stops being true is a defect in the change that made it false. The code,
its module README, the manual pages that describe it, its design status and its changelog line
land in one commit. Which pages form the manual: `references/manual.md`.

- A change that adds, renames or removes a public name, a signature, a header path, a CLI
  command or a behaviour a page describes searches the manual for the old name,
  `git grep -n <old name> -- '*.md'`, and corrects every hit in that commit.
- Architecture and guide pages are never a stage at the end of a plan.
- `tools/documentation/check_docs_truth.py` checks names, paths, examples and
  `docs/.docs_truth_allow`. A sentence about behaviour the code has lost is caught only by a reader.

### Editing is replacing

- The old paragraph is deleted, never kept beside the new one. Git keeps it.
- A page says what is, never what it used to be; `check_docs_truth.py` lists the refused words.
- When a section's subject is gone, the section goes, heading included.

### Size and one home

| Page | Ceiling |
| --- | --- |
| Root `README.md` | 120 lines |
| Manual page | 600 lines |
| Module README | 800 lines |
| Design document | 400 lines |

- One fact, one home: a repeated paragraph becomes one sentence and a link.
- A page is written for the reader who arrives cold: what the thing is, how to use it, then the
  detail.
- `check_docs_truth.py` enforces the ceilings, repeated passages, compiled and cited source
  examples and the em-dash ban; `references/manual.md` holds their detail.

## Pages follow what they describe

- A manual page names what it describes in a line of its first twelve lines:
  ``**Describes:** `src/a.py`, `lib` ``.
- A commit that changes a described file needs the page in the same commit, or a line in its message,
  last, that says why the page stays: `Docs: <page> unchanged (<reason>)`.
- `tools/documentation/check_docs_follow.py` and the `commit-msg` hook enforce it.

## Facts with one home

A fact that more than one page needs has one home and a stable id. A link comes before a quote; a
fact earns a home when two pages must say the same thing.

- The home wraps the text in `<!-- fact:begin ID -->` and `<!-- fact:end ID -->`.
- A verbatim quote sits between `<!-- quote:begin ID -->` and `<!-- quote:end ID -->`, filled by
  `facts_cli.py apply`.
- A paraphrase carries `<!-- follows: ID -->` beside it. A commit that changes the fact needs each
  page that follows it, or a `Docs:` line for it.
- `tools/documentation/check_docs_facts.py` enforces the markers.
