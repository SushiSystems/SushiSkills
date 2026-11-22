# Performance: benchmarks and red flags

Read this when writing or placing a benchmark or meeting a perf claim without numbers. The rules are in
`../SKILL.md`.

## Where a benchmark lives

| Shape | Placement detail |
| --- | --- |
| Micro | Beside the unit's tests (see `TESTS.md` in `repository-layout`), in the module's benchmark program; it sits beside what it measures so it is found there |
| Scenario | In `applications/benchmarks/<name>/`, listed in `applications/benchmarks/README.md`; it is an application, so it lives with the applications |

A scenario's lines `<name> <value> <unit>` or its CSV follow `file-formats`. A probe, from
`testing`, and a scenario benchmark of one subsystem may share its name because they live in
different folders and run through different commands.

## Red flags

- "This is obviously faster." → measure it.
- "One run was enough." → five.
- "I measured in debug." → the build type used for shipping.
- "While I was there I also optimised the neighbour function." → one change per measurement.
