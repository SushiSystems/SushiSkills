---
name: backlog
description: Use when asking what is left, what is next or what is open, when a defect, limitation or missing check turns up, when a piece of work is finished, when picking the next task, and before any commit, to read and write the backlog through the repository's backlog commands, in a repository.
---

# Backlog

The backlog is the only list of remaining work and known issues. Read and write it through the
repository's `backlog` commands (`<cli> backlog ...`; with no CLI, the module form), never
through a file, the git log or memory. Commands and the line forms: `references/commands.md`.
Columns: `BACKLOG_FORMAT.md` of `documentation`.

- Never read `docs/backlog/` to learn what is left; it can be stale.
- Never edit a row by hand; use `backlog set`.

## The order of a session

1. **Start.** The owner's task first; with none, take `backlog next`. With a task, `backlog list`
   tells whether an entry covers it; the commit names it.
2. **Before changing a file**, run `backlog here <path>`; its open entries are yours to close.
3. **A defect turns up.** `backlog add issue` (a condition a reader meets, with its origin) or
   `backlog add work` (to build, fix or check), when found. A change opens at most three on its
   own files; the rest is finished or kept in its work folder's entry. `--decision` is the owner's.
4. **Finish.** `backlog close <ID>` in the same commit, with the changelog line it prints. An entry
   on a changed file that stays open is named in the `Backlog:` line, or the hook refuses.
5. **Every commit** ends with `Backlog: <ID>` or `Backlog: none (<reason>)`.

A worker reports under "Backlog findings"; the orchestrator writes the entries.

## Priority

When two fit, take the higher. The one home of the limits: late after the days given.

- `P0`: data lost, gate broken, release regressed, security fix after disclosure. 2 days.
- `P1`: a defect with no workaround, or other work waits on it. 14 days.
- `P2`: a defect with a workaround, or a missing check let one through. 90 days.
- `P3`: an improvement. 180 days, then reviewed.

## Excuses

Each excuse is followed by its answer.

- "I will note it in a commit message, a TODO or memory." Use `backlog add`.
- "I will close it in a later commit." The same commit.
- "The rest of this change goes in new entries." Three at most; finish it.
- "I will pick the next task myself." With no owner task, `backlog next`.
- "This commit is too small for an ID." `Backlog: none (<reason>)`.
