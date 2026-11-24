# Unlinked cleanup: detail

Read this when judging what counts as unlinked, or how a cleanup keeps the engineering rules.

## Dynamic forms to search

A name built at run time is searched as the string a table holds (`"physics_world"` in a registry)
and as a glob pattern (`source/*_world.cpp` in a build file).

## What counts as unlinked

| Kind | Unlinked when |
| --- | --- |
| File, folder, skill | No code, build file, install step, link or index names it |
| Function, class, constant, setting | No caller, reader or test outside its own definition uses it |
| Test | It covers code that no longer exists |
| Page or section | It describes a name, path or tool that no longer exists |
| Dependency | No source includes or imports it |
| Outdated fact | A count, name or path in prose no longer matches the thing it describes |

A public surface is never unlinked: a symbol, a header, a CLI command or a file format.

History is never unlinked: the changelog, the archive, a closed work folder, the licence and the
notice.

A file another repository reads: search its siblings before calling anything unlinked.

## Engineering rules that still apply

- **SOLID** ([definition](../../sushiskills/references/solid.md)). Deleting the only other implementation of an interface leaves an abstraction with
  one user. Deleting a caller never leaves a function doing two jobs for the callers that
  remain.
- **Tests.** A test is deleted only with the code it covers.

## SOLID breaches seen

The principles to name ([definitions](../../sushiskills/references/solid.md)) are one responsibility, open for extension, substitution, narrow
interfaces and depending on abstractions. A cost is the change the breach makes harder or the
test it makes impossible.
