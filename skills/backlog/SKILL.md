---
name: backlog
description: Use when asking what is left, what is next or what is open, when a defect, limitation or missing check turns up, when a piece of work is finished, when picking the next task, and before any commit, to read and write the backlog through the repository's backlog commands, in a repository.
---

# Backlog

The backlog is the only list of remaining work and known issues. Read and write it through the
repository's `backlog` commands (`<cli> backlog ...`; with no CLI, the module form), never
through a file, the git log or memory. Commands and the line forms: `references/commands.md`.
Columns: `BACKLOG_FORMAT.md` of `documentation`.

- Never read `docs/backlog/` to learn what is left; it is stale tool output.
- Never edit a row by hand; use `backlog set`.

## The order of a session

1. **Start.** The owner's task comes first. With none, run `backlog next` and take what it
   gives. With a task, `backlog list` tells whether an entry covers it; the commit names it.
2. **A defect or limitation turns up.** Run `backlog add issue` (a condition a reader can meet,
   or a fault of a dependency, with its origin) or `backlog add work` (something to build, fix
   or check). Do it when found, never at the end. Only the owner can rule: `add work --decision`.
3. **Finish.** Run `backlog close <ID>` in the same commit as the work, and write the changelog
   line it prints.
4. **Every commit** ends with `Backlog: <ID>` or `Backlog: none (<reason>)`; the reason is
   written. A plan's job serves its work folder's entry.

A worker reads with `backlog next` and reports under "Backlog findings"; the orchestrator
writes the entries.

## Priority

When two fit, take the higher. This list is the one home of the limits (late after the days given).

- `P0`: data lost, gate broken, release regressed, security fix after disclosure. 2 days.
- `P1`: a defect with no workaround, or other work waits on it. 14 days.
- `P2`: a defect with a workaround, or a missing check let one through. 90 days.
- `P3`: an improvement. 180 days, then reviewed.

## Red flags

- "I will note it in a commit message, a TODO or memory." Use `backlog add`.
- "I will close it in a later commit." The same commit.
- "I will pick the next task myself." With no owner task, `backlog next`.
- "This commit is too small for an ID." `Backlog: none (<reason>)`.
