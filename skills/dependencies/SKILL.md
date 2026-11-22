---
name: dependencies
description: Use when adding, upgrading, removing or vendoring a third-party library, SDK or package, when a licence question comes up, or when a third-party type appears in a public header, in a repository.
---

# Dependencies

Adding a dependency is the owner's decision. Read `references/licences-and-flags.md` for the
licence table and red flags.

## Before proposing one

Name what it does that the repository cannot do in a reasonable brick, its licence (read from
the source, not a summary), its exact version and source, and the one module that uses it,
privately. Then ask and wait.

## Licences

Accepted: MIT, BSD, Apache-2.0, Zlib, ISC, public domain, and a same-organisation repository
under its own licence. LGPL: only linked dynamically, only after asking. Rejected: GPL, AGPL,
SSPL; non-commercial, source-available or field-of-use limits; vendor SDK licences that require
marks or vendor notices, or restrict redistribution. A dependency's own dependencies follow the
same rules.

## Ported code

Code translated or adapted from a third-party source is that source's work, in any language. Its
license block keeps the upstream copyright line and licence name, and `NOTICE.md` lists it. The
owner's licence covers the changes only.

## Notices

`NOTICE.md` at the root lists every third-party component, ported file and redistributed binary
with name, source URL, version, licence and tree location. An unlisted component is not shipped.

## Where it comes from

- Default: the organisation's dependency tool, declared in its manifest with an exact version;
  no ranges, no "latest".
- Vendored under `third_party/<name>/` only when the package manager lacks it or it needs a
  patch; the folder's `README.md` gives source URL, commit or version, licence and every patch.
- Never installed by hand, never copied into a module's `source/`.

## A sibling library as a dependency

A repository builds on its own: whoever clones only a library gets its dependencies through the
repository's `setup`, without the workspace tool. The dependency declaration pins each sibling
with a release tag and its full commit hash. The build never downloads; it reads only the path
the CLI hands it. Moving a pin is an upgrade.

Read [references/sibling-library.md](references/sibling-library.md) when declaring, finding,
fetching or moving a sibling pin.

## Wiring

1. Link a third-party library `PRIVATE`; its types stay out of public headers.
2. A public header exposes one only when the module's `README.md` names the type and the owner
   approved.
3. One module wraps each dependency; others use the wrapper.
4. A shared library's runtime file is copied beside every executable that loads it, tests and
   examples included, through `TARGET_RUNTIME_DLLS`; the install and every binary package ship
   it, listed in `NOTICE.md`.
5. An organisation library built shared exports its binary-interface version; a consumer checks
   it on first use, and a mismatch stops the process with one line naming consumer, both
   versions and library path.
6. Each CLI or workspace-tool capability is in the repository's manual: a guide page says what it
   does and how to run it, and the FAQ links it.

## Upgrading and removing

An upgrade is its own commit (`commits`) with the full test suite run. A dependency no module
uses is removed in the change that stopped using it.
