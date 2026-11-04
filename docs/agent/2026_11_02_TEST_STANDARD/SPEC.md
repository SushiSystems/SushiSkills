# Test standard

**Status:** Open — written; every point decided by the orchestrator on the owner's instruction
**Implements:** `TEST_PIPELINE#A`

## Problem

On 2026-11-02 the first rollout of the test pipeline checked labels and counts and called a
repository done. SushiBLAS came out with every label right and its suite shaped wrong: 602
`small` tests against 2 692 `medium`, and a default run of 1 741 s against a budget of 300 s. The
cause was one shared fixture that opened a SYCL queue for every test. The doctrine said what a
test is and how it is sized, but not how a fixture is scoped, how a numerical promise is checked,
how a flaky test is handled, which tests a change runs, or how a repository is brought to the
standard and accepted.

This SPEC decides those points. Each decision names the one skill that will hold it, because a
rule is stated in one file (`docs/CONTRIBUTING.md`). Nothing here restates a rule a skill already
holds; it cites it.

## What the skills already hold

| Subject | Home |
| --- | --- |
| What a test is, assertions, value rules (the cheapest level first) | `testing` |
| Sizes, timeouts, budget, exemptions, sizes written in source | `testing` |
| Determinism, quarantine, goldens, probes and benchmarks | `testing`, `performance` |
| The mirror, one test program per module, no kind folders | `repository-layout/TESTS.md` |
| Software device `medium`, real device `large` | `gpu-development` |
| CI stages and their budgets, `large` on no runner | `continuous-integration` |
| Who writes what, the job list, the model per dispatch | `multi-agent-work`, `model-routing` |

## Sources

Read on 2026-11-02 by two research dispatches. P is the publisher's own page or paper, S a third
party. Only P sources carry a number into a decision.

| Id | Source |
| --- | --- |
| G1 | Google Testing Blog, "Test Sizes", 2010 (P): small has no network, file, sleep or second thread, 60 s; medium localhost, 300 s; large 900 s |
| G2 | Software Engineering at Google, ch. 12 (P): about 80% unit and 20% broader tests as a rule of thumb; unit tests change only when behaviour does |
| G3 | SWE at Google, ch. 13 (P, read through a summary): prefer the real implementation, then a fake; a fake has contract tests run against the real one too; avoid interaction testing |
| G4 | SWE at Google, ch. 14 (P, summary): large tests run post-submit and may be non-hermetic |
| G5 | Google Testing Blog, "Flaky Tests at Google", 2016 (P): 1.5% of runs flaky, 16% of tests show flakiness, 84% of pass-to-fail transitions involve a flaky test; quarantine can mask a race |
| G6 | Memon et al., "Taming Google-Scale Continuous Testing", ICSE-SEIP 2017 (P): affected targets by reverse dependency; rerunning recent failures selects mostly flaky tests |
| G7 | Ivanković et al., "Code Coverage at Google", FSE 2019 (P): no codebase-wide threshold; changelist coverage computed only when tests pass |
| G8 | Petrović et al., "Practical Mutation Testing at Scale", 2021 (P): mutate changed, covered lines only, one mutant per line |
| B1 | Bazel test encyclopedia (P): timeouts 60, 300, 900, 3 600 s by size; pass or fail is the exit code; tests hermetic; a sharding contract |
| C1 | Chromium CQ and sanitizer docs (P): a curated presubmit set; ASan and MSan on named trybots |
| C2 | ChromiumOS "Breakages and flakes" (P): revert first |
| L1 | LLVM TestingGuide and lit (P): unit and regression tests always pass before commit; retry only through a per-test `ALLOW_RETRIES`, reported as `FLAKYPASS` |
| X1 | xUnit Test Patterns, Fresh and Shared Fixture (P): each test builds its own fixture; an immutable shared fixture before a mutable one |
| F1 | Fowler, "Mocks Aren't Stubs" and "Test Pyramid" (P) |
| N1 | Reference LAPACK testing (P): a dimensionless test ratio against a threshold of about 10 to 100, printed per test; inputs longer than the vector register length |
| N2 | Eigen tests and its numerics notes (P): `EIGEN_SEED`; loose default tolerances are no acceptance criterion for a new kernel |
| N3 | oneMath and oneMKL tests (P): device output compared to a pinned reference BLAS and LAPACK |
| N4 | PyTorch `instantiate_device_type_tests` and OpInfo (P): one test written once, run per device and type, CPU included; per-type `toleranceOverride` |
| N5 | Kokkos CI (P): Serial and OpenMP backends on every pull request; ASan and UBSan jobs, marked `continue-on-error` |
| Z1 | OSS-Fuzz ideal integration and ClusterFuzzLite (P): fuzz targets in the repository, seed corpus versioned, each target runs its corpus as a regression test under sanitizers; pull-request fuzzing 10 minutes, batch fuzzing daily |
| Z2 | Hypothesis, RapidCheck, fast-check docs (P): a CI profile that derandomises, a printed seed, a regression pinned with an explicit example |
| M1 | Microsoft, "Improving developer productivity via flaky test management", 2022 (P): a quarantined test still runs, its failure suppressed, a bug filed; quarantine lifts when the bug closes |
| S1 | Clang sanitizer docs (P): ASan about 2x time; TSan 5 to 15x time and 5 to 10x memory; MSan needs every library instrumented |
| U1 | Unity Test Framework and game-ci (P): EditMode and PlayMode run apart; `-randomOrderSeed` |

## Decisions

### D1. Size stays the only kind label, and small is the default

The size table and Value rule 1 of `testing` hold. The test command also prints the count per
size beside the budget line, and a reviewer asks of each `medium` and `large` suite why it is not
one size lower. There is no target ratio: G2's 80% is a rule of thumb, and the owner ruled that
every test is `small` unless its promise needs more.
**Home:** `testing`, Budget.

### D2. A fixture gives a test only what its promise needs

Each test builds its own fixture (X1). Fixtures form a ladder: host, then device, then scene or
system; a test takes the lowest rung its promise needs, so a check of arguments, shapes, offsets,
dispatch or errors never opens a device, a queue or a thread. A fixture shared between tests is
immutable and its README says why a fresh one costs too much. Mutable state shared between tests
is a defect.
**Home:** `testing`, a new section "Fixtures and doubles".

### D3. Doubles: the real code, then a fake, then a mock

A test uses the unit's real collaborators (Value rule 3). Where one is slow or needs a device, it
uses a fake that implements the same interface, and the fake's contract tests run against the
real implementation as well (G3). A mock that asserts calls is used only where the call is the
promise; otherwise state is asserted (F1).
**Home:** `testing`, "Fixtures and doubles".

### D4. Numerical code is checked against a reference, once per device

- A numerical routine has a host reference: a closed form, a naive implementation, or a pinned
  reference library (N3). Its reference tests are `small`.
- A comparison is a dimensionless ratio against a threshold: the error scaled by the problem's
  size, norm and machine epsilon (N1). The tolerance comes from the routine's error bound and is
  written per type in the test (N4); a library-wide epsilon is no acceptance criterion (N2).
- A device kernel is checked by one test written once and run per device and type, the host CPU
  device included (N4, N5). It is `medium` on a software device and `large` on hardware, and it
  does not repeat the host rows (Value rule 2).
- An input size crosses the vector register length, so vectorised paths are reached (N1).
**Home:** `testing`, a new section "Numerical code"; `gpu-development` cites it.

### D5. Inputs that vary are seeded, printed and replayable

Every random input, every shuffle and every property test prints its seed, and the same seed
replays it (gtest `--gtest_random_seed`, `pytest-randomly`, Hypothesis `--hypothesis-seed`,
RapidCheck `RC_PARAMS`, Unity `-randomOrderSeed`). A property test in CI runs derandomised with a
bounded case count; a failure it found is pinned as an explicit example, never left in its
database (Z2).
**Home:** `testing`, Determinism.

### D6. A flaky test is quarantined at once, still runs, and expires

- One pass and one fail on the same commit makes a test flaky (G5). It is quarantined the day it
  is seen, as Determinism rule 5 of `testing` says.
- A quarantined test still runs in every stage, its failure reported and never gating (M1). Its
  known issue names a fix-by date; on that date it is fixed, or deleted with the owner's ruling.
- Gating stages never retry. A retry exists only in a test's own source, as a named annotation
  with a count, and is reported apart from a pass (L1).
- A change that turns `main` red is reverted first and fixed after (C2).
**Home:** `testing`, Determinism; `continuous-integration`, "When CI fails".

### D7. Pipeline stages

`continuous-integration` keeps the stages; this decision changes what each runs.

| Stage | Runs | Gates |
| --- | --- | --- |
| Pre-merge | Checkers; the build on Windows and on a hosted Linux runner; `small` and `medium` of the changed modules and of every module above them, shuffled with a printed seed; ASan and UBSan over the same set on Linux; each fuzz target's corpus as a regression test | Yes |
| Post-merge | Everything pre-merge runs, over every module; ThreadSanitizer over the `medium` tests that start threads; downstream repositories built against the commit | Yes |
| Nightly | Each fuzz target for a fixed time; line and branch coverage; benchmarks against the last nightly; quarantined tests | Reports and opens backlog entries |
| Release | As `continuous-integration` says; the `large` tier run by the owner on the device machine | Yes |

- Selection is by reverse dependency in the module graph the build already has (G6). Post-merge
  runs everything, so a selection miss is caught within one merge.
- A sanitizer job gates. It is never `continue-on-error` (N5 shows what that costs).
- MemorySanitizer is not run: it needs every library instrumented, the device runtimes included
  (S1).
- A Unity project runs EditMode and PlayMode as two jobs (U1).
- The diff's coverage is printed in the pre-merge summary and never gates (G7).
- Mutation testing runs only on the owner's request, over the changed and covered lines of a
  numerical core module (G8).
**Home:** `continuous-integration`, Stages.

### D8. A fuzz target for every reader of untrusted bytes

A reader of a persistent file format or of untrusted input has a fuzz target beside its tests,
its seed corpus in `tests/<owner>/fixtures/<name>/`, and each crash committed there as an input
its regression test replays (Z1). `testing` already requires the target; D7 sets where it runs.
**Home:** `testing`, "What a change must carry".

### D9. Pins between the organisation's repositories are exact

`api-stability` and `dependencies` require an exact version, and every CLI today pins `sushicore`
by a range (`>=0.10.9,<0.11`). The rule stands. Each repository's stage 4 moves its pin to the
exact release it was tested against, in its own `build(deps)` commit.
**Home:** `api-stability`, unchanged.

## Bringing a repository to the standard

Each repository runs four stages. The orchestrator accepts a stage on its evidence, never on
"checkers green" alone.

| Stage | Output, in the repository's work folder | Accepted when |
| --- | --- | --- |
| 1. Measure | `REPORT.md`: every suite with its size, fixture rung, case count and time from a real run; the counts per size; promises kept twice; fixtures that give more than their tests need; quarantined, skipped and literal tests | Every suite is listed; every number comes from a run |
| 2. Design | `PLAN.md`: each suite's target size and fixture rung, the fixtures to split, the tests to merge or delete with the test that keeps each promise, the default-run time expected | The orchestrator approves; a plan that deletes or merges tests the work did not add waits for the owner (`testing`, Directions 3; doctrine boundary 5) |
| 3. Restructure | Commits that carry out the plan | Every suite sits at its planned size; the default run is within budget, or each excess is in `tests/budget_exemptions.toml`; every promise the plan names is kept by a named test; the suite passes shuffled under two seeds |
| 4. Finish | Determinism, assertion and name fixes; the exact pin; the CI workflows of D7 | Checkers green; the workflow files pass `check_workflows.py`; each sanitizer and shuffle finding is fixed or a backlog entry |

## Jobs

The jobs run in hierarchy order from `PLAN.md` of this folder, as `multi-agent-work` says.

1. The skill text of D1 to D8, by the orchestrator.
2. SushiSkills checkers: the count per size; a reason line for each `medium` and `large` suite if a
   checker can read it.
3. SushiCore: the shared test command prints the counts per size and takes the affected-module
   set; a CI workflow template for D7; then a release.
4. Every repository in tier order, stages 1 to 4: sushilog, sushiprofiler, sushiruntime,
   sushiblas, sushidsp, sushiai, sushitrack, sushiengine. Beside them, with no tier between
   them: sushistack, sushiweb, project-mobilerts. Out of scope: sushicars, sushiconverter,
   project-fs, project-fs-legacy, and sushifx, which is vendored.
5. SushiBLAS and SushiAI were left to the owner for the shared test command (changelog,
   2026-11-01). Their stage 1 runs; their stage 3 waits for the owner's word.

## Open questions

None. The owner asked for every point to be decided.
