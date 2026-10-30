---
name: multi-agent-work
description: Use when dispatching subagents, running agents in parallel, splitting a plan into tasks for other agents, or reviewing a report that came back from an agent, in a repository.
---

# Multi-Agent Work

Parallel agents multiply output and multiply mess by the same factor. One session orchestrates;
every other agent is a worker with a fixed file set, a fixed place to write, and a report that
must carry its evidence.

## Roles

| Role | Does | Writes |
| --- | --- | --- |
| Orchestrator | Plans, dispatches, reviews reports, integrates, commits | Code, design, manual, changelog, backlog |
| Worker | One task with one acceptance criterion | The files its dispatch lists, a module README only when listed, and the work folder under `docs/agent/` |

A worker never edits a file outside its assigned set, never writes to `docs/design/`, the
manual, `CHANGELOG.md` or `docs/backlog/`, and never commits unless the dispatch says so. It
reads its work with `backlog next` and reports what it found; the orchestrator writes the entries.

## Planning

Every plan puts hierarchy first: interfaces and the bricks they depend on come before their
callers, and a module boundary is fixed, with its build edges committed, before anything on
either side is written. A task needs one acceptance criterion and one build; a task needing two
builds is two tasks.

The owner chooses how the plan runs.

| Mode | Shape |
| --- | --- |
| Inline | One session implements the tasks in hierarchy order, without workers |
| Waves | Tasks the hierarchy leaves independent are grouped into waves with disjoint file sets, one worker per task |

A wave plan lists, per wave: the tasks, each task's files, what each waits on, and the build the
owner runs to close the wave.

## Dispatch

Every dispatch opens with the line `claude/CLAUDE.md` gives in its section "Delegation", which
sends the subagent to `claude/DISPATCH.md`. The rules live in that file and nowhere else.

Then: the task, its file list, its acceptance criterion, the skills it must load
(`cpp-code-style`, `source-comments`, ...), and the work folder path.

A worker does not see the orchestrator's memory or conversation. Anything it needs is in the
dispatch.

In a wave, a worker returns its report as its reply and the orchestrator writes `REPORT.md`;
the work folder holds one report, and two workers never hold one file.

## Choosing a model

The `model-routing` skill chooses the model and the effort for each dispatch, by phase and by
task, within the limits the same "Delegation" section sets.

## Accepting a report

The evidence a report must carry, and what a reviewer dispatch checks by name, are in the same
"Delegation" section. The orchestrator checks two things more.

1. The list of files changed matches the assigned set.
2. A report on work that changed a public name, a signature, a header path, a CLI command or a
   documented behaviour carries the output of `tools/documentation/check_docs_truth.py` and the
   pages and lines the change made false. Without both, the report is sent back.
3. A report on work that added tests lists them, as "Directions to the agent" in `testing` says.

A page a worker reports as false is handled as `AGENT_WORK.md` in `documentation` says.

## Shared working tree

- Staging, stash and worktrees follow `git-workflow`, section "Shared working tree".
- Two workers never hold the same file in one wave.
