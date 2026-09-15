---
name: commits
description: Use when writing a git commit message, a pull request title or description, or staging changes in a Sushi Systems repository.
---

# Commits

A commit history is read as a changelog of intent. Every subject line follows one grammar.

## Subject line

```
type(scope): sentence in lower case, present tense, no trailing period
```

| Type | For |
| --- | --- |
| `feat` | New behaviour |
| `fix` | Wrong behaviour made right |
| `refactor` | Same behaviour, different shape |
| `perf` | Same behaviour, fewer resources |
| `test` | Tests only |
| `docs` | Documentation only |
| `build` | CMake, CLI, checkers, toolchain |
| `chore` | Release bumps, housekeeping with no behaviour |

- `scope` is the module or subsystem folder name: `matter`, `interop`, `cli`, `layering`.
- The sentence says what the change does, as a full clause, under 72 characters:
  `feat(matter): reserve the neighbour list at tick start`.
- A change that needs two scopes is usually two commits.

## Body

Optional. Plain paragraphs wrapped at 72 columns: what changed and what it affects. The reason
for a design lives in a design document; the body may cite its path. Run the `humanizer` pass.

## What goes in one commit

1. One logical change.
2. Its tests.
3. Its documentation: module README, design status, changelog line. A change without them is
   not finished (see `documentation`).

## Staging

Stage by path, never `git add -A` or `git add .`. Check `git diff --cached --stat` before
committing; another session may share the working tree.

## Examples

| Bad | Good |
| --- | --- |
| `Fixed stuff` | `fix(audio): stop the mixer clipping at unity gain` |
| `feat: Added new feature for water.` | `feat(water): sample the sea surface on the device` |
| `update README` | `docs(ecs): list the world's public entry points` |
