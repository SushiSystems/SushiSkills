# Testing: sizes

Read this when choosing a size, writing it in a test, or reading the share of sizes a run prints.
The rules are in `../SKILL.md`.

## Sizes

A size is what a test may touch. Time follows from it; it does not define it.

| Size | May touch | Never | Timeout | Runs |
| --- | --- | --- | --- | --- |
| `small` | the memory of its own process, one thread, an injected clock and seed | a device, a file, a socket, a thread, a sleep, the environment, the real clock, a process-wide instance | 1 s | every build, pre-merge |
| `medium` | one machine: the device the test program made once, a per-test temporary folder, localhost, threads, a software device | making a device, queue or runtime, a sleep, the network beyond localhost, state remaining after the test ends | 10 s | pre-merge |
| `large` | anything, including whole scenes and real hardware at scale | — | 120 s | nightly or weekly, never pre-merge |

A process-wide instance has one exception in a `small` test: a scoped in-memory sink the test installs on
the process-wide logger and that puts the old sink back on exit. The tests of one program run one at a
time, so no other test sees it. A death test is `medium`, since it starts a child process, and so is a
test that replaces a process-wide hook such as the global allocator, scoped by a guard.

The timeouts detect hangs. Each holds for one test case, never for a run; a C++ shard's timeout is its
size's timeout times the number of cases in it. "Time" in `running.md` holds the limits a test is
held to.

**A medium test checks a boundary:** that a kernel matches its host reference, that an adapter writes
the bytes its port promises, that two threads hand a value over. Logic behind the boundary is tested
`small`. A medium test that would pass with the device replaced by its host implementation is a small
test in the wrong place.

**Small first.** A promise is tested at the smallest size that can check it. When only a `medium` test
can check a promise that is logic, the code lacks a seam: add it first (`architecture.md`, "Architecture for small
tests"), then write the `small` test.

**Small before larger, per unit.** The logic a `medium` or `large` test passes through has its
`small` tests first. A unit with a `medium` or `large` test and no `small` test of its logic lacks a
seam; the larger test then checks only its boundary or its scale, never a promise the `small` tests
already keep.

**Suite shape.** The test command prints the share of each size per module. The share is a reading,
never a target: no task, plan or acceptance criterion names a percentage. A module whose tests are
mostly `medium` holds logic that only a device, a file or a thread can reach, so every promise there
is checked on the slowest, flakiest path; the reading shows where a seam is missing. It is never
fixed by adding, splitting or relabelling tests. Work is accepted on what it proves: the logic it
touched runs in tests that reach no file, process, clock or device, each test file keeps the
boundary in one `medium` class, and the mutants on its changed lines are killed.

### Where the size is written

| Language | Where |
| --- | --- |
| C++ | The suite name opens with `Small_`, `Medium_` or `Large_`: `TEST(Small_TensorShape, RejectsANegativeExtent)` |
| Python | `pytest.mark.small`, `medium` or `large` on the test's class, or as `pytestmark` on its file; a `unittest` file that must run without pytest, such as a checker test, sets `K_TEST_SIZE = "small"` at file level, or as a class attribute on the test class, which overrides the file's |
| TypeScript | The `describe` block's name opens with `small:`, `medium:` or `large:` |
| C# (NUnit, Unity) | `[Category("small")]`, `"medium"` or `"large"` on the fixture class; a GameObject made and destroyed in an EditMode test is `small`, and a `[UnityTest]`, a yielded frame or a test that loads a scene is at least `medium` |

The build reads the size from there and sets the label and the timeout; no build file lists suites by
size. A suite with no size fails the build, and in Python fails collection. In Python the timeout
comes from `pytest-timeout`, set by the project's `conftest.py` from the size; in TypeScript the test
configuration sets it from the prefix; in C# the assembly's shared base fixture sets `[Timeout]`.

The rule reaches every test in the repository: `tests/`, `cli/tests/`, `tools/tests/`, a package's
`__tests__/`, a sub-tree such as `gui/tests/`.

`quarantined` is the one label a build file lists by name, because it is a state with a backlog
entry, not a property of the test. A `Benchmark_` suite is a benchmark and carries no size.

`tools/testing/check_test_sizes.py` checks that every test writes its size.
