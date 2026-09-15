---
name: project-tools
description: Use when adding a repository's tools/ folder, writing or changing a checker, running a manual audit of comments, layering, documentation layout or changelog, or before reporting work as finished, in a Sushi Systems repository.
---

# Project Tools

Every repository carries the same checkers under the same names, so one command audits any
repository. They are run by hand or through the project's CLI; they never build anything.

## The set

| Checker | Enforces |
| --- | --- |
| `tools/documentation/check_source_comments.py` | Every rule in `source-comments` |
| `tools/documentation/check_docs_layout.py` | The tree, names, work folder contents, status lines, broken links and 90-day archive candidates from `documentation` |
| `tools/documentation/check_changelog.py` | One line, 240 characters, one sentence, no nesting |
| `tools/layering/check_layering.py` | Module dependencies follow the declared tier order; nothing reaches into another module's private `source/` |

A repository may add checkers; it may not rename or drop these four.

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
| Configuration | `K_` constants at the top of the file; no configuration files |
| Side effects | None. A checker reads; it never rewrites a file |

```python
def rule_block_ceiling(lines: list[str]) -> Iterator[Finding]:
    """Yields a finding for each comment block longer than eight lines."""
```

Adding a rule adds one function and one table row. Nothing else in the checker changes.

## When to run

| Moment | Run |
| --- | --- |
| Before reporting a task finished | The checkers covering the files touched |
| Before a commit touching `docs/` | `check_docs_layout.py` and `check_changelog.py` |
| Periodically, or on request | All four with `--report`; act on the archive candidates |

A claim that a checker passed carries the command and its pasted output.
