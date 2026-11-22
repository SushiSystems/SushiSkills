# Logging: shape, levels, gates and what is logged

Read this when you add a project, a front, a category or a call, pick a level, or check what may
be logged. The rules are in `../SKILL.md`; level examples and settings are in `runtime.md`.

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

## Python

Python uses the standard `logging` module under the same rules: `_log =
logging.getLogger(__name__)` per module, the same seven levels, `%s` arguments and never an
f-string. Only the entry point configures handlers and levels; a library adds no handler. What a
command shows the user is output, not a log: stdout, from the command layer `tools/settings.py`
names.
