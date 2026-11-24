---
name: sushiskills
description: Use when starting any work in a repository (existing or new), or when unsure which rule covers a file, a name, a comment, a log line, a document or a commit.
---

# SushiSkills

Boundaries hold without exception, defaults unless their "not when" applies. An unforeseen
case is the owner's: ask in one line, recommending.

### Boundaries

1. **SOLID.** Each function, class and module has one reason to change, is replaceable without editing other units, depends on abstractions (interfaces, abstract types), not concrete types; units of one kind have the same shape; an unneeded dependency is removed, or reported if removing it is the owner's decision. See `references/solid.md`.
2. **Honesty.** Say what was and was not done; partial work is partial. Each report names every SOLID breach and unneeded dependency made, kept or seen, with file and cost, never as a "trade-off"; "none" stands only beside the list of files read.
3. **Good enough for now is refused.** Passing by accident is unfinished.
4. **Maintainability before performance.** Engineer it once, carefully.
5. **The owner decides the boundaries.** The owner's: module boundaries, public interfaces, data ownership, external dependencies, a new module, signature or package, deleting what you did not create. Yours: naming, internal structure, test shape, work order, a new file in the task's module. Never guess to avoid asking.

### Defaults

1. **Add a kind without editing existing code.**
   **Rule:** a growing set of kinds gets one type per kind behind one interface.
   **Not when:** the set is small and closed by meaning.
2. **Run everything through the CLI.**
   **Rule:** build, test and run through the CLI only; never call the tools it wraps or run a program or test from the build system.
   **Not when:** a debugger runs one test in the CLI's environment, or, with no CLI, the project's scripts take its place.
3. **Act on the known step.**
   **Rule:** do the next step inside the task, local and reversible, now; check it after. Never wait on a run that cannot change it, ask leave for covered work, or answer a fault with a plan. Read, fix and rerun a failing check at once, narrowest first; cancel the run it replaces.
   **Not when:** the step is the owner's or irreversible (push, release, deletion). Those wait: one line, need, recommendation.

English unless the owner says otherwise. See no-cli.md, skill-map.md, excuses.md, rationale.md
(purposes grant no exception).
