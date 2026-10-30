# Tooling at Sushi Systems

The doctrine's tooling skills name roles: the shared tooling library, the backlog tool, the design
tool. This page says who fills each role at Sushi Systems.

## The roles

| Role | At Sushi Systems |
| --- | --- |
| Shared tooling library | `sushicore` |
| Backlog tool | `sushicore`'s `backlog` commands: `<cli> backlog ...` in a repository with a module CLI, `python -m sushicore.backlog ...` in one without. Reference: sushicore's `docs/reference/BACKLOG.md` |
| Design tool | `sushicore`'s `design` commands, run the same two ways. Reference: sushicore's `docs/reference/DESIGN.md` |
| Build machinery | From sushicore: `build_tree`, `build_admission`, `build_gate`, `build_report` |
| Module manifest | `sushi-module.toml` |
| The shared checkers' source | the SushiSkills checkout: `python tools/checking/copy_shared_tools.py ROOT --from <the SushiSkills checkout>` |
| Documentation host | `docs.sushisystems.io`, named by `docs/publish.toml` |
