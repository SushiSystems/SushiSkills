# Test budget: report

**Status:** Open — spec and plan written and reviewed once on 2026-10-30; nothing built

## Steps

| Step | State | Commit |
| --- | --- | --- |
| Literature search | done; sources in `SPEC.md`, unread primary sources marked there | none yet |
| Spec and plan | written, then amended after the review | none yet, awaiting the owner |
| Independent review of both | done by a fresh subagent; findings below | |

## Review findings and what became of them

Checked by me against the repositories before acting: the 12 unsized cases are `Benchmark_`
cases, each case is its own CTest test so the JUnit file carries no program, `copy_shared_tools.py`
keeps `tools/settings.py`, and `check_all.py` takes shared checkers only through `K_CHECKERS`.

| Finding | Change |
| --- | --- |
| JUnit has no program; the per-program limit could not be computed | A suite-to-program map is written at configure time (`SPEC.md` "Who measures what", `PLAN.md` D2) |
| The 12 "unsized" cases are benchmarks | Problem table corrected; both checkers skip `Benchmark_`; open question 4 removed |
| The 1 s limit and the sum-versus-wall ambiguity | "What the numbers measure" added; both figures printed; start-up handled in D1 |
| `fix` label as a loophole; filler assertions | `fix` cap of 5; literal assertions are findings; mutation testing recorded as a follow-up |
| Rules an agent cannot follow (new module, old test over budget, no timing, nowhere to record) | A module's first program is free; "Suggested removals" section here; the line is printed for what was run |
| `settings.py` does not propagate | Constants per repository, checkers stay off without them, drift test skips without `skills/` |
| Wiring is `K_CHECKERS`, counting of cases unspecified | `PLAN.md` B3 and B2 say so |
| Missing "not when" lines; no gate mode switch | Added to value rules and to D2 (`test_budget` in `cli/config.toml`) |
| Ordering: open question 2 settled too late | Moved to A1 |

Not changed: the reviewer's point that decision 7 is the owner's. It stays the engineer's, marked
so in `SPEC.md`, because the owner asked the engineer to decide.

## A1: read before writing

Done on 2026-10-30, no file changed outside this folder. Commit: none yet.

| Question | Answer | Where |
| --- | --- | --- |
| Can a skill be a fact home? | Yes. `check_docs_facts.py` scans every `.md` outside `.git`, `third_party`, `node_modules`, `build` (line 25 and 47), and `skills/commits/SKILL.md` holds `fact:begin backlog-line`, quoted in `skills/backlog/SKILL.md`. Facts are Markdown only, so the Python constants still need the drift test | `tools/documentation/check_docs_facts.py` |
| May a project's command call a shared script? | Yes. `se check` runs scripts under `tools/` by path from a registry | `sushiengine/cli/sushiengine/services/checks.py:191` |
| How does a shared checker get run? | Only through the `K_CHECKERS` tuple; `own_checkers` adds checkers not in it | `tools/check_all.py:27`, `:52` |
| How does a commit checker read its range? | `commits_since(root, since)` returns `Commit(root, sha, parent, message)`, oldest first | `tools/commits/history.py:35` |
| Where is SushiEngine's CTest call? | `tools.driver.ctest_run`, which is `sushicore`'s `CMakeDriver.ctest_run` with no JUnit option (labels, filter, repeat, jobs, config only) | `sushiengine/cli/sushiengine/services/project.py:261`, `sushicore/.../cmake_driver.py:130` |

The last answer added phase D0 to the plan: a release of `sushicore` has to precede the change in
SushiEngine.

## Survey of the other test commands

Done on 2026-10-30, no commit. The table and the two consequences (one `CMakeDriver` seam,
differing defaults) are in `SPEC.md` under "The other projects' test commands". Not read: the build
behaviour of SushiRuntime, SushiBLAS and SushiAI, and the default sizes of SushiTrack, SushiBLAS
and SushiAI.

## A2: rules in `testing`

Done on 2026-10-30, not committed. `skills/testing/SKILL.md` gained "What a test is", "Value
rules", "Budget" (ten rows) and "Directions to the agent", a default of `small` and `medium` for a
project's test command, a `large` that means hardware, and three red flags.
`skills/multi-agent-work/SKILL.md` gained one line naming `testing` for the report's list of added
tests. `docs/reference/CHANGELOG.md` has the line. `python tools/check_all.py .` passes.

## CLI shape: RW-36

The survey showed that the project CLIs share a library but not a shape. The `test` command bodies of
SushiLog, SushiProfiler and SushiDSP differ by 40 to 56 changed lines out of 46 after names are
normalised, and no skill states the commands, options or defaults a project CLI follows.
`RW-36` (P2, decision) holds the question for the owner. This work does not wait for it: the budget
reaches the CLIs through `CMakeDriver.ctest_run`, which they already share.

## Suggested removals

None yet.

## Corrections made on the way

- An earlier chat message said the 700 s was mostly build and link time. The owner corrected it:
  the 700 s is a test run on an RTX 3080 Ti on another machine. `SPEC.md` records the run and
  leaves its labels as open question 1. The build and link costs in `BUILD_THROUGHPUT` are real
  but are a separate problem.

## Breaches met

- None found yet in the work so far; the review may add some.
