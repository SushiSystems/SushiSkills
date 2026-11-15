---
name: logging
description: Use when adding, reviewing or removing a log call, a log category, a log level, a sink or a logger, or when handling an error or a fallback that might need to be recorded, in a repository.
---

# Logging

A log records what the program decided. After a failure, a reader must tell what happened,
with which values, in which module and thread, and what the program did next, without a
debugger, and follow one project's records through a process that loads several.

`tools/logs/check_logging.py` enforces what a checker can see; its messages carry the detail.

Read `references/examples.md` for worked calls and common mistakes, and `references/runtime.md`
when you set levels, write a sink, read a record or join a host's logging system.

## Shape

| Part | Rule |
| --- | --- |
| Logger | One shared library, linked directly by every library of the organisation, loaded once per process: one queue, one thread, one sink. A plug-in a host may load twice links its static target, with hidden symbols, and joins the host. Only the logger writes a record |
| Front | Each project keeps its own macros, `LogProject`, categories and level variable in its foundation module, and writes through the logger. It adds no queue, thread or sink, and never re-exports a logger type, name or call. A new project extends the logger by declaring categories, never by changing it |
| Project | `K_<PROJECT>_LOG_PROJECT`, declared once, holding the project's name and its level variable |
| Category | A project and a module: `K_<MODULE>_LOG_CATEGORY`, named after the module's folder, in `<module>_log_category.hpp`. A module logs only under its own |
| Call | `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)` |
| Format | The logger's formatter: each `{}` takes the next argument through `operator<<`, `{{` and `}}` are literal, no format specs; precision, width, form or hex go through its helpers. No `std::format`, no concatenation, no project formatter or helper |

## Levels

A record passes at or above its category's level, which is `WARN` unless something sets it.

| Level | Records |
| --- | --- |
| `TRACE` | Step-by-step flow, for chasing one bug |
| `DEBUG` | Internal state at a decision point |
| `INFO` | A lifecycle event an operator cares about |
| `WARN` | The program recovered or fell back; the result may differ |
| `ERROR` | An operation failed; the caller sees a failure status |
| `FATAL` | The process cannot continue; written just before it ends |
| `OFF` | Nothing; a setting, never a call |

## Two gates

A call passes two gates before its arguments are evaluated.

1. **Compile time.** Each translation unit's ceiling is `ERROR` when `<PREFIX>_ENABLE_LOGGING`
   is 0, `DEBUG` under `NDEBUG`, `TRACE` otherwise. A call past it compiles to `((void)0)`.
2. **Run time.** Each category's level is one atomic. A call past it costs one relaxed load and a
   branch.

`FATAL` and `ERROR` are never compiled out.

## Levels, records and sinks

- `<PREFIX>_LOG_LEVEL` sets one project's levels: a level, then `module=level` pairs.
- A record is one line. The default sink is stderr; stdout belongs to the program.
- A sink never logs and never sets the sink, the level or the mode.
- A host's own logging system joins before the first log call, so one system writes everything.

## Python

Python uses the standard `logging` module under the same rules: `_log =
logging.getLogger(__name__)` per module, the same seven levels, `%s` arguments and never an
f-string. Only the entry point configures handlers and levels; a library adds no handler. What a
command shows the user is output, not a log: stdout, from the command layer `tools/settings.py`
names.

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
| Secrets, credentials, personal data | Nothing |
| Prose paragraphs | One line; details in the values |

## Errors and silence

A failure is either returned to the caller as a status or logged where it is handled, never
neither. An empty `catch` or an `except` whose body is only `pass` is forbidden.

A failure is logged once: when the helper that makes it logs it, the code that catches it does
not. A macro or helper used everywhere to throw only throws and never logs. A macro
that logs for its caller takes the caller's category.
