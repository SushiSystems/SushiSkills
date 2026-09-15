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

- Live under `tests/benchmark/`, named `benchmark_<subject>`.
- Run through the project CLI, never from CMake.
- Print numbers; they never pass or fail a test run.
- State their input size and build type in their output.

## Red flags

- "This is obviously faster." → measure it.
- "One run was enough." → five.
- "I measured in debug." → the build type used for shipping.
- "While I was there I also optimised the neighbour function." → one change per measurement.
