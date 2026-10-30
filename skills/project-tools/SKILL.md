---
name: project-tools
description: Use when adding a repository's tools/ folder, writing or changing a checker, running a manual audit of comments, layering, documentation layout or changelog, or before reporting work as finished, in a repository.
---

# Project Tools

**Describes:** `tools/check_all.py`

Every repository carries the same checkers under the same names, so one command audits any
repository. They are run by hand or through the project's CLI; they never build anything.

## The set

| Checker | Enforces |
| --- | --- |
| `tools/documentation/check_source_comments.py` | Every rule in `source-comments` |
| `tools/documentation/check_docs_layout.py` | The tree, required documents, names, work folder contents, status lines, broken links and anchors, reachability from the index, closed work past its grace and the forbidden kinds of file from `documentation` |
| `tools/documentation/check_changelog.py` | One line, 240 characters, one sentence, no nesting |
| `tools/documentation/check_backlog.py` | `BACKLOG_FORMAT.md` in `documentation`, through the backlog tool's `backlog check`: the store's shape, values, IDs, paths, references, pins, the index, and a backlog entry for every open design topic |
| `tools/documentation/check_design_format.py` | `DESIGN_FORMAT.md` in `documentation`, through the design tool's `design check`: the five sections in order, the status length, the phase table and its states, no commit hash, no dated record of work |
| `tools/documentation/check_design_topics.py` | `DESIGN_FORMAT.md` and `AGENT_WORK.md` in `documentation`: through the design tool's `design check`, the `Modules` line on every topic, the modules exist, each module owned by one topic, no loose document, and the topics and phases a work folder names exist; then the generated views and the opt-in rules for a glossary entry per topic and the folder ceiling |
| `tools/documentation/check_module_install.py` | `module-install`: the elements of a module, both install headings, no machine path, no workspace tool in code |
| `tools/documentation/check_docs_truth.py` | The manual against the source, from `documentation`: every name and path a page writes in code exists, every example cites the file it is taken from, no history words, the page ceilings, no paragraph in two pages, no em dash in prose, a reason on every allow-list entry |
| `tools/layering/check_layering.py` | Module dependencies follow the declared tier order; nothing reaches into another module's private `source/` |
| `tools/testing/check_test_mirror.py` | `tests/` mirrors the public headers, from `repository-layout` |
| `tools/testing/check_test_sizes.py` | Every test writes its size in its source, from `testing` |
| `tools/testing/check_probes.py` | Probes and scenario benchmarks live in `applications/probes/` and `applications/benchmarks/`, use no test framework, stay out of the test runner, carry a name of their own and are listed, from `testing` and `performance` |
| `tools/logs/check_logging.py` | Log calls carry their module's category, library code writes no console output and hides no failure, from `logging` |
| `tools/commits/check_backlog_trailer.py` | The `Backlog:` line of `commits`: each commit after `K_TRAILER_SINCE` names an entry open in its parent or in itself, or says `none (<reason>)` |
| `tools/documentation/check_docs_follow.py` | "Pages follow what they describe" in `documentation`: each commit after `K_DOCS_FOLLOW_SINCE` updates the pages that describe what it changes, or says why not with a `Docs:` line |
| `tools/layering/check_agnostic.py` | The folders `K_AGNOSTIC_PATHS` names hold no product, company tool, identity, machine path or technology name that the terms file lists; it checks nothing in a repository that names no folder |
| `tools/ci/check_workflows.py` | The workflow files GitHub would refuse before a job starts, from `continuous-integration` |

A repository may add checkers; it may not rename or drop these twelve. `tools/check_all.py` runs
all of them and the checker tests, and prints only what failed; it also runs every other
`tools/<area>/check_<what>.py` a repository holds as its own. A checker never reads a file git
ignores.

One tool beside them writes: `tools/licensing/write_license_block.py` puts the license block of
`source-comments` into every tracked source file. It is run when a repository is created, when
its licence changes, and with `--report` to prove the blocks are in place.

## Contract

Every checker has the same shape.

| Aspect | Rule |
| --- | --- |
| Language | Python 3.11, standard library only |
| Entry | `python tools/<area>/check_<what>.py [paths...]` |
| Default run | One line per finding, `path:line: rule_name: message`; exit 1 if any finding |
| `--report` | Counts per rule; exit 0 |
| `--rule NAME` | Runs one rule only |
| Rules | One function per rule, `rule_<what>`, registered in one table |
| Configuration | `K_` constants at the top of the file. What differs between repositories is read from `tools/settings.py`; no other configuration file, except the allow-list `docs/.docs_truth_allow` that `check_docs_truth.py` reads |
| Side effects | None. A checker reads; it never rewrites a file |

```python
def rule_block_ceiling(lines: list[str]) -> Iterator[Finding]:
    """Yields a finding for each comment block longer than eight lines."""
```

Adding a rule adds one function and one table row. Nothing else in the checker changes.

## Shared and own tools

The files git tracks under SushiSkills' `tools/` are shared. A repository holds them as
SushiSkills ships them, under its own license block, and never edits them. A shared checker that
needs to change is changed in SushiSkills first.

- `tools/settings.py` is shared by name only. It holds what differs between repositories, such
  as the tier order, and the copy never overwrites it. `tools/README.md` is kept the same way:
  it lists the repository's own tools beside the shared ones, which "The set" above names.
- Every other file under a repository's `tools/` is its own tool, at any path SushiSkills does
  not use. The copy never touches it.

`python tools/checking/copy_shared_tools.py ROOT --from <the sushiskills checkout>` copies the shared files;
with `--report` it lists the ones that differ and exits 1. It is run from the SushiSkills
checkout, never from a repository's copy, so a fix to the copier applies on the run that brings
it. A repository runs it after a checker changes upstream. A shared file whose text no upstream version
ever held is a local edit: the copy refuses, writes nothing and names the file, and `--force`
overwrites it. Move the edit upstream first, or drop it.

## Hooks

`tools/hooks/` is tracked, and `python tools/hooks/install_hooks.py` points git at it once per clone.
`pre-commit` runs `tools/check_all.py`, and `commit-msg` runs `tools/hooks/commit_msg.py`, which
refuses a message without the `Backlog:` line of `commits`. A hook is never skipped.

## When to run

| Moment | Run |
| --- | --- |
| Before reporting a task finished | `python tools/check_all.py .` |
| Before a commit touching `docs/` | `check_docs_layout.py`, `check_changelog.py` and `check_docs_truth.py` |
| Before a commit that adds, renames or removes a public name, a header path or a CLI command | `check_docs_truth.py` |
| Periodically, or on request | All ten with `--report`; delete the closed work it lists |
| Before a backlog migration, and on request | The backlog fact check below |
| Asking what is left, what is next or what is designed | The repository's `backlog` and `design` commands, never a file or the git log (`backlog`, `design`) |
| Before every commit | `python tools/check_all.py .`, which the commit hook runs; the commit message ends with a `Backlog:` line (`commits`) |

A claim that a checker passed carries the command and its pasted output.

## Backlog fact check

`check_backlog.py` sees the shape of an entry, not whether it is still true. The fact check
reads every entry of `docs/backlog/`, with its detail file, and every design document whose
status is `Open`:

1. Read the code and the files the entry names.
2. Search `git log` since the entry's last change for a commit that closed it.
3. Give one verdict: true, stale (true in part; say which part), closed, or foreign (closed by a
   commit in another repository; name it).

The verdicts go in the `REPORT.md` of the work folder that ran the check. Deleting or moving
an entry, and a design document's new status, are the owner's decisions.
