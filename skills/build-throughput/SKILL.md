---
name: build-throughput
description: Use when deciding when to build or run tests during a piece of work, choosing a build configuration or a build tree, changing how a repository compiles or links (job counts, pools, caches, precompiled headers, unity batches, optimisation or debug-information levels), when a build runs out of memory or takes too long, or when deciding where heavy code such as a large template set is compiled, in a repository.
---

# Build throughput

A build setup is engineered once and measured, for the development machine as it is: fixed
memory shared with everything else, fixed hardware threads. Why each rule exists, and the longer
reasoning behind boundaries 7 and 8, is in [references/rationale.md](references/rationale.md);
read it when a case is not covered below or a rule seems to cost more than it saves.

## Boundaries

1. **One tree per configuration.** Debug, RelWithDebInfo and Release, and each execution lane or
   platform, have their own build directory. A tree's configuration is fixed when it is created;
   the CLI refuses to configure an existing tree with another build type or other compile flags.
2. **Debug is the default; Release is built for releases.** The plain build command builds the
   development configuration. Release is built by `versioning-and-release` and for measurement
   by `performance`. Nothing else defaults to it.
3. **Memory decides parallelism.** No build pushes free memory under the repository's reserve,
   1.5 GB unless it names another. What runs at once is decided from measured peaks and the
   memory free when the build starts, never from a constant.
4. **A build change carries its numbers.** A change made to build faster or lighter follows the
   measuring rule of `performance`: same tree, same machine, before and after, wall time and
   peak memory.
5. **The CLI is the only door.** Every knob below is a CLI option or a machine-local CLI setting
   (`sushiskills`, default 2).
6. **One copy of the machinery.** A CLI built on the shared tooling library takes the tree rule,
   the gate, its launcher entries and the report from it (`build_tree`, `build_admission`,
   `build_gate`, `build_report`) and keeps no copy of its own.
7. **A module dependency is public only when a public header needs the whole type**: held by
   value or as a member, a base class, or used in an inline body. A type a public header only
   names by reference or pointer is forward-declared there, its include moves into the sources,
   and the dependency is private; a caller that builds such an argument includes and links it
   itself. Before declaring a dependency public, name the public-header line that needs it.
8. **Implement everything, build once, test once.** A piece of work, however large, is
   implemented in full before any build runs. The build comes once, after the last line; the
   tests run once, after the build is green. Never a build per task, module, job or edit, and
   never a test run before the final build. A build error, structural ones included, is fixed
   then and the build rerun until green. Syntax checks without a build (`clang -fsyntax-only`)
   and commit-hook checkers are not builds.

## Defaults

Each holds unless its "not when" applies. Read its entry in
[references/defaults.md](references/defaults.md) before setting up or changing that part of a
build; the entry holds the full rule and its "not when".

- **Measure first.** The CLI reports per-edge-kind count, wall time and peak memory, the lowest
  free memory and the slowest edges; time-trace the slowest units before trimming anything.
- **Admission by measured peak.** Jobs equal hardware threads; a launcher admits each edge only
  when its last measured peak fits in free memory less the reserve. Pools are the fallback.
- **Heavy code compiled once, where it is owned.** Large template sets are instantiated in their
  module and exposed through plain functions; consumers include declarations only.
- **Debug information sized to its use.** Debug is unoptimised, at the measured debug-info level;
  RelWithDebInfo carries full debug information.
- **Debug links what Release links.** On Windows: release C runtime, `_ITERATOR_DEBUG_LEVEL` 0,
  Release builds of imported packages.
- **A compiler cache for deterministic units.** Capped, in the build tree, keyed on the compiler;
  bundled objects only after an identical-output trial.
- **Batches for test targets.** Unity batches of about eight; name clashes are fixed.
- **Secondary products share the engine's tree** unless they need other flags (boundary 1).
- **The platform's own costs.** On Windows the owner excludes build, cache and toolchain
  directories from real-time scanning.

## Red flags

- "A quick build now will catch a mistake early." / "This module is done, so I build it." /
  "The build is green, so I test this part now." → boundary 8.
- "I will set `-j` to what worked last time." → admission by measured peak.
- "I will switch this tree to Release for one measurement." → the Release tree.
- "The test needs the template set, so the test compiles it." → the module compiles it.
- "The cache makes it faster, so bundled objects go in too." → the trial first.
- "The header names its type, so the dependency is public." → forward-declare; keep it private.
