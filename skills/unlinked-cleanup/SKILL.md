---
name: unlinked-cleanup
description: Use when work turns up a SOLID breach or an unneeded dependency, or something nothing references - a file, skill, page, function, test, setting, dependency or section that no code, link, build, install or caller uses - or a count, name or path that no longer matches what it describes, in a repository.
---

# Unlinked cleanup

Unlinked: nothing references it (code, build, install, link, index, caller, test), or a count,
name or path in prose no longer matches. Kinds: `references/detail.md`.

Never unlinked (kinds in `references/detail.md`): a public surface (removal follows
`api-stability`); an entry point run by name by a tool, hook, CI workflow or user; history; a
file another repository reads.

## The order

1. **Prove it.** Search name, path, extensionless file name and dynamic forms
   (`references/detail.md`). Keep output; one empty search proves nothing.
2. **Ask.** One question names every item, its searches and what its deletion also deletes. No
   deletion before the answer. A kept item gets a link or a backlog entry.
3. **Delete all of it**: the thing and all that exists only for it (tests, settings, index rows,
   sections, links). An outdated fact is corrected, not deleted.
4. **Check** fully; fix a failure before the commit, never by restoring half the removal.
5. **Commit separately**, with `Backlog:` line, subject naming the removal.

Task first; mid-task finds are asked once, at its end.

## During a cleanup

Every `sushiskills` rule holds. An interface with one implementation is replaced by that
implementation, or asked about. Code that loses its last test was not unlinked: ask. Pages naming
the removed thing change in the same commit. Fix a broken link; keep its target. Nothing outside
the repository (installed copy, setting, cache, other repository) goes without its own approval.

## SOLID breaches seen

Each breach and unneeded dependency met follows the order: prove (file, line, principle, cost),
ask in the same question with the smallest fix, fix separately, tests first. Never leave only a
note; a kept one gets a backlog entry. "None" only beside the files read.

## Subagents

A subagent never deletes. Its report carries "Unlinked found" (with searches) and "SOLID
breaches" (file, line, principle, cost), never empty without the files read. The orchestrator
proves each again, asks once, and runs or dispatches the cleanup.

Read `references/excuses.md` when a cleanup seems obvious or urgent.
