# The Sushi Systems logger

The `logging` skill names roles: the logger, the front, the format, the host's own logging system.
This page says who fills each role at Sushi Systems. [`INTERFACE.md`](INTERFACE.md) holds the
types and calls.

## The logger

SushiLog is the one logger. It is one shared library that every Sushi library links directly,
never through another Sushi library. A process loads it once, so it holds one queue, one thread
and one sink whatever it loads. A plug-in a host may load twice links SushiLog's static target,
whose symbols are hidden, and joins the host as "Hosts" below says. SushiLog is the only code that
writes a record.

The formatter is `SushiLog::text`, which the logger and every other message share: `format_text`,
where each `{}` takes the next argument through `operator<<`, `{{` and `}}` are literal braces and
there are no format specs. A value that needs a precision, a width, a form or hex goes first through
its helpers: `fixed`, `general`, `scientific`, `hex`, `right`, `left`.

## Projects

| Project | Macro prefix | Level variable |
| --- | --- | --- |
| SushiLog | `SL` | `SL_LOG_LEVEL` |
| SushiRuntime | `SR` | `SR_LOG_LEVEL` |
| SushiAI | `SA` | `SA_LOG_LEVEL` |
| SushiEngine | `SE` | `SE_LOG_LEVEL` |

```cpp
inline constexpr Logging::LogProject K_SUSHIENGINE_LOG_PROJECT{"sushiengine", "SE_LOG_LEVEL"};
inline constexpr Logging::LogCategory K_ECS_LOG_CATEGORY =
    Logging::make_log_category(K_SUSHIENGINE_LOG_PROJECT, "ecs");
```

Source: not compiled

## The front

| A front holds | Example |
| --- | --- |
| Its `LogProject` | `K_SUSHIRUNTIME_LOG_PROJECT{"sushiruntime", "SR_LOG_LEVEL"}` |
| Its ceiling, computed per translation unit | `K_LOG_LEVEL_FLOOR` from `SR_ENABLE_LOGGING` |
| Its macros, each on `SL_LOG_FRONT_AT` | `SR_LOG_WARN(category, ...)` |
| One category per module | `K_MEMORY_LOG_CATEGORY`, in `memory_log_category.hpp` |

A front never re-exports SushiLog: no alias of a SushiLog type (`using LogLevel =
SushiLog::LogLevel`), no `using` of a SushiLog name into the project's namespace, no function or
C function that only forwards to SushiLog (`sr_set_log_sink`). Code names SushiLog's types and
calls as `SushiLog::...` and `sl_...`. One thing keeps one name; and a call such as
`set_log_sink` or `set_log_synchronous` acts on the whole process, which a project-named copy
would hide.

## Hosts

| Host | Join |
| --- | --- |
| Its own logging system, in C++ | It sets SushiLog's sink to one that hands each record to its system |
| Its own logging system, outside C++ | The same, through the C interface |
| A host that wants its records in SushiLog's stream | It writes them through `log_forward_sink()` |
| A plug-in with a private SushiLog | The plug-in sets its sink to the host's, as either row above |

Unity and a Python program are hosts of the second kind.

## A record

```
[12:04:31.207] [WARN] [sushiruntime.memory] [t3] [usm_allocator.cpp:88] share refused for 64 MiB on device 1; falling back to a host copy
```
