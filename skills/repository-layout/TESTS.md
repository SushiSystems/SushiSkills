# Test folders

Read from the `repository-layout` skill before adding a test folder or a test program.

`unit/`, `integration/`, `regression/` and `common/` sit directly under `tests/`, with no level
between. A test kind that builds a different program gets its own folder beside them:

| Folder | Holds |
| --- | --- |
| `tests/benchmark/` | Benchmark programs; see `testing` and `performance` |
| `tests/package/` | An out-of-tree consumer that builds against the installed package |
| `tests/<kind>/fixtures/` | Input data of one test kind |
| `tests/goldens/` | Reference outputs a regression test compares against |

Any other folder under `tests/` names the program it builds and has a `README.md`.

With more than one module, a test of one module lives in that module's `tests/` folder and the
root `tests/` holds only the tests that cross modules.

- Each module with tests builds one test program, through the same build function as the root
  program, so every program is linked, labelled and placed the same way.
- A module test may include the umbrella header of the library: it is what a consumer includes,
  and a test that goes through it tests it too. A test that names a header of a higher-tier
  module by its own path crosses modules and belongs under the root `tests/`.
- The umbrella hides a header that forgot one of its own includes. The module's sources, compiled
  with the include roots the module declared, are what catches that, so a header-only module
  needs one test that includes each of its headers first and alone.
- The notes of a test follow the test: a module's `tests/README.md` holds them, and the root one
  holds what the tests share.
