---
name: dependencies
description: Use when adding, upgrading, removing or vendoring a third-party library, SDK or package, when a licence question comes up, or when a third-party type appears in a public header, in a repository.
---

# Dependencies

Adding a dependency is the owner's decision. Licence table and red flags:
`references/licences-and-flags.md`; a dependency's own dependencies follow the table.

## Before proposing one

Name what it does that a brick of the repository cannot, its licence (read from the source), its
exact version and source, and the one module that uses it, privately. Then ask and wait.

## Ported code

Code translated or adapted from a third-party source is that source's work. Its license block
keeps the upstream copyright line and licence name, and `NOTICE.md` lists it. The owner's licence
covers the changes only.

## Notices

Root `NOTICE.md` lists every third-party component, ported file and redistributed binary with
name, source URL, version, licence and tree location. An unlisted component is not shipped.

## Where it comes from

- Default: the organisation's dependency tool, in its manifest with an exact version; no ranges.
- Vendored under `third_party/<name>/` only when the package manager lacks it or it needs a
  patch; its `README.md` gives source URL, version, licence and every patch.
- Never installed by hand, never copied into a module's `source/`.

## A sibling library as a dependency

Pin, search order and fetching: `references/sibling-library.md`.

## Wiring

1. Link a third-party library `PRIVATE`; its types stay out of public headers.
2. A public header exposes one only when the module's `README.md` names it and the owner approved.
3. One module wraps each dependency; others use the wrapper.
4. A shared library's runtime file is copied beside every executable that loads it, tests
   included, through `TARGET_RUNTIME_DLLS`; install and binary packages ship it, listed in
   `NOTICE.md`.
5. A shared organisation library exports its binary-interface version; a consumer checks it on
   first use, and a mismatch stops the process with one line naming consumer, both versions and
   library path.
6. Each CLI or workspace-tool capability has a guide page in the repository's manual, linked from
   the FAQ.

## Upgrading and removing

An upgrade is its own commit (`commits`) with the full test suite run. An unused dependency is
removed in the change that stopped using it.
