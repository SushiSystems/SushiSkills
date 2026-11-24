# Logging: shape, levels, gates and what is logged

Read this when you add a project, a front, a category or a call, pick a level, or check what may
be logged. A log lets a reader reconstruct how a failure happened without a debugger: what happened, with which
values, in which module and thread, and what the program did next. The rules are in `../SKILL.md`; level examples and settings are in `runtime.md`.

## Shape

| Part | Rule |
| --- | --- |
| Logger | One queue, one thread, one sink per process |
| Front | A new project extends the logger by declaring categories, never by changing it |
| Project | Holds the project's name and its level variable |
| Category | A project and a module |
| Format | Each `{}` takes the next argument through `operator<<`; `{{` and `}}` are literal; precision, width, form or hex go through the logger's helpers |

## Levels

A record passes at or above its category's level, which is `WARN` unless something sets it.

| Level | Records |
| --- | --- |
| `TRACE` | Step-by-step flow, for finding the cause of one bug |
| `DEBUG` | Internal state at a decision point |
| `INFO` | A lifecycle event an operator cares about |
| `WARN` | The program recovered or fell back; the result may differ |
| `ERROR` | An operation failed; the caller sees a failure status |
| `FATAL` | The process cannot continue; written just before it ends |
| `OFF` | Nothing; a setting, never a call |

## Two gates

Each gate runs before a call's arguments are evaluated.

1. **Compile time.** Each translation unit's ceiling is `ERROR` when `<PREFIX>_ENABLE_LOGGING`
   is 0, `DEBUG` under `NDEBUG`, `TRACE` otherwise. A call past it compiles to `((void)0)`.
2. **Run time.** Each category's level is one atomic. A call past it costs one relaxed load and a
   branch.

## What is logged

Examples of what the rules in `../SKILL.md` ask for:

- a state change such as opened, closed or lost;
- a request refused, and why;
- a fallback taken, and to what.

## What is not logged

| Forbidden | Instead |
| --- | --- |
| Per frame, element or sample | A counter, reported once per interval |
| Entry and exit of functions | Nothing; use a profiler |
| Secrets, credentials, personal data | Nothing |
| Prose paragraphs | One line; details in the values |

## Python

Python keeps the same seven levels. A library adds no handler. The entry point configures levels
as well as handlers. Command output comes from the command layer `tools/settings.py` names.
