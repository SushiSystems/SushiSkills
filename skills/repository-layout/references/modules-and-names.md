# Module trees, module rules and names

Read this when adding or moving a module, a header or a file, or when a rule in `../SKILL.md` needs its full wording. `../SKILL.md` holds the short form of each rule.

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

Growing from one module to two moves `include/` and `source/` under `modules/<tier>/<module>/`,
moves `tests/<area>/` to `tests/<tier>/<module>/`, and changes nothing else.

## Module rules, full wording

1. A module owns one responsibility, named by its folder: the name says what the code does. A
   name that would fit any code (`utils`, `common`, `helpers`, `shared`, `misc`, `support`,
   `testing`, `test_support`), with or without a prefix, is never a module's name; code with no
   better name is split until each part has one. The bottom layer that wraps the platform and the
   language's primitives is named by what it wraps: `platform`, `status`, `allocation`.
2. A module's public surface is its `include/` tree; `source/` is private to it. A module whose
   build generates its headers, such as compiled shaders, writes them below
   `generated/<Project>/<module>/` and has no `include/` tree; its users include
   `<Project/module/name.h>` like any other module, and no source header stands in for them.
3. Dependencies point down the tier order declared in `cmake/`: never sideways into another
   module's `source/`, never up a tier. A same-tier edge is listed in the same table, and the build
   refuses one that is not. Tiers declared as domains share one rank and never include each
   other; a module named `umbrella` includes its scope without listed edges.
   `tools/layering/check_layering.py` enforces this.
4. A module is added by creating its folder and one line in its tier's list. If adding it
   requires editing another module, the boundary is wrong.
5. Every module carries `README.md` stating what it owns, what it depends on and its public
   entry points.
6. A module declares every module it includes and is compiled with those modules' include roots
   only, so an undeclared include fails to compile.
7. The tier order is stated once, in `cmake/`. Where a checker needs its own copy, a test
   compares the two.

## Names

- Folders and files: `snake_case`. One primary symbol per header, file named after it
  (`physics_world.hpp` holds `PhysicsWorld`).
- A header of free functions holds one family and is named after what the family computes
  (`substep_demand.hpp`), never after one of its functions.
- Include path: `<Project>/<module>/<name>.hpp` or `<Project>/<tier>/<module>/<name>.hpp`, always
  with angle brackets, one form for every module of a repository. With the tier in the path, a
  module's name is unique within its tier, so two tiers may each hold a `training`.
- An umbrella header includes every public header of its scope and sits at the include root, in
  a module named `umbrella`. The project's keeps the project folder's spelling (`Acme/Acme.hpp`),
  the one file name not in `snake_case`; a tier's is `<Project>/<tier>.hpp` (`Acme/vision.hpp`).
  It saves a consumer many includes; no module includes one, except another umbrella.
- Documents under `docs/` are `UPPER_SNAKE_CASE.md`; `check_docs_layout.py` enforces it.
