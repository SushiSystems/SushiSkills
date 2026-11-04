# Test pipeline

**Status:** Open — rules, checkers and the tolerance header built; the rework of every repository is next
**About:** How every repository tests: what a test is worth, the sizes, the architecture that makes tests small, how they run fast, the CI stages
**Modules:** `tools/testing`

## Problem

Agents added tests with no measure of their worth, and code was shaped so that most promises could
only be checked through a device, a file or a thread. Every C++ repository started a process per
test case and rebuilt its runtime in each one. sushiblas ended with 78% of its cases `medium`,
sushiruntime with 69%, and tests of minor features took seconds. Two earlier attempts limited time
and counted cases and files; neither asked what a test proves or touched the code that made tests
expensive. The survey of every repository and the literature are in
`docs/agent/2026_11_03_INDUSTRIAL_TESTING/SPEC.md`.

## Decision

Decided by the owner on 2026-11-03, the rest by the engineer on the owner's instruction to decide.

1. A test is a statement about the code: one promise, one named oracle, the smallest size that can
   see it. A new test kills a mutant or reproduces a bug.
2. Sizes are defined by what a test may touch; time follows.
3. Code that cannot be tested small is refactored until it can: the seam comes before the test.
4. Tests run in process, in shards, with one shared device per process.
5. The per-commit case cap and the one-file-per-public-header rule are withdrawn.
6. Coverage never gates; mutation testing of the diff is the proof that a test can fail.
7. The rework of each repository may delete tests other people wrote, each deletion listed with
   its reason.
8. The shared C++ test support lives in SushiSkills and each repository copies it with the tools;
   no new repository or module is made.
9. The share of each size is a reading, never a target (the owner, 2026-11-04). Work is accepted on
   purity, one medium class for the boundary and killed mutants.
10. A timeout holds for one test case: 1 s small, 10 s medium, 120 s large; a C++ shard's is its
    size's timeout times its cases. The limit on a module's small total is dropped (the owner,
    2026-11-05).
11. A repository brings in the shared tools with a baseline of its known findings that only shrinks,
    each entry tied to an open backlog entry, so the commit hook gates new findings from the first
    commit (the owner, 2026-11-05).
12. Every repository's tests are reviewed in full, not only split: the promise list first, then a
    verdict for every test, wave by wave (the owner, 2026-11-05).

## Design

The rules are the `testing` skill. The checkers under `tools/testing/` enforce what a scan can see:
`check_test_value.py` rejects the forbidden kinds in code written after `K_TEST_VALUE_SINCE` (no
assertion, only weak checks, literal assertions, sleeps, typed tolerances, a `small` case that
reaches a thread, a file, the clock or the environment, with each repository adding its own device
symbols in `K_SMALL_FORBIDDEN_EXTRA`); `check_test_sizes.py` requires a size; `test_budget.py`
reads a JUnit file and prints the time line with the suite's shape. `tools/testing/support/tolerance.hpp`
derives floating-point tolerances from rounding bounds.

Each repository is reworked in its own work folder: measure, fix how the tests run, build the seams
the owner approves, triage every test against its module's promise list, measure again. The order,
the CI stages and the seams already found are in [PIPELINE.md](PIPELINE.md).

## Phases

| Id | Phase | State |
| --- | --- | --- |
| A | The rules in testing: value, forbidden kinds, sizes by constraint, oracles, architecture, running fast, time | built |
| B | Checkers for the forbidden kinds and the time line with the suite shape; the case cap removed | built |
| C | The shared tolerance header and its self-check | built |
| D | SushiSkills's own tests: checkers split into a pure core and a shell, so most tests are small | planned |
| E | Checkers for build registration and for C# cases | planned |
| F | The shared test command in sushicore: shards, gtest XML times, shuffle, rerun alone, resource file | planned |
| G | The rework of every repository, wave by wave | planned |
| H | Mutation testing of the diff, piloted in one repository | planned |

## Open questions

1. The time limits are the owner's start values. A measured run calibrates them before they gate.
