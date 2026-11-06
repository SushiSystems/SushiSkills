# Test review: plan

**Status:** Open — paused by the owner on 2026-11-06; T1 done, T2 next

Applies the verdicts of `REPORT.md`, in hierarchy order: the shared helpers, adapters and seams the
rewrites need come first, then the defects the review found, then each module's tests. A module job
applies every record of its module: rewrite, resize, split, merge and delete as the record says, and
writes each add. Nothing in a module job changes production code except a seam a job above built.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| T1 | `skills/testing/REVIEWING.md`, `skills/testing/SKILL.md`: the page fixes above and the rulings of decision 2 |  | done |
| T2 | `tools/checking/copy_shared_tools.py` and its test: report the files a repository holds that upstream no longer does |  | todo |
| T3 | Tests for the rules with none, listed above |  | todo |
| M1 | the tests of `sushisystems` (1 file): 1 rewrite, 1 resize, 3 split, 2 merge | T1, T2, T3 | todo |
| M2 | the tests of `tools` (47 files): 43 rewrite, 15 resize, 36 split, 5 merge, 8 delete | T1, T2, T3 | todo |

## Acceptance

- **T1.** Each unclear point above has one sentence a reviewer can follow, and two blind reviewers agree on the sample tests that raised it. Build: `python tools/documentation/check_docs_truth.py .`
- **T2.** A copy into a repository that holds a file upstream dropped names that file; the test shows it with strings, no disk. Build: `python tools/check_all.py .`
- **T3.** Each rule has a small test that fails when the rule is broken. Build: `python tools/check_all.py .`
- **M jobs.** Every record of the module is applied: no test the report deletes remains, every kept and
  new test passes at the size its label states, and the module's tests pass through the project's own
  test command. Build: that command over the module.

The owner chooses inline or parallel mode.

## Pause

The owner paused the review on 2026-11-06 for other work. Every report, plan and finished job is
committed and pushed: on `main` here, on `feature/test_pipeline` in the other twelve repositories.
Each repository's `PLAN.md` in its own `docs/agent/2026_11_05_TEST_REVIEW/` holds its job table.

Done so far: T1 here, T1 and T3 in SushiCore (the in-memory adapters and the size timeouts), T1 in
SushiLog (`LogCapture`). Work resumes with the jobs those unblock, in this order:

1. The CLI tests on SushiCore's in-memory runner and console: SushiLog T2, SushiProfiler T4,
   SushiTrack T5, SushiDSP T5, SushiRuntime T6, SushiBLAS T6, SushiAI T7 and SushiEngine T8.
2. The log captures on `LogCapture`: SushiAI T5 and SushiTrack T3.
3. SushiRuntime T1, the tolerance header and the fixture base. SushiBLAS T2 and SushiAI T2 wait on it.
4. The other T jobs of each plan, then its M jobs.

The owner picks inline or parallel mode again when the work resumes.
