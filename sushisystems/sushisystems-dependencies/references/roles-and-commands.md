# Dependencies at Sushi Systems: roles and commands

Read this when the detail of a role or a `hub` command is needed. The rules themselves are in
`../SKILL.md`.

## The roles

- `<cli> setup` fetches through sushicore and clones into its home, the machine root `hub` reads
  too, so nothing is fetched twice.
- A person makes a sibling checkout by hand or with `hub add`.

## Moving a pin

| Command | Detail |
| --- | --- |
| `hub pins [--latest]` | Lists each module's pin of each dependency, SushiCore's range included |
| `hub bump <name> <tag>` | Moves the pin in every module that depends on `<name>`; for `sushicore` it also syncs the shared tools; prints a pass or fail table |
| `hub pin <name> <version>` | Skips the graph walk and the checks |

## A workspace takes over

`hub link` adopts a checkout the person made. `hub add` clones a library from the copy setup
fetched, when one at the pinned version exists, then points the clone's remote at the repository.
`hub status` lists each fetched copy that no module uses any more.
