---
name: project-tools
description: Use when adding a repository's tools/ folder, writing or changing a checker, running a manual audit of comments, layering, documentation layout or changelog, or before reporting work as finished, in a repository.
---

# Project Tools

**Describes:** `tools/check_all.py`

Every repository carries the same checkers under the same names; they read, never build or
rewrite. The set and what each enforces: [checkers](references/checkers.md), read
before running the sync. Contract, sharing, hooks, known findings, fact check in full:
[contract](references/contract.md).

- A repository may add checkers, never rename or drop the set. `check_all.py` runs all of them,
  every other `tools/<area>/check_<what>.py` and the checker tests, and prints only failures. A
  checker never reads a git-ignored file.
- Contract: Python 3.11, standard library only; `path:line: rule_name: message`, exit 1 on a
  finding; `--report` counts, exit 0; `--rule NAME`; one `rule_<what>` function and one table
  row per rule; settings only as `K_` constants or in `tools/settings.py`; no side effects.
- `tools/licensing/write_license_block.py` writes the license block of `source-comments`.
- Shared files, as the pinned library tag holds them, are never edited; change the library
  first. `tools/settings.py` and `tools/README.md` are the repository's. A file differing from
  its lock fails `check_all.py`.
- Run `python tools/hooks/install_hooks.py` once per clone. A hook is never skipped.
- `known_findings.toml` allows a count of one rule of one checker in one file, naming an open
  backlog entry. Its counts only decrease; nobody raises one by hand; a failing test is never
  listed.
- Run `python tools/check_all.py .` before reporting finished and before every commit. Before a
  commit touching `docs/`: `check_docs_layout.py`, `check_changelog.py`, `check_docs_truth.py`.
  After a public name, header path or CLI command changes: `check_docs_truth.py`.
- A claim that a checker passed carries the command and its pasted output.
- Read `references/fact-check.md` before a backlog fact check. Deleting or moving an entry and a
  design document's new status are the owner's decisions.
- What is left or designed is read with the `backlog` and `design` commands.
