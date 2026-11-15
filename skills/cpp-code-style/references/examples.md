# C++ code style: examples and common mistakes

Read this when you want to see the formatting rules applied, or when reviewing C++ for the
mistakes that recur. The rules themselves are in `../SKILL.md`.

## Formatting in practice

A class: Allman braces, access specifiers one level in, members one level further.

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

A function: a single-statement body on its own line, a longer body in braces.

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

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `struct Utils` with static helpers | Free functions in a namespace named for what they do |
| A header per module that includes everything | Include the exact headers used |
| `bool` return for "failed for some reason" | A status enum naming the reason |
| Boolean parameters (`load(path, true, false)`) | An enum or an options struct |
| A switch over a growing set of kinds that every new kind edits | A table or an interface each kind implements; a small closed set keeps its switch (`sushiskills`, default 1) |
