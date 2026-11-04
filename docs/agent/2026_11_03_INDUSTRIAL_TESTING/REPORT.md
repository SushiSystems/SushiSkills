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
| 2026-11-04: superseded `2026_11_02_TEST_STANDARD` deleted; its D1 to D9 were already in `testing` | done |
| 2026-11-04: triage of the trees the 2026-11-02 rollout left (J5 to J9) | done: sushicore 2 commits, sushiengine 2, the rest left with reasons |
| 2026-11-04: J1 and J1b, the core and shell pattern on the size checker | done, `a70043a` |

## SOLID breaches and unneeded dependencies met

- `tools/testing/test_budget.py` keeps its name although it no longer reads a budget; renaming it
  would break every project CLI that calls it by path, so the rename waits for the shared test
  command of phase F.
- `tools/testing/support/tolerance.hpp` is copied by `copy_shared_tools.py`, which writes the
  license header only into `.py` files, so the header keeps SushiSkills's file block in each copy.
- The checkers under `tools/testing/` mix file walking with their rules, which is why 36 of 41
  test files here are `medium` (RW-42).
- The size checker and the case reader read no C# cases for the forbidden kinds (RW-44).

## Owner's decisions waiting

- sushiruntime: work entries for the GLOBAL_HANDLE phases H0 to H9 and KI-23's Source path.
- sushiengine: whether the 7.4 MB `assets/astro/de440_1950_2050.sushiephemeris` is added.
- project-mobilerts: whether the editor re-save is kept; `ProjectSettings.asset` empties `preloadedAssets`.
- `claude/DISPATCH.md` rule 3 forbids `se`, while rule 9 needs `<cli> backlog`; a read-only exception is proposed.
- C++ mutation tool for RW-45.

## Dispatches

dispatch: J1 core/shell pattern — opus low, 2 rounds, passed, rung 1 (returned once for evidence)
dispatch: J1b move test-tree discovery — haiku high, 1 round, passed, rung 1
dispatch: J5 sushicore triage — sonnet medium, 2 rounds, passed, rung 1
dispatch: J6 sushiruntime triage — sonnet medium, 2 rounds, passed, rung 1
dispatch: J7 sushiengine triage — sonnet medium, 2 rounds, passed, rung 1
dispatch: J8 sushiweb triage — sonnet medium, 2 rounds, passed, rung 1
dispatch: J9 project-mobilerts triage — sonnet medium, 2 rounds, passed, rung 1
dispatch: J2 split testing checkers — haiku high, 1 round, passed, rung 1
dispatch: J3 split documentation checkers — haiku high, 1 round, partial (one checker), rung 1
dispatch: J3a check_docs_layout — haiku high, 1 round, passed, rung 1
dispatch: J3b check_docs_follow — haiku high, 1 round, passed, rung 1
dispatch: J3c check_source_comments — haiku high, 1 round, passed, rung 1
dispatch: J3d facts — haiku high, 1 round, passed, rung 1
dispatch: J3e design tools and RW-46 — haiku high, 1 round, partial (8 of 11), rung 1
dispatch: J4 remaining checkers — haiku high, 1 round, partial (two checkers), rung 1
dispatch: J4a layering — haiku high, 1 round, passed, rung 1
dispatch: J4b logs and ci — haiku high, 1 round, passed, rung 1
dispatch: J4c routing and check_all — haiku high, 1 round, passed with three survivors, rung 1
dispatch: J2b1 case reader — sonnet low, 2 rounds, passed, rung 1
dispatch: J11 diff mutator — sonnet medium, 1 round, passed, rung 1
dispatch: J12 sushicore test command map — haiku medium, 1 round, passed, rung 1

## Lessons of 2026-11-04

- A dispatch that names a share of sizes as acceptance invites tests split or added to move it; the
  owner ruled the share a reading. Acceptance is purity, one medium class and killed mutants.
- Workers sharing one tree blocked the commit hook and the mutation baseline while their files were
  half edited, and deleted each other's scratch folders. Each worker now has its own scratch folder,
  and the orchestrator commits by path once a job's files are done. Worktrees, tried once, broke the
  `git-workflow` rule that allows one only on the owner's request; through a commit hook their tests
  wrote `core.bare = true` into the repository's config (KI-5), restored the same evening.
- A job of more than two checkers ran out before its end on haiku; jobs are one or two files.

