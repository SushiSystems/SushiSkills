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

What a test covers is its scope, a second label, which says what the test proves and never
decides when it runs: `unit` for one brick in isolation, `integration` for two or more modules
working through their public surfaces. Why a test exists, a defect it guards, and how it checks, a
golden file, are written in its name and its body, not in a label. A benchmark is not a test; it
is a program of its own, from `performance`.

- Names read as behaviour: `StepRejectsNegativeTime`, `test_step_rejects_negative_time`,
  `it("rejects a negative time step")`.
- A test's name starts with the unit it tests, so a failing name leads to its file.

## Determinism

1. Every random source takes a fixed seed written in the test.
2. Every floating-point comparison states its tolerance in the test, absolute and relative,
   never a bare `==`.
3. A `large` test whose hardware is absent is reported as skipped, never as passed.
4. No test depends on wall-clock time, test order, network or a file outside the repository.
5. A test that fails intermittently is fixed the day it is seen, or quarantined: it gains the
   `quarantined` label, which takes it out of every gating stage, and an entry in
   `docs/reference/KNOWN_ISSUES.md` naming it, its owner and the date it is fixed by. A
   quarantined test is never deleted silently.
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
