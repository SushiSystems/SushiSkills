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
| Logger | One per project that depends on no other Sushi library, in its foundation module, inside its shared library. A project above one of them uses that logger. Where two loggers meet in one process, one forwards into the other, as "Meeting another logger" says, so the process still has one queue, one thread and one sink. The logger is the only code that writes a record |
| Front | Every project above the logger's owner keeps its own macros, categories and environment variable, and writes through the owner's logger. It adds no queue, thread or sink. A new project extends the logger by declaring categories, never by changing it |
| Project | A value holding the project's name and the environment variable that sets its levels, declared once per project: `K_<PROJECT>_LOG_PROJECT` |
| Category | A project and a module. Each module declares one, named after its folder, in `<module>_log_category.hpp`: `K_<MODULE>_LOG_CATEGORY`. A module logs only under its own |
| Call | `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)`, where `<PREFIX>` is the project's macro prefix |
| Format | The project's own C++17 formatter: each `{}` takes the next argument through `operator<<`, `{{` and `}}` are literal braces, no format specs. A value that needs width, precision or hex is formatted into a string before the call. No `std::format`, no concatenation at the call site |

```cpp
inline constexpr Logging::LogProject K_SUSHIENGINE_LOG_PROJECT{"sushiengine", "SE_LOG_LEVEL"};
inline constexpr Logging::LogCategory K_ECS_LOG_CATEGORY =
    Logging::make_log_category(K_SUSHIENGINE_LOG_PROJECT, "ecs");

PX_LOG_WARN(K_ECS_LOG_CATEGORY,
            "archetype {} rejected component {}: already {} components, limit {}",
            archetype_id, component_name, count, K_MAX_COMPONENTS);
```

Source: not compiled

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
category, the thread and the file and line of the call. The thread is a small number the logger gives each thread on its first
record, so one thread's records can be followed through the log. A record goes into the sink as
one record view: level, project, module, file, line, thread, message and the formatted line, all
valid during the call. A program can send one project's records to their own file, and a host
with a logging system of its own can file each field where it belongs.

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

A process can hold a logger besides ours: a second Sushi logger, as when SushiEngine loads
SushiRuntime and SushiDSP, or the host's own, as in Unity, a Python program or a game with a
logging library. The program joins them at start-up, before its first log call, so one of them
writes everything. Without the join each logger writes stderr on its own thread and their lines
interleave.

| Host | Join |
| --- | --- |
| Its own logging system | It sets the sink of every Sushi logger it loads to one that hands the record view to its system |
| A host outside C++ | The same, through the logger's `extern "C"` sink setter, which takes a function pointer, a user pointer and a plain struct of the record's fields |
| Only Sushi libraries | One Sushi logger receives, every other forwards into it, as below |

| Part | Rule |
| --- | --- |
| Receiver | Every logger offers `log_forward_sink()`: a sink that takes a record from another logger and enters it into its own queue |
| Sender | The other logger's sink is set to the receiver's forward sink. A logger whose sink forwards delivers on the calling thread, so the receiver numbers the thread and orders the record as if it had been called directly |
| Fields | The forward carries the level, project, module, file, line and message, never a formatted line, so the receiver writes one record shape |
| Levels | Each logger keeps the levels of its own projects and reads their variables. A record the sender's level drops is never forwarded |
| Choice | The receiver is the logger of the library the program depends on most; the program names the join in one place, its start-up |
| Delivery | A logger whose sink belongs to a host also delivers on the calling thread, so the host sees calls in the order they were made |

```cpp
SushiDSP::set_log_sink(SushiRuntime::log_forward_sink());
```

Source: not compiled

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
