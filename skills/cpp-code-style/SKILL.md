---
name: cpp-code-style
description: Use when writing, reviewing or refactoring C++ in a repository - formatting, braces, naming, class shape, includes, error handling, constants or macros.
---

# C++ Code Style

C++17 until a project moves to C++20; nothing from C++20 earlier. Naming: [rules](references/rules.md).
Reviews: [examples](references/examples.md).

- Formatting: `.clang-format` is authoritative: LLVM base, 4 spaces, 100 columns, Allman braces,
  pointers bind to the type. Single-statement body: braces optional, statement on its own
  line. Empty body: `{` and `}` on their own lines, a blank line between, never `{}`.
- Names: `snake_case` files, functions (verb first), locals, parameters, public fields;
  `PascalCase` namespaces, types, aliases, enumerators, template parameters; sized `enum class`; `Detail` internal namespace; `snake_case_` private members; `K_UPPER_SNAKE`
  constants; `<PREFIX>_UPPER_SNAKE` macros. A bool query reads as a question. Acronyms: capitals in `PascalCase`,
  lower case in `snake_case`. No `I` prefix,
  `m_`, Hungarian notation or unexpandable abbreviations.
- Files: `#pragma once`; one primary type per header, definitions in `source/<same_name>.cpp`;
  headers per `source-comments`.
- Includes, grouped by hand, blank line between: own header, standard, third-party, other
  modules, this module; angle brackets, path per `repository-layout`. A header forward-declares what it only names by pointer or
  reference (`build-throughput`, boundary 7).
- Class: `public`, `protected`, `private`, data last; constructors, special members, methods in
  the order a caller uses them. One-argument constructors `explicit`. Special members: rule of zero, else all five. `const`, `noexcept` where they hold;
  `[[nodiscard]]` on results and statuses. Base class: virtual or protected destructor, else `final`. Interfaces abstract, no data. Dependencies via the constructor, no global or singleton.
- Errors: broken precondition `<PREFIX>_ASSERT`, `_VERIFY` or `_FATAL`; external failure a `[[nodiscard]]` `enum class ...Status` or expected; convert third-party throws at the
  module boundary, none leaves a public function. Handle or forward every status; no
  empty `catch (...) {}` (`logging`); no `-1` or `nullptr` sentinel.
- Cheap types by value, others `const&`, sinks by value then moved; hot paths: `performance`.
- `cmake`, `ninja`, `ctest` run only through the repository's CLI (`sushiskills` default 2).
