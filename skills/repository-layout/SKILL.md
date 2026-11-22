---
name: repository-layout
description: Use when creating a repository, adding a module, file or top-level folder, moving code between folders, or when a file seems to have no obvious home.
---

# Repository Layout

Every repository has one tree: a path says what a file is.

## The root

The root holds only what a tool refuses to find elsewhere; add no other top-level folder.

## One module or many

The module count decides. One module: `include/<Project>/<area>/`, `source/<area>/`,
`tests/<area>/` under the root. More: `modules/<tier>/<module>/` with `README.md`,
`CMakeLists.txt`, `include/<Project>/<module>/`, `source/`; tests in `tests/<tier>/<module>/`.

## Read before

- A header no consumer includes, a header-only or internal module: `INTERNAL_MODULES.md`.
- A test, test folder or test program: `TESTS.md`.
- An entry in the root: `references/root.md`.
- A file with no obvious home, or a review of where one went: `references/common-mistakes.md`.
- Full module trees, rule wording, name rules: `references/modules-and-names.md`.

## Module rules

1. One responsibility, named by the folder. Never `utils`, `common`, `helpers`, `shared`, `misc`,
   `support`, `testing`, `test_support`, prefixed or not; split until each part has a name. The
   bottom layer is named by what it wraps.
2. The public surface is `include/`; `source/` is private. Generated headers go under
   `generated/<Project>/<module>/`, with no `include/`.
3. Dependencies point down the tier order in `cmake/`: never sideways into another module's
   `source/`, never up; a same-tier edge is listed. Domain tiers never include each other;
   `umbrella` needs no listed edges. `tools/layering/check_layering.py` enforces this.
4. A module is added by its folder and one line in its tier's list; needing an edit in another
   module means the boundary is wrong.
5. Every module has `README.md`: owns, depends on, entry points.
6. A module declares every module it includes and sees only those include roots.
7. The tier order is stated once, in `cmake/`; a checker's copy is tested against it.

## Names

- Folders and files `snake_case`; one primary symbol per header, named after it; a free-function
  header is named after what its family computes.
- Include path `<Project>/[<tier>/]<module>/<name>.hpp`, angle brackets, one form per repository.
- An umbrella header sits at the include root, in module `umbrella`; only another umbrella includes it.
- Documents under `docs/` are `UPPER_SNAKE_CASE.md`.
