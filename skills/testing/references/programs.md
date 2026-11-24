# Testing: tests, benchmarks, probes and programs

Read this when adding a program that is not a test, or when unsure which of the four kinds one is.
The rules are in `../SKILL.md`; `tools/testing/check_probes.py` enforces where each one goes.

## Tests, benchmarks, probes and programs

Every program a repository runs on purpose is one of four kinds, told apart by what it answers.

| Kind | Answers | Ends with | Located in | Runs through |
| --- | --- | --- | --- | --- |
| Test | Does the code keep its promise? | Pass or fail | `tests/`, with a size | `<cli> test`, by size |
| Benchmark | How fast or how light? | A measurement, no verdict | Beside the unit's tests, or a scenario under `applications/benchmarks/`, from `performance` | `<cli> bench` |
| Probe | What does this device, driver or simulation do? | Numbers or files a person reads, no verdict | `applications/probes/<name>/` | `<cli> probe <name>` |
| Program | How is the library used? | Whatever the program does | `applications/` | `<cli> run` |

A program that decides pass or fail is a test, whatever it measures, written at the size its
hardware needs. A command that only runs tests of one size is `<cli> test --label <size>`, never a
probe.

A probe:

- measures one subsystem, and a subsystem has one probe; a variant is an argument, never a second
  probe;
- has a name no other probe's name starts with;
- returns 0 whenever it ran, and non-zero only when it could not run, saying why on stderr;
- prints each measurement as one line, `<name> <value> <unit>`, or writes its files under one folder
  it names on start;
- takes every input that changes its numbers from its arguments;
- is listed in `applications/probes/README.md` with what it measures and an example run;
- is never added to the test runner and never decides whether CI passes.

A folder holding tests is never named `benchmarks/` or `Probe/`.
