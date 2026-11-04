---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, deciding whether a change is tested enough, making code testable, or when a test run is slow or the number of tests has grown, in a repository.
---

# Testing

## Why tests matter

A test is the only part of the code that says what the code promises. When someone changes the
engine a year from now, the tests are what tell them whether they broke it. A good test fails
exactly when a promise is broken, says which one, and costs milliseconds. A bad test fails for no
reason, passes when the code is wrong, or costs seconds, and every one of those teaches the people
who run it to stop reading test results. A suite of ten thousand tests nobody trusts is worth less
than a suite of five hundred everyone does. Write the test that a reviewer would be sorry to lose,
and no other.

## What a test is

A test checks one promise of a public interface, against a named oracle, at the smallest size that
can see the promise, and fails when the promise is broken.

- **Promise.** The name states it as a sentence: `GemmWithBetaZeroIgnoresNanInC`, not `SimpleGemm`.
  A name that cannot say which defect the test catches means there is no test. The name starts with
  the unit it tests, so a failing name leads to its file.
- **Oracle.** Where the expected value comes from. It never comes from running the code under test.
  "Oracles and tolerances" lists the kinds.
- **Can fail.** A new test kills at least one mutant of the code it tests, or reproduces the defect
  its commit fixes. A test that passes whatever the code does is not a test.
- **Public interface.** Private details are not tested directly. A private function that seems to
  need its own test is a brick that wants its own module.

A helper that asserts is named `expect_*` or `assert_*` (`expect*` or `assert*` in TypeScript), so a
checker can tell an assertion from a call. A project macro counts when its name opens with `EXPECT`
or `ASSERT`.

## Forbidden tests

Never written. The rework of an old suite deletes or rewrites each one it meets.

| Kind | Example |
| --- | --- |
| No assertion, or only `SUCCEED()`, a `static_assert` run as a test, `EXPECT_NO_THROW` around code that cannot throw | `flush(); SUCCEED();` |
| An assertion on a literal, or a value compared with itself | `EXPECT_TRUE(true)` |
| Printing or logging in place of asserting | `print(result)` |
| A sleep or a wall-clock wait, to synchronise or to prove that something did not happen | `std::this_thread::sleep_for(50ms)` |
| A bare tolerance literal in a floating-point comparison | `EXPECT_NEAR(a, b, 1e-5)` |
| A `small` test that reaches what its size forbids | a device queue in `Small_` |
| A private header, a `Detail::` symbol or a `_private` name | `#include ".../source/x.hpp"` |
| Control flow in a test body, outside a row table | `if (device) { EXPECT_... }` |
| A mock of a type the repository owns | mocking the module's own class |
| A test of trivial code: a getter, a default value, a constant, a log category, a version string | `EXPECT_EQ(kCategory, "Blas")` |
| A change detector: asserting how the code works rather than what it promises | asserting the order of internal calls |
| An expected value pasted from the code's current output | a golden array nobody derived |
| The same promise again at a larger size or in another file | `SimpleAxpy` beside the reference axpy test |

An expected value pasted from current output is allowed only in a test whose suite opens with
`Characterization_`, written to pin behaviour before a refactor, with a backlog entry that removes it.

## Sizes

A size is what a test may touch. Time follows from it; it does not define it.

| Size | May touch | Never | Timeout | Runs |
| --- | --- | --- | --- | --- |
| `small` | the memory of its own process, one thread, an injected clock and seed | a device, a file, a socket, a thread, a sleep, the environment, the real clock, a process-wide instance | 60 s | every build, pre-merge |
| `medium` | one machine: the shared device fixture, a per-test temporary folder, localhost, threads, a software device | a sleep, the network beyond localhost, a second device context, state left behind | 300 s | pre-merge |
| `large` | anything, including whole scenes and real hardware at scale | — | 900 s | nightly or weekly, never pre-merge |

The timeouts detect hangs. "Time" holds the limits a test is held to.

**A medium test checks a boundary:** that a kernel matches its host reference, that an adapter writes
the bytes its port promises, that two threads hand a value over. Logic behind the boundary is tested
`small`. A medium test that would pass with the device replaced by its host implementation is a small
test in the wrong place.

**Small first.** A promise is tested at the smallest size that can see it. When only a `medium` test
can see a promise that is logic, the code lacks a seam: add it first ("Architecture for small
tests"), then write the `small` test.

**Suite shape.**
**Rule:** at least 80% of each module's cases are `small` and at most 5% are `large`. The test
command prints the ratio per module.
**Why:** a module below 80% `small` holds logic its tests can only reach through a device, a file or
a thread, and every promise there is checked on the slowest, flakiest path. A repository-wide ratio
would let one heavy module hide behind light ones.
**Not when:** a module whose subject is the boundary itself, such as a device driver probe or a file
format adapter, states its own ratio in `tests/README.md` with the owner's ruling.

A module below the ratio is a refactoring finding. It is never answered by adding small tests to
raise the number.

### Where the size is written

| Language | Where |
| --- | --- |
| C++ | The suite name opens with `Small_`, `Medium_` or `Large_`: `TEST(Small_TensorShape, RejectsANegativeExtent)` |
| Python | `pytest.mark.small`, `medium` or `large` on the test's class, or as `pytestmark` on its file; a `unittest` file that must run without pytest, such as a checker test, sets `K_TEST_SIZE = "small"` |
| TypeScript | The `describe` block's name opens with `small:`, `medium:` or `large:` |
| C# (NUnit, Unity) | `[Category("small")]`, `"medium"` or `"large"` on the fixture class; a `[UnityTest]` or a test that loads a scene is at least `medium` |

The build reads the size from there and sets the label and the timeout; no build file lists suites by
size. A suite with no size fails the build, and in Python fails collection. In Python the timeout
comes from `pytest-timeout`, set by the project's `conftest.py` from the size; in TypeScript the test
configuration sets it from the prefix; in C# the assembly's shared base fixture sets `[Timeout]`.

The rule reaches every test in the repository: `tests/`, `cli/tests/`, `tools/tests/`, a package's
`__tests__/`, a sub-tree such as `gui/tests/`.

`quarantined` is the one label a build file lists by name, because it is a state with a backlog
entry, not a property of the test. A `Benchmark_` suite is a benchmark and carries no size.

## Oracles and tolerances

Strongest and cheapest first. A test uses the first that applies.

1. **Exact by construction.** Integer-valued or dyadic inputs whose result is exact in the type,
   compared bitwise. The default for BLAS, DSP and tensor kernels.
2. **A host reference.** The naive host implementation of the same routine, accumulating in a wider
   type. A device result is always checked against the host reference, never against values captured
   from a device run.
3. **A specified value** with its derivation in a comment beside it.
4. **A metamorphic relation** where no reference exists: a transposed product, a scaled input, a
   permuted batch, a serializer round trip.
5. **An implicit oracle,** no crash and no sanitizer finding, only for a fuzz target or a stress test.
6. **A golden file,** only when nothing above works.

**Tolerances are derived, never typed.** A floating-point comparison that is not exact goes through
the repository's tolerance helper, which computes `c · f(n) · u · gauge` (for a dot product or GEMM,
`n · u · Σ|aᵢbᵢ|`) and fails when error over bound exceeds the repository's one threshold. The C++
helper is `tests/support/tolerance.hpp`, copied from SushiSkills's `tools/testing/support/` as `project-tools`
gives for shared files. A bare `==` is kept only where the value is copied, not computed, or exactly
representable, and the name says so.

**Small shapes.** A routine is tested on the sizes {0, 1, 2, 3, 5, 9}, on tile size ± 1, on every
transpose and layout, on alpha and beta in {0, 1, another value}, with strides and leading dimensions
larger than the extent, and with aliased arguments where the interface allows them. Large shapes are
`large` tests and run nightly.

**Special values have their own tests:** NaN, Inf, −0, subnormals, empty extents.

**Rows, not copies.** The same promise over many inputs is one parametrised test (`TEST_P`,
`TYPED_TEST`, `pytest.mark.parametrize`, `it.each`, `[TestCase]`).

## Architecture for small tests

Code is shaped so that most promises can be tested small. When it is not, the seam is built before
the test, and building it is part of the task. A new or changed public interface is the owner's
decision; an internal one is yours.

1. **Functional core, imperative shell.** A module keeps its decisions in code that takes values and
   returns values. Device launch, file access, threads, sockets and the clock live in a thin shell
   around it.
2. **Ports with in-memory adapters.** Every outside dependency is reached through an interface the
   module owns, with a host or in-memory implementation beside the real one: clock, random seed, file
   system or stream, executor, transport, device queue, logger and profiler sink. Both pass the same
   contract tests. The in-memory one is the fake every other module's tests use; nobody mocks it.
   The contract tests are one typed or parametrised suite, `<Port>Contract`, in the test file of the
   port's own module, instantiated once per implementation: `small` for the in-memory one, the size
   its boundary needs for the real one.
3. **Kernels call host-callable functions.** The arithmetic and index math of a device kernel is a
   function compiled for host and device. Small tests call it on the host; one medium test per kernel
   family checks the launch against the host reference.
4. **No logic reaches a process-wide instance.** A singleton or a global context is passed in at the
   shell.
5. **Humble edges.** `main`, a MonoBehaviour, a React page, a kernel launcher and a CLI command only
   wire parts together. Logic in them moves into the core.
6. **Concurrency runs on an executor the code is given.** Tests pass a single-threaded executor that
   runs a seeded schedule, so a race reproduces from its seed. Real threads are tested `medium`,
   under ThreadSanitizer.
7. **Waiting takes a clock.** A component that waits takes a clock the test advances. Absence is
   proved by advancing the clock and asserting, never by sleeping.

Mocks are for an out-of-process dependency the repository does not own, in the test of the adapter
that reaches it. Everything else uses the real code or its in-memory port.

## Running fast

Tests run through the project's test command only. These rules shape how the command and the build
register and run them.

1. **One test program per module,** linking that module and what it uses, never a tier.
2. **Batches, not a process per case.** CTest gets one entry per shard of a program, sharded with
   `GTEST_TOTAL_SHARDS` and `GTEST_SHARD_INDEX` to about 10 s each; per-case results come from gtest's
   XML. `gtest_discover_tests` is kept only for a program that needs a process per case, such as
   death tests, and the program says why.
3. **One device per process.** A gtest `Environment` creates the runtime and the queue once; buffers,
   engines and graphs are per test, and teardown fails a test that leaks one. A device shard declares
   `RESOURCE_GROUPS gpus:1`.
4. **No recompilation.** Device code is compiled ahead of time for the build's targets, or the
   persistent kernel cache is on for every run.
5. **Shuffled.** Every run shuffles with a printed seed; a failure prints the command that
   reproduces it.
6. **Python and TypeScript** run in parallel workers. A small test takes no `tmp_path` and starts no
   subprocess.

## Time

The test command measures and prints these every run. An agent reads them and times nothing itself.
They gate once a measured run on the owner's machine has calibrated them; until then they report.

| Limit | Value |
| --- | --- |
| A `small` test | 100 ms |
| A `medium` test after the shared fixture | 5 s |
| The `small` tests of one module | 10 s |
| A repository's pre-merge run (`small` and `medium`), wall | 600 s |

The aims are a `small` test in 5 ms, a `medium` one in 200 ms and a pre-merge run in 3 minutes. A
test already over its limit is listed in the project's `tests/budget_exemptions.toml`, one test name
and one open backlog ID; the reader fails an entry whose test is back within its limit, so the list
only shrinks.

The project's test command runs `small` and `medium` unless a size is named, and runs `large` only
with a filter or the flag that means everything.

## Proof of value

- **Mutation testing of the diff** on host-compiled code: changed lines only, one mutant per line,
  logging and capacity hints skipped. A surviving mutant on a changed line is a review finding.
  Device code is reached through its host-callable functions.
- **Coverage** of the diff is printed and measured nightly. It never gates: a coverage gate is met by
  tests that run code without asserting.
- **Sanitizers** are oracles too: AddressSanitizer and UndefinedBehaviorSanitizer on `small` and
  `medium` pre-merge on Linux, ThreadSanitizer nightly. A report is a failure, never suppressed
  without an open backlog entry.
- **Fuzz targets** for every reader of a file format or of untrusted input. The corpus replays as a
  `small` test on every run; the fuzzer runs nightly, and each crash becomes a regression test.

## What a change carries

| Change | Tests |
| --- | --- |
| `fix` | The smallest reproduction of the defect, seen failing before the fix |
| `feat` | One test per promise it adds, at the smallest size that sees it, and the seam that makes that size possible |
| `perf` | The existing tests unchanged and green, plus the measurement from `performance` |
| `refactor` | No new test; every existing test green before and after |
| A reader of a file format or of untrusted input | A fuzz target, as "Proof of value" gives |
| An invariant over a range, such as a round trip or a conservation law | One property test with a fixed seed and a bounded case count, in place of many rows |

## What the agent does

1. List the promises the change makes before writing a test.
2. Choose the smallest size that sees each. If only `medium` sees a promise that is logic, build the
   seam first.
3. Name the oracle. Use the tolerance helper; never type an epsilon.
4. Use rows for one promise over many inputs.
5. Run the module's tests through the project's test command and read the time and mutation lines
   it prints.
6. Report each test added with the promise it keeps. `tools/testing/added_tests.py` prints the list;
   check it rather than write it from memory.
7. Never run the whole `large` tier. Run the `large` suites of the module you changed, with a filter.

**Reworking an old suite** is done module by module: write the module's promise list from its public
interface, then take each existing test and keep, relabel, rewrite, merge into rows or delete it. A
deletion is listed in the work folder's report with the forbidden kind or the duplicate it repeats.
Missing promises get tests. The owner ruled on 2026-11-03 that the rework may delete tests other
people wrote.

## Bug fix order

1. Write the regression test in the test file of the unit the defect lives in, its name naming the
   defect.
2. Run it through the project's test command and see it fail for the reason the defect describes.
3. Fix the code.
4. Run it again and see it pass, with the rest of the module's tests.

A fix whose test was never seen failing is not verified.

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

## Tests, benchmarks, probes and programs

Every program a repository runs on purpose is one of four kinds, told apart by what it answers.

| Kind | Answers | Ends with | Lives in | Runs through |
| --- | --- | --- | --- | --- |
| Test | Does the code keep its promise? | Pass or fail | `tests/`, with a size | `<cli> test`, by size |
| Benchmark | How fast or how light? | A measurement, no verdict | Beside the unit's tests, or a scenario under `applications/benchmarks/`, from `performance` | `<cli> bench` |
| Probe | What does this device, driver or simulation do? | Numbers or files a person reads, no verdict | `applications/probes/<name>/` | `<cli> probe <name>` |
| Program | How is the library used? | Whatever the program does | `applications/` | `<cli> run` |

A program that decides pass or fail is a test, whatever it measures, written at the size its
hardware needs. A command that only runs tests of one size is `<cli> test --label <size>`, never a
probe.

A probe:

- measures one subsystem, and a subsystem has one probe; a variant is an argument, never a second
  probe;
- has a name no other probe's name starts with;
- returns 0 whenever it ran, and non-zero only when it could not run, saying why on stderr;
- prints each measurement as one line, `<name> <value> <unit>`, or writes its files under one folder
  it names on start;
- takes every input that changes its numbers from its arguments;
- is listed in `applications/probes/README.md` with what it measures and an example run;
- is never added to the test runner and never gates CI.

A folder holding tests is never named `benchmarks/` or `Probe/`.

## Golden files

- A golden file is updated only with the owner's approval.
- When a golden test fails, the agent reports the difference (image diff, changed values) and stops.
  It does not regenerate the file to make the test pass.
- An approved update is its own commit: `test(scope): update the <name> golden`.

Where a test file lives is `TESTS.md` in `repository-layout`: the test tree mirrors the source. The
mirror says where a test goes; it never requires a test file for each header.

## Red flags

- "The fix is obvious, the test can come after." → the test first.
- "It needs the device, so it is medium." → which promise is logic? Build the seam and test it small.
- "Every public header should have a test file." → every promise should have a test.
- "1e-5 is close enough." → derive the tolerance with the helper.
- "I will sleep a little to be sure it did not happen." → take a clock and advance it.
- "I will cover every branch to be safe." → one promise, one test, and a mutant it kills.
- "The test prints the value so I can see it." → assert it or delete it.
- "It passed on the second run." → it is flaky; fix or quarantine.
- "No device here, so the test counts as passing." → skipped.
- "The golden is outdated anyway, I regenerated it." → report and stop.
- "I will run all the large tests to be sure." → the large suites of the module you changed, with a filter.
