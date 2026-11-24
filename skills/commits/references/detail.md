# Commit detail

Read when you need examples, or how the hook and checker enforce the rules.

## Subject examples

Scope examples are `matter`, `interop`, `cli` and `layering`. The sentence says what the change
does, for example `feat(matter): reserve the neighbour list at tick start`. The type decides the
next version: see `versioning-and-release`.

## Body

The reason for a design is stored in a design document; the body may cite its path.

## The backlog line, enforcement

- The hook asks a sibling repository about its entry when it is checked out beside this one and
  accepts it without checking when it is not.
- `tools/commits/check_backlog_trailer.py` checks the commits after `K_TRAILER_SINCE` in
  `tools/settings.py`, and the `commit-msg` hook in `tools/hooks/` refuses a message that
  breaks the rule before the commit exists. A repository's setup command installs the hook for
  the person.
- The work folder of a plan's job is described in `AGENT_WORK.md` (`documentation`).
- Pages follow what they describe: `documentation`, "Pages follow what they describe".
- The `commit-msg` hook refuses a `fix` or `feat` commit with no test and no `Tests:` line when
  `K_TESTS_LINE` is set.

## Examples

| Bad | Good |
| --- | --- |
| `Fixed stuff` | `fix(audio): stop the mixer clipping at unity gain` |
| `feat: Added new feature for water.` | `feat(water): sample the sea surface on the device` |
| `update README` | `docs(ecs): list the world's public entry points` |
