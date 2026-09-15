---
name: cpp-code-style
description: Use when writing, reviewing or refactoring C++ in a Sushi Systems repository - formatting, braces, naming, class shape, includes, error handling, constants or macros.
---

# C++ Code Style

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
| Include order | Not auto-sorted; grouped by hand (see Includes) |

```cpp
namespace Project::Physics
{
    class PhysicsWorld
    {
        public:
            explicit PhysicsWorld(Execution::Context& context) noexcept;

            void step(double seconds);

        private:
            Execution::Context& context_;
    };
} // namespace Project::Physics
```

```cpp
void PhysicsWorld::step(double seconds)
{
    if (bodies_.empty())
        return;

    for (RigidBody& body : bodies_)
    {
        integrate(body, seconds);
        clamp_velocity(body);
    }
}
```

## Naming

| Kind | Form | Example |
| --- | --- | --- |
| File, folder | `snake_case` | `physics_world.hpp` |
| Namespace | `PascalCase`, project root first | `Project::Physics` |
| Internal namespace | `Detail` | `Project::Physics::Detail` |
| Class, struct, alias | `PascalCase` | `PhysicsWorld`, `BodyId` |
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
- No `I` prefix on interfaces, no `m_`, no Hungarian notation, no abbreviations a newcomer
  cannot expand.

## Files

- `#pragma once` in every header.
- One primary type per header; the file is named after it. Its definitions go in
  `source/<same_name>.cpp`.
- Every file opens with the license block, then the `@file` block (see `source-comments`).

## Includes

Groups in this order, one blank line between groups:

1. The header this source file implements.
2. Standard library.
3. Third-party.
4. Other modules of this project.
5. This module.

Always `<Project/module/name.hpp>` with angle brackets. A header includes what it uses and
forward-declares what it only names by pointer or reference.

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
| The caller broke a precondition (a programmer error) | `<PREFIX>_ASSERT` / `<PREFIX>_VERIFY` / `<PREFIX>_FATAL` |
| An operation can fail for a reason outside the program (file, parse, device, network) | Return an `enum class ...Status` or an expected type carrying one; `[[nodiscard]]` |
| A third-party library throws | Catch at the module boundary and convert to a status; exceptions never cross a module's public surface |

- Every status value is handled or explicitly forwarded. A `catch (...) {}` that swallows is
  forbidden; see `logging`.
- No sentinel values (`-1`, `nullptr`) standing in for an error when a status can say what
  happened.

## Performance defaults

- Pass cheap types by value, everything else by `const&`; sinks by value then move.
- No allocation, virtual dispatch through a map, or logging inside a per-element hot loop.
- Reserve containers whose size is known.
- Prefer contiguous storage and handles (`BodyId`) over pointer graphs.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `struct Utils` with static helpers | Free functions in a namespace named for what they do |
| A header per module that includes everything | Include the exact headers used |
| `bool` return for "failed for some reason" | A status enum naming the reason |
| Boolean parameters (`load(path, true, false)`) | An enum or an options struct |
| A switch over kinds that every new kind edits | A table or an interface each kind implements |
