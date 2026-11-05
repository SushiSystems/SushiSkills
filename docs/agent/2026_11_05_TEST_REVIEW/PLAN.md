# Test review: plan

**Status:** Open — not started; the owner chooses inline or parallel

Applies the verdicts of `REPORT.md`, in hierarchy order: the shared helpers, adapters and seams the
rewrites need come first, then the defects the review found, then each module's tests. A module job
applies every record of its module: rewrite, resize, split, merge and delete as the record says, and
writes each add. Nothing in a module job changes production code except a seam a job above built.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| T1 | `skills/testing/REVIEWING.md`, `skills/testing/SKILL.md`: the page fixes the owner approves | owner decision 2 | todo |
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
