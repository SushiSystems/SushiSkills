---
name: performance
description: Use when optimising code, claiming a change is faster or lighter, writing a benchmark, choosing a data layout for a hot path, or reviewing a perf commit, in a repository.
---

# Performance

Performance comes second to maintainability and is never guessed. A hot path's structure is
designed in; every change beyond that is measured.

## Designed in, without measuring

For any per-frame, per-element or per-sample path:

- Contiguous storage and handles, not pointer graphs.
- No allocation, locking, logging or virtual dispatch per element.
- Work batched by kind; data laid out for the loop that reads it.
- Data stays on the device that computes it; no read-back to hand it to another device.
- Containers reserved when their size is known.

## Measured, always

An optimisation is a claim and carries evidence.

1. Measure first: same machine, build type and input, at least five runs.
2. Change one thing.
3. Measure again the same way.
4. The commit is `perf(scope): ...`, its body giving both numbers with spread:
   `step: 4.12 ms ± 0.05 → 2.87 ms ± 0.04 (6 runs, release build, 10 000 bodies)`.

An optimisation that does not move the number is reverted, not kept "because it cannot hurt". One
that costs readability must buy a gain worth the cost.

## Benchmarks

Two shapes; test sizes are for tests, a benchmark carries none. Every benchmark runs through the
project CLI, never the build system; prints numbers and never passes or fails a test run; states
its input size and build type.

- **Micro:** one unit's time or memory; beside the unit's tests as `benchmark_<name>.cpp`, labelled
  `benchmark`; run by `<cli> bench`. It gates a change only on a dedicated machine, against that
  machine's baseline and noise, never on a shared runner.
- **Scenario:** a whole subsystem run with its own `main()`, in `applications/benchmarks/<name>/`,
  listed in its `README.md`; run by `<cli> bench <name> -- <options>`. One per subsystem (a variant
  is an option); a meaningful default with no option; every number-changing input is an option;
  reports the median of at least three runs, machine and build, as `<name> <value> <unit>` lines or
  one CSV (`file-formats`); never gates a pull request or release, its numbers go in the release
  report.

A program measuring what a subsystem does, not how fast, is a probe (`testing`); a probe and a
scenario benchmark may share a name.

Red flags, folder placement reasons: `references/benchmarks.md`.
