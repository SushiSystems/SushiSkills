---
name: python-code-style
description: Use when writing, reviewing or refactoring Python in a repository - a library, a service, a command line interface, a checker under tools/ or tests - including its package layout, naming, class shape, errors and logging.
---

# Python Code Style

Python 3.11 or later. C++ discipline: one responsibility per module, one primary type per file,
entry points that only parse and delegate. Layouts, naming table, logging example:
[rules](references/rules.md).

- Layout: the module-count predicate of `repository-layout` holds; the public surface is what
  `__init__.py` re-exports, other module-level names start with `_`. Imports point down the
  tier order, never to another module's private names. A CLI is a module: `commands/` parses,
  `services/` works and never imports the command framework or prints.
- Formatting: 4 spaces, 100 columns, double quotes, trailing commas on multi-line collections
  and calls, two blank lines between top-level definitions, one between methods, annotations on
  every signature with built-in generics; `from __future__ import annotations` after each module
  docstring.
- Names: `snake_case` modules, files, functions (verb first), variables; `PascalCase` classes,
  exceptions, protocols, enums; `UPPER_SNAKE` enum members; `_snake_case` private;
  `K_UPPER_SNAKE` constants. A bool query reads as a question.
- Files: one primary class per file, named after it; no `utils.py`, `helpers.py`, `common.py`;
  license header and module docstring (`source-comments`).
- Class: public methods first; dependencies via `__init__`, no singletons or hidden globals;
  interfaces are stateless `typing.Protocol`, implementations separate; plain data
  `@dataclass(frozen=True, slots=True)` unless it must change; `@typing.final` unless designed
  for inheritance.
- Errors: each module has its own exceptions under one base error; raise the most specific,
  never bare `Exception`, never `assert` for input; re-raise third-party errors as the module's
  own with `raise ... from error`; no `except:` or `except Exception: pass`; a failure is raised
  or logged. The entry point catches the base error, prints one line, exits non-zero.
- Logging (`logging`): `K_LOGGER = logging.getLogger("<project>.<module>")` per module; `%s`
  placeholders, never f-strings.
- Tests: `pytest`, `test_<name>.py` per source file at the path `TESTS.md` in `repository-layout`
  gives; `test_<behaviour>_<condition>`. `tools/` checkers use the standard library only; their
  tests in `tools/tests/` use `unittest`.
- `uv`, `pytest` run only through the repository's CLI (`sushiskills`, default 2).
