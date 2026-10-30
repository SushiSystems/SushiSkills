---
name: commits
description: Use when writing a git commit message, a pull request title or description, or staging changes in a repository.
---

# Commits

A commit history is read as a changelog of intent. Every subject line follows one grammar.

## Subject line

```
type(scope): sentence in lower case, present tense, no trailing period
type(scope)!: the same, for a change that breaks a public interface, file format or CLI
```

| Type | For |
| --- | --- |
| `feat` | New behaviour |
| `fix` | Wrong behaviour made right |
| `refactor` | Same behaviour, different shape |
| `perf` | Same behaviour, fewer resources |
| `test` | Tests only |
| `docs` | Documentation only |
| `build` | Build files, CLI, checkers, toolchain |
| `chore` | Releases (`chore(release): v0.3.2`), housekeeping with no behaviour |

- `scope` is the module or subsystem folder name: `matter`, `interop`, `cli`, `layering`. The
  one scope that is not a folder is `deps`: `build(deps): upgrade <name> to <version>` upgrades
  a dependency, in its own commit.
- The sentence says what the change does, as a full clause, under 72 characters:
  `feat(matter): reserve the neighbour list at tick start`.
- A change that needs two scopes is usually two commits.
- The type decides the next version: see `versioning-and-release`. A breaking change without
  `!` hides a MAJOR bump.

## Body

Optional. Plain paragraphs wrapped at 72 columns: what changed and what it affects. The reason
for a design lives in a design document; the body may cite its path. Run the `humanizer` pass.

## What goes in one commit

1. One logical change.
2. Its tests.
3. Its documentation: module README, design status, changelog line. A change without them is
   not finished (see `documentation`).

## The backlog line

Every commit ends with one line, last in the message, that says which backlog entry it serves.

```
Backlog: RW-123
Backlog: RW-123, KI-4
Backlog: none (typo in a comment)
```

- An ID must be an entry open in the parent commit or in this commit, so the commit that closes an
  entry still names it (`backlog`).
- `none` carries its reason in brackets. A reason of no words is a refusal.
- `tools/commits/check_backlog_trailer.py` checks the commits after `K_TRAILER_SINCE` in
  `tools/settings.py`, and the `commit-msg` hook in `tools/hooks/` refuses a message that breaks
  the rule before the commit exists. A repository runs `python tools/hooks/install_hooks.py` once
  per clone; its setup command does it for the person.
- A hook is never skipped with `--no-verify`.

## Staging

Staging follows `git-workflow`, section "Shared working tree".

## Examples

| Bad | Good |
| --- | --- |
| `Fixed stuff` | `fix(audio): stop the mixer clipping at unity gain` |
| `feat: Added new feature for water.` | `feat(water): sample the sea surface on the device` |
| `update README` | `docs(ecs): list the world's public entry points` |
