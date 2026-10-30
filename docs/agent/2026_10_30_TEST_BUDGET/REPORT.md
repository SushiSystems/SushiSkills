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

## A3 and B1

A3 is commit `b02fc98`, B1 is `d71e73a`. B1 split the work into `case_reader.py` (cases of C++,
Python and TypeScript with their assertions, literal assertions and sleeps), `changed_lines.py`
(the lines a working tree changes after a commit) and the checker. The mock-density report of the
plan is not built: a checker's `--report` counts findings and cannot carry a number that is not a
gate.

Read on SushiEngine's sources, read-only, with no file written:

| Measure | Value |
| --- | --- |
| Cases read | 7 379: 5 487 `small`, 1 778 `medium`, 114 `large`; the 12 `Benchmark_` cases are skipped |
| Without an assertion | 27, after the reader learned `expect_*` and `assert_*` helpers, including template calls |
| Assertions on a literal, sleeps in a `small` case | 0, 0 |
| Where the 27 sit | `foundation/blas` 13, `foundation/native_blas` 6, `world/matter_scene` 3, `domain/matter` 2, `foundation/core` 2, `foundation/event_bus` 1 |

Two kinds in the sample read: tests that call `check_*` helpers, which assert inside but sit
outside the `expect_*` and `assert_*` naming (`test_lane_parity.cpp`), and a test that prints a
sweep with `std::printf` and asserts nothing (`test_golden_crush.cpp`), which is an observation.
The first run read 219: helpers named `expect_*` in snake_case were not recognised. The checker
judges only cases with a changed line, so these 27 matter only when someone edits them.

Defects in my own work, found by the checkers and the tests, and what became of them:

- `b02fc98` changed `tools/settings.py` with no `Docs:` line for `tools/README.md`, which
  `check_docs_follow.py` now reports as `commit-b02fc984e:1`. The hooks are not installed in this
  clone (`core.hooksPath` is empty), so the `commit-msg` hook never refused it. The commit is on
  the remote, so it cannot be amended. The finding stays until the owner decides: move
  `K_DOCS_FOLLOW_SINCE` past it, or leave it failing.
- A first draft of the Python size rule merged the marks of a file and a class into one set, so
  the smallest size won; a test caught it and the nearest mark wins now.

## B2 and B3

B2 is commit `4cf335d`: `check_test_additions.py` and `added_tests.py`; B3 (wiring into `K_CHECKERS`,
`tools/README.md`, `project-tools`) went in with B1 and B2. A fresh reviewer's finding that a case
moved between files would count as an addition led to matching cases by name across the files a
commit touches, and a first digest-only draft counted every edited test as new; a test caught it. The
rule that stands: a case keeps its name, or it has a new name and a case with the same body went
away (a rename). A copy under a new name counts, because the original stays.

Read on SushiEngine's last 60 commits, read-only: 371 cases added in 25 commits, an average of 15
a commit; two commits exceed 20. One is `refactor(matter_cooking)!`, which moves a module,
renames its suites and edits their bodies, and counts as 210 additions. The checker would refuse
it; the way through is a move commit (`git mv`, names unchanged) and a rename commit apart. A
`refactor` commit that adds cases at all is also against `testing` ("no new test").

## Repair and C1

`bb32e25` installed the hooks in this clone (`python tools/hooks/install_hooks.py`) and moved
`K_DOCS_FOLLOW_SINCE` to `b02fc98`, so `check_docs_follow.py` judges every later commit and not the
one that missed its page. `check_all.py` is green again (20 checkers, tests). The owner approved both
and the work goes on.

C1 is commit `b1fdbd9`: `test_budget.py` and 15 tests. It reads a CTest JUnit file, takes a map from
suite to program, an exemption table and an optional rerun file, and prints the budget line, a
`rerun:` regex for the slow tests and the findings. Exempt tests are left out of every limit and
total, which the skill now says; otherwise the matter tests would fail the large tier for good.
The standard library parser is the only one a checker may use, so a file with a DOCTYPE or an ENTITY is
refused unread.

Not verified: the exact layout of `ctest --output-junit`. The reader takes `testcase` elements with
`name`, `time` and a `skipped` child or `status="notrun"`, as the CTest documentation describes. No
CTest is installed on this machine and no JUnit file from a real run exists, so phase D1 checks the
reader against the owner's first file before anything gates.

Phases A to C and B3 are done. What is left needs more than this repository: D0 edits `sushicore`
and its release is the owner's, D1 needs the owner's machine, D2 to D4 edit SushiEngine, E1b opens
entries in seven other repositories.

## Where to resume

Written on 2026-10-30 for the owner's other computer. State of each repository when this was written:

| Repository | State |
| --- | --- |
| SushiSkills | Phases A to C done and committed: the rules in `testing`, `check_test_value.py`, `check_test_additions.py`, `added_tests.py`, `test_budget.py`. `check_all.py` is green |
| SushiCore | `v0.10.6` tagged and pushed. It holds `ctest_run(output_junit=)` (RW-60), the manual corrected in fourteen places and the build gate headroom (RW-61). The `Release` workflow publishes it; whether the upload finished was not checked |
| SushiTrack | Untouched; chosen as the pilot |
| SushiEngine | Untouched; not built on the computer that wrote this |

What to do, in order:

1. **RW-37, on the computer that builds SushiEngine.** Run the small and medium tiers and one `large` module with a JUnit
   file. This is the one direct CTest call the plan allows, because `se test` cannot write the file yet:

   ```
   ctest --test-dir build/default-debug -L "small|medium" -LE quarantined --output-junit <absolute path>/small_medium.xml
   ctest --test-dir build/default-debug -L large -R "<suites of one module>" --output-junit <absolute path>/large_module.xml
   ```

   Note the wall time of each run and the module whose `large` tests took 700 s. Hand over the two files.
2. **RW-38.** Write `register_test_command` in `sushicore` (phase D0b of `PLAN.md`).
3. **RW-39.** Move `sushitrack` onto it; its build tree is built on the computer that wrote this.
4. **RW-36 and RW-35.** The other CLIs follow; SushiEngine adopts it after step 1 sets the limits.

Facts a new session needs, found the hard way:

- Hooks are per clone. Run `python tools/hooks/install_hooks.py` once in each repository on the new computer.
- `python -m sushicore.backlog` needs `sushicore/source` on `PYTHONPATH` unless `sushicore` is installed; inside the
  `sushicore` repository use an absolute path, since an empty `sushicore/` folder at its root shadows the package.
- `pytest` in `sushicore` needs `pytest-timeout`; without it run `python -m pytest -o addopts=""`.
- Every pipx environment built here has `home = C:\ProgramData\Miniconda`, so removing Miniconda breaks `sl`, `st`, `se`
  and the rest. Install a standalone Python and run `pipx reinstall-all` first.
- `K_DOCS_FOLLOW_SINCE` in `tools/settings.py` was moved to `b02fc98`, the commit that missed its `Docs:` line.
- A commit that adds a second test program to a folder needs a `Test program:` line from the owner.

## Suggested removals

None yet.

## Corrections made on the way

- An earlier chat message said the 700 s was mostly build and link time. The owner corrected it:
  the 700 s is a test run on an RTX 3080 Ti on another machine. `SPEC.md` records the run and
  leaves its labels as open question 1. The build and link costs in `BUILD_THROUGHPUT` are real
  but are a separate problem.

## Breaches met

- None found yet in the work so far; the review may add some.
