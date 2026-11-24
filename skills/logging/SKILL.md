---
name: logging
description: Use when adding, reviewing or removing a log call, a log category, a log level, a sink or a logger, or when handling an error or a fallback that might need to be recorded, in a repository.
---

# Logging

Checked by `tools/logs/check_logging.py`.

## Shape

- **Logger:** one shared library every organisation library links directly, loaded once per
  process. A plug-in a host may load twice links its static target, hidden, and sends records to the host's logger. Only the logger writes a record.
- **Front:** each project keeps its macros, `LogProject`, categories and level variable in its
  foundation module and writes through the logger: no queue, thread, sink or re-export.
- **Project:** `K_<PROJECT>_LOG_PROJECT`, declared once.
- **Category:** `K_<MODULE>_LOG_CATEGORY`, named for the module's folder, in
  `<module>_log_category.hpp`; a module logs only under its own.
- **Call:** `<PREFIX>_LOG_<LEVEL>(category, "format {}", value)`. The logger's formatter
  only: no format specs, `std::format`, concatenation or project formatter.

## Levels and gates

`TRACE` flow, `DEBUG` state at a decision, `INFO` lifecycle event, `WARN` recovered or
fell back, `ERROR` operation failed, `FATAL` cannot continue, `OFF` a setting.
Default `WARN`. `FATAL` and `ERROR` are never compiled out; a call past
the compile-time ceiling or the run-time level evaluates no argument.

- `<PREFIX>_LOG_LEVEL` sets one project's levels.
- A record is one line. The default sink is stderr, never stdout.
- A sink never logs or sets the sink, level or mode.
- The host connects its logging system to the logger before the first log call.
- Python: standard `logging`, `_log = logging.getLogger(__name__)`, `%s` not f-strings; handlers
  only in the entry point; command output is stdout.

## What is logged

An event or decision: a long-lived object's state change, a refused request, a fallback, a
resource limit, every failure status made at a boundary. Every `WARN`, `ERROR` and `FATAL` says
in one line what happened, the values, what the program does now.

Never: anything per frame, element or sample; function entry and exit; secrets, credentials,
personal data; prose paragraphs.

## Errors and fallbacks

A failure is returned as a status or logged where handled. An empty `catch` or `except: pass`
is forbidden. A failure is logged once, where the helper makes it. A throw macro only throws. A logging macro takes the caller's category.

Detail: `references/`.
