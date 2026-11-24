# Testing: determinism, reworking a suite and goldens

Read this when a test fails intermittently, when quarantining one, when reworking an old suite, or
when a golden test fails. The rules are in `../SKILL.md`.

## Determinism

1. Every random source takes a fixed seed written in the test. A shuffle or a property test that
   draws its seed prints it, and the same seed replays the run. A property test in CI runs
   derandomised with a bounded case count, and an input it found failing is pinned as an explicit
   example in the test, never left in its database.
2. A `large` test whose hardware is absent is reported as skipped, never as passed.
3. No test depends on wall-clock time, test order, the network or a file outside the repository.
4. A test that fails once and passes on the same commit is failing. The test command reruns a failed
   case once, alone, and reports a pass on rerun as flaky; gating never retries. A flaky test is
   fixed the day it is seen or quarantined: it gains the `quarantined` label and a known issue whose
   detail file names the test, its owner and the date it is fixed by, as `BACKLOG_FORMAT.md` in
   `documentation` gives. A quarantined test still runs in every stage, its result reported and
   never gating; on its fix-by date it is fixed, or deleted with the owner's ruling.
5. Tests run shuffled and in parallel. A test that passes only in one order, or alone, shares state
   with another and is a defect; each test builds its own fixture.
6. A retry exists only in the test's own source, as a named annotation with its count, and is
   reported apart from a pass. A test that passes only on a retry is intermittent, and rule 4 applies.

## Reworking an old suite

**Reworking an old suite** is done module by module: write the module's promise list from its public
interface, then take each existing test and keep, relabel, rewrite, merge into rows or delete it. A
deletion is listed in the work folder's report with the forbidden kind or the duplicate it repeats.
Missing promises get tests. The owner ruled on 2026-11-03 that the rework may delete tests other
people wrote.

## Golden files

- The difference to report is an image diff or the changed values. The file is never regenerated to
  make the test pass.
- An approved update is its own commit: `test(scope): update the <name> golden`.

The location of a test file is `TESTS.md` in `repository-layout`: the test tree mirrors the source. The
mirror says where a test goes; it never requires a test file for each header.
