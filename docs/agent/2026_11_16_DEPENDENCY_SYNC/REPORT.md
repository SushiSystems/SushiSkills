# Dependency sync: report

**Status:** C1 to C4, H1, H2 and S1 are done. R1 is done in eleven repositories; SushiAI holds its
sync staged and SushiEngine applies it itself, each through its own session. R2 is done for SushiDSP
and SushiTrack; the splits left are in SushiAI, SushiBLAS and SushiEngine.

## What was built

- SushiCore v0.14.0 and v0.14.1, local tags: every shared checker held in SushiCore,
  `python -m sushicore.shared_tools sync|check`, `tools/shared_tools.lock` and
  `check_shared_tools.py`.
- SushiStack: `hub pins` and `hub bump` with `--skip` and `--only`.
- SushiSkills: the rule in `api-stability`, `sushisystems-dependencies`, `sushisystems-tooling` and
  `project-tools`; SushiSkills is a consumer of the shared tools.

## Defects found and fixed on the way

- The SushiCore requirement regex missed range pins, so `hub pins` saw no SushiCore split.
- New shared Python files took SushiCore's open licence header (RW-83).
- Two checkers walked git-ignored folders: 55 s to 2 s on SushiStack (RW-84; RW-85 for the rest).
- SushiCore's own checkers were shared (RW-82).
- KI-22 in SushiStack: a test stub lacked the `windows` argument.

## Open

- KI-33: the sync calls an old SushiSkills copy a local edit; `--force` after checking.
- RW-69 (SushiStack): a CI fan-out per tag needs tokens, the owner's decision.
- Pushing the tags and branches is the owner's step.

## Dispatches

dispatch: explore hub pins — haiku medium, 34 turns, passed, rung 1
dispatch: explore shared tools — haiku medium, 34 turns, passed, rung 1
dispatch: C1 merge — sonnet medium, 22 turns, passed, rung 3
dispatch: C2 sync package — sonnet medium, 50 turns, passed, rung 3
dispatch: H1 hub pins — sonnet medium, 49 turns, passed, rung 3
dispatch: H2 hub bump — opus low, 16 turns, passed, rung 4
dispatch: H3 hub integration — opus low, 62 turns, passed, rung 4
dispatch: C3 lock check — haiku high, 35 turns, passed, rung 2
dispatch: R1 sushidsp — sonnet medium, 14 turns, passed, rung 3
dispatch: R1 sushilog — sonnet medium, 13 turns, passed, rung 3
dispatch: R1 sushiprofiler — sonnet medium, 16 turns, passed, rung 3
dispatch: R1 sushiruntime — sonnet medium, 11 turns, passed, rung 3
dispatch: R1 sushitrack — sonnet medium, 18 turns, passed, rung 3
dispatch: R1 sushiweb — sonnet medium, 30 turns, passed, rung 3
dispatch: R1 sushistack — sonnet medium, 43 turns, passed, rung 3
dispatch: R1 sushiskills — sonnet medium, 15 turns, passed, rung 3
dispatch: R1 sushiai — sonnet medium, 36 turns, failed, rung 3
dispatch: RW-83 licence header — sonnet medium, 29 turns, passed, rung 3
dispatch: RW-84 ignored folders — sonnet low, 26 turns, passed, rung 3
dispatch: H4 hub bump fixes — opus low, 21 turns, passed, rung 4
