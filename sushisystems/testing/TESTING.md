# Tests at Sushi Systems

The `testing` skill names a project's test command, its budget line and its exemption file. This
page says what fills those roles at Sushi Systems and what is known about the machines that run
the tests.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| The project's test command | `<cli> test`; the shared version is written in `sushicore` and each project CLI moves onto it in turn, SushiTrack first |
| The CTest call | `CMakeDriver.ctest_run` of `sushicore`, which writes a JUnit file when it is given a path |
| The budget reader | `tools/testing/test_budget.py`, called by the project's test command |
| The exemption file | `tests/budget_exemptions.toml` of the project |
| The machine that runs the `large` tier | the owner's machine with an RTX 3080 Ti; no agent runs the whole tier |

## What the projects do today

Surveyed on 2026-10-30 by reading each CLI's `test` command. The shared command replaces these
differences, so the table is a record of where each project starts.

| Project | Default sizes |
| --- | --- |
| SushiEngine | `small` and `medium` |
| SushiLog, SushiProfiler, SushiDSP | every size, `large` included |
| SushiTrack, SushiRuntime, SushiBLAS, SushiAI | not read |

## SushiEngine

- Its suites are named `Small_`, `Medium_` and `Large_`; its `Benchmark_` cases belong to
  `se bench` and are not tests.
- It declares a test program with a CMake function whose name ends in `add_test_program`, which is
  what the additions checker counts.
- The owner measured one run of the `large` tests at 700 s on the RTX 3080 Ti and reports that the
  whole `large` tier takes hours. Which module took the 700 s is not recorded. The limits of the
  `testing` budget for time stay unproven until the measured run names it.
- The matter module's tests are reworked in their own piece of work and are outside the budget.
