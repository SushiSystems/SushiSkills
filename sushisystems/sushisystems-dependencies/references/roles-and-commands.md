# Dependencies at Sushi Systems: roles and commands

Read this when the detail of a role or a `hub` command is needed. The rules themselves are in
`../SKILL.md`.

## The roles

- `<cli> setup` fetches through sushicore and clones into the machine root, which
  `hub` reads too, so nothing is fetched twice.
- A person makes a sibling checkout by hand or with `hub add`.

## Changing a pin

| Command | Detail |
| --- | --- |
| `hub pins [--latest]` | Lists each module's pin of each dependency, SushiCore's range included |
| `hub bump <name> <tag>` | Changes the pin in every module that depends on `<name>`; for `sushicore` it also syncs the shared tools; prints a pass or fail table |
| `hub pin <name> <version>` | Skips the dependency-order walk and the checks |

## Workspace checkouts take precedence

`hub link` registers a checkout the person made. `hub add` clones a library from the copy setup
fetched, when one at the pinned version exists, then points the clone's remote at the repository.
`hub status` lists each fetched copy that no module uses any more.
