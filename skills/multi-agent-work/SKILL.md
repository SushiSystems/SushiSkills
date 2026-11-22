---
name: multi-agent-work
description: Use when dispatching subagents, running agents in parallel, splitting a plan into tasks for other agents, or reviewing a report that came back from an agent, in a repository.
---

# Multi-Agent Work

One session orchestrates; every other agent is a worker with a fixed file set. Read
`references/running-the-plan.md` for job lists, parallel mode and literal-reading examples, and
`references/roles-and-planning.md` for the role and mode tables.

## Roles

- Orchestrator: plans, dispatches, reviews, integrates, commits; writes code, design, manual,
  changelog, backlog.
- Worker: one task, one acceptance criterion; writes its dispatch's files, a module README only
  when listed, and its work folder under `docs/agent/`. Never `docs/design/`, the manual,
  `CHANGELOG.md` or `docs/backlog/`; never commits unless told; reports findings under "Backlog
  findings" for the orchestrator to file.

## Planning

- Hierarchy first: interfaces before callers; a module boundary and its build edges are
  committed before either side is written.
- One acceptance criterion per task; tasks are plan rows, not backlog entries. No task builds or
  tests; one build and one test run follow the last task (`build-throughput`, boundary 8).
- The owner picks inline or parallel (subagents only, the orchestrator keeps no job). Both run
  from the `## Jobs` table in `PLAN.md`; `tools/routing/next_jobs.py` names jobs that may start.

## Dispatch

Open with the line `claude/CLAUDE.md` gives in "Delegation"; the rules live in
`claude/DISPATCH.md` only. Give task, files, acceptance criterion, skills, work folder; a worker
sees none of the orchestrator's memory. `model-routing` sets model and effort.

## Accepting a report

Evidence is in "Delegation". Also:

1. Files changed match the assigned set.
2. A change to a public name, signature, header path, CLI command or documented behaviour carries
   `check_docs_truth.py` output and the pages and lines made false; else send it back.
3. Added tests are listed (`testing`, "Directions to the agent").

A page reported false follows `AGENT_WORK.md` in `documentation`.

## Instructions are read literally

Every agent, orchestrator included, does each plan, job, record, ruling and owner instruction one
at a time, in order, as written.

- One that cannot be done as written is reported not done, with the reason, never swapped for a
  reading that can; its job stays `todo` or `failed`.
- A missing build is no reason; the change needed is part of the job.
- The orchestrator checks each report against every instruction and sends back a different result.
- Before each dispatch, acceptance and owner report it rereads its own earlier instructions.

## Shared working tree

Staging, stash and worktrees follow `git-workflow`. No file is held by two jobs.
