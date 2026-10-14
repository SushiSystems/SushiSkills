# Test tree

Read from the `repository-layout` skill before adding a test, a test folder or a test program.

`tests/` is a mirror of the source. A test's path is found from the path of what it tests, and
the other way round, so nobody has to remember where a test lives.
`tools/testing/check_test_mirror.py` enforces the mirror.

## The mirror

A unit is a public C++ header, or a Python or TypeScript source file. Each unit has one test file,
at the path its owner's folders give it under `tests/`:

| Repository | Unit | Test |
| --- | --- | --- |
| One module | `include/<Project>/<area>/<name>.hpp` | `tests/<area>/test_<name>.cpp` |
| Many modules | `modules/<tier>/<module>/include/<Project>/<module>/<name>.hpp` | `tests/<tier>/<module>/test_<name>.cpp` |
| Application | `applications/<app>/<path>/<name>.hpp` | `tests/applications/<app>/<path>/test_<name>.cpp` |
| Python | `source/<package>/<area>/<name>.py` | `tests/<area>/test_<name>.py` |
| TypeScript | `source/<area>/<name>.ts` | `tests/<area>/<name>.test.ts` |

A Unity repository mirrors under `Assets/<Product>/Tests/`; `UNITY.md` gives that tree.

A test file is named for what it is of: `test_<name>`, and a benchmark `benchmark_<name>`.
TypeScript keeps `<name>.test.ts`, the name vitest finds without configuration.

A Python or TypeScript module is mirrored the same way under `tests/<tier>/<module>/`. A header
with no area, such as the umbrella `include/<Project>/<project>.hpp`, has its test directly under
the owner's folder.

- A private header under `source/`, a Python file whose name starts with `_`, `__init__.py` and
  `index.ts` have no test file of their own. They are tested through the public unit that uses
  them.
- A test that crosses modules belongs to the highest-tier module it uses, in the test file of the
  unit whose behaviour it checks. Dependencies point down, so every such test has one owner.
- A module that grows out of an area of a one-module repository moves its tests with it:
  `tests/<area>/` becomes `tests/<tier>/<area>/`, file names unchanged.

## What else sits in the tree

| Path | Holds |
| --- | --- |
| `tests/<owner>/fixtures/<name>/` | Input data of the tests in `<name>`'s test file |
| `tests/<owner>/goldens/<name>/` | Reference outputs those tests compare against; see `testing` |
| `tests/<owner>/benchmark_<name>.cpp` | The benchmark of a unit, built into the module's benchmark program; see `performance` |
| `tests/package/` | An out-of-tree consumer that builds against the installed package |
| `tests/<owner>/README.md` | Notes the tests of one owner share |

No other folder sits under `tests/`: no `unit/`, `integration/`, `regression/`, `common/` or
scenario folder. Code that the tests of several modules share is a module of its own, mirrored
like any other.

`cli/` and `tools/` are packaged or copied whole, so their tests travel with them: `cli/tests/`
mirrors `cli/` by the same table, and `tools/tests/` holds the checker tests.

## Kinds are labels

Whether a test is unit, integration, regression, golden, benchmark or device-bound is a label on
the test, registered with the test framework and the build, never a folder. The CLI runs a label
(`--label unit`) or a unit (`--for <path>`). The labels and what each requires are in `testing`.

## Programs

- Each module, and each application with tests, builds one test program, through the same build
  function, so every program is linked, labelled and placed the same way.
- A module's test may include the library's umbrella header: it is what a consumer includes. A
  test that includes a higher-tier module's header belongs to that module.
- The umbrella hides a header that forgot one of its own includes. The module's sources, compiled
  with the include roots the module declared, are what catches that, so a header-only module's
  test of each header includes that header first.
