# Industrial testing

**Status:** Open — approved; phases A to C built on 2026-11-03

Replaces the direction of `2026_10_30_TEST_BUDGET` and the design topic `TEST_PIPELINE`. Rules go
into the `testing` skill, enforcement into `tools/testing/`, run mechanics into `sushicore`'s
shared test command, and every repository's tests are reworked against them.

## Problem

The owner's brief of 2026-11-03:

- Every test must be effective and say something about the engine. No pointless tests.
- The small test is written first.
- Tests run as fast and as comfortably as the machine allows. A test of a minor feature that
  takes 4 s on a Ryzen 7600X with an RTX 3080 Ti is a defect.
- Agents must understand why tests matter.
- Every test in every repository is reworked once the rules stand, with deep refactors where the
  code cannot be tested well.

The two earlier attempts limited cost (time budgets, a cap on cases per commit) and required
coverage (one test file per public header). Neither asked what a test proves, and neither
touched the code that made tests expensive. The survey below shows the result.

### What the repositories hold

Surveyed read-only on 2026-11-03 by grep over each tree; nothing was built or timed. Counts are
cases by suite prefix or size mark.

| Repository | Cases | Small | Medium | Large | Main cause of medium |
| --- | --- | --- | --- | --- | --- |
| sushiblas | 2 342 (about 3 000 CTest tests after typed expansion) | 22% | 78% | 2 | device runtime per process; host logic run through the engine |
| sushiruntime | 1 464 | 31% | 69% | 8 | `Runtime::create` in 494 places; no fake device, clock or executor |
| sushiai | 4 578 C++, 701 Python | 71% | 28% | 41 | no host backend under SushiBLAS: 79% of medium cases need the device |
| sushiengine (feature branch) | 6 914 | 74% | 25% | 28 | `create_simulation()` 398 times; serializers go through disk |
| sushidsp | 1 584 C++, 111 Python | 81% | 19% | 0 | — |
| sushiprofiler, sushilog, sushitrack | 956 C++ | 88% | 12% | 0 | process-wide `Collector` singleton (profiler) |
| sushicore, sushihub, sushiskills | 2 287 Python | 31% | 69% | 0 | logic tangled with `tmp_path`, subprocess and git |
| sushiweb | about 2 980 | 212 small and 11 medium describes; about 320 files unmarked | | | real Postgres per package |
| project-mobilerts | 1 476 | sizes written as `unit`, `integration`, `regression` | | | scene loads in PlayMode |

The owner's "about 500 small and 2 500 medium" matches sushiblas.

Facts that hold across every C++ repository:

1. **One process per case.** Every repository registers tests with `gtest_discover_tests`, so
   each case starts a process, loads a tier binary with its device images, and, for medium
   cases, creates the runtime and a SYCL queue. sushiblas builds JIT-only with no persistent
   kernel cache, so each process also recompiles the kernels it touches. No repository records
   test times, so the 4 s figure is not yet split into start-up and work. The cost is inferred,
   not measured.
2. **Medium is mostly a missing seam, not a real need.** Sampled medium cases that need nothing
   but host code: about 70% in sushiblas, 35–45% in sushiengine, 14–25% in sushiai, 150–400 cases
   in sushiruntime. A bulk rename in sushiruntime turned `Unit_` into `Medium_` without reading
   the tests.
3. **Oracles are weak.** sushiai has 1 027 `NEAR` assertions, all with bare absolute epsilons.
   sushiblas has about 170 magic tolerances, while its own rounding-bound helper is used by 11
   files. GEMM is checked with 1e-4 for `double`.
4. **Copy-paste instead of rows.** sushiruntime has no `TEST_P`; sushidsp has none, and each amp
   node repeats the same four test files; sushiblas copies shape × transpose cases by hand.
5. **Filler exists.** `SUCCEED()`-only bodies, `static_assert` run as tests, `EXPECT_NO_THROW`
   around C calls, log-category constants restated, struct defaults read back. The
   one-file-per-header work in sushiruntime added 104 files, 83 of them with one or two tests;
   about 40–50% is filler by the survey's estimate.
6. **Sleeps prove absence.** sushiprofiler sleeps 2.5 s, sushidsp 700 ms, sushiruntime 50 ms,
   each to show that something did not happen. None of those modules takes a clock.
7. **Large scenarios sit in the gate.** sushiengine records one test at 117 s and one at about
   351 s.

The full survey files are kept in the session scratchpad and summarised here; this table is the
record.

## What the literature says

Searched on 2026-11-03. [V] marks a primary source read in full, [A] one read only in its
abstract or table of contents, [U] a claim not verified. A figure marked [U] is not used as a
rule's reason.

### Sizes are constraints, time is a consequence

- Google defines a small test as one process, one thread, no sleep, no I/O, and a medium test as
  one machine with localhost only. Time limits follow from the size, not the other way round.
  [V] [Stewart, Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html);
  [V] [SWE at Google ch. 11](https://abseil.io/resources/swe-book/html/ch11.html)
- Flakiness grows with size: 0.5% of small, 1.6% of medium and 14% of large tests were flaky.
  Binary size (r² 0.82) and memory (r² 0.76) predict flakiness better than the tool. [V]
  [Listfield 2017](https://testing.googleblog.com/2017/04/where-do-our-flaky-tests-come-from.html)
- SWE at Google aims at about 80% narrow-scope, 15% medium, 5% large tests. [V] ch. 11.

### What a test is worth

- Khorikov's four pillars: protection against regressions, resistance to refactoring, fast
  feedback, maintainability. Resistance to refactoring is the one that cannot be traded. Mocks
  are for unmanaged out-of-process dependencies only. [A]
  [Khorikov ch. 1](https://enterprisecraftsmanship.com/files/Unit-Testing-Chapter-1-Excerpt.pdf);
  [V] [When to mock](https://enterprisecraftsmanship.com/posts/when-to-mock/)
- Test through the public interface, test state not interactions, prefer real objects to fakes
  and fakes to mocks; a fake is owned by the owner of the real code. [V] SWE at Google ch. 12–13.
- Beck's Test Desiderata: isolated, composable, fast, inspiring, writable, readable, behavioural,
  structure-insensitive, automated, specific, deterministic, predictive. [V]
  [testdesiderata.com](https://testdesiderata.com/)
- Coverage is not strongly correlated with a suite's effectiveness once suite size is controlled
  for. [V] [Inozemtseva & Holmes 2014](https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf)
  Mutants are a valid substitute for real faults. [V]
  [Just et al. 2014](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014.pdf)
- Google runs mutation testing on the changed lines of a diff, at most one mutant per line,
  skipping lines not worth testing, and shows survivors in code review; tests written only to
  kill mutants on logging or capacity hints are change detectors. [V] Petrović & Ivanković 2018,
  2021 (doi:10.1145/3183519.3183521).
- Test smells (van Deursen 2001; tsDetect's 19 smells) are machine-detectable: empty test, no
  assertion, sleep, print in test, conditional logic, exception handling in place of an expected
  throw, assertion roulette, magic number. [V] [van Deursen](https://ir.cwi.nl/pub/4324/04324D.pdf);
  [V] [tsDetect](https://testsmells.github.io/)

### Oracles for numeric, GPU and engine code

- Reference BLAS tests with N ∈ {0, 1, 2, 3, 5, 9} and fails a case when the dimensionless ratio
  error / (eps · n · |A||B|) exceeds 16; LAPACK uses sizes up to 50 and a threshold of 30. No
  per-test epsilon exists. [V]
  [dblat3.in](https://raw.githubusercontent.com/Reference-LAPACK/lapack/master/BLAS/TESTING/dblat3.in)
- CUTLASS fills inputs with small integers and compares device GEMM to a host reference
  bitwise. [V] [CUTLASS utilities](https://docs.nvidia.com/cutlass/media/docs/cpp/utilities.html)
- Relative and ULP comparisons are meaningless near zero; use a tolerance scaled by the input
  magnitude, and fix the algorithm rather than widen epsilon. [P] Dawson, Comparing Floating
  Point Numbers.
- The oracle problem: specified, derived (metamorphic, differential) and implicit oracles. [V]
  [Barr et al. 2015](https://web.eecs.umich.edu/~weimerw/2018-481/readings/testoracles.pdf)

### Speed and reliability

- Both CMake helpers make one CTest test per case. LLVM moved its unit tests to sharded gtest
  binaries: check-clang-unit went from 177 s to 37 s on Windows and from 46 s to 7 s on Linux.
  [V] [llvm-project#134196](https://github.com/llvm/llvm-project/pull/134196)
- Chromium's launcher runs 10 tests per process by default. [V]
  [unit_test_launcher.cc](https://chromium.googlesource.com/chromium/src/base/+/c3551cc8a93b4487f51c50cf34eb5d9bb881bfa2/test/launcher/unit_test_launcher.cc)
- Causes of flakiness: async wait, concurrency and test order lead; 78% of flaky tests are flaky
  from the day they are written. [V] Luo et al. 2014 (doi:10.1145/2635868.2635920). In Python,
  order dependency causes 59%. [V] [Gruber et al. 2021](https://arxiv.org/abs/2101.09077)
- Only 1.23% of Google's test targets ever caught a breakage. [V] Memon et al. 2017.
- Agents add mocks in 36% of their test commits against 26% for others. [V]
  [arXiv 2602.00409](https://arxiv.org/abs/2602.00409) Tests agents write while solving tasks are
  mostly printed observations, and writing more of them did not change success. [V]
  [arXiv 2602.07900](https://arxiv.org/abs/2602.07900)
- Rare's Sea of Thieves: the vast majority of tests are unit tests; small tests run per
  check-in, multiplayer and performance tests overnight. [U, secondary]
  [GDC 2019](https://gdcvault.com/play/1026366/)

## Decision

The owner decided on 2026-11-03: the brief above. The engineer, on the owner's instruction to
decide, made the rest; the owner may overrule any line.

1. A test is a statement about the code: one promise, one named oracle, the smallest size that
   can see it. Value is proved, not counted.
2. Sizes are defined by what a test may touch. Time limits detect regressions and hangs; they do
   not define a size.
3. Code that cannot be tested small is refactored until it can. The seam comes before the test.
4. Tests run in process in batches, with one shared device per process. One process per case is
   kept only for a test that needs isolation, such as a death test.
5. The per-commit case cap (20, or 5 for a `fix`) and the one-file-per-public-header rule are
   withdrawn. The first counted the wrong thing; the second produced filler. The mirror layout
   stays: a test lives at the path of the code it tests.
6. Mutation testing of the diff becomes the proof that a new test can fail, on code compiled for
   the host. Coverage is printed and never gates.
7. The rework deletes, merges, rewrites and relabels existing tests, including tests the agent
   did not write; the owner confirmed this on 2026-11-03. Each deletion is listed in the
   repository's work-folder report with its reason.
8. `docs/agent/2026_10_30_TEST_BUDGET/` is deleted once this SPEC is approved; what is still true
   in it is here. `docs/design/TEST_PIPELINE/` is rewritten from this SPEC.

## Design

### Why tests matter, for the agent

This text goes into `testing` verbatim, first, before any rule.

> A test is the only part of the code that says what the code promises. When someone changes the
> engine a year from now, the tests are what tell them whether they broke it. A good test fails
> exactly when a promise is broken, says which one, and costs milliseconds. A bad test fails for
> no reason, passes when the code is wrong, or costs seconds, and every one of those teaches the
> people who run it to stop reading test results. A suite of ten thousand tests nobody trusts is
> worth less than a suite of five hundred everyone does. Write the test that a reviewer would be
> sorry to lose, and no other.

### What a test is

A test checks one promise of a public interface, against a named oracle, at the smallest size
that can see the promise, and fails when the promise is broken.

- **Promise.** The test name states it as a sentence: `GemmWithBetaZeroIgnoresNanInC`, not
  `SimpleGemm`. A test whose name cannot say which defect it catches is not written.
- **Oracle.** Where the expected value comes from, and it never comes from running the code
  under test. One of: exact by construction; a host reference; a specified value with its
  derivation in a comment; a metamorphic relation; an implicit oracle (no crash, no sanitizer
  finding) only for a fuzz target or a stress test; a golden file approved by a person.
- **Can fail.** A new test must kill at least one mutant of the code it tests, or reproduce a bug
  that the commit fixes.

### Forbidden tests

The checker rejects each of these in code written after the rule's start date. Old tests are
rejected by the rework, not by the gate.

| Kind | How it is found |
| --- | --- |
| No assertion, or only `SUCCEED()`, `static_assert`, `EXPECT_NO_THROW` / `does not raise` | source scan |
| An assertion on a literal or a value compared with itself | source scan |
| Printing or logging in place of asserting | source scan |
| A sleep or a wall-clock wait (`sleep_for`, `time.sleep`, `setTimeout`, `WaitForSeconds`) | source scan |
| A bare tolerance literal in a floating-point comparison (`EXPECT_NEAR(a, b, 1e-5)`) | source scan |
| A small test that reaches a device, a file, a thread, a socket, the environment or the real clock | include and symbol bans per size, listed per repository in `tools/settings.py` |
| A test that includes a private header or names a `Detail::` symbol | source scan (exists) |
| Control flow (`if`, loop) in a test body outside a row table | source scan, warning |
| A mock of a type the repository owns | review; mock libraries are allowed only in tests of an adapter |
| A test of trivial code: a getter, a default value, a constant, a log category, a version string | review |
| A change detector: asserting how the code works rather than what it promises | review; mutation results show it |
| An expected value pasted from the code's current output | review; allowed only in a test named `Characterization_` that a backlog entry removes |

### Sizes

| Size | May touch | Never | Runs |
| --- | --- | --- | --- |
| `small` | memory of its own process, one thread, injected clock and seed | device, file, socket, thread, sleep, environment, real clock, a singleton | every build, pre-merge |
| `medium` | one machine: the shared device fixture, a per-test temp directory, localhost, threads | sleep, network beyond localhost, a second device context, global state left behind | pre-merge |
| `large` | anything, including whole scenes and real hardware at scale | — | nightly or weekly, never pre-merge |

A medium test exists to check a boundary: that a kernel matches its host reference, that an
adapter writes the bytes its port promises, that two threads hand off correctly. Logic behind the
boundary is tested small. A medium test that would pass with the device replaced by its host
implementation is a small test in the wrong place.

**Shape of a repository's suite:** at least 80% of cases small and at most 5% large. The checker
prints the ratio per module. A module below 80% small is a refactoring finding, not a reason to
add small tests.

### Oracles and tolerances

1. **Exact first.** Integer-valued or dyadic inputs whose result is exact in the type are
   compared bitwise. This is the default for BLAS, DSP and tensor kernels.
2. **Derived tolerance otherwise.** A floating-point comparison goes through a named helper that
   computes `c · f(n) · u · gauge` (for a dot product or GEMM, `n · u · Σ|aᵢbᵢ|`) and reports
   error over bound. The helper fails above a threshold stated once per repository. A bare
   epsilon literal is forbidden. sushiblas's `blas_truth.hpp` is the model and moves to the
   repository's test support for the others to use.
3. **Small shapes.** A routine is tested on the sizes {0, 1, 2, 3, 5, 9}, on tile size ± 1, on
   every transpose and layout, on alpha and beta in {0, 1, other}, and with strides and leading
   dimensions larger than the extent. Large shapes run nightly as large tests.
4. **Device against host.** A device result is checked against the host reference of the same
   routine, never against values captured from a device run.
5. **Special values have their own tests:** NaN, Inf, −0, subnormals, empty extents, aliasing.
6. **Metamorphic relations** where no reference exists: a transposed product, a scaled input, a
   permuted batch, a round trip through a serializer.
7. **Goldens last.** A golden file is the oracle only when nothing above works. An update shows
   the diff to a person.

### Architecture for small tests

These rules go into `testing` and are checked where a scan can see them.

1. **Functional core, imperative shell.** Each module keeps its decisions in code that takes
   values and returns values. Device launch, file access, threads, sockets and the clock live in
   a thin shell around it. sushiruntime's `dispatch_record` is the model: the scheduler's
   decisions pulled out and tested small.
2. **Ports with in-memory adapters.** Every outside dependency is reached through an interface
   the module owns, with a host or in-memory implementation in the same module: clock, random
   seed, file system or stream, executor, transport, device queue, logger and profiler sink. The
   in-memory implementation passes the same contract tests as the real one.
3. **Kernels call host-callable functions.** The arithmetic and index math of a device kernel is
   a function compiled for host and device. The small test calls it on the host; one medium test
   per kernel checks the launch.
4. **No logic reaches a singleton.** A process-wide instance, such as sushiprofiler's
   `Collector::instance()` or ImGui's global context, is passed in at the shell.
5. **Humble edges.** `main`, a MonoBehaviour, a React page, a kernel launcher and a CLI command
   only wire parts together. Logic in them moves into the core.
6. **A deterministic executor for concurrent code.** The runtime takes an executor; tests use a
   single-threaded one that runs a seeded schedule, so a race is reproduced from its seed rather
   than hoped for in a stress loop. Real threads are tested medium, under ThreadSanitizer.
7. **No sleep to prove absence.** A component that waits takes a clock it can be told to advance.

Seams already identified by the survey, each to be approved by the owner in its repository's plan
because each adds or changes an interface:

| Repository | Seam |
| --- | --- |
| sushiblas | a shape-only tensor for validation; a host engine that runs the reference kernels; index and tail math out of the SYCL launch |
| sushiruntime | a clock; a deterministic executor; a host-only graph and plan core; a threadless transport; a fake device |
| sushiai | a host backend under the SushiBLAS engine for tensor values |
| sushiengine | simulation registry and lifecycle buildable without a runtime; serializers on streams; a fake render device; fakes for the audio and platform interfaces that exist |
| sushiprofiler | `Collector` passed in, not reached |
| sushidsp | a clock or trigger for `CounterPollThread` |
| sushitrack | environment and console out of `config_loader` |
| sushicore, sushihub, sushiskills | subprocess, git, network and the file walk behind interfaces so checkers and services test small |
| sushiweb | logic out of the large pages into functions; Postgres only in adapter tests |
| project-mobilerts | MonoBehaviour logic into the Simulation assemblies; `[Test]` by default, `[UnityTest]` with a written reason |

### Running fast

1. **One test program per module**, linking only that module and what it uses. A tier-wide
   program that links every module is split.
2. **Registered in batches.** CTest gets one entry per shard of a program, using
   `GTEST_TOTAL_SHARDS` and `GTEST_SHARD_INDEX`, sized to about 10 s. Per-case results come from
   gtest's XML. `gtest_discover_tests` stays only for a program that needs a process per case.
3. **One device per process.** A gtest `Environment` creates the runtime and the queue once.
   Buffers, engines and graphs are per test, and teardown checks that none leaked. A device
   shard declares `RESOURCE_GROUPS gpus:1`; the CLI writes the resource file.
4. **No recompilation.** Device code is compiled ahead of time for the build's targets, or the
   persistent kernel cache is on for every test run.
5. **Order shuffled** with a printed seed on every run; a failure prints the command that
   reproduces it.
6. **A flaky test is a failing test.** The CLI reruns a failed case once, alone, in a new
   process, and reports a pass on rerun as flaky; the test is quarantined at once with a backlog
   entry. Gating never retries.
7. **Python and TypeScript** run in parallel workers (pytest-xdist, vitest threads). Small tests
   take no `tmp_path` and start no subprocess.

### Time

Times are consequences of the rules above, measured by the shared test command from the XML and
printed every run. They gate after a measured calibration on the owner's machine (Release, 7600X,
3080 Ti); until then they report.

| Measure | Target | Gate after calibration |
| --- | --- | --- |
| A small test | 5 ms median | 100 ms |
| A medium test after the shared fixture | 200 ms | 5 s |
| Shared device fixture, cold | 5 s | 15 s |
| One module's small tests | 2 s | 10 s |
| A repository's pre-merge run (small and medium), wall | 3 min | 10 min |

The 60, 300 and 900 s timeouts stay as hang detectors.

### Proof of value

- **Mutation testing of the diff** on host-compiled code: Mull or an equivalent for C++, mutmut
  for Python, Stryker for TypeScript. Changed lines only, one mutant per line, logging and
  capacity hints skipped. A surviving mutant on a changed line is a finding in review. Device
  code is covered through its host-callable functions (architecture rule 3).
- **Coverage** of the diff is printed pre-merge and measured nightly. It never gates, because a
  coverage gate is met by tests that run code without asserting.
- **Sanitizers** are implicit oracles: AddressSanitizer and UndefinedBehaviorSanitizer on small
  and medium pre-merge on Linux, ThreadSanitizer nightly.
- **Fuzz targets** for every reader of a file format or untrusted input; the corpus replays as a
  small test on every run, the fuzzer runs nightly.

### What an agent does

1. List the promises the change makes before writing a test.
2. For each, choose the smallest size that can see it. If only a medium test can see a promise
   that is logic, refactor the seam first; adding the seam is part of the task, and a new
   interface is the owner's call.
3. Name the oracle. Use the tolerance helper; never type an epsilon.
4. Use rows for the same promise over many inputs.
5. Run the module's tests through the project's test command; read the time line and the
   mutation result it prints. Do not time anything yourself.
6. Report each test added with the promise it keeps and the mutant it kills. The checker prints
   the list; the agent checks it.

## Rework

Each repository gets its own work folder and plan, written when its turn comes, in this order:

1. **Measure.** Turn on JUnit and times in the current suite and record the baseline: counts by
   size, start-up against work, the slowest tests.
2. **Run mechanics.** Batch registration, the shared device fixture, the kernel cache. This
   changes no test and should take most of the 4 s away; it is measured again.
3. **Seams.** The repository's seam table, approved by the owner, built module by module, each
   seam with its contract tests.
4. **Triage every test.** For each module, write its promise list from the public interface, then
   take each existing test: keep, relabel, rewrite, merge into rows, or delete. A deletion names
   the forbidden kind or the duplicate it repeats. Missing promises get tests.
5. **Measure again** and record the before and after in the report.

Order, lowest tier first so each repository's tools and seams reach the ones above it:

| Wave | Repositories | Why first |
| --- | --- | --- |
| 0 | sushiskills | the rules, checkers and the tolerance and size support |
| 1 | sushicore | the shared test command: batching, XML times, shuffle, rerun, resource file |
| 2 | sushilog, sushiprofiler, sushitrack, sushidsp, sushihub | small suites; prove the method |
| 3 | sushiruntime | the executor, clock and fake device the upper tiers need |
| 4 | sushiblas | the host engine sushiai needs |
| 5 | sushiai, sushiengine | the largest suites, on the seams below them |
| any | sushiweb, project-mobilerts | independent stacks |

sushifx is vendored AMD FidelityFX with no tests and is out of scope.

## Phases in SushiSkills

| Phase | Holds |
| --- | --- |
| A | `testing` rewritten from this SPEC; the old budget rules removed; `TEST_PIPELINE` rewritten; `2026_10_30_TEST_BUDGET` deleted |
| B | Checkers: forbidden-kind scan for C++, Python, TypeScript and C#; size bans read from `tools/settings.py`; suite-shape report; registration check; the case cap and mirror-per-header rules removed |
| C | Test support shared by every C++ repository: the tolerance helper and the shared device environment, as a header the projects copy or a module of their own (owner decides where) |
| D | The rework of SushiSkills's own tests: checkers split into a pure core and a file-walking shell, so 36 medium files become mostly small |
| E | Hand-off: the rework waves above, each in its own repository |

## Objections and answers

1. **Mutation testing is slow and our code is SYCL.** It runs on the diff only, on host-compiled
   code. Device code is reached through host-callable functions. If a pilot on sushiblas shows
   it too slow for pre-merge, it moves to nightly on the diff since the last nightly.
2. **One process per test isolated failures; batching lets one test break another.** Shuffling
   with a printed seed finds the coupling; a test that leaks state is a defect and the teardown
   leak check catches device leaks. Death tests and global-state tests keep their own process.
3. **The rework is enormous.** It is. Step 2 changes no test and should give most of the speed
   back early. Seams before triage keeps each triage step a local decision.
4. **New interfaces for seams change public surfaces.** Most are internal to a module. Each one
   that is public goes to the owner in the repository's plan, per the doctrine.
5. **80% small is arbitrary.** It is Google's published aim and matches what sushidsp and
   sushitrack already reach. It is reported, not gated.
6. **Agents will game the promise list.** The mutation result is machine evidence that a test can
   fail; the list makes the reviewer's reading fast.
7. **The time targets are guesses.** They are calibrated by step 1 of the first repositories and
   report until then.

## Open questions

None. Answered by the owner on 2026-11-03: the shared C++ test support lives in SushiSkills and
each repository copies it, as it copies `tools/`; no new repository or module is made. A drift
check keeps the copies equal. The shared device environment is written per repository against
its own runtime, from a pattern `testing` gives.
