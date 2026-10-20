# Known issues scope

**Status:** Open — rule decided by the owner on 2026-10-20; checker built, migrations not started

## Problem

`KNOWN_ISSUES.md` began as a place for niche conditions that a reader would otherwise rediscover.
Over time it became a second backlog. A survey of the twelve estate repositories on 2026-10-20
found 264 known issues and 1 027 backlog entries:

| Group | Entries | What the entry adds over the backlog |
| --- | --- | --- |
| `own`, `Fix: RW-<n>`, `Workaround: none` | 119 | Nothing: a defect with a scheduled fix, recorded twice under two IDs |
| `own`, `Fix: RW-<n>`, a workaround | 88 | A reader's instruction for the symptom |
| `own`, `Fix: none, <reason>` | 32 | A limitation chosen on purpose, which no backlog entry can hold because it never closes |
| `toolchain`, `dependency`, a sibling | 25 | A condition outside the repository, which it cannot close |

The first group is the cost: two IDs, two counters and two edits to close one piece of work. The
other three are what `KNOWN_ISSUES.md` is for.

## Decision

Both files stay. A known issue is a condition a reader can meet and act on, and it stays in the
file while the condition holds, whether or not work is planned. A defect that has a scheduled fix
and no workaround is work, and lives only in the backlog.

## Rules

1. **Scope.** An entry with `Origin: own` carries a workaround other than `none`, or a `Fix:` of
   the form `none, <reason>`. `Fix: RW-<n>` with `Workaround: none` is a finding. Entries of
   another origin are unchanged: a toolchain, a dependency or a sibling is not the repository's to
   fix, so no backlog entry can close them.
2. **The backlog entry takes the detail.** When a known issue leaves the file, the backlog entry
   it names in `Fix:` receives what the reader needs: the symptom as a sentence of prose, the
   cause, and an optional `Where:` field. The backlog entry stays within 25 lines; a longer
   investigation goes to the entry's `Source:`.
3. **`Where:` on a backlog entry.** An optional field, at most five paths in backticks, each
   existing from the repository root, as in a known issue.
4. **Citations.** A reference to the removed ID in prose is rewritten to the backlog ID. An
   `Upstream:` never names a removed ID: none of the 119 is cited that way today.
5. **A discovered defect.** A defect found in the middle of work goes to the backlog. It is
   copied to the known issues once a workaround exists, with `Fix: RW-<n>`.

## What changes

- `skills/documentation/BACKLOG_FORMAT.md`: rules 1 to 3, in the one place the format lives.
- `skills/debugging/SKILL.md`, "Known issues": says which failures get an entry.
- `tools/documentation/check_backlog.py`: `rule_scope`, and `Where` in the backlog's fields.
- Each repository: the 119 known issues leave, their detail moves, citations are rewritten.

## Not in scope

- Whether the 88 entries that hold a workaround should also be deleted: they stay.
- Re-judging whether an entry is still true. That is the fact check in `project-tools`.
