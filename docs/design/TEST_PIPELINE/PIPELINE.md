# Pipeline

Decided on 2026-11-03. Phases F, G and H carry it out.

## Stages

| Stage | When | Runs | Gates |
| --- | --- | --- | --- |
| Pre-merge | Every pull request and push to a branch | The checkers, then `small` and `medium` of the selected modules, shuffled, under AddressSanitizer and UndefinedBehaviorSanitizer on Linux; diff coverage and diff mutation results printed | Yes |
| Nightly | Once a day, on the device machine | `large` of the modules changed since the last nightly; ThreadSanitizer on `medium`; fuzz targets for a fixed time each; coverage; benchmarks against the last nightly | Reports, opens backlog entries |
| Weekly | Once a week, on the device machine | The whole `large` tier | Reports, opens backlog entries |

- Windows and Linux both build and run `small` and `medium` pre-merge.
- A test that fails once and passes on the same commit is quarantined at once; gating never
  retries.
- A stage that skipped a size it was asked to run prints the skip and is not green.
- `large` never runs pre-merge: large tests were flaky in 14% of cases at Google against 0.5% for
  small ones.

## Selection

A change runs the tests of the modules it touches and of every module that depends on them, read
from the module graph the build already has. A per-test impact map is not built: it goes stale and
misses non-code inputs.

## Rework order

Lowest tier first, so each repository's tools and seams reach the ones above it.

| Wave | Repositories |
| --- | --- |
| 0 | sushiskills |
| 1 | sushicore: the shared test command |
| 2 | sushilog, sushiprofiler, sushitrack, sushidsp, sushihub |
| 3 | sushiruntime |
| 4 | sushiblas |
| 5 | sushiai, sushiengine |
| any | sushiweb, project-mobilerts |

sushifx is vendored AMD FidelityFX with no tests and is out of scope.

## Seams found by the survey

Each adds or changes an interface and is approved by the owner in its repository's plan.

| Repository | Seam |
| --- | --- |
| sushiblas | a shape-only tensor for validation; a host engine that runs the reference kernels; index and tail math out of the SYCL launch; ahead-of-time device code or a persistent kernel cache |
| sushiruntime | a clock; a deterministic executor; a host-only graph and plan core; a threadless transport; a fake device |
| sushiai | a host backend under the SushiBLAS engine for tensor values |
| sushiengine | simulation registry and lifecycle without a runtime; serializers on streams; a fake render device; fakes for the audio and platform interfaces |
| sushiprofiler | `Collector` passed in, not reached |
| sushidsp | a clock or trigger for `CounterPollThread`; amp-node tests as rows |
| sushitrack | environment and console out of `config_loader` |
| sushicore, sushihub, sushiskills | subprocess, git, network and the file walk behind interfaces |
| sushiweb | logic out of the large pages; Postgres only in adapter tests |
| project-mobilerts | sizes as `small`, `medium`, `large`; MonoBehaviour logic into the Simulation assemblies |
