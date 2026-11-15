# Testing: what a change carries, the agent's steps and red flags

Read this when deciding which tests a change needs, when reporting tests added, when fixing a bug, or
to check a thought against the full list of red flags. The rules are in `../SKILL.md`.

## What a change carries

| Change | Tests |
| --- | --- |
| `fix` | The smallest reproduction of the defect |
| `feat` | One test per promise it adds, at the smallest size that sees it, and the seam that makes that size possible |
| `perf` | The existing tests unchanged and green, plus the measurement from `performance` |
| `refactor` | No new test; every existing test green before and after |
| A reader of a file format or of untrusted input | A fuzz target, as "Proof of value" in `running.md` gives |
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

## Bug fix order

1. Write the regression test in the test file of the unit the defect lives in, its name naming the
   defect.
2. Fix the code.
3. The test runs once, in the single test run after the single build at the end of the work
   (`build-throughput`, boundary 8), with the rest of the module's tests, and passes.

The test is not run before the fix, so it is not seen failing first.

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
