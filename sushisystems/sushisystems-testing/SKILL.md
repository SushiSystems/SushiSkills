---
name: sushisystems-testing
description: Use in a Sushi Systems repository together with the testing or continuous-integration skill, to know the project's test command, the CTest call, the time reader, the exemption file, the tolerance helper and which machine runs the large tier.
---

# Tests at Sushi Systems

The `testing` skill names roles such as the test command and the time reader; this page names the
file or command that fills each role at Sushi Systems.

| Role | At Sushi Systems |
| --- | --- |
| Test command | `<cli> test`; the shared version is in `sushicore`, each project CLI switches to it one at a time, SushiTrack first |
| CTest call | `CMakeDriver.ctest_run` of `sushicore`: writes JUnit when given a path, passes `--parallel` with the command's job count (bounded by its memory limit when none is given) |
| Time reader | `tools/testing/test_budget.py`, called by the test command |
| Exemption file | `tests/budget_exemptions.toml` of the project |
| C++ tolerance helper | `tools/testing/support/tolerance.hpp`, synced from SushiCore with the shared tools |
| `large` tier and time calibration | the owner's machine (Ryzen 7600X, RTX 3080 Ti); no agent runs the whole tier |

SushiEngine suites are `Small_`, `Medium_`, `Large_`; its `Benchmark_` cases belong to `se bench`
and are not tests.

Survey of each repository's case counts and small share, measured start-up cost, SushiEngine's
`large` timings: `references/survey.md`.
