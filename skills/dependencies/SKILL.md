---
name: dependencies
description: Use when adding, upgrading, removing or vendoring a third-party library, SDK or package, when a licence question comes up, or when a third-party type appears in a public header, in a Sushi Systems repository.
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
| LGPL | Only linked dynamically, and only after asking |
| GPL, AGPL, SSPL | Rejected |
| Non-commercial, source-available, field-of-use limits | Rejected |
| Vendor SDK licences that require marks, notices to the vendor, or restrict redistribution | Rejected |

A dependency's own dependencies are held to the same table.

## Where it comes from

- **Default:** installed through the organisation's dependency tool (`hub install`), declared in
  its manifest with an exact version. No ranges, no "latest".
- **Vendored under `third_party/<name>/`** only when the package manager does not carry it, or
  when it needs a patch. The folder carries a `README.md` with the source URL, the commit or
  version, the licence, and every local patch listed.
- Never installed by hand, never copied into a module's `source/`.

## Wiring

1. A module links a third-party library `PRIVATE`. Its types never appear in the module's public
   headers.
2. When a public header must expose a third-party type (a graphics API handle, for example), the
   module's `README.md` says so and names the type, and the owner has approved it.
3. One module wraps each dependency. Other modules use the wrapper, not the library.

## Upgrading and removing

- An upgrade is its own commit: `build(deps): upgrade <name> to <version>`, with the full test
  suite run.
- A dependency no module uses any more is removed in the same change that stopped using it.

## Red flags

- "It is header-only, so it is not really a dependency." → it is.
- "The licence is probably MIT." → read it.
- "It is simpler to expose its type in our header." → wrap it.
