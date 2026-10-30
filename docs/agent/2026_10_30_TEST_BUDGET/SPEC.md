# Test budget

**Status:** Open — phases A to C built, D0 released as sushicore v0.10.6; the measured run (RW-37) and the shared test command (RW-38) are next

Closes `RW-35`. Rules go into the `testing` skill, enforcement into `tools/testing/`, measurement
into each project's test command. SushiEngine is the first project to adopt it.

## Problem

Tests grow faster than anyone reads them, and the agents that write them do not know a time
limit exists. The owner reported on 2026-10-30 that a run of `large` tests on an RTX 3080 Ti took
700 s, that the module is not recorded, that the whole `large` tier takes hours, and that more
than half of a working day goes to building and testing. The pain is the `large` tier. Nothing
yet says how long the default run (`small` and `medium`) takes.

What the repositories say today:

| Fact | Value | Source |
| --- | --- | --- |
| Test cases in SushiEngine | 7 360: 5 479 `Small_`, 1 767 `Medium_`, 114 `Large_`; 12 more are `Benchmark_` cases that `se bench` runs | counted by `grep` over `tests/` and `modules/` on 2026-10-30; the 12 checked by name |
| Test files and programs | 1 086 files, 135 programs | same count; `BUILD_THROUGHPUT/REPORT.md` |
| Large tier at `-O3` | 4 737 s; "hours" on the owner's machine | `BUILD_THROUGHPUT/SPEC.md`, D6; the owner |
| Measured run time of the small and medium tiers | not known | no document records it; the engine is not built on this machine |
| What `testing` limits | each test's timeout: 60, 300, 900 s | `skills/testing/SKILL.md` |
| What `testing` does not limit | the number of cases, a module's total, the default run's total | |

Three gaps follow.

1. **A timeout is a hang detector, not a budget.** A suite of 7 000 tests that each finish in
   59 s passes every rule.
2. **"Every behaviour of the public surface gets a test" has no upper bound.** An agent that wants
   to be thorough has no reason to stop.
3. **Nothing tells an agent that a test it adds costs the owner's time.** The cost is paid later,
   by someone else, in a number nobody shows the agent.

### What the literature says

Searched on 2026-10-30. Where I could not read the primary source, the line says so.

- **Sizes and timeouts.** Bazel gives small 60 s, medium 300 s, large 900 s and enormous 3 600 s,
  and allows any size with any timeout.
  ([Bazel test encyclopedia](https://bazel.build/reference/test-encyclopedia)) Google's own post
  defines sizes by what a test may touch, not by time.
  ([Test Sizes, secondary summary](https://documentdrivendx.github.io/helix/research/google-test-sizes/))
- **Larger tests are flakier.** A secondary summary of a Google study reports weekly flaky rates of
  0.5% for small, 1.6% for medium and 14% for large tests. I could not read the Google posts' bodies,
  so the figures are unverified.
  ([summary](https://www.besthub.dev/articles/analyzing-the-origins-of-flaky-tests-size-tooling-and-instability-at-google-da99e297788a))
- **Running fewer tests per change.** Facebook's predictive test selection halves test
  infrastructure cost while reporting over 95% of individual failures and over 99.9% of faulty
  changes. ([Machalica et al.](https://ar5iv.arxiv.org/html/1810.05286)) Test impact analysis maps
  tests to the code they touch; Fowler's survey reports 60 to 70% time savings for Google's Testar,
  and lists the risks: a map that goes stale, missed non-code dependencies, little saved when a
  widely used function changes.
  ([Fowler](https://martinfowler.com/articles/rise-test-impact-analysis.html))
- **Agent-written tests add cost, not outcomes.** Across six models on SWE-bench Verified, the
  volume of tests an agent wrote did not change whether it solved the task, prompt changes that
  raised or cut test writing did not change the outcome, and the tests were mostly value-printing
  observation, not assertion. ([arXiv 2602.07900](https://arxiv.org/abs/2602.07900)) In 1.2 million
  commits, 36% of agent commits added mocks against 26% for others.
  ([arXiv 2602.00409](https://arxiv.org/abs/2602.00409)) Atlassian found that the generic instruction
  "kill mutants" produced excess tests and that mutant-specific guidance reduced them.
  ([Atlassian](https://www.atlassian.com/blog/development/automating-mutation-coverage-with-ai))
- **Not found:** a published project that caps total suite time or the number of tests per change.
  The budget below has no precedent I could cite. Its numbers are the owner's and are calibrated
  by measurement, not derived.

## Decision

The owner decided on 2026-10-30:

1. A test has a definition, and a test that does not meet it is not written.
2. Tests have value rules, written as concrete directions, not as "write fewer".
3. Time is a budget with the limits in the table under "Budget".
4. The budget is measured by the machine. An agent reads the result and does not time anything.
5. Matter's tests are reworked in their own piece of work and are outside this one.

Decided by the engineer on the owner's instruction to decide:

6. An agent merges or deletes only tests it added itself. It reports old tests that look
   redundant and does not touch them, because deleting what it did not create is the owner's
   decision.
8. The owner ruled on 2026-10-30 that every project CLI runs alike. The test command moves into
   `sushicore` as one shared command, `sushitrack` is the pilot, and SushiEngine adopts it after the
   measured run (RW-36, RW-37, RW-38, RW-39).
7. A `fix` commit may add up to 5 cases, not 20, because a regression test is the smallest
   reproduction and a `fix` that needs more is a `feat`. It is held to the time budget; if it
   breaks the budget the fix lands and a backlog entry asks for the compression. Decisions 6 and
   7 are the engineer's; the owner may overrule either.

## Design

### What a test is

> A test checks one promise the code makes, with the smallest input that can break it, at the
> cheapest level that can see it, and fails when the promise is broken.

Consequences, written into `testing` as rules:

- A test has at least one assertion. A test that only prints or runs the code is an observation,
  not a test.
- A test's name says the promise. A name that cannot say which defect the test catches means
  there is no test.
- A test that repeats the implementation is not a test. A fully mocked unit checks its mocks.

### Value rules

1. **Cheapest level.** Whatever a `small` test can see is not written as `medium` or `large`.
2. **One promise, one test.** A promise that a higher test already covers is not repeated below it.
3. **Mocks sit at the unit's boundary,** at the network, disk or device. A unit's own module is
   used for real.
4. **A regression test is the smallest reproduction,** a few lines that show the defect, not the
   scenario that exposed it.
5. **Rows, not copies.** The same promise over ten inputs is one parametrised test with ten rows.
6. **Helpers that assert are named `expect_*` or `assert_*`,** so a checker can tell an assertion
   from a call.

**Not when:** rule 3 does not hold when a collaborator inside the module is itself slow or needs a
device; the test then uses a fake with that collaborator's interface. Rule 1 does not hold for a
promise that only shows at a size the cheaper level cannot reach, such as a converged simulation;
that test is `large` with an exemption and the owner's ruling.

Rules 1 to 3 and 5 are judgement. The checker cannot decide them; a reviewer reads them against
the list of added tests that the checker prints. An assertion on a literal, such as
`EXPECT_TRUE(true)`, is a finding.

### Budget

The values live in `tools/settings.py` as constants, so each repository sets its own, and in the
`testing` skill as the table agents read. `copy_shared_tools.py` keeps each repository's
`settings.py`, so a repository takes the constants only by writing them, and a checker that finds
none stays off, as `check_all.py` does for its other optional settings. A test in `tools/tests`
compares the constants with the skill's table and skips when `skills/` is absent. Open question 3
may replace this with a fact marker.

| Limit | Value |
| --- | --- |
| A `small` test | 1 s |
| A `medium` test | 10 s |
| A new `large` test | 120 s |
| The `small` tests of one test program | 10 s in total |
| The `large` tests of one test program | 600 s in total |
| The default run (`small` and `medium`) of a repository | 300 s |
| The whole `large` tier of a repository | 1 800 s |
| Test cases added by one commit | 20; 5 for a `fix` |
| A second test program in a module, added by one commit | 0 without the owner |

The 60, 300 and 900 s timeouts stay; they stop hangs. `large` is for tests that need real
hardware. A test that runs long without hardware is made shorter and is not labelled `large`.

A test program is the unit of a module's budget because the test tree mirrors the source and each
module builds into one program. A new module's first program is the layout's doing and needs no
approval; only a second program in an existing module does.

**What the numbers measure.** In SushiEngine each case is its own CTest test, run as its own
process, so the time CTest reports for a case includes process start, library load and Debug
overhead. The per-test limits count that time. The program total is the sum of its cases' CTest
times. The default run's limit is wall time of the whole run, which `-j` shortens, so the budget
line prints both the sum and the wall time. If start-up alone exceeds a quarter of the `small`
limit on the owner's machine, phase D raises that limit for the repository and records why.

**Counting added cases.** The commit checker counts lines a commit adds that declare a case:
`TEST`, `TEST_F`, `TEST_P` and `TYPED_TEST` in C++, `def test_` in Python, `it(` in TypeScript.
`INSTANTIATE_TEST_SUITE_P` and `pytest.mark.parametrize` add rows, not cases, so a parametrised
case counts once.

**Noise.** Wall time on a loaded machine is not a number to gate on. The rules:

- Counts (cases added, programs added, assertions present) are exact and gate at once.
- A single test fails the gate only if it exceeds its limit in a serial rerun of that test alone.
- A total fails the gate only above 1.25 times its limit. The factor is a placeholder; phase D
  sets it from a real run.
- Every run prints all times, gate or not.

**Existing tests that break a limit** are listed in `tests/budget_exemptions.toml` of the
project: one test name, one backlog ID. The checker fails an entry whose test no longer breaks its
limit and an entry with no open backlog entry, so the list can only shrink. Matter's large tier
goes in it with one backlog entry for the rework.

### Who measures what

| Layer | Where | Does |
| --- | --- | --- |
| Rules and table | `skills/testing/SKILL.md` | The definition, value rules, budget, agent directions |
| Source checks | `tools/testing/check_test_value.py` | An assertion in every test body, no assertion on a literal, no sleep in a `small` test; applies to code written after `K_TEST_VALUE_SINCE`. `Benchmark_` cases are skipped: they are not tests |
| Commit checks | `tools/testing/check_test_additions.py` | Cases added per commit, a second test program added without the owner's line, the list of added tests for the reviewer |
| Budget report | `tools/testing/test_budget.py` | Reads a JUnit file and a map from test name to program, applies the limits, prints the budget line and the findings |
| Measurement | the project's test command | Runs the tests with JUnit output, writes the map at configure time, calls the report, writes the exit code |

CTest's JUnit file names a case and its time, not its program. The project's build writes the map
of suite to program when it configures; `test_budget.py` does not guess it from names.

The budget line the report prints, one line:

```
budget: small 4.1 s of 10 s (core), default 212 s of 300 s, 7 cases added since origin/main
```

Findings are printed under it, one per line, with the test name, its time and its limit.

### The other projects' test commands

Surveyed on 2026-10-30 by reading each CLI's `test` command; sushiruntime, sushiblas and sushiai
only for their options and CTest call, not their build behaviour.

| Project | Default sizes | `--repeat` | Build behaviour before the run | CTest call |
| --- | --- | --- | --- | --- |
| SushiEngine | `small`, `medium` | yes | always builds; `--no-build` skips | `tools.driver.ctest_run` |
| SushiLog, SushiProfiler, SushiDSP | every size, `large` included | no | builds when needed | `CMakeDriver` |
| SushiTrack | not read | yes | returns 1 when the tree is absent or stale | `DRIVER.ctest_run` |
| SushiRuntime | every size but the package; one label only | yes | not read | `_DRIVER.ctest_run` |
| SushiBLAS, SushiAI | not read; SushiAI names a `gating` suite | yes | not read | `ctest_run` |

SushiHub has no `test` command that I found. Two facts matter here.

1. **Every C++ CLI runs CTest through `sushicore`'s `CMakeDriver.ctest_run`.** The JUnit option of
   phase D0 reaches all of them with one release.
2. **The default differs.** Three projects run `large` by default, which the budget cannot allow.
   `testing` states no default today. Phase A2 states it: a project's test command runs `small`
   and `medium` unless a size is named. Each project that differs gets a backlog entry; the budget
   does not wait for them.

`--no-build` runs a binary that may be out of date. A budget line from such a run is printed with
"(not rebuilt)" and never gates.

### Directions to the agent

Written once, in `testing`:

1. Add a new test to the existing test program of its module. A second program in a module needs
   the owner.
2. Run the module's tests through the project's test command and read the budget line it prints for
   them. Do not time anything yourself. The default run's total is printed only when the whole
   default run happened; pre-merge CI runs it, and an agent does not run it to find out.
3. When a limit is broken, merge, parametrise or delete the tests you added in this piece of work
   first. When the cause is an old test, stop adding tests, and write it under "Suggested
   removals" in the work folder's `REPORT.md`; do not touch it.
4. The report lists the tests added and the promise each keeps. The checker prints the list; the
   agent checks it and does not write it from memory.
5. Never run the whole `large` tier. Run the `large` suites of the module you changed with
   `--filter`. The project's command refuses `--label large` without a filter and names the flag
   that runs everything; the owner runs that on the device machine, not an agent per change.

`multi-agent-work` names `testing` for these and restates none of them.

## Objections and answers

The engineer's own list; a reviewer adds to it.

1. **An agent games the count.** It merges ten promises into one test with ten assertions, or
   parametrises everything. *Answer:* value rule 2 forbids the first; a parametrised case counts
   once but its time counts in full, and time is the limit that matters. A reviewer reads the added
   tests; this is not machine-proof.
2. **Many commits dodge a per-commit cap.** *Answer:* the cap is per commit by design, since the
   checkers judge commits; a branch that adds 80 tests in four commits is visible to the list of
   added tests. If it happens, the cap moves to the range since the base.
3. **Branches that each fit alone break the budget together.** *Answer:* the budget gates on the
   merged branch, not on a feature branch's lead.
4. **Timing noise makes the gate flaky.** *Answer:* see "Noise". The gate is report-only until the
   factor is calibrated.
5. **The numbers may be wrong.** The small and medium tiers have never been timed in a document.
   Applied blind, most programs could break their limit and the exemption list would hold the
   whole suite. *Answer:* phase D starts with a measured run on the owner's machine and sets the
   numbers from it. The values above are the owner's start values until then.
6. **The assertion check misreads helpers.** *Answer:* only a body with no `EXPECT_*`,
   `ASSERT_*`, `FAIL`, `SUCCEED`, and no call to an `expect_*` or `assert_*` helper is a finding; a
   body that calls anything else is read by the reviewer.
7. **Mock-at-the-boundary cannot be checked from source.** *Answer:* it stays a reviewed rule. A
   checker's report counts findings and cannot hold a number that is not a gate, so no mock count
   is built; the reviewer reads the list of added tests.
8. **The rules do not shorten the build.** A new test file still costs a compile and may cost a
   link; `BUILD_THROUGHPUT` handles that. *Answer:* out of scope here; direction 1 limits new
   programs, and that is the only overlap.
9. **The checks reward filler and nobody reads the list.** A body of `EXPECT_TRUE(true)` has an
   assertion; the owner's own complaint is that nobody reads. *Answer:* literal assertions are
   findings, and that is all a source check can reach. Whether a test would fail on a broken
   promise is a mutation question. Mutation testing is recorded as a follow-up, since Atlassian
   uses mutation coverage to find tests that check nothing.
10. **The `fix` label is a loophole.** Any new test can be called a regression test. *Answer:* a
   `fix` commit has a cap of 5 and the time budget; nothing proves the test failed before the fix,
   and the skill's bug fix order already makes the agent show that. A reviewer checks it.
11. **Selecting which tests run (impact analysis, prediction) is the larger saving** and is not in
   this piece. *Answer:* it has a setup cost and a stale-map risk, and it works better on a suite
   that has first been made small. It is recorded as a follow-up in the backlog.

## Phases

| Phase | Holds | Where |
| --- | --- | --- |
| A | Rules, table and constants; the drift test; changelog line | SushiSkills |
| B | `check_test_value.py` and `check_test_additions.py`, with their tests, wired into `check_all` | SushiSkills |
| C | `test_budget.py` and its JUnit fixture tests | SushiSkills |
| D0 | Done: `CMakeDriver.ctest_run` takes `output_junit`, released as `v0.10.6` | SushiCore |
| D0b | `register_test_command`: the shared test command with the JUnit file, the budget line, the default sizes and the `large` guard (RW-38) | SushiCore |
| D | Measured run on the owner's machine; numbers set; `se test` writes JUnit, prints the budget line and refuses `--label large` without a filter; exemptions file; the engine's docs follow; report-only for a trial period, then the gate | SushiEngine |
| E | Close: `RW-35` closed, follow-up entries opened, changelog, work folder deleted by its grace rule | SushiSkills |

## Open questions

1. Which module's `large` tests took 700 s, in which build type, and how long does the default
   run take? The first sizes the large limits; the second decides whether 300 s is reachable.
   Phase D1 answers both.

Answered by phase A1 on 2026-10-30, and now part of the design:

- A project's command may call a shared script. `se check` in SushiEngine runs the scripts under
  `tools/` by path with `subprocess.run([sys.executable, ...])` from one registry
  (`cli/sushiengine/services/checks.py`). `se test` calls `test_budget.py` the same way.
- A skill can be a fact home: `check_docs_facts.py` scans every `.md` outside `.git`,
  `third_party`, `node_modules` and `build`, and `skills/commits/SKILL.md` holds one. Facts are
  Markdown to Markdown, so the budget constants in Python still need the drift test.
- SushiEngine's CTest call is `tools.driver.ctest_run`, which is `sushicore`'s `CMakeDriver`, in
  another repository, and takes no JUnit option. Phase D0 adds one.
