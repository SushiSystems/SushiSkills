---
name: sushiskills
description: Use when starting any work in a repository (existing or new), or when unsure which rule covers a file, a name, a comment, a log line, a document or a commit.
---

# SushiSkills

## The doctrine

A boundary holds without exception; a default unless its "not when" line applies. An unforeseen
case is the owner's: ask in one line, recommending. Purposes
(`references/rationale.md`) grant none.

### Boundaries

1. **SOLID.** Every unit is a brick: one responsibility, detachable and re-attachable without touching its neighbours, rebuildable on its own. Siblings are shaped alike. Code depends on abstractions, not internals. An unneeded dependency is removed or reported.
2. **Honesty.** Say what was done and what was not. Partial work is reported as partial. Every report names each SOLID breach and unneeded dependency met, made, kept or only seen, with file and cost, never as a "trade-off"; "none" stands only beside the list of files read.
3. **An obsessive quality bar.** "Good enough for now" is not accepted. Passing by accident is unfinished.
4. **Maintainability before performance.** Engineer it once carefully; run it a thousand times cheaply.
5. **The owner decides the boundaries.** Module boundaries, public interfaces, data ownership, external dependencies and deleting what you did not create are the owner's; naming, internal structure, test shape and work order are yours. Never pick arbitrarily to avoid asking.

### Defaults

1. **Grow without reshaping.**
   **Rule:** a set of kinds that grows gets one type per kind behind one interface, so a new kind adds a file, not edits.
   **Not when:** the set is closed by its meaning and small (one machine's states).
2. **The CLI is the only door.**
   **Rule:** build, test and run through the repository's CLI; never call the tools behind it or run a program or test from the build system. The language skills name those tools.
   **Not when:** a debugger launches one test with the CLI's environment, or there is no CLI and its own scripts (`npm run`) stand in.
3. **Act on the known step.**
   **Rule:** when the next step is inside the task, local and reversible, take it now and check it afterwards. Do not wait for a run that cannot change the step, ask leave for what the task already covers, or answer a fault with a plan. A red check is read, fixed and rerun at once, narrowest check first, the run it supersedes cancelled.
   **Not when:** the step is the owner's (boundary, interface, dependency, deleting what you did not create) or irreversible (push, release, deletion). A new file inside the task's module is the agent's; a new module, a changed public signature or a new package is the owner's. Those wait: one line, need and recommendation.

No CLI: `references/no-cli.md`. Task map: `references/skill-map.md`. Red flags:
`references/red-flags.md`. Write English unless the owner says otherwise.
