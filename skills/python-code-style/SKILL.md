---
name: python-code-style
description: Use when writing, reviewing or refactoring Python in a Sushi Systems repository - a library, a service, a command line interface, a checker under tools/ or tests - including its package layout, naming, class shape, errors and logging.
---

# Python Code Style

Python 3.11 or later. The same brick discipline as the C++: one responsibility per module, one
primary type per file, dependencies pointing down a declared order, entry points that only
parse and delegate.

## Layout

The module-count predicate from `repository-layout` holds unchanged.

**One module:**

```
pyproject.toml            the package definition (a CLI keeps its own under cli/)
source/<package>/
    __init__.py           re-exports the public surface, nothing else
    <area>/<name>.py
    py.typed
tests/{unit,integration,regression,common}/
```

**More than one module:**

```
modules/<tier>/<module>/
    README.md
    pyproject.toml
    source/<package>_<module>/
        __init__.py
        <name>.py
    tests/
```

- A module's public surface is what its `__init__.py` re-exports. Anything else is private and
  starts with an underscore when it is a module-level name.
- Imports point down the tier order. A module never imports another module's private names.
- A command line interface is a module like any other: `commands/` parses arguments,
  `services/` does the work. A service never imports the command framework or writes to the
  terminal.

## Formatting

| Rule | Value |
| --- | --- |
| Indent | 4 spaces |
| Line length | 100 |
| Quotes | Double |
| Trailing commas | On every multi-line collection and call |
| Blank lines | Two between top-level definitions, one between methods |
| Annotations | On every signature; built-in generics (`list[str]`, `X \| None`) |

`from __future__ import annotations` opens every module after its docstring.

## Naming

| Kind | Form | Example |
| --- | --- | --- |
| Package, module, file | `snake_case` | `physics_world.py` |
| Class, exception, protocol, enum | `PascalCase` | `PhysicsWorld`, `AssetUnreadableError` |
| Enum member | `UPPER_SNAKE` | `BuildType.RELWITHDEBINFO` |
| Function, method | `snake_case`, verb first | `add_body`, `read_wave_file` |
| Variable, parameter | `snake_case` | `sample_rate` |
| Private attribute or helper | `_snake_case` | `_pending_bodies` |
| Module constant | `K_UPPER_SNAKE` | `K_BLOCK_CEILING` |

A bool-returning query reads as a question: `is_empty`, `has_status`.

## Files

- One primary class per file; the file is named after it. Small free functions that serve
  only that class stay in its file.
- No `utils.py`, `helpers.py` or `common.py`. Name the responsibility.
- Every file opens with the license header and a module docstring (see `source-comments`).

## Class shape

1. Public methods first, in the order a caller uses them; private helpers after.
2. Dependencies arrive through `__init__`; no module-level singletons, no hidden globals.
3. Interfaces are `typing.Protocol` classes with no state; implementations are separate classes
   in separate files.
4. Plain data is a `@dataclass(frozen=True, slots=True)` unless it must change.
5. A class not designed for inheritance is marked `@typing.final`.

## Errors

- Each module defines its own exception classes, all derived from one module base error.
- Raise the most specific class; never bare `Exception`, never `assert` for input validation.
- Exceptions from third-party libraries are caught at the module boundary and re-raised as the
  module's own, with `raise ... from error`.
- `except:` and `except Exception: pass` are forbidden. A failure is raised or logged, never
  neither.
- The entry point catches the module base error, prints one line, exits non-zero.

## Logging

The rules in `logging` apply. Each module gets one logger named after its category,
`logging.getLogger("<project>.<module>")`, created once at module level as `K_LOGGER`. Use
`%s` placeholders with arguments, never f-strings, so a disabled level costs nothing.

```python
K_LOGGER = logging.getLogger("project.assets")

K_LOGGER.warning(
    "asset %s rejected: %d bytes over the %d byte limit",
    asset_id,
    size - K_MAX_BYTES,
    K_MAX_BYTES,
)
```

## Tests

- `pytest`. One test file per source file: `test_<name>.py`, mirroring the source path.
- Test functions: `test_<behaviour>_<condition>`, e.g. `test_step_rejects_negative_time`.
- Checkers under `tools/` use the standard library only, so they run without installing
  anything (see `project-tools`).
