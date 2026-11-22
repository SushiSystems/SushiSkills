# Unlinked cleanup: full wording

Read this when judging what counts as unlinked, what never does, or how a cleanup keeps the engineering rules. `../SKILL.md` holds the short form.

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

