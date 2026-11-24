# C++ code style: examples and detail

Elaboration of the rules in `../SKILL.md`. Read this when a naming, include or class-shape case
is unclear. `examples.md` shows the rules applied and the common mistakes.

## C++20 features not used before the move

`std::format`, concepts, `std::span` and designated initialisers.

## Formatting examples

`const Buffer& buffer` and `Node* parent`: a pointer or reference binds to the type. Allman
braces apply to namespaces, classes, functions, control flow and lambdas with bodies. Access
specifiers are indented one level inside the class, members one level further.

## Naming examples

| Kind | Example |
| --- | --- |
| File, folder | `physics_world.hpp` |
| Namespace | `Project::Physics` (project root first) |
| Internal namespace | `Project::Physics::Detail` |
| Class, struct, alias | `PhysicsWorld`, `BodyID` |
| Enum | `enum class ShaderStage : std::uint8_t` |
| Enumerator | `ShaderStage::Vertex` |
| Function, method | `add_body`, `read_wave_file` |
| Local, parameter | `sample_rate` |
| Private or protected member | `pending_bodies_` |
| Public struct field | `position` |
| Constant (`constexpr`, `static const`) | `K_ECS_LOG_CATEGORY` |
| Template parameter | `Real`, `Projection` |
| Macro | `PR_ASSERT`, `PR_LOG_WARN` |

- Bool queries: `is_empty`, `has_backward_rule`.
- Acronyms in `PascalCase` names: `BodyID`, `BLAS::fold`, never `BodyId` or `Blas`; a plural
  adds a small `s`: `TaskIDs`. In `snake_case` an acronym is lower case: `body_id`,
  `usm_kind.hpp`.

## Includes

Keeping a header's includes to what it names by value keeps a module dependency private.

## Class shape

- The rule of zero is the default. A type that owns a resource or holds a reference declares
  all five special members, deleting what does not apply.
- `const` goes on every method that does not change observable state.
- Implementations of an interface are separate classes in separate files.
