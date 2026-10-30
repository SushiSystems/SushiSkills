---
name: repository-layout
description: Use when creating a Sushi Systems repository, adding a module, file or top-level folder, moving code between folders, or when a file seems to have no obvious home.
---

# Repository Layout

Every repository has the same tree, so a file's path says what it is before it is opened.

## The root

The root holds only what a tool refuses to find anywhere else.

```
README.md  LICENSE  NOTICE.md  COMMERCIAL.md  CMakeLists.txt  CMakePresets.json  AGENTS.md
CLAUDE.md  sushi-module.toml  .clang-format  .editorconfig  .gitignore  .gitattributes
.config/  .github/  cmake/  cli/  tools/  modules/  tests/  applications/  assets/  third_party/
docs/
```

| Entry | Holds |
| --- | --- |
| `README.md` | The front page; its shape is in `documentation`, section "The root README" |
| `NOTICE.md` | Third-party components, ported files and redistributed binaries; see `dependencies` |
| `COMMERCIAL.md` | How a company obtains a commercial licence; absent from a closed repository |
| `CMakeLists.txt` | `project()`, options and `add_subdirectory`; no logic |
| `CMakePresets.json` | The configure presets, when the project has them; CMake reads them from the root only |
| `AGENTS.md`, `CLAUDE.md` | Agent instructions and skill declarations; names the skills the repository follows |
| `sushi-module.toml` | The module manifest the stack's tooling reads from the root |
| `.config/` | Configuration a flag or a key can point a tool at, such as `doxygen/Doxyfile` and `docker/Dockerfile`; its `README.md` has one row per file, naming the tool and the call site that passes the path |
| `.github/` | What GitHub resolves by name: workflows, templates, `SECURITY.md` and `CODE_OF_CONDUCT.md`; the last two are SushiSkills' own, copied unchanged by `copy_shared_tools.py` and edited only there |
| `cmake/` | Every CMake function and the layer table |
| `cli/` | The project CLI package, with its own `pyproject.toml` |
| `tools/` | Manual checkers; see `project-tools` |
| `modules/` | Source, one tree per module |
| `include/`, `source/` | Source of a one-module repository, in place of `modules/` |
| `tests/` | Every test, in a tree that mirrors the source; see `TESTS.md` |
| `applications/` | Executables, one folder each; example programs under `applications/examples/`, probes under `applications/probes/`, scenario benchmarks under `applications/benchmarks/`; which kind a program is comes from `testing` |
| `assets/` | Content an application loads at run time and the package ships; absent when there is none |
| `third_party/` | Vendored code, outside this discipline |
| `docs/` | Everything written in prose; see `documentation` |

Forbidden in the root: `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`,
`Doxyfile`, build output, object files, scratch files. Each has a home above.

`pyproject.toml` sits in the root only when the repository is a Python package: pip, uv and
pytest look for it there. In any other repository the CLI's own sits under `cli/`.

A dotfile stays in the root only when its tool refuses to find it anywhere else: clang-format and
EditorConfig walk up from the file being edited, and git reads `.gitignore` and `.gitattributes`
for the folder they sit in. A file a flag can redirect goes to `.config/`.

A repository that holds skills and no modules has `skills/` and `claude/` in place of `cmake/`,
`cli/`, `modules/`, `tests/` and `applications/`. Each skill folder is a module whose `SKILL.md`
is its README. Skills for one organisation alone go in a folder named for it, beside `skills/` and
never inside it, one folder per skill.

## One module or many

The predicate is the module count.

**One module:** source sits directly under the root.

```
include/<Project>/<area>/<name>.hpp
source/<area>/<name>.cpp
tests/<area>/test_<name>.cpp
```

**More than one module:** each module is a tree of its own, and its tests mirror it under
`tests/`.

```
modules/<tier>/<module>/
    README.md
    CMakeLists.txt
    include/<Project>/<module>/<name>.hpp
    source/<name>.cpp
tests/<tier>/<module>/test_<name>.cpp
```

A project that grows from one module to two moves `include/` and `source/` under
`modules/<tier>/<module>/`, moves `tests/<area>/` to `tests/<tier>/<module>/`, and changes
nothing else.

## Read before

| Task | File in this folder |
| --- | --- |
| A header no consumer includes, a header-only module, an internal module | `INTERNAL_MODULES.md` |
| A test, a test folder or a test program | `TESTS.md` |
| A Unity repository | `UNITY.md` |

## Module rules

1. A module owns one responsibility, named by its folder. The name says what the code does. A
   name that would fit any code, such as `utils`, `common`, `helpers`, `shared`, `misc`,
   `support`, `testing` or `test_support`, names no responsibility and is never a module's
   name, with or without a prefix. Code that has no better name is split until each part has one.
   The bottom layer that wraps the platform and the language's primitives is such a module too,
   named by what it wraps: `platform`, `status`, `allocation`.
2. A module's public surface is its `include/` tree. `source/` is private to it. A module whose
   headers its build generates, such as compiled shaders, writes them below
   `generated/<Project>/<module>/` and has no `include/` tree; its users include
   `<Project/module/name.h>` like any other module, and no source header stands in for them.
3. Dependencies point down the tier order declared in `cmake/`. Never sideways into another
   module's `source/`, never up a tier. An edge between two modules of one tier is listed in the
   same `cmake/` table, and the build refuses one that is not. Tiers declared as domains share
   one rank and never include each other; a module named `umbrella` includes its scope without
   listed edges.
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
- A header of free functions holds one family and is named after what the family computes
  (`substep_demand.hpp` holds the terms of the substep demand), never after one of its functions.
- Include path: `<Project>/<module>/<name>.hpp` or `<Project>/<tier>/<module>/<name>.hpp`, always
  with angle brackets. A repository uses one of the two for every module. With the tier in the
  path, a module's name is unique within its tier, so two tiers may each hold a `training`.
- An umbrella header includes every public header of its scope and sits at the include root, in
  a module named `umbrella`. The project's umbrella keeps the project folder's spelling
  (`SushiAI/SushiAI.hpp`), the one file name that is not `snake_case`; a tier's umbrella is
  `<Project>/<tier>.hpp` (`SushiAI/vision.hpp`). An umbrella saves a consumer the writing of
  many includes; no module includes one, except another umbrella.
- Documents under `docs/` are the exception: `UPPER_SNAKE_CASE.md`.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| A `utils/` or `common/` module | Name the responsibility; split it by what each part does |
| A `testing/` or `test_support/` module for shared test code | The same: `test_runner`, `fake_audio_device`, each in the tier of what it depends on |
| A `utils.hpp` header | The same: one header per responsibility, each in the lowest module that uses it |
| Two modules of one tier sharing a header of one of them | Move the header down a tier, into a module both depend on |
| Test data beside the source | `tests/<owner>/fixtures/<name>/` |
| A `unit/`, `integration/` or `regression/` test folder | The mirror in `TESTS.md`; the kind is a label |
| A second CLI or script folder | Everything runnable goes through `cli/` or lives in `tools/` |
| New top-level folder "for now" | It is not allowed; pick a home from the table |
| A `samples/` or `examples/` folder in the root | `applications/examples/` |
| Test input under `assets/` | `tests/<owner>/fixtures/<name>/`; `assets/` holds what ships |
