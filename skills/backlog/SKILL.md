---
name: backlog
description: Use when asking what is left, what is next or what is open, when a defect, limitation or missing check turns up, when a piece of work is finished, when picking the next task, and before any commit, to read and write the backlog through the repository's backlog commands, in a repository.
---

# Backlog

The backlog is the only list of remaining work and known issues. It is read and written through
the repository's `backlog` commands and nowhere else. Its files and columns are in
`BACKLOG_FORMAT.md` of `documentation`.

## State comes from the command

`<cli>` is the repository's CLI. A repository with none runs the module form of the same commands, named by the tooling role.

A question about state is answered by a command, never by a file, the git log or memory.

| Question | Command |
| --- | --- |
| What do I do next? | `<cli> backlog next`, with `--json` for an agent |
| What is open, blocked or late in one area? | `<cli> backlog list`, filtered |
| What waits for the owner? | `<cli> backlog decisions` |
| What does one entry say? | `<cli> backlog show <ID>` |
| Is the store well-formed? | `<cli> backlog check` |
| Which entry does my commit serve? | The ID from `backlog next`, or the one `backlog add` printed |

A markdown file under `docs/backlog/` is output of the tool. Reading it to learn what is left
answers from a stale copy; running the command answers from the store.

## The order of a session

1. **Start.** The owner's task comes first. With none, run `backlog next`: the owner's pins, then
   the ready entries by priority and age; take what it gives. With a task, `backlog list` tells
   whether an entry covers it, and the commit names that entry.
2. **A defect or limitation turns up.** Run `backlog add issue` for a condition a reader can meet,
   or `backlog add work` for something to do. Do it at the moment it is found. A thing noted for
   the end is a thing lost.
3. **Finish.** Run `backlog close <ID>` in the same commit as the work, and write the changelog
   line it prints. The command takes no commit hash; the line names the ID. The commit ends with
   `Backlog: <ID>`.
4. **A commit that serves no entry** ends with `Backlog: none (<reason>)`. The reason says why no
   entry exists. A plan's job serves its work folder's entry (`AGENT_WORK.md` in `documentation`).

The line, last in the message, takes one of these forms:

<!-- quote:begin backlog-line -->
```
Backlog: RW-123
Backlog: RW-123, KI-4
Backlog: SushiSkills RW-38
Backlog: none (typo in a comment)
```
<!-- quote:end backlog-line -->

A worker reads with `backlog next` and reports what it found under "Backlog findings"; the
orchestrator writes the entries (`multi-agent-work`, "Roles").

## Work or issue

| What was found | Entry |
| --- | --- |
| Something to build, fix or check, with a scheduled fix and no workaround | `backlog add work` |
| A condition a reader can meet that has a workaround, or a limitation chosen on purpose | `backlog add issue` |
| A fault of a dependency, a toolchain or a sibling that is not the repository's to close | `backlog add issue`, with its origin |
| Something only the owner can rule on | `backlog add work --decision` |

The columns and the rule for a known issue are in `BACKLOG_FORMAT.md`.

## Choosing a priority

| Priority | Chosen when | Late after |
| --- | --- | --- |
| `P0` | Data is lost, a gate is broken, a release regressed, or a security fix follows a disclosure | 2 days |
| `P1` | A defect has no workaround, or other work waits on this | 14 days |
| `P2` | A defect has a workaround, or a missing check let a defect through | 90 days |
| `P3` | An improvement | 180 days, then reviewed |

When two fit, take the higher. This table is the one home of the limits.

## Red flags

- "I will read `docs/backlog/` to see what is left." → `backlog next` or `backlog list`.
- "I will note it in the commit message, a TODO or memory." → `backlog add`.
- "I will close it in a later commit." → the same commit.
- "I will edit the row." → `backlog set`; nobody edits a row by hand.
- "I will pick the next task myself." → with no task from the owner, `backlog next`.
- "This commit carries out a plan job, so it has no entry." → it serves the work folder's entry.
- "This commit is too small for an ID." → `Backlog: none (<reason>)`, and the reason is written.
