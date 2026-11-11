# Test budget gate: plan

**Status:** Open — run inline by the owner's choice on 2026-11-11

The time limits of `testing` only ever reported: the test command never passed `--gate`, no CLI told it
whether the tree was current, and nothing handed CTest a resource file, so device shards could share the
one accelerator. This work makes the limits gate, gives `large` a limit, shares the accelerator through
resource groups, and brings each repository's shared tools back to upstream.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| S1 | SushiSkills `tools/testing/test_budget.py`, `tools/settings.py`, `skills/testing/SKILL.md` and their tests: `large_test_s` of 30 s, a repeatable `--rerun`, `--list-over` |  | done |
| C1 | SushiCore `testing/budget.py`, `slow_rerun.py`, `accelerator_slots.py`, `session.py`, `filtered_run.py`, `shard_registrations.py`, `cmake_driver.py` and their tests | S1 | done |
| C2 | SushiCore release v0.13.0 | C1 | done |
| R1 | Each repository: the shared tools copied from upstream, `large_test_s` in its settings, the stale copies and the dead `K_TEST_BUDGET` removed, `RESOURCE_GROUPS gpus:1` on its `large` shards, `rebuilt` wired to `tree_is_current`, the SushiCore pin raised | C2 | done |
| R2 | KI-28 of SushiRuntime run again with the accelerator shared out | R1 | done |

## Acceptance

- **S1.** A test over its limit alone fails a gated run, `large` included, and settings without a limit are refused. Build: `python tools/check_all.py .`
- **C1.** A passing run of a current tree that breaks a limit exits non-zero, and CTest gets a resource file. Build: `python tools/check_all.py .` in SushiCore.
- **R1.** Each repository's own test command prints a budget line without "(not rebuilt)" after a build, and `copy_shared_tools.py --report` prints nothing. Build: the project's own test command.
