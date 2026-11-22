---
name: api-stability
description: Use when changing, renaming or removing a public function, type, header, CLI command or file format, when deprecating something, or when a lower-tier repository releases and repositories above it must follow.
---

# API Stability

A public surface is a promise to every caller, here and in the repositories above. It changes
deliberately, visibly and in order. Read `references/red-flags.md` when a change feels harmless.

## What is public

Everything under a module's `include/` (C++), re-exported from `__init__.py` (Python) or
`index.ts` (TypeScript); CLI commands and flags; file formats (`file-formats`). Everything else
is private and may change in any commit.

## Deprecation

1. Mark it: `[[deprecated("use <replacement>")]]`, `warnings.warn(..., DeprecationWarning)`, or
   `/** @deprecated use <replacement> */`.
2. Add a changelog entry naming the replacement.
3. Keep it through at least the next MINOR release.
4. Remove it later as a breaking change, `!` in the commit subject.

Before `v1.0.0` step 3 may be skipped, but the removal is still a breaking entry with `!`. A
deprecated surface forwards to its replacement; it never keeps a second implementation.

## Export boundary

Exported symbols carry `<PREFIX>_API`; default visibility is hidden (`platform-portability`). A
change to an exported type's layout or an exported function's signature is breaking.

## Across repositories

Repositories depend on each other in tiers, lowest first.

1. Pin every dependency on another of the organisation's repositories to an exact tag, `v0.3.2`,
   never a branch or range.
2. When a lower repository releases, those above upgrade in tier order, one at a time, each in
   its own upgrade commit (`commits`), followed by its own release if its changelog calls for one.
3. A breaking release below is adapted to above in the same upgrade commit; none runs against a
   mix of old and new.
4. No repository depends on unreleased work of another; the lower one releases first.
5. A dependency has one version across the workspace. Two pins at different versions is a defect;
   the workspace tool reports the split, and rule 2's upgrade runs through its graph-walking
   command, never by hand edits repository by repository.
