---
name: api-stability
description: Use when changing, renaming or removing a public function, type, header, CLI command or file format, when deprecating something, or when a lower-tier Sushi Systems repository releases and repositories above it must follow.
---

# API Stability

A public surface is a promise to every caller, inside the repository and in the repositories
above it. It changes deliberately, visibly and in order.

## What is public

- Everything under a module's `include/` (C++), re-exported from `__init__.py` (Python) or from
  `index.ts` (TypeScript).
- CLI commands and their flags.
- File formats (see `file-formats`).

Everything else is private and may change in any commit.

## Deprecation

1. Mark the old surface: `[[deprecated("use <replacement>")]]` in C++, `warnings.warn(...,
   DeprecationWarning)` in Python, `/** @deprecated use <replacement> */` in TypeScript.
2. Add a changelog entry naming the replacement.
3. Keep it for at least the next MINOR release.
4. Remove it in a later release, as a breaking change with `!` in the commit subject.

Before `v1.0.0` step 3 may be skipped, but the removal is still a breaking entry in the
changelog and the commit carries `!`.

A deprecated surface forwards to its replacement; it never keeps a second implementation.

## Export boundary

- Symbols a shared library exports carry the project's `<PREFIX>_API` macro; the default
  visibility is hidden (see `platform-portability`).
- A change to the layout of an exported type, or to an exported function's signature, is
  breaking.

## Across repositories

Repositories depend on each other in tiers, lowest first.

1. Each repository pins every Sushi Systems dependency to an exact tag, `v0.3.2`, never to a
   branch or a range.
2. When a lower repository releases, repositories above it upgrade in tier order, one at a time,
   each in its own commit (`build(deps): upgrade <name> to vX.Y.Z`) followed by its own release
   when its changelog calls for one.
3. A breaking release below is adapted to above in the same upgrade commit; no repository runs
   against a mix of old and new.
4. No repository depends on unreleased work of another. If it needs it, the lower one releases
   first.

## Red flags

- "Nobody outside this module calls it." → check the repositories above before calling it private.
- "I will keep the old function as well, just in case." → deprecate and forward, then remove.
- "Point the dependency at main until the release is out." → release first.
