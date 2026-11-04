---
name: sushisystems-testing
description: Use in a Sushi Systems repository together with the testing or continuous-integration skill, to know the project's test command, the CTest call, the time reader, the exemption file, the tolerance helper and which machine runs the large tier.
---

# Tests at Sushi Systems

The `testing` skill names a project's test command, its time line, its exemption file and its
tolerance helper. This page says what fills those roles at Sushi Systems and what is known about
the machines that run the tests.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| The project's test command | `<cli> test`; the shared version is written in `sushicore` and each project CLI moves onto it in turn, SushiTrack first |
| The CTest call | `CMakeDriver.ctest_run` of `sushicore`, which writes a JUnit file when it is given a path |
| The time reader | `tools/testing/test_budget.py`, called by the project's test command |
| The exemption file | `tests/budget_exemptions.toml` of the project |
| The C++ tolerance helper | `tools/testing/support/tolerance.hpp`, copied from SushiSkills with the shared tools |
| The machine that runs the `large` tier and calibrates the time limits | the owner's machine, a Ryzen 7600X with an RTX 3080 Ti; no agent runs the whole tier |

## Where each repository starts

Surveyed on 2026-11-03 by grep over each tree; the full table is in
`docs/agent/2026_11_03_INDUSTRIAL_TESTING/SPEC.md` until that folder closes.

| Repository | Cases | Small share |
| --- | --- | --- |
| SushiBLAS | 2 342 | 22% |
| SushiRuntime | 1 464 | 31% |
| SushiAI | 4 578 C++ | 71% |
| SushiEngine | 6 914 on its feature branch | 74% |
| SushiDSP | 1 584 C++ | 81% |
| SushiProfiler, SushiLog, SushiTrack | 956 C++ | 88% |

Every C++ repository registers each case as its own CTest test today, so each case pays process
start-up and, for `medium`, device start-up. No repository records test times yet.

## SushiEngine

- Its suites are named `Small_`, `Medium_` and `Large_`; its `Benchmark_` cases belong to
  `se bench` and are not tests.
- The owner measured one run of the `large` tests at 700 s and reports that the whole `large` tier
  takes hours. One recorded test takes 117 s and another about 351 s.
