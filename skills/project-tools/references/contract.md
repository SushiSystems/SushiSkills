# Project tools: the set, sharing, hooks and schedule

Detail for the sections that `../SKILL.md` states as rules. `SKILL.md` holds the rules; read this
when setting up, syncing or running the tools.

## The set

- `tools/documentation/`: `check_source_comments.py`, `check_docs_layout.py`,
  `check_changelog.py`, `check_backlog.py`, `check_design_format.py`, `check_design_topics.py`,
  `check_module_install.py`, `check_docs_truth.py`, `check_docs_facts.py`, `check_docs_follow.py`
- `tools/layering/`: `check_layering.py`, `check_agnostic.py`
- `tools/testing/`: `check_test_mirror.py`, `check_test_sizes.py`, `check_test_value.py`,
  `check_test_odr.py`, `check_probes.py`
- `tools/logs/check_logging.py`, `tools/commits/check_backlog_trailer.py`,
  `tools/ci/check_workflows.py`

Read `checkers.md` for what each checker enforces and which skill holds the rule.

`tools/check_all.py` runs the set and the checker tests side by side, in the order listed above.
`write_license_block.py` is run when a repository is created, when its licence changes, and with
`--report` to prove the blocks are in place.

## Contract details

- Entry: `python tools/<area>/check_<what>.py [paths...]`.
- Configuration has two exceptions to the `K_` constants and `tools/settings.py` rule:
  `docs/.docs_truth_allow` for `check_docs_truth.py` and the known-findings baseline for
  `check_all.py`.

## Shared and own tools

The files the shared tooling library's `tools/` holds at a release tag are shared, each under the
repository's own license block.

- `tools/settings.py` and `tools/README.md` are shared by name only: they hold what differs
  between repositories and list its own tools, and the copy never overwrites them.
- Every other file under a repository's `tools/` is its own tool, at any path the library does
  not use. The copy never touches it.

The library's sync command copies the shared files from the tag the repository pins and writes a
lock file with a hash per file. Read `checkers.md` before running it.

## Hooks

`python tools/hooks/install_hooks.py` points git at the tracked `tools/hooks/`. `pre-commit` runs
`tools/check_all.py --skip-history` on the files the commit will hold, written from the index to a
throwaway folder, so a session's unfinished file cannot refuse another's commit; CI runs the
checkers that read every commit. `commit-msg` runs `tools/hooks/commit_msg.py`, which enforces the
`Backlog:` line of `commits`.

## Known findings

The file `known_findings.toml` sits beside `settings.py`, and the copy never touches it. Read
`checkers.md` for what fails and how the list is written.

## When to run

| Moment | Run |
| --- | --- |
| Periodically, or on request | All ten with `--report`; delete the closed work it lists |
| Before a backlog migration, and on request | The backlog fact check, `fact-check.md` |

The `Backlog:` line of a commit message is in `commits`.
