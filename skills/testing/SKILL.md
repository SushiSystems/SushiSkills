---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, deciding whether a change is tested enough, making code testable, or when a test run is slow or the number of tests has grown, in a repository.
---

# Testing

A test checks one promise of a public interface, against a named oracle, at the smallest size that
sees it, and fails when the promise breaks. `REVIEWING.md` derives promises and gives verdicts.

## A test

- One promise, one when. The name is the promise as a sentence, opening with the unit:
  `GemmWithBetaZeroIgnoresNanInC`.
- The expected value never comes from running the code under test.
- It kills a mutant or reproduces its commit's defect; a refactor never breaks it.
- Public interface only; a private function that needs a test wants its own module.
- Straight line: no `if`, loop or `try` outside a row table. An asserting helper is `expect_*` or
  `assert_*`.

**Forbidden:** no assertion; an assertion on a literal; printing for asserting; a sleep; a bare
tolerance literal; a `small` test past its size; a private header or `Detail::` symbol; control
flow in the body; a mock of what the repository owns; a test of trivial code; a change detector;
an expected value pasted from current output (except a `Characterization_` suite with a backlog
entry); the same promise again. Detail: `references/test-shape.md`.

## Sizes

`small`: own memory, one thread, injected clock and seed; 1 s; every build. `medium`: one machine
(shared device, temp folder, localhost, threads); 10 s; pre-merge. `large`: anything; 120 s;
nightly, never pre-merge. Every test writes its size.

- Small first; logic only a medium test sees lacks a seam, built first.
- The printed size share is a reading, never a target.

## Time

The test command fails a run over one.

| Limit | Value |
| --- | --- |
| A `small` test | 100 ms |
| A `medium` test after the shared fixture | 5 s |
| A `large` test | 30 s |
| A repository's pre-merge run (`small` and `medium`), wall | 600 s |

Touch lists, quarantine: `references/sizes.md`. Time reader, exemptions, mutation, coverage,
sanitizers, fuzzing: `references/running.md`.

## Oracles and seams

Oracle, first that applies: exact by construction, host reference, specified value with its
derivation, metamorphic relation, implicit (fuzz or stress only), golden file. Tolerances come
from the repository's helper, never typed. One promise over many inputs is one parametrised test.
Decisions live in a functional core; devices, files, threads and the clock sit behind owned ports
with in-memory adapters; mock only an out-of-process dependency the repository does not own.
`references/oracles.md`, `references/architecture.md`.

## Running fast

One test program per module; shards of about 10 s; one device per process, made once and handed
out by the module's fixture base, so no test makes a device, queue or runtime; no device-code
recompilation; every run shuffles with a printed seed; Python and TypeScript run in parallel.

## The agent

List the promises first; take the smallest size; name the oracle; run the module's tests through
the project's test command and read its time and mutation lines; report each test added
(`tools/testing/added_tests.py`); never run the whole `large` tier. Bug fix: the regression test,
named for the defect, is written before the fix and runs once, in the single run after the single
build (`build-throughput`, boundary 8). Red flags: `references/workflow.md`.

## Determinism

Every random source has a fixed seed in the test. A `large` test without its hardware is skipped,
never passed. No test depends on wall-clock time, order, the network or a file outside the
repository. A test that fails once and passes on the same commit is flaky: fixed that day or
quarantined with a known issue. A golden file changes only with the owner's approval; when one
fails, report the difference and stop. `references/determinism.md`.

Test, benchmark, probe or program: `references/programs.md`.
