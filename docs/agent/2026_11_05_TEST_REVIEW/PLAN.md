# Test review: plan

**Status:** Open — paused by the owner on 2026-11-07; see Pause

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

## Acceptance

- **T1.** Each unclear point above has one sentence a reviewer can follow, and two blind reviewers agree on the sample tests that raised it. Build: `python tools/documentation/check_docs_truth.py .`
- **T2.** A copy into a repository that holds a file upstream dropped names that file; the test shows it with strings, no disk. Build: `python tools/check_all.py .`
- **T3.** Each rule has a small test that fails when the rule is broken. Build: `python tools/check_all.py .`
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
- Decisions the plans leave open are delegated to the lead of each repository, public interface
  changes inside that repository included. Each ruling is written into that repository's
  `REPORT.md`.
- One repository lead at a time per repository, at most two workers each. Machine memory is short.

### Where each repository stands

| Repository | State |
| --- | --- |
| SushiLog | Finished; released as v0.3.1; work folder closed |
| SushiStack | Finished; gui build 96 of 96; work folder closed |
| SushiSkills | Every job done; this folder stays open as the plan of the whole review |
| SushiCore | Every job but M6 (provision, 40 files) done; v0.10.15 released, a release is due for the rest |
| SushiProfiler, SushiTrack, SushiDSP | Python jobs done; the C++ T and M jobs not started |
| SushiRuntime | Every T job and most M jobs done unbuilt; M7 and the decision entries in progress |
| SushiBLAS | Every T job and 30 of 49 M jobs done unbuilt; RW-140 to RW-147 and 19 M jobs left |
| SushiAI | Every T job and about 20 M jobs done unbuilt; RW-155 and the other M jobs left |
| SushiWeb | T1, T5, T6, T7 and security fixes done; T2 to T4 and M1 to M30 left |
| SushiEngine | T8 and T10 done; T1 to T7, T9 and M1 to M136 left; 7 uncommitted test files in its tree belong to another session |
| Project mobileRTS | Not started |

Work resumes with a fresh lead per repository from its Status column. The lead briefs used on
2026-11-07 were in the session scratchpad; a resumed lead is briefed from this section and the
repository's `REPORT.md`.
