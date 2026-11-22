# Dependencies at Sushi Systems: roles and commands

Read this when the role table or the `hub` command table is needed in full. The rules themselves
are in `../SKILL.md`.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Dependency tool | `hub install`, declared in the manifest with an exact version |
| Dependency declaration | `cli/sushistack.deps.toml`: each Sushi library it links in `[module] depends_on`, pinned in `[sushisystems.<name>]` with `version` (a release tag) and `commit` (its full hash) |
| Path variable | `<NAME>_DIR`, set by the person or the CLI |
| Sibling checkout | `../<name>` |
| The copy setup fetched | `<cli> setup`, through sushicore, clones the pinned tag into its home under `sources/<name>/<version>/` and refuses it when the commit differs from the pin |
| Workspace tool | SushiHub |
| Licence of its own libraries | Apache License 2.0 |

## Moving a pin

| Command | Does |
| --- | --- |
| `hub pins [--latest]` | Lists each module's pin of each dependency, SushiCore's range included; exits 1 when one dependency is pinned at two versions |
| `hub bump <name> <tag>` | Moves the pin in every module that depends on `<name>`, lowest tier first; for `sushicore` it also syncs the shared tools; runs each module's `check_all.py` and prints a pass or fail table. It commits nothing |
| `hub pin <name> <version>` | Moves one pin without the graph walk or the checks |

## A workspace takes over

The toolchains `<cli> setup` installed sit in the machine root that `hub` reads too, so nothing is
fetched twice. `hub link` adopts a checkout the person made. `hub add` clones a library from the
copy setup fetched, when one at the pinned version exists, then points the clone's remote at the
repository. The workspace sibling then wins the search. `hub status` lists each fetched copy that
no module uses any more, and `hub clean` removes it.
