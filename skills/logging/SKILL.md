---
name: logging
description: Use when adding, reviewing or removing a log call, a log category, a log level, a sink or a logger, or when handling an error or a fallback that might need to be recorded, in a repository.
---

# Logging

A log records what the program decided: after a failure a reader can tell what happened, with
which values, in which module and thread, and what the program did next, without a debugger.
`tools/logs/check_logging.py` enforces what a checker can see.

## Shape

- **Logger:** one shared library, linked directly by every library of the organisation, loaded
  once per process (one queue, one thread, one sink). A plug-in a host may load twice links its
  static target, hidden symbols, and joins the host. Only the logger writes a record.
- **Front:** each project keeps its macros, `LogProject`, categories and level variable in its
  foundation module and writes through the logger. It adds no queue, thread or sink and never
  re-exports a logger type, name or call.
- **Project:** `K_<PROJECT>_LOG_PROJECT`, declared once.
- **Category:** `K_<MODULE>_LOG_CATEGORY`, named after the module's folder, in
  `<module>_log_category.hpp`. A module logs only under its own.
- **Call:** `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)`. The logger's formatter only:
  `{}` through `operator<<`, `{{` `}}` literal, no format specs (helpers for precision, width,
  hex). No `std::format`, concatenation or project formatter.

## Levels and gates

`TRACE` flow; `DEBUG` state at a decision; `INFO` operator lifecycle event; `WARN` recovered or
fell back; `ERROR` operation failed, caller sees a status; `FATAL` process cannot continue; `OFF`
a setting, never a call. Default is `WARN`. `FATAL` and `ERROR` are never compiled out; a call
past the compile-time ceiling or the category's run-time level evaluates no argument.

- `<PREFIX>_LOG_LEVEL` sets one project's levels: a level, then `module=level` pairs.
- A record is one line. The default sink is stderr; stdout belongs to the program.
- A sink never logs and never sets the sink, the level or the mode.
- A host's own logging system joins before the first log call.
- Python: standard `logging`, `_log = logging.getLogger(__name__)`, `%s` never f-strings; only the
  entry point configures handlers; command output is stdout, not a log.

## What is logged

An event or decision: a long-lived object's state change, a request refused and why, a fallback
and to what, a resource limit, every failure status created at a boundary. Every `WARN`, `ERROR`
and `FATAL` says in one line what happened, the values, and what the program does now.

Never: anything per frame, element or sample (a counter per interval instead); function entry and
exit; secrets, credentials, personal data; prose paragraphs.

## Errors and silence

A failure is returned as a status or logged where handled, never neither. An empty `catch` or an
`except` with only `pass` is forbidden. A failure is logged once: where the helper makes it, not
where it is caught. A throw macro or helper only throws. A macro that logs takes the caller's
category.

Level table, gates, shape table, Python detail: `references/shape.md`. Worked calls and mistakes:
`references/examples.md`. Levels from the environment, sinks, records, hosts:
`references/runtime.md`.
