# Test pipeline

**Status:** Open — phases A to C built; the shared test command and the measured run are next
**About:** How every repository tests: what a test is, its size and budget, the CI stages and the industrial practices each stage runs
**Modules:** `tools/testing`

## Problem

Agents told to be thorough add tests with no upper bound, and nothing shows them what a test costs
the owner. A timeout only stops a hang, so a suite of thousands of tests that each finish just
under their timeout passes every rule. The owner reported a run of one `large` tier taking
700 s and the whole tier taking hours. The full record, with the measurements and the literature,
is `docs/agent/2026_10_30_TEST_BUDGET/SPEC.md`.

## Decision

Decided by the owner on 2026-10-30.

1. A test has a definition: one promise, at least one assertion, a name that says the promise.
2. Value rules are written as concrete directions an agent can follow.
3. Time and the number of cases added are a budget; the limits are the table in `testing`.
4. The machine measures the budget and prints one line. An agent reads it and times nothing.
5. An agent merges or deletes only the tests it added, and reports old ones it thinks redundant.
6. Every project CLI runs the tests through one shared command in the tooling package.

## Design

The rules live in the `testing` skill, the constants in `tools/settings.py` with a drift test that
keeps them equal to the skill's table. `case_reader.py` reads the cases of C++, Python and
TypeScript; `check_test_value.py` judges the cases a commit changes; `check_test_additions.py`
judges how many a commit adds; `test_budget.py` reads a CTest JUnit file and prints the budget line.
A limit gates only once it is measured: counts gate at once, times gate after a report-only trial.


## Phases

| Id | Phase | State |
| --- | --- | --- |
| A | The rules in testing: definition, value rules, budget table, directions | built |
| B | Checkers for the value of a test and the cases a commit adds | built |
| C | The budget reader of a CTest JUnit file | built |
| D | One shared test command in the tooling package, then the measured run and the time gate | planned |
| E | Roll the tools out to the other repositories | planned |
| F | CI stages: pre-merge small and medium with the checkers, nightly large per changed module, weekly whole large tier, quarantine out of gating | planned |
| G | Module selection: a change runs the tests of the modules it touches and of their dependants | planned |
| H | Coverage report: nightly line and branch coverage, diff coverage printed pre-merge, never a gate | planned |
| I | Refactor every repository to the doctrine, tier by tier: small, then medium, then large | planned |
| J | Industrial practice: Windows and Linux matrix, sanitizers, shuffled parallel runs, fuzz targets, benchmark trends, JUnit results in CI | planned |

## Open questions

1. Which module took 700 s, and how long does the default run take? The measured run answers both
   and sets the time limits.
