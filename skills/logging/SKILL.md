---
name: logging
description: Use when adding, reviewing or removing a log call, a log category, a log level, a sink or a logger, or when handling an error or a fallback that might need to be recorded, in a Sushi Systems repository.
---

# Logging

A log records what the program decided. After a failure, a reader must be able to tell what
happened, with which values, in which module and thread, and what the program did next, without
a debugger, and follow one project's records through a process that loads several. A level
that is off costs nothing.

`tools/logs/check_logging.py` enforces the rules a checker can see. It reads the project's
macro prefix and the paths that may write to the console from `tools/settings.py`.

## Shape

| Part | Rule |
| --- | --- |
| Logger | SushiLog, one shared library that every Sushi library links directly, never through another Sushi library. A process loads it once, so it holds one queue, one thread and one sink whatever it loads. A plug-in a host may load twice links SushiLog's static target, whose symbols are hidden, and joins the host as "Meeting another logger" says. SushiLog is the only code that writes a record |
| Front | Every project keeps its own macros, `LogProject`, categories and environment variable, and writes through SushiLog. It adds no queue, thread or sink. A new project extends the logger by declaring categories, never by changing it. What a front holds and what it never does is "Fronts" below |
| Project | A value holding the project's name and the environment variable that sets its levels, declared once per project: `K_<PROJECT>_LOG_PROJECT` |
| Category | A project and a module. Each module declares one, named after its folder, in `<module>_log_category.hpp`: `K_<MODULE>_LOG_CATEGORY`. A module logs only under its own |
| Call | `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)`, where `<PREFIX>` is the project's macro prefix |
| Format | SushiLog's formatter: each `{}` takes the next argument through `operator<<`, `{{` and `}}` are literal braces, no format specs. A value that needs width, precision or hex is formatted into a string before the call. No `std::format`, no concatenation at the call site. Text built outside a log call, such as an error message, uses the one general formatter of the lowest Sushi library the project links; a project never keeps a formatter of its own |

```cpp
inline constexpr Logging::LogProject K_SUSHIENGINE_LOG_PROJECT{"sushiengine", "SE_LOG_LEVEL"};
inline constexpr Logging::LogCategory K_ECS_LOG_CATEGORY =
    Logging::make_log_category(K_SUSHIENGINE_LOG_PROJECT, "ecs");

PX_LOG_WARN(K_ECS_LOG_CATEGORY,
            "archetype {} rejected component {}: already {} components, limit {}",
            archetype_id, component_name, count, K_MAX_COMPONENTS);
```

Source: not compiled

## Fronts

A project's front is the part of logging that belongs to the project, in its foundation module.

| A front holds | Example |
| --- | --- |
| Its `LogProject`, naming the project and its level variable | `K_SUSHIRUNTIME_LOG_PROJECT{"sushiruntime", "SR_LOG_LEVEL"}` |
| Its ceiling, computed per translation unit | `K_LOG_LEVEL_FLOOR` from `SR_ENABLE_LOGGING` |
| Its macros, each on `SL_LOG_FRONT_AT` | `SR_LOG_WARN(category, ...)` |
| One category per module, in `<module>_log_category.hpp` | `K_MEMORY_LOG_CATEGORY` |

A front never re-exports SushiLog: no alias of a SushiLog type (`using LogLevel =
SushiLog::LogLevel`), no `using` of a SushiLog name into the project's namespace, no function or
C function that only forwards to SushiLog (`sr_set_log_sink`). Code names SushiLog's types and
calls as `SushiLog::...` and `sl_...`. One thing keeps one name; and a call such as
`set_log_sink` or `set_log_synchronous` acts on the whole process, which a project-named copy
would hide.

## Levels

Seven levels, in this order. A record passes when its level is at or above the level set for its
category.

| Level | Records | Example |
| --- | --- | --- |
| `TRACE` | Step-by-step flow, for a developer chasing one bug | Every node visited in one graph pass |
| `DEBUG` | Internal state at a decision point | Chosen memory tier and its size |
| `INFO` | A lifecycle event an operator cares about | Device opened, world loaded, 1842 assets cooked |
| `WARN` | The program recovered or fell back; the result may differ from what was asked | Share refused, falling back to a host copy |
| `ERROR` | An operation failed; the caller sees a failure status | Asset file unreadable |
| `FATAL` | The process cannot continue; written just before it terminates | Device lost with no recovery path |
| `OFF` | Nothing; a setting, never a call | |

The level of every category is `WARN` unless something sets it.

## Two gates

A call passes two gates before its arguments are evaluated.

1. **Compile time.** Each translation unit has a ceiling: `ERROR` when `<PREFIX>_ENABLE_LOGGING`
   is defined as 0, `DEBUG` under `NDEBUG`, `TRACE` otherwise. A call past the ceiling compiles
   to `((void)0)`.
2. **Run time.** Each category's level is one atomic. A call past it costs one relaxed load and a
   branch.

`FATAL` and `ERROR` are never compiled out.

## Setting the level

Each project's `<PREFIX>_LOG_LEVEL` sets the levels of that project's categories at the first
log call, and touches no other project's. It takes a level for all of them, then any number of
`module=level` pairs, in any case:

```
SR_LOG_LEVEL=off
SA_LOG_LEVEL=warn,autograd=trace
```

These two lines silence one project and follow one module of another, in the same process. A
value the logger cannot read is reported once on stderr, and that project's levels stay at
`WARN`. In code, `set_log_level(project, level)` sets one project and
`set_log_level(category, level)` sets one category. A call made before the first log call wins
over the environment.

## Record

A record is one line, with no line break inside it:

```
[12:04:31.207] [WARN] [sushiruntime.memory] [t3] [usm_allocator.cpp:88] share refused for 64 MiB on device 1; falling back to a host copy
```

The fields are local time to the millisecond, the level, the project and module of the
category, the thread and the file and line of the call. The thread is a small number the logger
gives each thread on its first record, so one thread's records can be followed through the log.
The sink receives every field apart, as the `LogRecord` of [`INTERFACE.md`](INTERFACE.md), so a
program can send one project's records to their own file and a host can file each field where
its own logging system keeps it.

## Sink

| Rule | Detail |
| --- | --- |
| Default | stderr, one write per record, flushed. Stdout belongs to the program |
| Replacing | `set_log_sink(sink)`; an empty sink restores stderr |
| Thread | Applications deliver from one logger thread. Tests switch to synchronous delivery, which first waits for the queue, so records arrive in order |
| Queue | Bounded. A record that finds it full is dropped and counted, and the next record delivered is preceded by a `WARN` naming how many were dropped |
| Re-entry | A sink never logs and never sets the sink, the level or the mode |
| Failure | A sink that throws loses nothing: the logger writes the exception and the record to stderr |
| `FATAL` | Delivered on the calling thread after the queue is drained, then flushed, before the process ends |
| Exit | The logger is never destroyed, so a call is valid during static initialisation and process exit. At static destruction it stops its thread and delivers what is queued. A process ended without static destruction loses its queue |

## Meeting another logger

A process can hold a logging system besides SushiLog: the host's own, as in Unity, a Python
program or a game with a logging library, or a plug-in's private SushiLog. The program joins
them at start-up, before its first log call, so one of them writes everything.

| Host | Join |
| --- | --- |
| Its own logging system, in C++ | It sets SushiLog's sink to one that hands each record to its system |
| Its own logging system, outside C++ | The same, through the C interface |
| A host that wants its records in SushiLog's stream | It writes them through `log_forward_sink()` |
| A plug-in with a private SushiLog | The plug-in sets its sink to the host's, as either row above |

A sink that belongs to a host is delivered on the calling thread, so the host sees records in
the order they were made. The types, the calls, forwarding and the C interface are in
[`INTERFACE.md`](INTERFACE.md).

## Python

A Python package uses the standard `logging` module under the same rules.

| Part | Rule |
| --- | --- |
| Logger | `_log = logging.getLogger(__name__)` at the top of each module; the module name is the category |
| Levels | The seven levels above. `TRACE` is registered as level 5 and `FATAL` is `CRITICAL` |
| Configuration | Only the program's entry point configures handlers and levels, from `<PREFIX>_LOG_LEVEL` read the same way. A library adds no handler |
| Record | The same line, on stderr |
| Calls | `%s` arguments, never an f-string, so a level that is off formats nothing |

What a command shows the user is output, not a log. It goes to stdout from the command layer
only, which `tools/settings.py` names.

## What is logged

Log an event or a decision:

- a state change of a long-lived object, such as opened, closed or lost;
- a request refused, and why;
- a fallback taken, and to what;
- a resource limit reached;
- every failure status created at a boundary.

Every `WARN`, `ERROR` and `FATAL` answers three questions in one line: what happened, the values
involved, and what the program does now.

## What is not logged

| Not logged | Instead |
| --- | --- |
| Anything per frame, per element or per sample | A counter, reported once per interval |
| Entry and exit of functions | Nothing; use a profiler |
| A failure already carried by a returned status, logged again at every level | Log once, where the status is created |
| Secrets, credentials, personal data | Nothing |
| Prose paragraphs | One line; details in the values |

## Errors and silence

A failure is either returned to the caller as a status or logged where it is handled, never
neither. An empty `catch` or an `except` whose body is only `pass` is forbidden.

A failure is logged once. A helper that makes the failure at a boundary may log it there; then
the code that catches it does not log it again. A macro or helper used everywhere to throw, such
as a check that throws on a false condition, only throws and never logs. A macro that logs on
behalf of its caller takes the caller's category, so its records filter by the module that made
them.

```cpp
try
{
    device.wait();
}
catch (const std::exception& error)
{
    PX_LOG_WARN(K_SCHEDULER_LOG_CATEGORY, "wait() threw '{}'; treating the event as complete",
                error.what());
    return EventStatus::CompletedWithError;
}
```

Source: not compiled

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `PX_LOG_ERROR(category, "failed")` | Name the operation, the input and the consequence |
| `INFO` inside the frame loop | A counter plus one `INFO` per interval, or `TRACE` |
| A module logging under another module's category | Declare the module's own category |
| `std::cout`, `printf` or `print` in library code | The logger |
| `logging.info(...)` on the root logger | The module's `_log` |
