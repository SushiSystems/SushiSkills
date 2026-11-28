---
name: project-tools
description: Use when adding a repository's tools/ folder, writing or changing a checker, running a manual audit of comments, layering, documentation layout or changelog, or before reporting work as finished, in a repository.
---

# Project Tools

**Describes:** the shared check command and a repository's `tools/`

Every repository runs the same checkers under the same names; they read, never build or
rewrite. They ship in the shared tooling library's package and run from it, at the release the
repository requires; no repository holds a copy. The set and what each enforces:
[checkers](references/checkers.md). Contract, hooks, known findings, fact check in full:
[contract](references/contract.md). A skill's `tools/<area>/<name>.py` names a module of the library's
`tools` package, run as `python -m <library>.tools.<area>.<name>`.

- The library's check command runs the set, then each `tools/<area>/check_<what>.py` the
  repository owns and the checker tests, and prints only failures. A repository may add
  checkers, never rename or drop the set. A checker never reads a git-ignored file.
- Contract: Python 3.11, standard library only; `path:line: rule_name: message`, exit 1 on a
  finding; `--report` counts, exit 0; `--rule NAME`; one `rule_<what>` function and one table
  row per rule; settings only as `K_` constants or in `tools/settings.py`; no side effects.
- The library's `write_license_block` writes the license block of `source-comments`.
- A shared checker changes in the library and reaches a repository with the library's release;
  none is copied into `tools/`. `tools/` holds the repository's `settings.py`, `README.md`,
  `known_findings.toml`, hooks and own tools.
- Install the hooks once per clone with the library's `install-hooks` command. A hook is never
  skipped.
- `known_findings.toml` allows a count of one rule of one checker in one file, naming an open
  backlog entry. Its counts only decrease; nobody raises one by hand; a failing test is never
  listed.
- Run the check command on the repository root before reporting finished and before every
  commit. Before a commit touching `docs/`: `check_docs_layout`, `check_changelog`,
  `check_docs_truth`. After a public name, header path or CLI command changes: `check_docs_truth`.
- A claim that a checker passed carries the command and its pasted output.
- Read `references/fact-check.md` before a backlog fact check. Deleting or moving an entry and a
  design document's new status are the owner's decisions.
- What is left or designed is read with the `backlog` and `design` commands.
