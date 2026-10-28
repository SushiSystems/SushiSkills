# Backlog and design tool: plan

SPEC.md holds the rulings; this file holds the order of work. Code lands in sushicore, rules in
SushiSkills, and each repository moves its records once both have shipped.

## Module boundaries

| Module | Holds | Depends on |
| --- | --- | --- |
| `sushicore.backlog.model` | Entry kinds, columns, values, ceilings; parsing and writing one row | nothing |
| `sushicore.backlog.store` | Reading and writing `docs/backlog/<AREA>.md`, `ids.toml` and the generated index | `model` |
| `sushicore.backlog.order` | Age, lateness and the order of `next` | `model` |
| `sushicore.backlog.check` | Every rule `check` enforces | `model`, `store` |
| `sushicore.backlog.importer` | `import` and `renumber`, with the citation rewrite | `store` |
| `sushicore.backlog.commands` | The `backlog` group, `register_backlog_commands` | the four above |
| `sushicore.design.model` | A topic's frame: status, metadata, sections, phase table | nothing |
| `sushicore.design.store` | Reading and writing topic folders, ownership of modules | `design.model` |
| `sushicore.design.check` | The format, metadata and ownership rules | `design.model`, `design.store` |
| `sushicore.design.merge` | `overlap` and `merge`, with the citation rewrite | `design.store` |
| `sushicore.design.commands` | The `design` group, `register_design_commands` | the four above |

The citation rewrite is shared: `sushicore.citations`, taken from
`tools/documentation/repair_design_citations.py` and `drop_retired_citations.py`, depends on
nothing in either package. The groups register as `docs_bundle/commands.py` registers `docs`.

## Hierarchy

| Wave | Tasks | Files | Waits on | Closing build |
| --- | --- | --- | --- | --- |
| 0 | Package skeletons and `sushicore.citations` | `source/sushicore/backlog/__init__.py`, `source/sushicore/design/__init__.py`, `source/sushicore/citations.py`, `tests/test_citations.py` | approval | `python -m pytest tests/test_citations.py` |
| 1 | A: `backlog.model` · B: `design.model` | A: `backlog/model.py`, `tests/backlog/test_model.py` · B: `design/model.py`, `tests/design/test_model.py` | wave 0 | `python -m pytest tests/backlog tests/design` |
| 2 | A: `backlog.store` · B: `backlog.order` · C: `design.store` | each module and its test file | wave 1 | `python -m pytest tests/backlog tests/design` |
| 3 | A: `backlog.check` · B: `backlog.importer` · C: `design.check` · D: `design.merge` | each module and its test file | wave 2 | `python -m pytest` |
| 4 | A: `backlog.commands` · B: `design.commands`; sushicore README, `docs/reference/BACKLOG.md`, `docs/reference/DESIGN.md`, changelog | each commands module, its test, its reference page | wave 3 | `python -m pytest` and `python tools/check_all.py .` in sushicore |
| 5 | SushiSkills: `BACKLOG_FORMAT.md`, `DESIGN_FORMAT.md`, `documentation/SKILL.md`, the three checkers as calls into sushicore with their tests; SushiSkills' own records moved with `backlog import` | the files named | sushicore release with wave 4 | `python tools/check_all.py .` in SushiSkills |
| 6 | One task per repository: `backlog import`, `design overlap`, the merges the owner approves, the checkers synced | that repository's `docs/` and `tools/` | wave 5 | `python tools/check_all.py .` in that repository |

Wave 6 starts with sushiweb, the smallest, and ends with sushiengine. The merges in sushiengine
are listed by `design overlap` and each is approved by the owner before it runs.

## Not in this plan

- The work folders under `docs/agent/`. They stay as they are; a later piece of work reviews them.
- The light board at `company.sushisystems.io`. Its change is sushiweb's own work.

## Owner's answers

- 2026-10-28: the plan runs inline, to its end, with every decision delegated to the
  orchestrator, commits and tags allowed. The design merges of wave 6 are the orchestrator's to
  make under that delegation.
