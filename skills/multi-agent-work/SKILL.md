---
name: multi-agent-work
description: Use when dispatching subagents, running agents in parallel, splitting a plan into tasks for other agents, or reviewing a report that came back from an agent, in a repository.
---

# Multi-Agent Work

One session orchestrates; every other agent is a worker with a fixed file set, a fixed place to
write, and a report that carries its evidence.

Read `references/running-the-plan.md` when writing a plan's job list, when running a plan in
parallel mode, or for examples of reading an instruction literally.

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
either side is written. A task needs one acceptance criterion. No task runs a build or a test:
the one build and the one test run come after the last task, as `build-throughput` boundary 8 says.

The owner chooses how the plan runs.

| Mode | Shape |
| --- | --- |
| Inline | One session implements the jobs in hierarchy order, without workers |
| Parallel | The orchestrator gives the jobs to subagents, several at once, and keeps no job for itself |

Both modes run from the `## Jobs` table in `PLAN.md`. In parallel mode a job starts only when
everything it waits on is done, a free subagent gets the next ready job at once, and
`tools/routing/next_jobs.py` names the jobs that may start.

## Dispatch

Every dispatch opens with the line `claude/CLAUDE.md` gives in its section "Delegation", which
sends the subagent to `claude/DISPATCH.md`. The rules live in that file and nowhere else.

Then: the task, its file list, its acceptance criterion, the skills it must load
(`cpp-code-style`, `source-comments`, ...), and the work folder path. A worker does not see the
orchestrator's memory or conversation; anything it needs is in the dispatch.

## Choosing a model

The `model-routing` skill chooses the model and the effort for each dispatch, within the limits
the same "Delegation" section sets.

## Accepting a report

The evidence a report must carry, and what a reviewer dispatch checks by name, are in the same
"Delegation" section. The orchestrator checks more:

1. The list of files changed matches the assigned set.
2. A report on work that changed a public name, a signature, a header path, a CLI command or a
   documented behaviour carries the output of `tools/documentation/check_docs_truth.py` and the
   pages and lines the change made false. Without both, the report is sent back.
3. A report on work that added tests lists them, as "Directions to the agent" in `testing` says.

A page a worker reports as false is handled as `AGENT_WORK.md` in `documentation` says.

## Instructions are read literally

A plan, a job, a review record, a ruling and an instruction from the owner are read one at a
time, in order, and done as written, by every agent, the orchestrator included.

- An instruction that cannot be done as written is never swapped for a reading of it that can.
  It is reported as not done, with the reason, and its job stays `todo` or `failed`, never `done`.
- A missing build is not a reason: the change the instruction needs is part of the job.
- The orchestrator checks each report against every instruction it was given, one by one, before
  accepting it. A report that did something else in its place is sent back, whatever reason it gives.
- An instruction the orchestrator wrote binds it too. Before each dispatch, each acceptance and
  each report to the owner, it reads its earlier instructions of the session again and checks
  each against what was done.

## Shared working tree

- Staging, stash and worktrees follow `git-workflow`, section "Shared working tree".
- Two running jobs never hold the same file, and two workers never hold one file.
