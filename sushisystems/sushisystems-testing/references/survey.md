# Tests at Sushi Systems: the survey of each repository

Read this when judging a repository's test sizes or run time, or SushiEngine's suites. The roles are in
`../SKILL.md`.

## Case counts and small share per repository

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

Every C++ repository registers each case as its own CTest test today, so each case spends time on process
start-up and, for `medium`, device start-up. Measured on 2026-11-10: SushiAI's 8 145 `small` and
`medium` cases summed to 1 004 s and ran serially in 1 028 s of wall time, a `small` case averaging
55 ms of which start-up was most; the shared test command passed no job count unless asked.

## SushiEngine

- The owner measured one run of the `large` tests at 700 s and reports that the whole `large` tier
  takes hours. One recorded test takes 117 s and another about 351 s.
