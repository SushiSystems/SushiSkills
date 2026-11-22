# Performance: benchmarks and red flags

Read this when writing or placing a benchmark or meeting a perf claim without numbers. The rules are in
`../SKILL.md`.

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

- runs through the project CLI, never from the build system;
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
