# RW-3 Decide where C++ tests live

The row of this entry is in `docs/backlog/GENERAL.md`. This file holds what did not fit the row.

- State: decision
- Done when: the owner has kept the `tests/` mirror, or moved C++ tests into their module at `modules/<tier>/<module>/tests/`

Under study since 2026-10-16. The owner wants the mirror used longer first, so every case is
known. Cases so far: a test that spans several modules, a second target inside a module folder,
a shader twin, a test that reaches a private header.
