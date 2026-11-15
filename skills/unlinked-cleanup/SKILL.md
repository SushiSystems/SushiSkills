---
name: unlinked-cleanup
description: Use when work turns up a SOLID breach or an unneeded dependency, or something nothing reaches - a file, skill, page, function, test, setting, dependency or section that no code, link, build, install or caller uses - or a count, name or path that no longer matches what it describes, in a repository.
---

# Unlinked cleanup

Every place an agent looks is left cleaner than it was found: proven, asked for, kept apart.

## What counts as unlinked

| Kind | Unlinked when |
| --- | --- |
| File, folder, skill | No code, build file, install step, link or index names it |
| Function, class, constant, setting | No caller, reader or test outside its own definition uses it |
| Test | It covers code that no longer exists |
| Page or section | It describes a name, path or tool that no longer exists |
| Dependency | No source includes or imports it |
| Stale fact | A count, name or path in prose no longer matches the thing it describes |

These are never unlinked, whatever a search shows:

- A public surface: an exported symbol, a public header, a CLI command, a file format. Its
  removal follows `api-stability`.
- An entry point a tool, a hook, a CI workflow or a user runs by name.
- History: the changelog, the archive, a closed work folder, a licence or notice file.
- A file another repository reads. Search its siblings before calling it unlinked.

## The order

1. **Prove it.** Search for every way the thing could be reached: its name, its path, its
   file name without extension, and dynamic forms such as a string in a table or a glob. Keep
   the commands and their output. One search that finds nothing is not proof.
2. **Ask.** Name every item found in one question to the owner: what it is, the searches that
   found nothing, and what deleting it also deletes. Never delete before the answer. An item the
   owner keeps gets a link from where it belongs, or a backlog entry saying why it stays.
3. **Delete whole.** Remove the thing and everything that exists only for it: its tests, its
   settings, its rows in an index or a table, its section in a page, its install link. A
   stale fact is corrected, not deleted.
4. **Check.** Run the repository's full check and the tests. A red check is fixed before the
   commit, never by restoring a half of what was removed.
5. **Commit apart.** The cleanup is its own commit, never folded into the task's commit, with
   its `Backlog:` line and a subject that names what was removed.

The task comes first; items found mid-task are asked about once, at its end.

## The engineering stays

A cleanup is a change like any other. Every rule of `sushiskills` holds through it:

- **SOLID.** A removal leaves each remaining unit with one reason to change. Deleting the only
  other implementation of an interface leaves an abstraction with one user: fold it in, or ask.
  Deleting a caller never leaves a function doing two jobs for the callers that remain.
- **Tests.** Code that loses its last test because of a cleanup was not unlinked; stop and ask.
  A test is deleted only with the code it covers.
- **Pages follow.** Every page that names the removed thing is updated in the same commit
  (`documentation`).
- **No workaround.** A thing that looks unlinked because a link is broken gets the link fixed,
  not the thing deleted.
- **Nothing outside the repository** is removed without its own approval: an installed copy,
  a user setting, a package cache, another repository.

## SOLID breaches seen

Boundary 2 of `sushiskills` makes every report name each SOLID breach and unneeded dependency
met in the work. Named is not enough: each one seen is fixed through the same order.

1. **Prove it.** File and line, the principle it breaks (one responsibility, open for extension,
   substitution, narrow interfaces, depending on abstractions), and what it costs: the change
   it makes harder, the test it makes impossible.
2. **Ask** in the same question as the unlinked items, with the smallest fix that removes it.
3. **Fix apart,** with the tests that pin the behaviour first, in its own commit, as
   `testing` asks of a refactor.

A breach is never left with only a note. One the owner keeps gets a backlog entry naming it.
"None" is written only beside the list of files read.

## Subagents

A subagent never deletes. It lists what it found under two headings of its report, always
present and never empty without the files read: "Unlinked found" with the searches, and "SOLID
breaches" with file, line, principle and cost. The orchestrator proves each item again, asks the owner once for all of them, and
runs the cleanup itself or dispatches it as its own task.

## Red flags

Read `references/red-flags.md` when a cleanup feels obvious or urgent.
