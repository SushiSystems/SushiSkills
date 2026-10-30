---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, deciding whether a change is tested enough, or when a test run is slow or the number of tests has grown, in a repository.
---

# Testing

A test states what the code promises. A change is finished when its promise is written as a test
that fails without the change and passes with it.

## What a change must carry

| Change | Required test |
| --- | --- |
| `fix` | A regression test that reproduces the defect, seen failing before the fix |
| `feat` | A unit test for each behaviour of the public surface it adds, within the limits of "Budget"; an integration test when it crosses a module boundary |
| `perf` | The existing tests unchanged and green, plus the measurement from `performance` |
| `refactor` | No new test; every existing test green before and after |

A unit that is hard to reach is still tested:

| Unit | Tested through |
| --- | --- |
| A device backend | The real device, labelled `large` |
| A plugin or ABI boundary | A fake host that calls its entry points |
| A GUI panel | The toolkit run without a window, such as an immediate-mode toolkit's frame calls with no rendering backend |

A panel that cannot be tested that way holds logic that belongs in a unit of its own.

Private details are not tested directly. If a private function seems to need its own test, it is
a brick that wants its own module.

## What a test is

A test checks one promise the code makes, with the smallest input that can break it, at the
cheapest level that can see it, and fails when the promise is broken.

- A test has at least one assertion. A test that prints a value, or only runs the code, is an
  observation, not a test.
- Its name says the promise. If the name cannot say which defect the test would catch, there is no
  test.
- A test that repeats the implementation checks nothing, and a unit with every collaborator mocked
  checks its mocks.
- A helper that asserts is named `expect_*` or `assert_*` (`expect*` or `assert*` in TypeScript),
  so a checker can tell an assertion from a call. An assertion on a literal, such as `EXPECT_TRUE(true)`, is a defect.

## Value rules

**Rule:**

1. **Cheapest level.** What a `small` test can see is not written as `medium` or `large`.
2. **One promise, one test.** A promise that a higher test already covers is not repeated below it.
3. **Mocks sit at the unit's boundary:** the network, the disk, the device. The unit's own module
   is used for real.
4. **A regression test is the smallest reproduction,** a few lines that show the defect, not the
   scenario that exposed it.
5. **Rows, not copies.** The same promise over ten inputs is one parametrised test with ten rows.

**Why:** every test costs run time on every later change. A test that keeps no promise pays that
cost for nothing, and an agent told only to be thorough has no reason to stop.

**Not when:** rule 3 does not hold when a collaborator inside the module is itself slow or needs a
device; the test then uses a fake with that collaborator's interface. Rule 1 does not hold for a
promise that shows only at a size the cheaper level cannot reach, such as a converged simulation;
that test is `large`, listed in the exemption file below, and has the owner's ruling.

A checker reads assertions and counts. Rules 1 to 3 and 5 are judged by a reviewer, from the list
of added tests that the checker prints.

## Budget

Time is a budget, and every test spends it. The timeouts of the size table stay; they stop hangs.
These limits are the budget.

| Limit | Value |
| --- | --- |
| A `small` test | 1 s |
| A `medium` test | 10 s |
| A new `large` test | 120 s |
| The `small` tests of one test program | 10 s in total |
| The `large` tests of one test program | 600 s in total |
| The default run (`small` and `medium`) of a repository | 300 s |
| The whole `large` tier of a repository | 1 800 s |
| Test cases added by one commit | 20 |
| Test cases added by one `fix` commit | 5 |
| A second test program in one module, added by one commit | 0 without the owner |

- A parametrised case counts once as a case; its rows count in full in the time. A module's first
  test program needs no approval.
- The project's test command measures the time and prints one budget line: the sums, the wall time
  and the cases added since the base. An agent reads that line and times nothing itself.
- Counts gate at once. A single test fails the gate only when it exceeds its limit in a rerun of
  that test alone; a total fails above 1.25 times its limit. A run that did not rebuild prints
  "(not rebuilt)" and never gates.
- A test already over its limit is listed in the project's `tests/budget_exemptions.toml`, one test
  name and one open backlog ID. The checker fails an entry whose test no longer breaks its limit,
  so the list only shrinks. An exempt test is left out of every limit and total.
- A project's test command runs `small` and `medium` unless a size is named. It runs `large` only
  with a filter, or with the flag that means everything.

## Directions to the agent

1. Add a new test to the existing test program of its module. A second program in a module needs
   the owner.
2. Run the module's tests through the project's test command and read its budget line. The
   default run's total appears only when the whole default run happened; pre-merge CI runs it, and
   an agent does not run it to find out.
3. When a limit is broken, merge, parametrise or delete the tests you added in this piece of work
   first. When the cause is an old test, stop adding tests and report it under "Suggested
   removals" in the work folder's `REPORT.md`; do not touch it.
4. The report lists the tests added and the promise each keeps. The checker prints the list; check
   it and do not write it from memory.
5. Never run the whole `large` tier. Run the `large` suites of the module you changed, with a
   filter. The owner runs the whole tier on the device machine.

## Bug fix order

1. Write the regression test in the test file of the unit the defect lives in, its name naming
   the defect.
2. Run it through the project CLI and see it fail for the reason the defect describes.
3. Fix the code.
4. Run it again and see it pass, with the rest of the module's tests.

A fix whose test was never seen failing is not verified.

## Sizes, scopes and names

Where a test file lives is `TESTS.md` in `repository-layout`: the test tree mirrors the source.
What a test needs to run is its size, a label that CI chooses stages by and the test runner
enforces as a timeout. Every test carries exactly one.

| Size | The test may use | Timeout |
| --- | --- | --- |
| `small` | One process and one thread; no network, no sleep, no device, no file outside the build tree | 60 s |
| `medium` | Threads and processes, localhost, files in a temporary folder, a software device, a null audio driver, a fake plugin host | 300 s |
| `large` | Real hardware, such as a GPU or an audio device | 900 s |

A test that needs no hardware and runs long is made shorter. It is not labelled `large` to hide
its cost.

A test's size is written in its source, once, where the test is declared:

| Language | Where the size is written |
| --- | --- |
| C++ | The suite's name opens with `Small_`, `Medium_` or `Large_`: `TEST(Small_TensorShape, RejectsANegativeExtent)` |
| Python | `pytest.mark.small`, `medium` or `large` on the test's class, or as `pytestmark` on its file |
| TypeScript | The `describe` block's name opens with `small:`, `medium:` or `large:` |

In Python the timeout comes from `pytest-timeout`, a development dependency of every package
with tests, which the project's `conftest.py` sets from each test's size.

The build reads the size from there and sets the label and the timeout; no build file lists
suites or files by size. A suite that opens with no size fails the build, and in Python one
that carries none fails collection. `quarantined` is the one label a build file lists, by test
name, because it is a state with a known issue in the backlog, not a property of the test.

Size is the only kind label. What a test covers, why it exists and how it checks, such as a
defect it guards or a golden file it compares, are written in its name and its body. A benchmark is not a test; it
is a program of its own, from `performance`.

- Names read as behaviour: `StepRejectsNegativeTime`, `test_step_rejects_negative_time`,
  `it("rejects a negative time step")`.
- A test's name starts with the unit it tests, so a failing name leads to its file.

## Tests, benchmarks, probes and programs

Every program a repository runs on purpose is one of four kinds, told apart by what it answers.

| Kind | Answers | Ends with | Lives in | Runs through |
| --- | --- | --- | --- | --- |
| Test | Does the code keep its promise? | Pass or fail | `tests/`, with a size | `<cli> test`, by size |
| Benchmark | How fast or how light? | A measurement, no verdict | Beside the unit's tests, or a scenario under `applications/benchmarks/`, from `performance` | `<cli> bench` |
| Probe | What does this device, driver or simulation do? | Numbers or files a person reads, no verdict | `applications/probes/<name>/` | `<cli> probe <name>` |
| Program | How is the library used? | Whatever the program does | `applications/` | `<cli> run` |

A program that decides pass or fail is a test, whatever it measures: a frame compared against
its golden, a device checked against its own capability report, two pixels read back. It is
written as a test of the size its hardware needs, usually `large`, and runs with the other tests
of that size. A command that only runs tests of one size is `<cli> test --label <size>`, never a
probe.

A probe:

- measures one subsystem, and a subsystem has one probe; a variant of it, such as a regional
  nest against the global core, is an argument (`--scope global`), never a second probe;
- has a name that no other probe's name starts with, so two probes are never told apart by a
  suffix;
- returns 0 whenever it ran, and non-zero only when it could not run, saying why on stderr;
- prints each measurement on stdout as one line, `<name> <value> <unit>`, or writes its files
  under one folder it names on start;
- takes every input that changes its numbers, such as a seed, a viewpoint or a duration, from
  its arguments, so two runs with the same arguments can be compared;
- is listed in `applications/probes/README.md` with what it measures and an example run;
- is never added to the test runner and never gates CI.

## Determinism

1. Every random source takes a fixed seed written in the test.
2. Every floating-point comparison states its tolerance in the test, absolute and relative,
   never a bare `==`.
3. A `large` test whose hardware is absent is reported as skipped, never as passed.
4. No test depends on wall-clock time, test order, network or a file outside the repository.
5. A test that fails intermittently is fixed the day it is seen, or quarantined: it gains the
   `quarantined` label, which takes it out of every gating stage, and a known issue whose
   detail file names the test, its owner and the date it is fixed by, as `BACKLOG_FORMAT.md` in
   `documentation` gives. A quarantined test is never deleted silently.
6. A `small` test is never retried. A `medium` or `large` test that passes only on a retry is
   intermittent, and rule 5 applies.

## Golden files

- A golden file is updated only with the owner's approval.
- When a golden test fails, the agent reports the difference (image diff, changed values) and
  stops. It does not regenerate the file to make the test pass.
- An approved update is its own commit: `test(scope): update the <name> golden`.

## Running

Tests run through the project CLI only, scoped to what changed. A claim that tests pass carries
the command and its output.

## Red flags

- "The fix is obvious, the test can come after." → the test first.
- "The golden is outdated anyway, I regenerated it." → report and stop.
- "It passed on the second run." → it is flaky; fix or quarantine.
- "No device here, so the test counts as passing." → skipped.
- "It is GUI, plugin or device code; list it as untested." → test it as above.
- "I will cover every branch to be safe." → one promise, one test; the budget is the limit.
- "The test prints the value so I can see it." → that is an observation; assert it or delete it.
- "I will run all the large tests to be sure." → the large suites of the module you changed, with a filter.
