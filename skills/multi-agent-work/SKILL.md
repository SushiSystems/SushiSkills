---
name: multi-agent-work
description: Use when dispatching subagents, running agents in parallel, splitting a plan into tasks for other agents, or reviewing a report that came back from an agent, in a Sushi Systems repository.
---

# Multi-Agent Work

Parallel agents multiply output and multiply mess by the same factor. One session orchestrates;
every other agent is a worker with a fixed file set, a fixed place to write, and a report that
must carry its evidence.

## Roles

| Role | Does | Writes |
| --- | --- | --- |
| Orchestrator | Plans, dispatches, reviews reports, integrates, commits | Code, design, manual, changelog, backlog |
| Worker | One task with one acceptance criterion | The task's files, its module README, its work folder under `docs/agent/` |

A worker never edits a file outside its assigned set, never writes to `docs/design/`, the
manual, `CHANGELOG.md` or `REMAINING_WORK.md`, and never commits unless the dispatch says so.

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

A wave plan lists, per wave: the tasks, each task's files, what each waits on, and the build that
closes the wave.

## Dispatch

Every dispatch opens with this block, verbatim, whatever the task:

```
1. SOLID, without exception. Every unit is a brick: one responsibility, detachable and
   re-attachable without touching its neighbours, rebuildable on its own. Siblings that do the
   same kind of thing are shaped the same. No quick hacks that happen to pass.
2. Before writing any prose, apply the `humanizer` skill in the language of the prose.
3. Do not run the build system or edit build configuration unless this task says so.
4. Write only to the files listed below and to docs/agent/<work folder>/.
5. Report what was done and what was not. Paste the output of every verification you claim.
```

Then: the task, its file list, its acceptance criterion, the skills it must load
(`cpp-code-style`, `source-comments`, ...), and the work folder path.

A worker does not see the orchestrator's memory or conversation. Anything it needs is in the
dispatch.

## Choosing a model

| Work | Tier |
| --- | --- |
| Implementation, exploration, mechanical checks | Fast, capable model |
| Review, architecture, anything that fixes an interface | Strongest reasoning model |

The model is set on every dispatch, never inherited by default.

## Accepting a report

A report is sent back, not accepted, when it lacks any of:

- the list of files changed, matching the assigned set;
- pasted output of every check it claims (syntax check, tests, checkers);
- what was not done.

Reviewer dispatches check SOLID shape and prose register as named items.

## Shared working tree

- Stage by path. Check `git diff --cached --stat` before every commit.
- No `git stash`, no `git add -A`, no worktrees unless the owner asks.
- Two workers never hold the same file in one wave.
