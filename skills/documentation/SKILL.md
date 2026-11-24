---
name: documentation
description: Use when creating, editing, moving or archiving any file under docs/ or a module README in a repository, when adding, renaming or removing a public name, a signature, a header path, a CLI command or a behaviour a page may describe, when recording a spec, plan, report, design decision, backlog item or changelog entry, or when unsure where a written fact belongs.
---

# Documentation

One location per kind of fact. Read `references/tree.md` before adding to `docs/`; `references/root-readme.md` for the root README.

## Placement

Use the first item that applies.

1. One module's fact: its `README.md`.
2. Written by an agent in a piece of work: its folder in `docs/agent/`.
3. Work to do or a reader-visible defect: `backlog add`.
4. Intent with an open phase: the topic of `design owner <path>`; a new topic only by `design new`.
5. Finished work: nowhere; delete it once its decisions are in the topic.
6. Otherwise the manual: `getting_started/`, `architecture/`, `guides/`, `reference/`.

Formats: `DESIGN_FORMAT.md`, `AGENT_WORK.md`, `CHANGELOG_FORMAT.md`, `BACKLOG_FORMAT.md`. Findings, markers, excuses: `references/manual.md`.

## Keeping the manual true

A false page is a defect of the change that made it false: code, pages, design status and changelog go in one commit.

- A changed public name, signature, header path, command or behaviour: `git grep -n <old name> -- '*.md'`, fix every hit in that commit.
- `check_docs_truth.py` checks names, paths, examples.
- Edit by replacing: delete the old paragraph, say what is, never what was, drop a section whose subject is gone.

## Size and one location

| Page | Maximum |
| --- | --- |
| Root `README.md` | 120 lines |
| Manual page | 600 lines |
| Module README | 800 lines |
| Design document | 400 lines |

A repeated paragraph is a sentence and a link.

## Pages follow what they describe

A manual page names what it describes within its first twelve lines: ``**Describes:** `src/a.py` ``. A commit changing a described file updates the page or ends with `Docs: <page> unchanged (<reason>)`; `check_docs_follow.py` enforces it.

## Facts with one location

A fact two pages state has one location and an id; link before quoting. Location: `<!-- fact:begin ID -->` to `<!-- fact:end ID -->`. Quote: `quote:begin/end ID`, filled by `facts_cli.py apply`. Paraphrase: `<!-- follows: ID -->`. A commit changing a fact needs each following page or a `Docs:` line; `check_docs_facts.py` checks it.
