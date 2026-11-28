# Project tools: the set, sharing, hooks and schedule

Detail for the sections that `../SKILL.md` states as rules. `SKILL.md` holds the rules; read this
when setting up or running the tools.

## The set

The set ships in the shared tooling library's package, under these areas:

- `documentation/`: `check_source_comments.py`, `check_docs_layout.py`,
  `check_changelog.py`, `check_backlog.py`, `check_design_format.py`, `check_design_topics.py`,
  `check_module_install.py`, `check_docs_truth.py`, `check_docs_facts.py`, `check_docs_follow.py`
- `layering/`: `check_layering.py`, `check_agnostic.py`
- `testing/`: `check_test_mirror.py`, `check_test_sizes.py`, `check_test_value.py`,
  `check_test_odr.py`, `check_probes.py`
- `logs/check_logging.py`, `commits/check_backlog_trailer.py`, `ci/check_workflows.py`

Read `checkers.md` for what each checker enforces and which skill holds the rule.

The library's check command runs the set and the checker tests, in the order listed above.
`write_license_block.py` is run when a repository is created, when its licence changes, and with
`--report` to prove the blocks are in place.

## Contract details

- Entry: a shared checker runs as a module of the library package, `[paths...]`; a repository's
  own one as `python tools/<area>/check_<what>.py [paths...]`.
- Configuration has two exceptions to the `K_` constants and `tools/settings.py` rule:
  `docs/.docs_truth_allow` for `check_docs_truth.py` and the known-findings baseline for
  the check command.

## Shared and own tools

The shared checkers live only in the library package and run at the release the repository
requires; a fix reaches every repository with that release, and no file under `tools/` copies one.
A repository's `tools/` holds what differs between repositories: `settings.py`, `README.md`, which
lists its own tools, `known_findings.toml`, the hooks, and its own checkers at any path.

## Hooks

The library's `install-hooks` command points git at the tracked `tools/hooks/`. `pre-commit` runs
the check command with `--skip-history` on the files the commit will hold, written from the index to a
temporary folder, so a session's unfinished file cannot refuse another's commit; CI runs the
checkers that read every commit. `commit-msg` runs the library's commit-message hook, which enforces the
`Backlog:` line of `commits` and the touched-entry and three-entry rules of `backlog`.

## Known findings

The file `known_findings.toml` is beside `settings.py`; only the repository changes it. Read
`checkers.md` for what fails and how the list is written.

## When to run

| Moment | Run |
| --- | --- |
| Periodically, or on request | All ten with `--report`; delete the closed work it lists |
| Before a backlog migration, and on request | The backlog fact check, `fact-check.md` |

The `Backlog:` line of a commit message is in `commits`.
