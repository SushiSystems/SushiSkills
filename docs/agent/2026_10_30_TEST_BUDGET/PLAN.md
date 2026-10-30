# Test budget: plan

**Spec:** `SPEC.md` in this folder. **Rules:** the `testing`, `project-tools`, `documentation` and
`commits` skills. **Runs:** inline, one session per repository, in the order A, B, C, D0, D, E.
Phases A to C and E are in SushiSkills, D0 is in SushiCore, and D is in SushiEngine and needs the
owner's machine. A1, A2, A3, B1 to B3, C1 and D0 are done; `REPORT.md` says where to resume. D0b is new: the shared test
command in `sushicore` (RW-38), then the pilot in `sushitrack` (RW-39), then D1 (RW-37) and SushiEngine.

## Global constraints

- Tests and checkers run through `python tools/check_all.py .`; nothing else reports a task done.
- Every task that changes a rule edits the skill that holds it and no other file restates it;
  `docs/CONTRIBUTING.md` says how.
- Every task that adds or changes a checker changes its test in the same commit and the checker's
  row in `tools/README.md`.
- Each finished task is written into `REPORT.md` of this folder at once, with its commit.
- SushiEngine is not built on this machine. Nothing in phase D claims a measured number until the
  owner's machine has produced it.
- Prose is written under `humanizer`; the changelog line carries the scope `testing`.

## A1. Read before writing

**Files read:** `tools/check_all.py`, `tools/checking/checker.py`, `tools/commits/history.py`,
`tools/commits/check_backlog_trailer.py`, `tools/settings.py`, `tools/documentation/check_docs_facts.py`,
`skills/project-tools/SKILL.md`, `skills/multi-agent-work/SKILL.md`, `skills/module-install/SKILL.md`;
in SushiEngine `cli/sushistack.deps.toml` and the place `cli/sushiengine/services/project.py` gets
its `ctest` runner from.

Answers what the spec leaves open: whether a skill can be a fact home (open question 3), whether a
project's command may call a shared script (open question 2), and where SushiEngine's CTest call
is made. Confirms from the code that `check_all.py` takes a shared checker only through its
`K_CHECKERS` tuple and that `commits_since(root, since)` returns the commits of a range. Writes the
answers to `REPORT.md`; changes no file.

**Acceptance:** open questions 2 and 3 in `SPEC.md` are answered in `REPORT.md`, each with the file
and line that settles it, and the file that must take `--output-junit` is named.

## A2. Rules in `testing`

**Files:** `skills/testing/SKILL.md`.

Adds, in this order, after "What a change must carry": "What a test is", "Value rules", "Budget"
and "Directions to the agent", with the text of the spec's Design section and the table of its
values. Tightens `large` to hardware that needs a device. Adds the `expect_*` and `assert_*` naming
rule to "Sizes, scopes and names". Adds two red flags: "I will cover every branch to be safe" and
"The test prints the value so I can see it".

States the default as a rule: a project's test command runs `small` and `medium` unless a size is
named, and runs `large` only when it is named with a filter or the flag that means everything.

`multi-agent-work` gets one sentence naming `testing` for these directions and nothing else.

**Acceptance:** `check_docs_truth.py` and the paragraph-copy check pass; `grep -rn "20 cases"
skills/` finds the number in `testing` only.

## A3. Constants and the drift test

**Files:** `tools/settings.py`, `tools/tests/test_test_budget_settings.py` (new).

Adds `K_TEST_BUDGET` (the table's ten rows), `K_TEST_VALUE_SINCE` and `K_TEST_ADDITIONS_SINCE`
here. `copy_shared_tools.py` keeps `tools/settings.py`, so the constants do not reach another
repository; each takes them by writing them. The checkers read them with `getattr` and stay off
when they are absent, as `check_all.py` does for `K_EXTRA_TEST_FOLDERS`. The test parses the table
in `skills/testing/SKILL.md`, fails when any value differs from the constant, and skips when
`skills/` is absent. If A1 shows a skill can be a fact home, this task becomes a fact marker and
the test is dropped. Runs after A1.

**Acceptance:** the test passes, and passes again after changing the skill's table by one value
and the constant to match; fails when only one changes; skips in a tree with no `skills/`.

## B1. `check_test_value.py`

**Files:** `tools/testing/check_test_value.py` (new), `tools/tests/test_check_test_value.py` (new).

Rules, each a function in the checker's rule table: a C++ case with no `EXPECT_*`, `ASSERT_*`,
`FAIL`, `SUCCEED` and no `expect_*` or `assert_*` call; a Python test with no `assert`,
`pytest.raises` or `pytest.approx`; a TypeScript `it` with no `expect(`; an assertion on a literal
such as `EXPECT_TRUE(true)` or `EXPECT_EQ(1, 1)`; `sleep_for`, `time.sleep` or `setTimeout` in a
`small` test. Skips `Benchmark_` suites. Applies to the cases that have a line changed after
`K_TEST_VALUE_SINCE`; a repository that sets none is not checked.

**Acceptance:** the test file holds one passing and one failing example per rule per language,
including a body that asserts through a helper, a body that only calls an unnamed helper, a
`Benchmark_` case that is left alone and a tautology that is caught.

## B2. `check_test_additions.py`

**Files:** `tools/testing/check_test_additions.py` (new), `tools/tests/test_check_test_additions.py`
(new).

Reads each commit after `K_TEST_ADDITIONS_SINCE` through `commits_since` in `commits/history.py`.
Counts the lines a commit adds that declare a case, by the rule in the spec's "Counting added
cases". Fails a commit that adds more than 20 cases, or more than 5 when its message type is
`fix`, and a commit that adds a second test program to a module with no
`Test program: <owner, date>` line. Always prints the list of added tests with their names.

**Acceptance:** the test builds a temporary repository with commits for each outcome; the two
limits, a parametrised case counted once, a `Benchmark_` case not counted, a module's first
program, and the program line each have a pass and a fail.

## B3. Wire the checkers in

**Files:** `tools/check_all.py` (the `K_CHECKERS` tuple), `tools/README.md`, `skills/project-tools/SKILL.md`
if it counts the shared checkers.

**Acceptance:** `python tools/check_all.py .` runs both checkers; `tools/README.md` counts them in
its opening line and has a row for each; both skip in a repository whose `settings.py` sets no
`*_SINCE`; this repository passes.

## C1. `test_budget.py`

**Files:** `tools/testing/test_budget.py` (new), `tools/tests/test_test_budget.py` (new),
`tools/tests/fixtures/junit_*.xml` (new).

Reads a JUnit file and the project's map of suite to test program, groups cases by program,
applies `K_TEST_BUDGET`, prints the budget line (sum of times and wall time) and the findings, and
returns the exit code the spec's "Noise" rules give. The noise factor is a parameter with the
spec's 1.25 as its default, so D1 sets it without a code change. The serial rerun is the caller's
job: `test_budget.py` names the tests to rerun and accepts a second JUnit file with their times.
Reads the exemption file and fails a stale entry. Skips `Benchmark_` cases.

**Acceptance:** fixtures for a run inside every limit, a test over its limit that passes its
rerun, one that fails it, a total at 1.2 and 1.3 times the limit, an exempted test, and a stale
exemption; each gives the line and the exit code the spec states.

## D0. JUnit output in `sushicore`

**Files:** `sushicore/cmake_driver.py` in the `sushicore` repository (its source file, not the
`build/lib` copy), its test, its changelog and README line.

`CMakeDriver.ctest_run` gains an optional `output_junit: Path | None = None` that passes
`--output-junit <path>` to CTest, which needs CMake 3.21; SushiEngine's tests set 3.22. The change
is additive, so by `api-stability` the lower tier releases a minor and SushiEngine follows by
raising its pin (`cli/pyproject.toml` holds `sushicore>=0.10.2,<0.11`). The release is the owner's
to cut.

**Acceptance:** a test in `sushicore` shows the argument reaching the command line and being absent
by default; the owner has cut the release before D2 starts.

## D0b. The shared test command in `sushicore`

**Files:** `sushicore` only: a new module for the command, its tests, `docs/reference/COMMAND_SURFACE.md`,
`docs/guides/CLI_INTEGRATION.md`, the changelog.

`register_test_command(app, module)` declares `test` once: `--label`, `--filter`, `--repeat`, `--jobs`;
the default of `small` and `medium`; `--label large` refused without a filter; a JUnit file through
`ctest_run(output_junit=)`; the budget line from `tools/testing/test_budget.py` in the module's root,
skipped when it is absent. A module supplies only its build tree, its environment and its labels.

**Acceptance:** `--describe` of a CLI shows the same `test` options as any other; the module tests show each
behaviour. Then `sushitrack` replaces its own `test` with it (RW-39) and prints a budget line from a real
CTest JUnit file, which is also the first check of the reader of `test_budget.py`.

## D1. Measure

**Where:** the owner's machine; SushiEngine.

The owner runs `ctest --output-junit` for the small and medium tiers and, apart, for the large
tier, in the build type the owner works in, and hands over the two files with the wall time of
each run and the name of the module whose `large` tests took 700 s. Nothing is changed. The agent runs `test_budget.py`
on them with the map from D2's configure step, or with a one-off map from `ctest -N`, writes the
numbers to `REPORT.md`, and proposes the limits and the factor from the data, including whether
process start-up alone breaks the `small` limit.

**Acceptance:** `REPORT.md` holds, per test program, the small total and the slowest three tests;
the default run's sum and wall time; the count of tests and programs over each limit; open
question 1 of `SPEC.md` answered. The owner approves the limits before D2.

## D2. `se test` writes JUnit and prints the budget line

**Files:** `cli/sushiengine/commands/test.py`, `cli/sushiengine/services/project.py` and the file
A1 named for the CTest call, `cmake/TestSizes.cmake` (the suite-to-program map), `cli/config.toml`,
`cli/tests/` (a new test file), `docs/guides/COMMAND_LINE_INTERFACE.md`,
`docs/architecture/TOOLING.md`.

`se test --label large` without `--filter` is refused with exit code 2; the message names the
filter and the flag `--everything`, which runs the whole tier. `se test` passes `output_junit` to
the CTest call, calls the budget report through the route that
open question 2 picked, prints its line last, and exits non-zero only when `cli/config.toml`
sets `test_budget = "gate"`; the default is `"report"` and D4 flips it. The configure step writes
the suite-to-program map beside the build tree. A run with `--filter` prints the line for the
programs it ran and says the default run was not run. `--no-build` and `--suite python` behave as
before. The guide's "60 s each" line is replaced by the limits.

**Acceptance:** the CLI's pytest suite passes with a fixture JUnit file; the guide's `se test`
section and `TOOLING.md` match the command; `git grep` finds no page that states the old figures.

## D3. Exemptions and backlog

**Files:** `tests/budget_exemptions.toml` (new), the backlog through the `backlog` commands.

Every test over a limit in D1 gets one line in the exemptions file and shares a backlog entry per
area. Matter's large tier gets one entry for its rework, which is its own piece of work.

**Acceptance:** `test_budget.py` run on the D1 files passes with the file and fails without it;
every exemption names an open backlog ID.

## D4. Report-only, then the gate

A trial period of the owner's choosing runs with the budget line printed and no exit code. After
it, `se test` exits non-zero on a finding, `check_all.py` runs the two checkers of phase B in the
SushiEngine copy of `tools/`, and the factor is set from the trial's noise.

**Acceptance:** the owner has seen the line on real work and named the end of the trial in
`REPORT.md`; a deliberate over-limit test fails `se test` once and passes after it is cut.

## E1. Copy the tools out

`checking/copy_shared_tools.py --report` lists what differs in each sibling repository; the
owner decides which repositories take the new checkers now.

**Acceptance:** SushiEngine's `tools/` matches this repository's for the files of phases B and C,
except `settings.py`, which holds SushiEngine's own `K_TEST_BUDGET` and `*_SINCE` values.

## E1b. Other projects

SushiLog, SushiProfiler, SushiDSP, SushiTrack, SushiRuntime, SushiBLAS and SushiAI each get a
backlog entry, opened with the `backlog` commands in their own repository, to take the default of
A2, the large-tier guard and the budget line once SushiEngine has run the trial of D4. Where a
project's default differs (SushiLog, SushiProfiler and SushiDSP run `large` by default), the entry
says so.

**Acceptance:** each of the seven repositories has an open entry that names this work folder.

## E2. Close

In one commit, by the orchestrator: `RW-35` closed with the backlog commands; follow-up entries
opened for impact analysis and for mutation testing (the spec's objections 11 and 9) and for the
cap per range if objection 2 happens; the changelog line; the work folder's status dated.

**Acceptance:** `python tools/check_all.py .` passes; the backlog shows `RW-35` closed and the
follow-ups open.
