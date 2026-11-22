---
name: cpp-code-style
description: Use when writing, reviewing or refactoring C++ in a repository - formatting, braces, naming, class shape, includes, error handling, constants or macros.
---

# C++ Code Style

C++17 until a project moves to C++20; nothing from C++20 before (no `std::format`, concepts,
`std::span`, designated initialisers). Naming table, detail: [rules](references/rules.md).
Worked examples and mistakes: [examples](references/examples.md); read when reviewing.

- Formatting: `.clang-format` is authoritative. LLVM base, 4 spaces, 100 columns, Allman braces.
  Single-statement body: braces optional, statement on its own line. Empty body: `{` and `}` on
  their own lines, a blank line between, never `{}`. Pointers bind to the type.
- Names: `snake_case` files, functions (verb first), locals, parameters, public fields;
  `PascalCase` namespaces, types, aliases, enumerators, template parameters; sized
  `enum class`; `Detail` internal namespace; `snake_case_` private members; `K_UPPER_SNAKE`
  constants; `<PREFIX>_UPPER_SNAKE` macros. A bool query reads as a question. Acronyms keep
  capitals in `PascalCase` (`BodyID`, `TaskIDs`), lower case in `snake_case`. No `I` prefix,
  `m_`, Hungarian notation or unexpandable abbreviations.
- Files: `#pragma once`; one primary type per header, definitions in `source/<same_name>.cpp`;
  headers per `source-comments`.
- Includes, grouped by hand, blank line between: own header, standard, third-party, other
  modules, this module. Angle brackets, by the path `repository-layout` gives. A header
  forward-declares what it only names by pointer or reference (`build-throughput`, boundary 7).
- Class: `public`, `protected`, `private`, data last; constructors, special members, methods in
  caller order. Single-argument constructors `explicit`. Special members all or none: rule of
  zero, else all five. `const`, `noexcept` where they hold; `[[nodiscard]]` on results and
  statuses. Derived-from: virtual or protected destructor, else `final`. Interfaces abstract,
  no data. Dependencies via the constructor, never a global or singleton.
- Errors: broken precondition `<PREFIX>_ASSERT`, `_VERIFY` or `_FATAL`; external failure a
  `[[nodiscard]]` `enum class ...Status` or expected type; convert third-party throws at the
  module boundary, no exception crosses a public surface. Handle or forward every status; no
  swallowing `catch (...) {}` (`logging`); no `-1` or `nullptr` sentinel.
- Cheap types by value, others `const&`, sinks by value then moved; hot paths: `performance`.
- `cmake`, `ninja`, `ctest` run only through the repository's CLI (`sushiskills`, default 2).
