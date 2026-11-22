# C++ code style: tables and detail

Full text of the sections that `../SKILL.md` states in brief. `SKILL.md` holds the rules; read
this when a naming, include or class-shape case is unclear.

C++17 until a project moves to C++20. Nothing from C++20 is used before then: no `std::format`,
no concepts, no `std::span`, no designated initialisers. Every file reads as if one person wrote
the whole repository.

## Formatting

The repository's `.clang-format` is authoritative; it encodes these rules.

| Rule | Value |
| --- | --- |
| Base | LLVM |
| Indent | 4 spaces, no tabs |
| Column limit | 100 |
| Braces | Allman: every `{` on its own line, for namespaces, classes, functions, control flow, lambdas with bodies |
| Single-statement bodies | Braces optional; the statement goes on its own line, never on the `if` line |
| Empty bodies | `{` and `}` on their own lines with one blank line between them, never `{}` |
| Access specifiers | Indented one level inside the class, members one level further |
| Pointers and references | Bind to the type: `const Buffer& buffer`, `Node* parent` |

Read `examples.md` for worked examples and common mistakes, when reviewing C++ or
unsure how a rule looks in code.

## Naming

| Kind | Form | Example |
| --- | --- | --- |
| File, folder | `snake_case` | `physics_world.hpp` |
| Namespace | `PascalCase`, project root first | `Project::Physics` |
| Internal namespace | `Detail` | `Project::Physics::Detail` |
| Class, struct, alias | `PascalCase` | `PhysicsWorld`, `BodyID` |
| Enum | `enum class PascalCase` with a sized underlying type | `enum class ShaderStage : std::uint8_t` |
| Enumerator | `PascalCase` | `ShaderStage::Vertex` |
| Function, method | `snake_case`, verb first | `add_body`, `read_wave_file` |
| Local, parameter | `snake_case` | `sample_rate` |
| Private or protected member | `snake_case_` | `pending_bodies_` |
| Public struct field | `snake_case` | `position` |
| Constant (`constexpr`, `static const`) | `K_UPPER_SNAKE` | `K_ECS_LOG_CATEGORY` |
| Template parameter | `PascalCase` | `Real`, `Projection` |
| Macro | `<PREFIX>_UPPER_SNAKE` | `PR_ASSERT`, `PR_LOG_WARN` |

- A query that returns a bool reads as a question: `is_empty`, `has_backward_rule`.
- An acronym keeps its capitals inside a `PascalCase` name: `BodyID`, `BLAS::fold`, never
  `BodyId` or `Blas`. A plural adds a small `s`: `TaskIDs`. In
  `snake_case` it is lower case like any other word: `body_id`, `usm_kind.hpp`.
- No `I` prefix on interfaces, no `m_`, no Hungarian notation, no abbreviations a newcomer
  cannot expand.

## Files

- `#pragma once` in every header.
- One primary type per header; the file is named after it. Its definitions go in
  `source/<same_name>.cpp`.
- File headers follow `source-comments`.

## Includes

Grouped by hand, not auto-sorted, in this order, one blank line between groups:

1. The header this source file implements.
2. Standard library.
3. Third-party.
4. Other modules of this project.
5. This module.

Always with angle brackets, by the include path Names in `repository-layout` gives. A header includes what it uses and
forward-declares what it only names by pointer or reference. That is also what keeps a module
dependency private (`build-throughput`, boundary 7).

## Class shape

1. `public` first, then `protected`, then `private`. Data members last.
2. Inside `public`: constructors and destructor, special members, then methods in the order a
   caller uses them.
3. Single-argument constructors are `explicit`.
4. Special members are all declared or none: rule of zero by default; when a type owns a
   resource or holds a reference, declare all five, deleting what does not apply.
5. `const` on every method that does not change observable state; `noexcept` where it holds.
6. `[[nodiscard]]` on every function whose return value carries a result or a status.
7. A class meant to be derived from has a virtual or protected destructor; otherwise it is
   `final`.
8. Interfaces are abstract classes with pure virtual methods and no data; implementations are
   separate classes in separate files.
9. Dependencies arrive through the constructor, never through a global or a singleton.

## Errors

| Situation | Mechanism |
| --- | --- |
| A broken precondition (a programmer error) | `<PREFIX>_ASSERT` / `<PREFIX>_VERIFY` / `<PREFIX>_FATAL` |
| An operation can fail for a reason outside the program (file, parse, device, network) | Return an `enum class ...Status` or an expected type carrying one; `[[nodiscard]]` |
| A third-party library throws | Catch at the module boundary and convert to a status; exceptions never cross a module's public surface |

- Every status value is handled or explicitly forwarded. A `catch (...) {}` that swallows is
  forbidden; see `logging`.
- No sentinel values (`-1`, `nullptr`) standing in for an error when a status can say what
  happened.

## Passing values

Cheap types by value, everything else by `const&`, sinks by value then moved. Hot-path rules
are in `performance`.

## Tools behind the CLI

`cmake`, `ninja` and `ctest` run only through the repository's CLI (`sushiskills`, default 2).
