# Test review: plan

**Status:** Open — paused by the owner on 2026-11-10 in the evening; resume from "Where each repository stands" below and each repository's PLAN.md resume note

Applies the verdicts of `REPORT.md`, in hierarchy order: the shared helpers, adapters and seams the
rewrites need come first, then the defects the review found, then each module's tests. A module job
applies every record of its module: rewrite, resize, split, merge and delete as the record says, and
writes each add. Nothing in a module job changes production code except a seam a job above built.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| T1 | `skills/testing/REVIEWING.md`, `skills/testing/SKILL.md`: the page fixes above and the rulings of decision 2 |  | done |
| T2 | `tools/checking/copy_shared_tools.py` and its test: report the files a repository holds that upstream no longer does |  | done |
| T3 | Tests for the rules with none, listed above |  | done |
| M1 | the tests of `sushisystems` (1 file): 1 rewrite, 1 resize, 3 split, 2 merge | T1, T2, T3 | done |
| M2 | the tests of `tools` (47 files): 43 rewrite, 15 resize, 36 split, 5 merge, 8 delete | T1, T2, T3 | done |
| R1 | SushiCore `testing/session.py`, `cmake_driver.py` and their tests: the test command runs in parallel by default, the core count bounded by its memory limit, device tests sharing the device through resource groups | | done |
| R2 | each C++ repository's test-program CMake: register the cases of a program in shards, one process per shard, where start-up is most of a `small` case's time; SushiAI first | R1 | todo |
| R3 | each repository's one final test run is taken in parallel, and its pre-merge wall time is held to 600 s (SushiAI RW-166 tracks its own) | R1, R2 | todo |

## Acceptance

- **T1.** Each unclear point above has one sentence a reviewer can follow, and two blind reviewers agree on the sample tests that raised it. Build: `python tools/documentation/check_docs_truth.py .`
- **T2.** A copy into a repository that holds a file upstream dropped names that file; the test shows it with strings, no disk. Build: `python tools/check_all.py .`
- **T3.** Each rule has a small test that fails when the rule is broken. Build: `python tools/check_all.py .`
- **R1.** `<cli> test` with no job count runs as many tests at once as the machine has cores and prints that count; a small test shows the count falls when the memory limit asks. Build: `python tools/check_all.py .` in SushiCore.
- **R2, R3.** A repository's `small` and `medium` run, taken in parallel, stays within 600 s of wall time on the owner's machine. Build: the project's own test command.
- **M jobs.** Every record of the module is applied: no test the report deletes remains, every kept and
  new test passes at the size its label states, and the module's tests pass through the project's own
  test command. Build: that command over the module.

The owner chooses inline or parallel mode.

## Pause

The owner paused the work on 2026-11-07 to shut the machine down. Every repository's lead stopped
at a clean, pushed point on `feature/test_pipeline` (`main` here); each repository's `PLAN.md` in
its own `docs/agent/2026_11_05_TEST_REVIEW/` holds its job table and Status column, and its
`REPORT.md` holds the rulings, the dispatch lines and the risks its final build must check.

### The owner's rules for the rest of this work

- A repository is refactored completely first. Then it gets one build and one test run, at the
  very end, and nothing else: no test run per job, no C++ build per job, no Python test run per
  job. Only the checkers the commit hook runs stay on every commit.
- Decisions the plans leave open are delegated to the orchestrator, public interface changes inside
  a repository included. Each ruling is written into that repository's `REPORT.md`.
- No lead layer: it cost most of the quota in idle turns. The orchestrator dispatches one worker
  per repository directly; the worker commits each job, pushes, and reports in 20 lines.
- SOLID without exception, and the pyramid per unit: the logic a medium or large test passes
  through has its small tests first. A medium or large test of a unit with no small tests of its
  logic is a missing seam.
- Two answers are refused: "it cannot be checked without a build", and an in-memory adapter placed
  in `tests/support`.
- A worker may edit build files to split a module, fix a dependency edge or register a test file;
  it runs no build.

### Where each repository stands

| Repository | State |
| --- | --- |
| SushiLog | Finished; released as v0.3.1; work folder closed. To reopen: real collection counts, C++ at 76% small |
| SushiStack | Finished; gui build 96 of 96; work folder closed. To reopen: subprocess, git and network ports |
| SushiSkills | Every job done; this folder stays open as the plan of the whole review |
| SushiCore | Finished; v0.12.1 released and installed in every CLI (2 232 tests pass). R1 done: `<cli> test` runs in parallel by default. Shard support done (gtest XML, per-case rerun, 256 MB small share). Open: RW-74 (`-f` over shards), RW-75 (CLIs supply `run_program`). The stray v0.12.0 tag on 2b1d1a9 is the owner's to delete or keep |
| SushiProfiler | Python jobs done. C++: M1 done (f46b8e1); M2 in progress, next step in its PLAN.md resume note. Rulings in its REPORT.md decision 7 and after |
| SushiTrack, SushiDSP | Python jobs done. SushiTrack C++ M jobs started 2026-11-10 (resume note in its PLAN.md); SushiDSP C++ T and M jobs not started |
| SushiRuntime | Finished: built and tested at eed9a512, 1 433 of 1 433 pass. Left: R2 (shard registration) and R3 (parallel final run) |
| SushiBLAS | Unbuilt. Done: M2 to M4, M24, M25, M33, M34, M37. In progress: M35 (operations/blas, about 11 files) and M47, M49, S5; resume notes in its PLAN.md. Then R2 shard registration, one build and one test run |
| SushiAI | Finished on 2026-11-10: 8 145 of 8 145 pass. R2 done (62 shards): the run takes 234 s at 2 jobs, against 1 028 s serial. Open: RW-163 to RW-166 |
| SushiWeb | Untyped, untested, at c6aa738a. M21, M25 done (decisions 46, 47). Left: M28 (24 files; records at the session scratchpad `m28.txt`), then the SOLID review and one typecheck and test. Rulings for the next worker: delete the unused `PostgresCompanyRolePermissions`; make the recovery-code two-owner race a seeded repeated check |
| SushiEngine | T8 and T10 done; T1 to T7, T9 and M1 to M136 left; 7 uncommitted test files in its tree belong to another session |
| Project mobileRTS | Not started |

Work resumes per repository from its Status column and its `REPORT.md` Decisions. The worker brief
is kept in the session scratchpad as `J16/worker_direct.md`; its rules are the ones above.
