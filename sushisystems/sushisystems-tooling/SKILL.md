---
name: sushisystems-tooling
description: Use in a Sushi Systems repository together with the backlog, design, project-tools, build-throughput or versioning-and-release skill, to know that sushicore fills the tooling roles, how its backlog and design commands run with and without a module CLI, what tools/settings.py sets, and the CLAUDE.md block every repository carries.
---

# Tooling at Sushi Systems

The doctrine's tooling skills name roles; this page says who fills each at Sushi Systems.

- Shared tooling library: `sushicore`.
- Backlog and design tools: `sushicore`'s commands, `<cli> backlog ...` and `<cli> design ...`
  in a repository with a module CLI, `python -m sushicore.backlog ...` (design the same way) in
  one without (a web application run by `npm`). References:
  sushicore's `docs/reference/BACKLOG.md` and `DESIGN.md`.
- Build machinery: from sushicore (`build_tree`, `build_admission`, `build_gate`, `build_report`).
- Module manifest: `sushi-module.toml`.
- Shared checkers' source: SushiCore's `tools/`, at the release the CLI pins. Sync with
  `python -m sushicore.shared_tools sync ROOT --tag <that release>`, check with
  `python -m sushicore.shared_tools check ROOT`; `hub bump sushicore <tag>` runs it in every
  module.
- Documentation host: `docs.sushisystems.io`, named by `docs/publish.toml`.

`tools/settings.py` sets the constants in `references/settings.md`; SushiSkills' own copy is the
reference. A repository's `CLAUDE.md` carries the block in `CLAUDE_TEMPLATE.md`. A repository
that adopted the `Backlog:` commit line sets `K_TRAILER_SINCE` to the commit after which it
applies, and its setup command runs `tools/hooks/install_hooks.py`.
