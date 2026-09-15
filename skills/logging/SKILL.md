---
name: logging
description: Use when adding, reviewing or removing a log call, a log category, a log level, a sink, or when handling an error or a fallback that might need to be recorded, in a Sushi Systems repository.
---

# Logging

A log is the record of what the program decided. Someone reading it after a failure must be
able to tell what happened, with which values, and what the program did next, without a
debugger. It costs nothing when a level is off.

## Shape

| Part | Rule |
| --- | --- |
| Logger | One per project, in its foundation module; the only thing that writes to a sink |
| Category | Each module declares exactly one, in `<module>_log_category.hpp`: `K_<MODULE>_LOG_CATEGORY` |
| Call | `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)` |
| Format | The project's own C++17 formatter: positional `{}` markers only, no format specs; a value needing width, precision or hex is formatted into a string before the call. No `std::format`, no string concatenation at the call site |
| Sink | Asynchronous in applications; synchronous in tests, so output order is deterministic |
| Compile-time cut | Levels below the build's minimum compile to `((void)0)`, arguments unevaluated |

```cpp
inline constexpr Logging::LogCategory K_ECS_LOG_CATEGORY = Logging::make_log_category("ecs");

PR_LOG_WARN(K_ECS_LOG_CATEGORY,
            "archetype {} rejected component {}: already {} components, limit {}",
            archetype_id, component_name, count, K_MAX_COMPONENTS);
```

## Levels

| Level | Records | Example |
| --- | --- | --- |
| `TRACE` | Step-by-step flow, for a developer chasing one bug; compiled out of release | Every node visited in one graph pass |
| `DEBUG` | Internal state at decision points | Chosen memory tier and its size |
| `INFO` | A lifecycle event an operator cares about | Device opened, world loaded, 1 842 assets cooked |
| `WARN` | The program recovered or fell back; output may differ from what was asked | Share refused, falling back to host copy |
| `ERROR` | An operation failed; the caller sees a failure status | Asset file unreadable |
| `FATAL` | The process cannot continue; logged immediately before termination | Device lost with no recovery path |

## What is logged

Log an event or a decision:

- a state change of a long-lived object (opened, closed, lost);
- a request refused, and why;
- a fallback taken, and to what;
- a resource limit reached;
- every failure status created at a boundary.

Every `WARN` and `ERROR` answers three questions in one line: what happened, the values
involved, and what the program does now.

## What is not logged

| Not logged | Instead |
| --- | --- |
| Anything per frame, per element or per sample | A counter, reported once per interval |
| Entry and exit of functions | Nothing; use a profiler |
| A value already carried by a returned status, logged again at every level | Log once, where the status is created |
| Secrets, credentials, personal data | Nothing |
| Prose paragraphs | One line; details in the values |

## Errors and silence

A failure is either returned to the caller as a status or logged where it is handled. Never
neither.

```cpp
// Forbidden: the failure disappears.
try { device.wait(); } catch (...) {}

// Required: the boundary converts and records.
try
{
    device.wait();
}
catch (const std::exception& error)
{
    PR_LOG_WARN(K_SCHEDULER_LOG_CATEGORY, "wait() threw '{}'; treating event as complete",
                error.what());
    return EventStatus::CompletedWithError;
}
```

## Common mistakes

| Mistake | Fix |
| --- | --- |
| `PR_LOG_ERROR(cat, "failed")` | Name the operation, the input and the consequence |
| `INFO` inside the frame loop | Counter plus one `INFO` per interval, or `TRACE` |
| A module logging under another module's category | Declare the module's own category |
| `std::cout` or `printf` in engine code | The logger; stdout belongs to the CLI |
