# Performance: benchmarks and excuses

Read this when writing or placing a benchmark or when a perf claim comes without numbers. The rules are in
`../SKILL.md`.

## Where a benchmark goes

| Shape | Placement detail |
| --- | --- |
| Micro | Beside the unit's tests (see `TESTS.md` in `repository-layout`), in the module's benchmark program; it is placed beside what it measures so it is found there |
| Scenario | In `applications/benchmarks/<name>/`, listed in `applications/benchmarks/README.md`; it is an application, so it goes with the applications |

A scenario's lines `<name> <value> <unit>` or its CSV follow `file-formats`. A probe, from
`testing`, and a scenario benchmark of one subsystem may share its name because they are in
different folders and run through different commands.

## Excuses

- "This is obviously faster." → measure it.
- "One run was enough." → five.
- "I measured in debug." → the build type used for shipping.
- "While I was there I also optimised the neighbour function." → one change per measurement.
