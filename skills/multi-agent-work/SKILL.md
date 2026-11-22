---
name: multi-agent-work
description: Use when dispatching subagents, running agents in parallel, splitting a plan into tasks for other agents, or reviewing a report that came back from an agent, in a repository.
---

# Multi-Agent Work

One session orchestrates; every other agent is a worker with a fixed file set. Job list, parallel mode,
literal-reading examples: `references/running-the-plan.md`.

## Roles

- Orchestrator: plans, dispatches, reviews, integrates, commits; writes code, design, manual,
  changelog, backlog.
- Worker: one task, one acceptance criterion; writes its dispatch's files, a module README only
  when listed, and its `docs/agent/` folder; never `docs/design/`, the manual,
  `CHANGELOG.md` or `docs/backlog/`; commits only when told; reports findings under "Backlog
  findings"; the orchestrator files them.

## Planning

- Hierarchy first: interfaces before callers; a module boundary and its build edges come
  before either side.
- One acceptance criterion per task; tasks are plan rows, not backlog entries. No task builds or
  tests; one build and one test run follow the last task (`build-throughput`, boundary 8).
- The owner picks the mode: inline (one session, jobs in hierarchy order) or parallel (subagents
  only; the orchestrator keeps no job). Both use one job list.

## Dispatch

Open with the line `claude/CLAUDE.md` gives in "Delegation"; the rules live only in
`claude/DISPATCH.md`. Give task, files, criterion, skills, work folder; a worker
sees no orchestrator memory. `model-routing` sets model and effort. Staging, stash and
worktrees follow `git-workflow`; no file is held by two jobs.

## Accepting a report

Beyond the evidence in "Delegation":

1. Changed files match the assigned set.
2. A change to a public name, signature, header path, CLI command or documented behaviour carries
   `check_docs_truth.py` output and the pages and lines made false (`AGENT_WORK.md` in
   `documentation`); else send it back.
3. Added tests are listed (`testing`).

## Instructions are read literally

Every agent, orchestrator included, does each plan, job, record, ruling and owner instruction one
at a time, in order, as written. One that cannot be done so is reported not done, with the reason,
never swapped for a reading that can. A missing build is no reason. The orchestrator checks each report against every
instruction, sends back a different result and rereads its earlier instructions before each dispatch,
acceptance and owner report.
