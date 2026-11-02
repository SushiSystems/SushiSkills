# Pipeline

Decided by the owner on 2026-11-02, who left the choices to engineering judgement. Phases F, G
and H carry it out; phase I brings every repository to it.

## Stages

| Stage | When | Runs | Gates |
| --- | --- | --- | --- |
| Pre-merge | Every pull request and push to a branch | The checkers, then `small` and `medium` of the selected modules | Yes |
| Nightly | Once a day, on the device machine | `large` of the modules changed since the last nightly; coverage | Reports, opens backlog entries |
| Weekly | Once a week, on the device machine | The whole `large` tier | Reports, opens backlog entries |

- A test that fails once and passes on the same commit is quarantined at once, as `testing`
  gives; gating never retries.
- A stage that skipped a size it was asked to run prints the skip and is not green.
- `large` never runs pre-merge. Google's figures put large tests' flaky rate near 14% a week
  against 0.5% for small ones (SPEC, "What the literature says"); in the merge path that is noise.

## What each stage adds beyond the tests

The owner widened the aim on 2026-11-02: the tests must match industrial practice, not only the
budget. Each item follows the practice of Chromium, LLVM and Google's TAP.

| Practice | Stage | Gates |
| --- | --- | --- |
| Windows and Linux both build and run `small` and `medium` | Pre-merge | Yes |
| C++ under AddressSanitizer and UndefinedBehaviorSanitizer, `small` and `medium` | Pre-merge, Linux | Yes |
| C++ under ThreadSanitizer, `medium` | Nightly | Opens backlog entries |
| Test order shuffled with a printed seed (`--gtest_shuffle`, `pytest-randomly`, vitest `sequence.shuffle`) | Every stage | Yes; a failure reruns with the printed seed |
| Tests run in parallel; a test that shares state with another fails the run | Every stage | Yes |
| Fuzz targets for every reader of a persistent file format or untrusted input | Nightly, a fixed time per target | Opens backlog entries; the crashing input becomes a regression test |
| Benchmarks recorded against the last nightly | Nightly | Reports a regression above its noise, never gates |
| Results as JUnit, kept by CI | Every stage | No |

## Selection

A change runs the tests of the modules it touches and of every module that depends on them,
read from the module graph the build already has. A per-test impact map is not built: it goes
stale, misses non-code inputs and needs build infrastructure no repository has. It is
reconsidered only when the pre-merge run exceeds its 300 s budget after phase I.

## Coverage

Line and branch coverage is measured nightly and the diff's coverage is printed pre-merge.
Neither gates. A coverage gate is met by tests that run code without asserting, the observation
tests the literature finds agents write most.

## Not adopted

Mutation testing costs many full runs, and Atlassian found generic mutation goals made agents
write excess tests. A manual run on a numerical core module, such as SushiBLAS or SushiDSP, may be
asked for by the owner.
