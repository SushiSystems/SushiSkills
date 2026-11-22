---
name: commits
description: Use when writing a git commit message, a pull request title or description, or staging changes in a repository.
---

# Commits

A commit history is read as a changelog of intent. Examples, hook detail: `references/detail.md`.

## Subject line

`type(scope): sentence` in lower case, present tense, no trailing period, a full clause under 72
characters. `type(scope)!:` marks a break of a public interface, file format or CLI; without
the `!` a MAJOR bump hides (`versioning-and-release`).

Types: `feat` new behaviour; `fix` wrong behaviour made right; `refactor` same behaviour,
different shape; `perf` fewer resources; `test` tests only; `docs` documentation only; `build`
build files, CLI, checkers, toolchain; `chore` releases (`chore(release): v0.3.2`) and
housekeeping.

- `scope` is the module or subsystem folder name. The one other scope is `deps`:
  `build(deps): upgrade <name> to <version>`, in its own commit.
- A change that needs two scopes is usually two commits.
- The body is optional: paragraphs at 72 columns, the `humanizer` pass.

## One commit holds

One logical change, its tests, and its documentation (module README, design status, changelog
line). A change without them is not finished (`documentation`).

## The backlog line

Every commit ends with one line, last in the message, naming the entry it serves.

<!-- fact:begin backlog-line -->
```
Backlog: RW-123
Backlog: RW-123, KI-4
Backlog: SushiSkills RW-38
Backlog: none (typo in a comment)
```
<!-- fact:end backlog-line -->

- The ID is an entry open in the parent commit or in this one, so the commit that closes an
  entry still names it. An amend is judged against the parent of the commit it replaces.
- A sibling's entry is `<repository> <ID>`, the repository being its folder name.
- `none` carries a reason in brackets; no words is a refusal. A release closes no entry and says
  so. A plan's job is no reason: it serves the work folder's entry.
- Never skip a hook with `--no-verify`. A repository runs `python tools/hooks/install_hooks.py`
  once per clone.
- A commit that changes what a page describes carries the pages, or a `Docs: <page> unchanged
  (<reason>)` line after the `Backlog:` line.
- A `fix` or `feat` commit stages a test, or carries `Tests: none (<reason>)`.

## Staging

Follows `git-workflow`, section "Shared working tree".
