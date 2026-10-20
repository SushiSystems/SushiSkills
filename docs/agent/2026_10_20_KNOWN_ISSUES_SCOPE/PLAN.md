# Known issues scope: plan

**Status:** Open — part 1 done, no repository migrated

Runs inline, as the owner chose on 2026-10-20. Each task has one acceptance criterion and one
build, the build being `python tools/check_all.py .` in the repository the task changes. Part 1
changes sushiskills only.

## Part 1: sushiskills

### Task 1. The rule in the skills

Files: `skills/documentation/BACKLOG_FORMAT.md`, `skills/debugging/SKILL.md`.

Acceptance: each rule of `SPEC.md` is written in one of these two files, and `check_all.py`
passes.

### Task 2. `check_backlog.py`

Files: `tools/documentation/check_backlog.py`, `tools/tests/test_check_backlog.py`.

`rule_scope` reports an `own` known issue whose `Fix:` is `RW-<n>` and whose workaround is
`none`; `Where` becomes a field of a backlog entry, and `_value_shapes` already checks it.

Tests first: a failing and a passing case for the rule, and a backlog entry with `Where:`.

Acceptance: the new tests fail before the change and pass after, and `check_all.py` passes.

### Task 3. Close part 1

Files: `docs/reference/CHANGELOG.md`, `docs/design/REMAINING_WORK.md` (an entry for part 2),
this plan's status.

Acceptance: `check_all.py` passes and the owner has approved the commit.

## Part 2: migrations

One task per repository, in the order of the previous backlog migration, the shared checker
copied in first. A migration moves each known issue that `rule_scope` reports:

1. Find the backlog entry named in `Fix:`.
2. Append the symptom, the cause and the `Where:` to it.
3. Delete the known issue, and rewrite every prose citation of its ID.
4. Lower nothing: the `Next id:` counters stay.

An entry over the 25-line ceiling after the move sends its detail to a `Source:`. One stop for the
owner per repository: the commit.

Acceptance per repository: `check_all.py` passes there.

## Risks

- A merged entry reads as pasted. The migration is read entry by entry; it is not a find and
  replace.
- A known issue with its own `Source:` meets a backlog entry with one. The backlog entry keeps
  its own and the migration cites the other in the prose.
