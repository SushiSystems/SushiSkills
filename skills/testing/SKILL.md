---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, deciding whether a change is tested enough, making code testable, or when a test run is slow or the number of tests has grown, in a repository.
---

# Testing

A test checks one promise of a public interface, against a named oracle, at the smallest size that
can see the promise, and fails when the promise is broken. Write the test a reviewer would be sorry
to lose, and no other. `REVIEWING.md` derives promises and gives verdicts.

## What a test is

- **One promise, one when:** given, when, then. The name states the promise as a sentence and opens
  with the unit: `GemmWithBetaZeroIgnoresNanInC`, not `SimpleGemm`.
- **Oracle:** the expected value never comes from running the code under test.
- **Can fail, rightly:** it kills a mutant or reproduces its commit's defect; a refactor never
  breaks it.
- **Public interface only.** A private function that needs a test wants its own module.
- **Straight line:** no `if`, loop or `try` outside a row table.
- A helper that asserts is named `expect_*` or `assert_*`.

**Forbidden:** no assertion; an assertion on a literal; printing in place of asserting; a sleep;
a bare tolerance literal; a `small` test reaching past its size; a private header or `Detail::`
symbol; control flow in the body; a mock of what the repository owns; a test of trivial code; a
change detector; an expected value pasted from current output, except in a `Characterization_`
suite with a backlog entry; the same promise again. `tools/testing/check_test_value.py` reports
them. Examples, `static_assert` files and edge cases: `references/test-shape.md`.

## Sizes

| Size | May touch | Timeout | Runs |
| --- | --- | --- | --- |
| `small` | its own process memory, one thread, an injected clock and seed | 1 s | every build |
| `medium` | one machine: the shared device, a temporary folder, localhost, threads | 10 s | pre-merge |
| `large` | anything | 120 s | nightly, never pre-merge |

- **Small first.** A medium test checks a boundary; logic it alone sees lacks a seam, built first.
- The size share the test command prints is a reading, never a target.
- `tools/testing/check_test_sizes.py` checks that every test writes its size.

What each size never touches, where each language writes it, quarantine: `references/sizes.md`.

## Oracles and tolerances

Use the first that applies: exact by construction, a host reference, a specified value with its
derivation, a metamorphic relation, an implicit oracle (fuzz or stress only), a golden file.
Tolerances are derived through the repository's helper, never typed. One promise over many inputs
is one parametrised test. Shapes and special values: `references/oracles.md`.

## Seams

Decisions live in a functional core; devices, files, threads and the clock sit behind owned ports
with in-memory adapters. Mock only an out-of-process dependency the repository does not own. The
seven seams: `references/architecture.md`.

## Running fast

1. One test program per module.
2. Shards of about 10 s, not a process per case.
3. One device per process, made once before the first test and handed out by the module's one
   fixture base; no test makes a device, queue or runtime.
4. No device-code recompilation.
5. Every run shuffles with a printed seed.
6. Python and TypeScript run in parallel workers.

Shards, exemptions, mutation, coverage, sanitizers and fuzzing: `references/running.md`.

## Time

The test command measures these and fails a run over one.

| Limit | Value |
| --- | --- |
| A `small` test | 100 ms |
| A `medium` test after the shared fixture | 5 s |
| A `large` test | 30 s |
| A repository's pre-merge run (`small` and `medium`), wall | 600 s |

## What the agent does

1. List the promises before writing a test.
2. Choose the smallest size that sees each; build a missing seam first.
3. Name the oracle; use the tolerance helper.
4. Run the module's tests through the project's test command; read its time and mutation lines.
5. Report each test added with its promise, from `tools/testing/added_tests.py`.
6. Never run the whole `large` tier; filter to the module you changed.

The tests each kind of change carries, the bug fix order and the red flags:
`references/workflow.md`.

**Bug fix:** the regression test, named for the defect, is written before the fix and runs once, in the
single run after the single build (`build-throughput`, boundary 8).

## Determinism

- Every random source takes a fixed seed written in the test.
- A `large` test without its hardware is skipped, never passed.
- No test depends on wall-clock time, order, the network or a file outside the repository.
- A test that fails once and passes on the same commit is flaky: fixed that day or quarantined with
  a known issue.

A golden file changes only with the owner's approval; when one fails, report the difference and
stop. Retries, quarantine, reworking an old suite: `references/determinism.md`.

Test, benchmark, probe or program: `references/programs.md`.
