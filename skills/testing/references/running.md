# Testing: running fast, time and proof of value

Read this when registering tests in a build, changing the test command, reading the time lines or
exemptions, or running mutation, coverage, sanitizers or fuzzing. The rules are in `../SKILL.md`.

## Running fast

Tests run through the project's test command only. These rules shape how the command and the build
register and run them.

1. **One test program per module,** linking that module and what it uses, never a tier.
2. **Batches, not a process per case.** CTest gets one entry per shard of a program, sharded with
   `GTEST_TOTAL_SHARDS` and `GTEST_SHARD_INDEX` to about 10 s each; per-case results come from gtest's
   XML. `gtest_discover_tests` is kept only for a program that needs a process per case, such as
   death tests, and the program says why.
3. **One device per process, made by no test.** The test program makes the runtime and the queue
   once, before the first test, in a gtest `Environment` registered from the program's own `main`,
   and the one fixture base of the module hands them to each test. No test body, fixture `SetUp` or
   helper makes a device, a queue or a runtime; a test that needs one asks the base for it. Buffers,
   engines and graphs are per test, and teardown fails a test that leaks one or leaves a device error
   behind. A fatal device error stops the program rather than run the remaining tests on a broken
   context. A test of logic gets no device at all: it runs on the host implementation of the port. A
   shard that runs on a real accelerator declares `RESOURCE_GROUPS gpus:1`, and the test command hands
   CTest a resource file with one slot per accelerator, so two such shards never share one. A shard on
   a software device needs no slot.
4. **No recompilation.** Device code is compiled ahead of time for the build's targets, or the
   persistent kernel cache is on for every run.
5. **Shuffled.** Every run shuffles with a printed seed; a failure prints the command that
   reproduces it.
6. **Python and TypeScript** run in parallel workers. A small test takes no `tmp_path` and starts no
   subprocess.

## Time

The test command measures and prints these every run, and a run over one fails. An agent reads them
and times nothing itself. A test over its limit is run again alone, and only its time alone is judged,
so the load of a parallel run does not fail it. A run of a tree older than its sources is reported and
never fails, since its times are not the code's.

| Limit | Value |
| --- | --- |
| A `small` test | 100 ms |
| A `medium` test after the shared fixture | 5 s |
| A `large` test | 30 s |
| A repository's pre-merge run (`small` and `medium`), wall | 600 s |

The aims are a `small` test in 5 ms, a `medium` one in 200 ms and a pre-merge run in 3 minutes. A
test already over its limit is listed in the project's `tests/budget_exemptions.toml`, one test name
and one open backlog ID; the reader fails an entry whose test falls to half its limit, so the list
only shrinks and a test that hovers at its limit cannot flip a run.

The project's test command runs `small` and `medium` unless a size is named, and runs `large` only
with a filter or the flag that means everything.

The test command runs in parallel by default: as many tests at once as the machine has cores,
lowered only to keep the run inside the memory limit it prints, and device tests share each device
through the resource groups of rule 3. A serial default is a defect, because the wall time of the
pre-merge run then becomes the sum of every test. A case registered as its own process pays process
and runtime start-up on every case; when that start-up is most of a `small` test's time, the build
registers the cases of a program in shards, each shard one process running its share of the cases.

## Proof of value

- **Mutation testing of the diff** on host-compiled code: changed lines only, one mutant per line,
  logging and capacity hints skipped. A surviving mutant on a changed line is a review finding.
  Device code is reached through its host-callable functions. For Python,
  `tools/testing/mutate_diff.py --base <commit>` runs it on the diff.
- **Coverage** of the diff is printed and measured nightly. It never gates: a coverage gate is met by
  tests that run code without asserting.
- **Sanitizers** are oracles too: AddressSanitizer and UndefinedBehaviorSanitizer on `small` and
  `medium` pre-merge on Linux, ThreadSanitizer nightly. A report is a failure, never suppressed
  without an open backlog entry.
- **Fuzz targets** for every reader of a file format or of untrusted input. The corpus replays as a
  `small` test on every run; the fuzzer runs nightly, and each crash becomes a regression test.
