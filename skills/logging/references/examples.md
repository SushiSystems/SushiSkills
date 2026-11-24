# Logging: examples and common mistakes

Read this when you want to see a project, a category, a call or an error handler written out, or
when reviewing log calls for the mistakes that recur. The rules are in `../SKILL.md`.

## A project, a category and a call

```cpp
inline constexpr LogProject K_ACME_LOG_PROJECT{"acme", "AC_LOG_LEVEL"};
inline constexpr LogCategory K_ECS_LOG_CATEGORY = make_log_category(K_ACME_LOG_PROJECT, "ecs");

AC_LOG_WARN(K_ECS_LOG_CATEGORY,
            "archetype {} rejected component {}: already {} components, limit {}",
            archetype_id, component_name, count, K_MAX_COMPONENTS);
```

Source: not compiled

## A front

| A front holds | Example |
| --- | --- |
| Its `LogProject`, naming the project and its level variable | `K_ACME_LOG_PROJECT{"acme", "AC_LOG_LEVEL"}` |
| Its ceiling, computed per translation unit | `K_LOG_LEVEL_FLOOR` from `AC_ENABLE_LOGGING` |
| Its macros, each on the logger's front macro | `AC_LOG_WARN(category, ...)` |
| One category per module, in `<module>_log_category.hpp` | `K_MEMORY_LOG_CATEGORY` |

A front never re-exports the logger because one thing keeps one name, and a call such as
`set_log_sink` or `set_log_synchronous` acts on the whole process, which a project-named copy
would hide.

## A failure handled and logged once

```cpp
try
{
    device.wait();
}
catch (const std::exception& error)
{
    AC_LOG_WARN(K_SCHEDULER_LOG_CATEGORY, "wait() threw '{}'; treating the event as complete",
                error.what());
    return EventStatus::CompletedWithError;
}
```

Source: not compiled

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `AC_LOG_ERROR(category, "failed")` | Name the operation, the input and the consequence |
| `INFO` inside the frame loop (a log call once per frame) | A counter plus one `INFO` per interval, or `TRACE` |
| A module logging under another module's category | Declare the module's own category |
| `std::cout`, `printf` or `print` in library code | The logger |
| `logging.info(...)` on the root logger | The module's `_log` |
