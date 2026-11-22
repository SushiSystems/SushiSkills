# Project tools: contract, sharing, hooks and schedule

Full text of the sections that `../SKILL.md` states in brief. `SKILL.md` holds the rules; read this
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

A repository may add checkers; it may not rename or drop these. `tools/check_all.py` runs
all of them and the checker tests side by side, and prints only what failed, in the order they
are listed; it also runs every other `tools/<area>/check_<what>.py` a repository holds as its
own. A checker never reads a file git ignores.

One tool beside them writes: `tools/licensing/write_license_block.py` puts the license block of
`source-comments` into every tracked source file. It is run when a repository is created, when
its licence changes, and with `--report` to prove the blocks are in place.

## Contract

| Aspect | Rule |
| --- | --- |
| Language | Python 3.11, standard library only |
| Entry | `python tools/<area>/check_<what>.py [paths...]` |
| Default run | One line per finding, `path:line: rule_name: message`; exit 1 if any finding |
| `--report` | Counts per rule; exit 0 |
| `--rule NAME` | Runs one rule only |
| Rules | One function per rule, `rule_<what>`, registered in one table; adding a rule adds one function and one row |
| Configuration | `K_` constants at the top of the file; what differs between repositories comes from `tools/settings.py`. No other configuration file, except `docs/.docs_truth_allow` for `check_docs_truth.py` and the "Known findings" baseline for `check_all.py` |
| Side effects | None. A checker reads; it never rewrites a file |

## Shared and own tools

The files the shared tooling library's `tools/` holds at a release tag are shared. A repository
holds them as that tag holds them, every source file under the repository's own license block,
and never edits them. A shared checker that needs to change is changed in the library first.

- `tools/settings.py` and `tools/README.md` are shared by name only: they hold what differs
  between repositories and list its own tools, and the copy never overwrites them.
- Every other file under a repository's `tools/` is its own tool, at any path the library does
  not use. The copy never touches it.

The library's sync command copies the shared files from the tag the repository pins and writes a
lock file with a hash per file; `check_all.py` fails when a file differs from its lock. The sync
refuses a local edit unless given `--force` and never deletes a file dropped upstream; read
`checkers.md` before running it.

## Hooks

`tools/hooks/` is tracked, and `python tools/hooks/install_hooks.py` points git at it once per
clone. `pre-commit` runs `tools/check_all.py --skip-history` on the files the commit will hold,
written from the index to a throwaway folder, so a session's unfinished file cannot refuse
another's commit; CI runs the checkers that read every commit. `commit-msg` runs
`tools/hooks/commit_msg.py`, which enforces the `Backlog:` line of `commits`. A hook is never
skipped.

## Known findings

Findings a repository had before the shared tools arrived go in its own `known_findings.toml`
beside `settings.py`, which the copy never touches. Each entry allows a count of findings of one
rule of one checker in one file, and names an open backlog entry. The list only shrinks:
`check_all.py` fails anything it does not match exactly, and nobody grows it by hand. A failing
test is never listed. Read `checkers.md` for what fails and how the list is written.

## When to run

| Moment | Run |
| --- | --- |
| Before reporting a task finished, and before every commit (the hook runs it) | `python tools/check_all.py .` |
| Before a commit touching `docs/` | `check_docs_layout.py`, `check_changelog.py` and `check_docs_truth.py` |
| Before a commit that adds, renames or removes a public name, a header path or a CLI command | `check_docs_truth.py` |
| Periodically, or on request | All ten with `--report`; delete the closed work it lists |
| Before a backlog migration, and on request | The backlog fact check below |

What is left, next or designed is read with the `backlog` and `design` skills' commands; the
commit message's `Backlog:` line is in `commits`.

A claim that a checker passed carries the command and its pasted output.

## Backlog fact check

`check_backlog.py` sees an entry's shape, not whether it is still true. The fact check gives
every entry and every `Open` design document a verdict against the code and the history; read
`fact-check.md` before running it. Deleting or moving an entry, and a design
document's new status, are the owner's decisions.
