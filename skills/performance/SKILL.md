---
name: performance
description: Use when optimising code, claiming a change is faster or lighter, writing a benchmark, choosing a data layout for a hot path, or reviewing a perf commit, in a Sushi Systems repository.
---

# Performance

Performance comes second to maintainability and is never guessed. The structure of a hot path is
designed in from the start; every change beyond that is measured.

## Designed in, without measuring

These are defaults for any per-frame, per-element or per-sample path:

- Contiguous storage and handles instead of pointer graphs.
- No allocation, no locking, no logging and no virtual dispatch per element.
- Work batched by kind; data laid out for the loop that reads it.
- Data stays on the device that computes it; no read-back to the host to hand it to another
  device.
- Containers reserved when their size is known.

## Measured, always

An optimisation is a claim, and a claim carries evidence.

1. Measure before changing anything: the same machine, the same build type, the same input, at
   least five runs.
2. Change one thing.
3. Measure again the same way.
4. The commit is `perf(scope): ...`, and its body gives both numbers with their spread:
   `step: 4.12 ms ± 0.05 → 2.87 ms ± 0.04 (6 runs, release build, 10 000 bodies)`.

An optimisation that does not move the number is reverted, not kept "because it cannot hurt".
An optimisation that costs readability must buy a measured gain worth that cost.

## Benchmarks

A benchmark has one of two shapes, told apart by what it measures. Test sizes are for tests; a
benchmark carries none.

| Shape | Measures | Lives in | Runs through |
| --- | --- | --- | --- |
| Micro | One unit's time or memory, one code path | Beside the unit's tests, `benchmark_<name>.cpp` (see `TESTS.md` in `repository-layout`), in the module's benchmark program, labelled `benchmark` | `<cli> bench` |
| Scenario | A whole run of a subsystem, with its own `main()`, options and output | `applications/benchmarks/<name>/`, listed in `applications/benchmarks/README.md` | `<cli> bench <name> -- <options>` |

A micro benchmark sits beside what it measures so it is found there. A scenario benchmark is an
application, so it lives with the applications.

Every benchmark:

- runs through the project CLI, never from CMake;
- prints numbers and never passes or fails a test run;
- states its input size and build type in its output.

A micro benchmark may gate a change only on a dedicated machine, against a baseline measured on
that machine, with a threshold set from that machine's own noise. It never gates on a shared
runner.

A scenario benchmark:

- measures one subsystem, and a subsystem has one scenario benchmark; a variant is an option;
- runs a meaningful default scenario when it is given no option;
- takes every input that changes its numbers from its options;
- reports the median of at least three runs and the machine and build it ran on, as lines
  `<name> <value> <unit>` or one CSV, whose shape follows `file-formats`;
- never gates a pull request or a release; its numbers go into the release report.

A program that measures what a subsystem does rather than how fast it does it is a probe, from
`testing`. A probe and a scenario benchmark of one subsystem may share its name, since they live
in different folders and run through different commands.

## Red flags

- "This is obviously faster." → measure it.
- "One run was enough." → five.
- "I measured in debug." → the build type used for shipping.
- "While I was there I also optimised the neighbour function." → one change per measurement.
