---
name: sushisystems-dependencies
description: Use in a Sushi Systems repository together with the dependencies or api-stability skill, when pinning, finding, fetching or upgrading a Sushi library, or shipping the shared logger's runtime file.
---

# Dependencies at Sushi Systems

Who fills the roles the `dependencies` skill names. Read `references/roles-and-commands.md` for
the role table, the `hub` command table and the workspace takeover.

## The roles

- Dependency tool: `hub install`, manifest with an exact version.
- Declaration: `cli/sushistack.deps.toml`. Each linked Sushi library is in `[module] depends_on`
  and pinned in `[sushisystems.<name>]` with `version` (release tag) and `commit` (full hash).
- Path variable `<NAME>_DIR`, set by the person or the CLI; sibling checkout `../<name>`.
- `<cli> setup` clones the pinned tag under `sources/<name>/<version>/` and refuses a commit that
  differs from the pin.
- Workspace tool SushiHub; own libraries are Apache License 2.0.

## Moving a pin

Every repository pinning a library moves together; the library's CI builds and tests each
repository that pins it before a release. `hub pins [--latest]` lists pins and exits 1 when one
dependency sits at two versions; it exits 0 before a release is proposed. `hub bump <name> <tag>`
walks the graph lowest tier first, runs each `check_all.py` and commits nothing. `hub pin <name>
<version>` moves one pin unchecked.

## A workspace takes over

`hub link` adopts a checkout and `hub add` clones one; the workspace sibling wins the
search. `hub status` lists unused fetched copies; `hub clean` removes them.

## The logger's runtime file

SushiLog's `sushilog.dll` is copied beside every executable that loads it and listed in
`NOTICE.md`. Its binary-interface check is "ABI version" in `INTERFACE.md` of
`sushisystems-logging`.

## The manual

Every capability the CLI or `hub` has is in the repository's manual: a guide page says what it
does and how to run it, and the FAQ links it.
