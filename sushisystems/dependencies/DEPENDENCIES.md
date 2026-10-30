# Dependencies at Sushi Systems

The `dependencies` skill names the roles: the dependency tool, the dependency declaration, the
pin, the workspace tool, the logger. This page says who fills each role at Sushi Systems.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Dependency tool | `hub install`, declared in the manifest with an exact version |
| Dependency declaration | `cli/sushistack.deps.toml`: each Sushi library it links in `[module] depends_on`, pinned in `[sushisystems.<name>]` with `version` (a release tag) and `commit` (its full hash) |
| Path variable | `<NAME>_DIR`, set by the person or the CLI |
| Sibling checkout | `../<name>` |
| The copy setup fetched | `<cli> setup`, through sushicore, clones the pinned tag into its home under `sources/<name>/<version>/` and refuses it when the commit differs from the pin |
| Workspace tool | SushiHub |
| Licence of its own libraries | PolyForm Noncommercial 1.0.0, accepted as a dependency |

## Moving a pin

Every repository pinning a library moves together, through `hub pin <name> <version>`, and the
library's CI builds and tests each repository that pins it before a release.

## A workspace takes over

The toolchains `<cli> setup` installed sit in the machine root that `hub` reads too, so nothing is
fetched twice. `hub link` adopts a checkout the person made. `hub add` clones a library from the
copy setup fetched, when one at the pinned version exists, then points the clone's remote at the
repository. The workspace sibling then wins the search. `hub status` lists each fetched copy that
no module uses any more, and `hub clean` removes it.

## The logger's runtime file

SushiLog is the shared library whose runtime file, `sushilog.dll`, is copied beside every
executable that loads it and listed in `NOTICE.md`. Its binary-interface check is "ABI version" in
`../logging/INTERFACE.md`.

## The manual

Every capability the CLI or `hub` has is in that repository's manual: a guide page says what it
does for the person and how to run it, and the FAQ links it.
