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

Private details are not tested directly. If a private function seems to need its own test, it is
a brick that wants its own module.

## Bug fix order

1. Write the regression test under `tests/regression/`, named after the defect.
2. Run it through the project CLI and see it fail for the reason the defect describes.
3. Fix the code.
4. Run it again and see it pass, with the rest of the module's tests.

A fix whose test was never seen failing is not verified.

## Layout and names

| Kind | Place | Proves |
| --- | --- | --- |
| Unit | Beside the module, `tests/` | One brick's behaviour in isolation |
| Integration | Root `tests/integration/` | Two or more modules working through their public surfaces |
| Regression | Root `tests/regression/` | A defect stays fixed |
| Golden | Root `tests/golden/` | An output (image, file, numeric table) stays identical |
| Benchmark | Root `tests/benchmark/` | A measurement; never pass or fail |

- Files: `test_<subject>` in the language's extension.
- Names read as behaviour: `StepRejectsNegativeTime`, `test_step_rejects_negative_time`,
  `it("rejects a negative time step")`.

## Determinism

1. Every random source takes a fixed seed written in the test.
2. Every floating-point comparison states its tolerance in the test, absolute and relative,
   never a bare `==`.
3. Tests that need a GPU or another device carry a device label. Without the device they are
   reported as skipped, never as passed.
4. No test depends on wall-clock time, test order, network or a file outside the repository.
5. A test that fails intermittently is fixed the day it is seen, or quarantined with an entry in
   `docs/reference/KNOWN_ISSUES.md` naming it. A quarantined test is never deleted silently.

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
