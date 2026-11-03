# Industrial testing: report

**Status:** Open — SushiSkills phases A to C built; phase D and the rework waves are next

Restarts the testing doctrine from the test's value and the code's architecture, not from a time
budget. Replaces the direction of the deleted `2026_10_30_TEST_BUDGET`.

## Owner's brief, 2026-11-03

- The two earlier attempts were budget-led, did not refactor deeply and missed the architecture.
- Every test must be effective and say something about the engine; no pointless tests.
- Tests must run as fast and as comfortably as possible.
- The small test is written first. A trivial feature's test taking 4 s on a 7600X with a 3080 Ti
  is a defect.
- Agents must be told why tests matter.
- Every test in every repository is reworked once the rules stand. Scope: every Sushi Systems
  repository and `project-mobilerts`; IpekWeb, MAYAGAWeb and SerkanGaripWeb are out.

## Decisions

- 2026-11-03, the engineer on the owner's instruction to decide: the SPEC absorbs what was still
  true in `docs/agent/2026_10_30_TEST_BUDGET/`, which is deleted; `docs/design/TEST_PIPELINE/` is
  rewritten from the SPEC.
- 2026-11-03, the owner: the rework may delete tests other people wrote, each with its reason.
- 2026-11-03, the owner: the shared C++ test support lives in SushiSkills and is copied; no
  `sushitest` repository.
- 2026-11-03, the owner: finish the SushiSkills work and commit; the owner continues the rework of
  the other repositories later.
- 2026-11-03, the owner: the time limits are calibrated on the desktop (Ryzen 7600X, RTX 3080 Ti),
  not on the laptop this session ran on (Ryzen 5 7640HS, RTX 4050 Laptop, 15 GB); nothing is built
  on the laptop. Until the desktop run, the limits report and never gate (RW-37).

## Progress

| Step | State |
| --- | --- |
| Sources read: `2026_10_30_TEST_BUDGET`, `design/TEST_PIPELINE`, sushiruntime `2026_10_14_TEST_COVERAGE`, `skills/testing` | done |
| Survey of every repository's tests (six read-only agents) | done, summarised in SPEC |
| Literature review (three agents): value and architecture; numeric, GPU and engine oracles; speed, sizes, flakiness | done, summarised in SPEC |
| SPEC | done, the owner answered its open questions |
| Phase A: `testing` rewritten; `TEST_PIPELINE` rewritten; the company testing page updated; the old work folder deleted | done |
| Phase B: `check_test_value.py` gains four rules; `check_test_additions.py` removed; `test_budget.py` reads `K_TEST_TIMES` and prints the shape | done |
| Phase C: `tools/testing/support/tolerance.hpp` with a self-check, run green with MSVC 18 | done |
| Phase D: SushiSkills's own tests made mostly small | not started, RW-42 |
| Registration and C# checkers, mutation pilot | not started, RW-43, RW-44, RW-45 |
| Rework waves in the other repositories | not started, RW-35 |

## SOLID breaches and unneeded dependencies met

- `tools/testing/test_budget.py` keeps its name although it no longer reads a budget; renaming it
  would break every project CLI that calls it by path, so the rename waits for the shared test
  command of phase F.
- `tools/testing/support/tolerance.hpp` is copied by `copy_shared_tools.py`, which writes the
  license header only into `.py` files, so the header keeps SushiSkills's file block in each copy.
- The checkers under `tools/testing/` mix file walking with their rules, which is why 36 of 41
  test files here are `medium` (RW-42).
- The size checker and the case reader read no C# cases for the forbidden kinds (RW-44).
