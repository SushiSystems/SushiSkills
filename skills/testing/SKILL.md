---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, or deciding whether a change is tested enough, in a Sushi Systems repository.
---

# Testing

A test states what the code promises. A change is finished when its promise is written as a test
that fails without the change and passes with it.

## What a change must carry

| Change | Required test |
| --- | --- |
| `fix` | A regression test that reproduces the defect, seen failing before the fix |
| `feat` | A unit test for each behaviour of the public surface it adds; an integration test when it crosses a module boundary |
| `perf` | The existing tests unchanged and green, plus the measurement from `performance` |
| `refactor` | No new test; every existing test green before and after |

A unit that is hard to reach is still tested:

| Unit | Tested through |
| --- | --- |
| A device backend | The real device, labelled `large` |
| A plugin or ABI boundary | A fake host that calls its entry points |
| A GUI panel | The toolkit run without a window, such as ImGui's `NewFrame` and `Render` with no backend |

A panel that cannot be tested that way holds logic that belongs in a unit of its own.

Private details are not tested directly. If a private function seems to need its own test, it is
a brick that wants its own module.

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
| `medium` | Threads and processes, localhost, files in a temporary folder, a software device: Lavapipe for Vulkan, a CPU SYCL device, a null audio driver, a fake plugin host | 300 s |
| `large` | Real hardware, such as a GPU or an audio device, or a run longer than `medium` allows | 900 s |

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
name, because it is a state with an entry in `KNOWN_ISSUES.md`, not a property of the test.

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
   `quarantined` label, which takes it out of every gating stage, and an entry in
   `docs/reference/KNOWN_ISSUES.md` naming it, with the `Owner:` and `Fix by:` fields of
   `BACKLOG_FORMAT.md` in `documentation`. A quarantined test is never deleted silently.
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
- "No GPU here, so the test counts as passing." → skipped.
- "It is GUI, plugin or device code; list it as untested." → test it as above.
