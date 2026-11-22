---
name: build-throughput
description: Use when deciding when to build or run tests during a piece of work, choosing a build configuration or a build tree, changing how a repository compiles or links (job counts, pools, caches, precompiled headers, unity batches, optimisation or debug-information levels), when a build runs out of memory or takes too long, or when deciding where heavy code such as a large template set is compiled, in a repository.
---

# Build throughput

A build setup is engineered once and measured. Full boundaries, defaults and red flags:
[boundaries](references/boundaries.md). Why: [rationale](references/rationale.md).

## Boundaries

1. **One tree per configuration** (Debug, RelWithDebInfo, Release, each lane or platform), fixed
   at creation; the CLI refuses to reconfigure it.
2. **Debug is the default; Release is built for releases.**
3. **Memory decides parallelism.** Free memory never falls under the reserve (1.5 GB unless the
   repository names another); jobs come from measured peaks and free memory at start.
4. **A build change carries its numbers** (`performance`).
5. **The CLI is the only door** (`sushiskills`, default 2).
6. **One copy of the machinery**: tree rule, gate, launcher entries, report come from the shared
   tooling library.
7. **A dependency is public only when a public header needs the whole type** (value, member,
   base class, inline body). Else forward-declare, include in sources, keep it private; name the
   header line first.
8. **Implement everything, build once, test once**, after the last line and a green build; never
   per task, module or edit. Fix a build error then, rerun until green. `clang -fsyntax-only` and
   commit-hook checkers are not builds.
9. **A build needs the owner's permission.** Single: one run, a rerun included. Standing: the
   session, until revoked. Never inferred or widened; with neither, ask in one line.

## Defaults

Each holds unless its "not when" applies; read its entry in
[defaults](references/defaults.md) before changing that part of a build.

- Measure first; admit jobs by measured peak, never a constant `-j`.
- Heavy code compiled once, in the module that owns it.
- Debug information sized to its use; debug links what Release links.
- A compiler cache for deterministic units only; unity batches for test targets.
- Secondary products share the engine's tree unless they need other flags.
- The platform's own costs (Windows scanning exclusions).
