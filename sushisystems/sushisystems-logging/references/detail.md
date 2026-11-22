# Sushi Systems logger: detail

Read this when you declare a project or a front or read a record. The rules are in `../SKILL.md`;
the types and calls are in `../INTERFACE.md`.

## Projects

```cpp
inline constexpr Logging::LogProject K_SUSHIENGINE_LOG_PROJECT{"sushiengine", "SE_LOG_LEVEL"};
inline constexpr Logging::LogCategory K_ECS_LOG_CATEGORY =
    Logging::make_log_category(K_SUSHIENGINE_LOG_PROJECT, "ecs");
```

Source: not compiled

## The front

| Part | Example |
| --- | --- |
| `LogProject` | `K_SUSHIRUNTIME_LOG_PROJECT{"sushiruntime", "SR_LOG_LEVEL"}` |
| Ceiling | `K_LOG_LEVEL_FLOOR` from `SR_ENABLE_LOGGING` |
| Macro | `SR_LOG_WARN(category, ...)` |
| Category | `K_MEMORY_LOG_CATEGORY`, in `memory_log_category.hpp` |

Re-exporting means an alias such as `using LogLevel = SushiLog::LogLevel`, or a function such as
`sr_set_log_sink`. One thing keeps one name, and a call such as `set_log_sink` or
`set_log_synchronous` acts on the whole process, which a project-named copy would hide.

## A record

```
[12:04:31.207] [WARN] [sushiruntime.memory] [t3] [usm_allocator.cpp:88] share refused for 64 MiB on device 1; falling back to a host copy
```
