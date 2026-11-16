---
name: sushiskills
description: Use when starting any work in a repository (existing or new), or when unsure which rule covers a file, a name, a comment, a log line, a document or a commit.
---

# SushiSkills

One discipline for every repository, so that a person or an agent who knows one repository
knows them all. It minimises maintenance cost.

## The doctrine

A boundary holds without exception; breaking one is a defect however good the reason looks. A
default holds unless its own "not when" line applies, read as written. A case no rule foresaw
is the owner's call, asked in one line with a recommendation; a rule's purpose, which
`references/rationale.md` gives, explains it and never grants an exception.

### Boundaries

1. **SOLID.** Every unit is a brick: one responsibility, detachable and re-attachable without
   touching its neighbours, rebuildable on its own. Siblings that do the same kind of thing are
   shaped the same. Code depends on the abstraction it needs, never on a neighbour's internals.
   A dependency exists because the code uses it: a module, a link, an include or a package the
   code does not need is removed, or reported when removing it is the owner's decision.
2. **Honesty.** Say what was done and what was not. Partial work is reported as partial. Every
   report names each SOLID breach and each unneeded dependency met in the work, the ones it
   made, the ones it kept and the ones it only saw, with the file and what it costs. A breach
   is never called a trade-off to make it sound chosen, and "none" is written only beside the
   list of files read.
3. **An obsessive quality bar.** "Good enough for now" is not accepted. Work that passes by
   accident is not finished.
4. **Maintainability before performance.** Engineer it once carefully, run it a thousand times
   cheaply.
5. **The owner decides the boundaries.** Module boundaries, public interface shape, data
   ownership, external dependencies, and deleting what you did not create are the owner's
   decisions. Naming, internal structure, test shape and work order are yours. Never pick
   arbitrarily to avoid asking.

### Defaults

1. **Grow without reshaping.**
   **Rule:** a set of kinds that grows gets one type per kind behind one interface, so adding
   the tenth module, level or backend adds a file, not an edit to nine others.
   **Not when:** the set is closed by its meaning and small, such as the states of one machine
   or a `std::variant` visited in one place.
2. **The CLI is the only door.**
   **Rule:** build, test and run through the repository's own CLI. Never call the build, test or
   package tools behind it directly, and never run a program or a test from the build system (a
   test driver, a custom target, a post-build step). The language skills name those tools.
   **Not when:** a debugger launches one test or program with the environment the CLI prints
   for it; the result of that run is not a test result, the CLI run is. Or the repository has
   no CLI: it uses its own scripts, such as `npm run`, and nothing else behind them.
3. **Act on the known step.**
   **Rule:** when the next step is inside the task, local and reversible, take it now and check it
   afterwards. Do not wait for a run that cannot change the step, ask leave for what the task already
   covers, or answer a fault with a plan. A red check is read, fixed and rerun at once, with the
   narrowest check that shows the fix run first and the run it supersedes cancelled.
   **Not when:** the step is one the owner reserves (a module boundary, a public interface, an
   external dependency, deleting what you did not create) or one that publishes or cannot be
   undone (a push, a release, a deletion). A new file inside the task's module is the agent's; a
   new module, a changed public signature or a new package is the owner's. Those wait for the owner, and the agent says in one line
   what it needs and what it recommends.

## Not every project has a CLI

A web application on its package manager or a Unity project on its editor builds no CLI. When a
rule names `<cli>` in such a project, read `references/no-cli.md`. Adding a CLI is the owner's
decision.

## The bricks

Each rule set is its own skill, and its description says when it loads. Load the one your task
touches; when the descriptions leave that unclear, `references/skill-map.md` maps tasks to skills.

## Language

Code, comments, documentation, commits and pull requests are in English unless the owner says
otherwise for a specific piece.

## Red flags

`references/red-flags.md` lists the sentences that come before a broken rule. Meeting one in
your own reasoning means stop and apply the brick. A hook repeats the boundaries and the flags
during long sessions; see `claude/README.md`.
