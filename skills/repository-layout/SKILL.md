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

## Module rules

1. A module owns one responsibility, named by its folder.
2. A module's public surface is its `include/` tree. `source/` is private to it.
3. Dependencies point down the tier order declared in `cmake/`. Never sideways into another
   module's `source/`, never up a tier.
4. A module is added by creating its folder and one line in its tier's list. If adding it
   requires editing another module, the boundary is wrong.
5. Every module carries `README.md` stating what it owns, what it depends on and its public
   entry points.

## Names

- Folders and files: `snake_case`. One primary symbol per header, file named after it
  (`physics_world.hpp` holds `PhysicsWorld`).
- Include path: `<Project>/<module>/<name>.hpp`, always with angle brackets.
- Documents under `docs/` are the exception: `UPPER_SNAKE_CASE.md`.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| A `utils/` or `common/` module | Name the responsibility; split it by what each part does |
| Test data beside the source | `tests/<kind>/fixtures/` |
| A second CLI or script folder | Everything runnable goes through `cli/` or lives in `tools/` |
| New top-level folder "for now" | It is not allowed; pick a home from the table |
