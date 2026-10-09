---
name: repository-layout
description: Use when creating a Sushi Systems repository, adding a module, file or top-level folder, moving code between folders, or when a file seems to have no obvious home.
---

# Repository Layout

Every repository has the same tree, so a file's path says what it is before it is opened.

## The root

The root holds only what a tool refuses to find anywhere else.

```
README.md  LICENSE  NOTICE.md  COMMERCIAL.md  CMakeLists.txt  AGENTS.md  CLAUDE.md
sushi-module.toml  .clang-format  .editorconfig  .gitignore  .gitattributes
.config/  .github/  cmake/  cli/  tools/  modules/  tests/  applications/  third_party/  docs/
```

| Entry | Holds |
| --- | --- |
| `README.md` | What the project is, one build line, a link to `docs/README.md` |
| `NOTICE.md` | Third-party components, ported files and redistributed binaries; see `dependencies` |
| `COMMERCIAL.md` | How a company obtains a commercial licence; absent from a closed repository |
| `CMakeLists.txt` | `project()`, options and `add_subdirectory`; no logic |
| `AGENTS.md`, `CLAUDE.md` | Agent instructions and skill declarations; names the skills the repository follows |
| `sushi-module.toml` | The module manifest the stack's tooling reads from the root |
| `.config/` | Configuration a flag or a key can point a tool at, such as `doxygen/Doxyfile` and `docker/Dockerfile`; its `README.md` has one row per file, naming the tool and the call site that passes the path |
| `.github/` | What GitHub resolves by name: workflows, `SECURITY.md`, `CODE_OF_CONDUCT.md` |
| `cmake/` | Every CMake function and the layer table |
| `cli/` | The project CLI package, with its own `pyproject.toml` |
| `tools/` | Manual checkers; see `project-tools` |
| `modules/` | Source, one tree per module |
| `tests/` | Tests that cross module boundaries only |
| `applications/` | Executables |
| `third_party/` | Vendored code, outside this discipline |
| `docs/` | Everything written in prose; see `documentation` |

Forbidden in the root: `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`,
`Doxyfile`, `pyproject.toml`, build output, object files, scratch files. Each has a home above.

A dotfile stays in the root only when its tool refuses to find it anywhere else: clang-format and
EditorConfig walk up from the file being edited, and git reads `.gitignore` and `.gitattributes`
for the folder they sit in. A file a flag can redirect goes to `.config/`.

A repository that holds skills and no modules has `skills/` and `claude/` in place of `cmake/`,
`cli/`, `modules/`, `tests/` and `applications/`. Each skill folder is a module whose `SKILL.md`
is its README.

A Unity repository keeps these rules with a different tree and PascalCase names; read `UNITY.md`
in this folder before laying one out.

## One module or many

The predicate is the module count.

**One module:** source sits directly under the root.

```
include/<Project>/<area>/<name>.hpp
source/<area>/<name>.cpp
tests/{unit,integration,regression,common}/
```

**More than one module:** each module is a self-contained tree.

```
modules/<tier>/<module>/
    README.md
    CMakeLists.txt
    include/<Project>/<module>/<name>.hpp
    source/<name>.cpp
    tests/
```

A project that grows from one module to two moves `include/` and `source/` under
`modules/<tier>/<module>/` and changes nothing else.

A header that nothing outside the module includes is private and lives under `source/`, beside
the code that uses it. A private tree of headers, such as a library's kernels, is a folder under
`source/`, never a top-level folder.

A header that another module of the same repository includes, and a consumer must not, cannot
stay under `source/`: rule 3 below forbids the reach. It goes to the `include/` tree of an
internal module. An internal module is marked so in its `CMakeLists.txt`, its headers are never
installed, and its README says so in the first paragraph. A module's `include/` root is installed
whole or not at all, so headers of both kinds are two modules.

## Tests

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

## Module rules

1. A module owns one responsibility, named by its folder.
2. A module's public surface is its `include/` tree. `source/` is private to it.
3. Dependencies point down the tier order declared in `cmake/`. Never sideways into another
   module's `source/`, never up a tier. An edge between two modules of one tier is listed in the
   same `cmake/` table, and the build refuses one that is not.
4. A module is added by creating its folder and one line in its tier's list. If adding it
   requires editing another module, the boundary is wrong.
5. Every module carries `README.md` stating what it owns, what it depends on and its public
   entry points.
6. A module names every module it includes in its build declaration, and is compiled with the
   include roots of those modules only. An include of a module it did not declare then fails to
   compile, which is what makes the boundary real.
7. The tier order is stated once, in `cmake/`. Where a checker needs its own copy, a test
   compares the two.

## Names

- Folders and files: `snake_case`. One primary symbol per header, file named after it
  (`physics_world.hpp` holds `PhysicsWorld`).
- Include path: `<Project>/<module>/<name>.hpp`, always with angle brackets.
- Documents under `docs/` are the exception: `UPPER_SNAKE_CASE.md`.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| A `utils/` or `common/` module | Name the responsibility; split it by what each part does |
| A `utils.hpp` header | The same: one header per responsibility, each in the lowest module that uses it |
| Two modules of one tier sharing a header of one of them | Move the header down a tier, into a module both depend on |
| Test data beside the source | `tests/<kind>/fixtures/` |
| A second CLI or script folder | Everything runnable goes through `cli/` or lives in `tools/` |
| New top-level folder "for now" | It is not allowed; pick a home from the table |
