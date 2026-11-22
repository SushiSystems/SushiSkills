# Commit detail

Read when you need the type table, examples, or how the hook and checker enforce the rules.

## Types

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

Scopes are folder names such as `matter`, `interop`, `cli`, `layering`. The sentence says what
the change does, for example `feat(matter): reserve the neighbour list at tick start`. The type
decides the next version: see `versioning-and-release`.

## Body

Optional. Plain paragraphs wrapped at 72 columns: what changed and what it affects. The reason
for a design lives in a design document; the body may cite its path. Run the `humanizer` pass.

## What goes in one commit

1. One logical change.
2. Its tests.
3. Its documentation: module README, design status, changelog line. A change without them is
   not finished (see `documentation`).

## The backlog line, enforcement

- The hook asks a sibling repository about its entry when it is checked out beside this one and
  takes it on trust when it is not.
- `tools/commits/check_backlog_trailer.py` checks the commits after `K_TRAILER_SINCE` in
  `tools/settings.py`, and the `commit-msg` hook in `tools/hooks/` refuses a message that
  breaks the rule before the commit exists. A repository's setup command installs the hook for
  the person.
- A plan's job is no reason for `none`; a commit that only closes an entry names that entry
  (`documentation`, `AGENT_WORK.md`).
- Pages follow what they describe: `documentation`, "Pages follow what they describe".
- The `commit-msg` hook refuses a `fix` or `feat` commit with no test and no `Tests:` line when
  `K_TESTS_LINE` is set.

## Examples

| Bad | Good |
| --- | --- |
| `Fixed stuff` | `fix(audio): stop the mixer clipping at unity gain` |
| `feat: Added new feature for water.` | `feat(water): sample the sea surface on the device` |
| `update README` | `docs(ecs): list the world's public entry points` |
