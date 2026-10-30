---
name: dependencies
description: Use when adding, upgrading, removing or vendoring a third-party library, SDK or package, when a licence question comes up, or when a third-party type appears in a public header, in a repository.
---

# Dependencies

Every dependency is a permanent cost: its licence, its build, its bugs, its upgrades. Adding one
is the owner's decision; this skill says what the agent brings to that decision and how an
accepted dependency is wired.

## Before proposing one

The proposal names:

1. What it does that the repository cannot do in a reasonable brick of its own.
2. Its licence, read from the source, not from a summary.
3. Its exact version and where it comes from.
4. Which module uses it, and that it stays private to that module.

Then the agent asks and waits.

## Licences

| Licence | Decision |
| --- | --- |
| MIT, BSD, Apache-2.0, Zlib, ISC, public domain | Accepted |
| A repository of the same organisation, under its own licence | Accepted |
| LGPL | Only linked dynamically, and only after asking |
| GPL, AGPL, SSPL | Rejected |
| Third-party non-commercial, source-available, field-of-use limits | Rejected |
| Vendor SDK licences that require marks, notices to the vendor, or restrict redistribution | Rejected |

A dependency's own dependencies are held to the same table.

## Ported code

Code translated or adapted from a third-party source is that source's work, whatever language
it ends up in. The file keeps the upstream copyright line and licence name in its license
block, and `NOTICE.md` lists it. The owner's licence covers the changes, not the original.

## Notices

`NOTICE.md` at the repository root lists every third-party component, every ported file and
every redistributed binary: its name, source URL, version, licence and where it sits in the
tree. A component that is not listed is not shipped.

## Where it comes from

- **Default:** installed through the organisation's dependency tool, declared in
  its manifest with an exact version. No ranges, no "latest".
- **Vendored under `third_party/<name>/`** only when the package manager does not carry it, or
  when it needs a patch. The folder carries a `README.md` with the source URL, the commit or
  version, the licence, and every local patch listed.
- Never installed by hand, never copied into a module's `source/`.

## A sibling library as a dependency

A repository builds on its own, with or without a workspace: whoever clones only a library gets
what it depends on through the repository's own `setup`, without the workspace tool.

1. The repository's dependency declaration lists each sibling library it links and pins it with a
   release tag and the library's full commit hash.
2. The build finds it in this order, the CLI and the build files alike, and stops at the first
   that exists:
   1. a path variable, set by the person or the CLI;
   2. the sibling checkout beside the repository;
   3. the copy `setup` fetched at the pinned version, which it refuses when the commit differs
      from the pin.
3. The build never downloads; it only reads the path the CLI hands it.
4. `doctor` reports a sibling whose commit differs from the pin, and which of the three it used.
5. Moving a pin is an upgrade, as below. Every repository pinning a library moves together, and
   the library's CI builds and tests each repository that pins it before a release.
6. A workspace tool takes over what a repository set up on its own. The toolchains `setup`
   installed sit in a machine root the tool reads too, so nothing is fetched twice, and the tool
   adopts a checkout the person made. The workspace sibling then wins the search above.

When `setup` cannot fetch, it says in one message what it tried to fetch, from where, and how to
hand it a checkout through the path variable. Two pins of one library in one dependency chain at
different versions are an error `doctor` names, with both pinning repositories.

## Wiring

1. A module links a third-party library `PRIVATE`. Its types never appear in the module's public
   headers.
2. When a public header must expose a third-party type (a graphics API handle, for example), the
   module's `README.md` says so and names the type, and the owner has approved it.
3. One module wraps each dependency. Other modules use the wrapper, not the library.
4. A shared library's runtime file is copied beside every executable
   the build makes that loads it, tests and examples included, through `TARGET_RUNTIME_DLLS`,
   and the install and every binary package ship it, listed in `NOTICE.md`.
5. A library of the organisation built as a shared library exports the version of its binary
   interface, and a consumer checks it on first use: a mismatch stops the process with one line
   naming the consumer, both versions and the library's path, never a crash later.
6. Every capability a CLI or the workspace tool has is in that repository's manual: a guide page says what
   it does for the person and how to run it, and the FAQ links it.

## Upgrading and removing

- An upgrade is its own commit, in the shape `commits` gives, with the full test suite run.
- A dependency no module uses any more is removed in the same change that stopped using it.

## Red flags

- "It is header-only, so it is not really a dependency." → it is.
- "The licence is probably MIT." → read it.
- "It is simpler to expose its type in our header." → wrap it.
