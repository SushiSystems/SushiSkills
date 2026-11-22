# Python code style: layouts and examples

Elaboration of the rules in `../SKILL.md`: the package layouts, the naming examples and the
logging example.

## Layout

**One module:**

```
pyproject.toml            the package definition (a CLI keeps its own under cli/)
source/<package>/
    __init__.py           re-exports the public surface, nothing else
    <area>/<name>.py
    py.typed
tests/<area>/test_<name>.py
```

**More than one module:**

```
modules/<tier>/<module>/
    README.md
    pyproject.toml
    source/<package>_<module>/
        __init__.py
        <name>.py
tests/<tier>/<module>/test_<name>.py
```

## Formatting

Built-in generics read `list[str]` and `X | None`.

## Naming examples

| Kind | Example |
| --- | --- |
| Package, module, file | `physics_world.py` |
| Class, exception | `PhysicsWorld`, `AssetUnreadableError` |
| Enum member | `BuildType.RELWITHDEBINFO` |
| Function, method | `add_body`, `read_wave_file` |
| Variable, parameter | `sample_rate` |
| Private attribute or helper | `_pending_bodies` |
| Module constant | `K_BLOCK_CEILING` |
| Bool query | `is_empty`, `has_status` |

## Class shape

Small free functions that serve only one class stay in that class's file.

## Logging

A `%s` placeholder with arguments costs nothing when the level is disabled; an f-string does
not.

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

Example name: `test_step_rejects_negative_time`. Checkers under `tools/` use the standard
library only so they run without installing anything (see `project-tools`); pytest runs their
`unittest` tests too.
