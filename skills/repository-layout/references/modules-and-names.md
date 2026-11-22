# Module trees, module rules and names

Read this when adding or moving a module, a header or a file, or when a rule in `../SKILL.md` needs its detail.

## One module or many

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

## Module rules, detail

1. Names that fit any code, such as `utils` or `test_support`, are the ones rule 1 rules out. The
   bottom layer that wraps the platform and the language's primitives is named by what it wraps:
   `platform`, `status`, `allocation`.
2. A module whose build generates its headers, such as compiled shaders, writes them below
   `generated/<Project>/<module>/`; its users include `<Project/module/name.h>` like any other
   module, and no source header stands in for them.
3. A same-tier edge is listed in the same table, and the build refuses one that is not. Tiers
   declared as domains share one rank. A module named `umbrella` includes its scope.
6. A module is compiled with the include roots of its declared modules only, so an undeclared
   include fails to compile.

## Names

- `physics_world.hpp` holds `PhysicsWorld`. A header of free functions is named
  `substep_demand.hpp`, never after one of its functions.
- With the tier in the include path, a module's name is unique within its tier, so two tiers may
  each hold a `training`.
- The project's umbrella header keeps the project folder's spelling (`Acme/Acme.hpp`), the one
  file name not in `snake_case`; a tier's is `<Project>/<tier>.hpp` (`Acme/vision.hpp`). It
  includes every public header of its scope and saves a consumer many includes.
- `check_docs_layout.py` enforces the names under `docs/`.
