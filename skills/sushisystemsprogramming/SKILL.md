---
name: sushisystemsprogramming
description: Use when starting any work in a Sushi Systems repository (existing or new), or when unsure which Sushi rule covers a file, a name, a comment, a log line, a document or a commit.
---

# Sushi Systems Programming

One discipline for every Sushi Systems repository, so that a person or an agent who knows one
repository already knows them all. Maintenance cost is the thing being minimised; every rule
below exists because its absence made a repository more expensive to change.

Every repository serves one aim: Sushiverse, a digital twin of the universe.

## The doctrine

1. **SOLID, without exception.** Every unit is a brick: one responsibility, detachable and
   re-attachable without touching its neighbours, rebuildable on its own. Siblings that do the
   same kind of thing are shaped the same.
2. **Grow without reshaping.** A structure is chosen so that adding the tenth module, level or
   backend adds a file, not an edit to nine others. A switch over kinds that every new kind must
   extend is a defect.
3. **Maintainability first, performance second.** Engineer it once carefully, run it a thousand
   times cheaply. A wasted cycle is a real cost, in money and in energy; a hack that saves one
   is a larger one.
4. **An obsessive quality bar.** "Good enough for now" is not accepted. Work that passes by
   accident is not finished.
5. **Honesty.** Say what was done and what was not. Partial work is reported as partial.
6. **Ask on boundaries, decide the rest.** Module boundaries, public interface shape, data
   ownership, external dependencies, and deleting what you did not create are the owner's
   decisions. Naming, internal structure, test shape and work order are yours. Never pick
   arbitrarily to avoid asking.
7. **The CLI is the only door.** Build, test and run through the repository's own CLI. Never call
   cmake, ninja, ctest, npm or uv directly, and never run a program or a test from CMake
   (`ctest`, a custom target, a post-build step). Only the CLI sets up the runtime search path,
   so a binary launched any other way fails to find its DLLs or shared objects.

## The bricks

Each rule set is its own skill. Load the one your task touches.

| Task touches | Skill |
| --- | --- |
| Prose of any kind, in English or Turkish | `humanizer` |
| Where a file or folder goes | `repository-layout` |
| C++ formatting, naming, class shape, errors | `cpp-code-style` |
| Python layout, formatting, naming, class shape | `python-code-style` |
| TypeScript layout, brace symmetry, naming, class shape | `typescript-code-style` |
| Doxygen headers and comments in source | `source-comments` |
| Log calls, categories, levels | `logging` |
| Any file under `docs/` or a module README | `documentation` |
| More than one agent on one piece of work | `multi-agent-work` |
| A commit message or pull request | `commits` |
| The checkers under `tools/` | `project-tools` |

## Language

Chat in the owner's language. Code, comments, documentation, commits and pull requests are in
English unless the owner says otherwise for a specific piece.

## Red flags

- "This one is small, it does not need its own file."
- "I will put the note here for now and move it later."
- "The checker does not cover this case, so it is allowed."
- "Asking would slow things down; this choice is obvious."

Each of these is how a repository starts to cost more. Stop and apply the brick.
