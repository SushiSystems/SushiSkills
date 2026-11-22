# Multi-agent work: roles and planning tables

Read this when a role, a plan mode or a red-flag question needs the original table form. The
rules themselves are in `../SKILL.md`.

## Roles

| Role | Does | Writes |
| --- | --- | --- |
| Orchestrator | Plans, dispatches, reviews reports, integrates, commits | Code, design, manual, changelog, backlog |
| Worker | One task with one acceptance criterion | The files its dispatch lists, a module README only when listed, and the work folder under `docs/agent/` |

## Plan modes

| Mode | Shape |
| --- | --- |
| Inline | One session implements the jobs in hierarchy order, without workers |
| Parallel | The orchestrator gives the jobs to subagents, several at once, and keeps no job for itself |

In parallel mode a free subagent gets the next ready job at once.

## Task rows

The tasks are rows of the plan, not backlog entries; `AGENT_WORK.md` in `documentation` says
which entry serves the work folder.
