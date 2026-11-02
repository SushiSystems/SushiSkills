# Parallel jobs

**Status:** Open — built and tested; the backlog entry RW-41 closes in the next commit

Closes `RW-41`. The rules of parallel mode say how the orchestrator hands out jobs. This work
builds the one tool that lets it follow them without judging each case by eye.

## Problem

`skills/multi-agent-work/SKILL.md` says the orchestrator gives a free subagent the next job that is
ready, never starts a job before what it waits on is done, and never runs two jobs on one file.
Nothing computes that. With forty jobs, the orchestrator reads the whole list each time a
subagent frees up and can start a blocked job or a file clash by mistake.

## Decision

A job list is a table in `PLAN.md`, in hierarchy order. A new tool reads it and prints the jobs
the orchestrator may start now. The orchestrator still decides who takes which job, and edits the
`Status` cell itself.

| Column | Holds |
| --- | --- |
| `Job` | An id: letters and digits, no spaces |
| `Files` | Paths the job writes, separated by commas |
| `Waits on` | Job ids separated by commas, or `-` |
| `Status` | `todo`, `running`, `done` or `failed` |

A job is ready when:

1. Its status is `todo`.
2. Every job it waits on is `done`. A `failed` job blocks the jobs behind it until the
   orchestrator changes the status.
3. None of its files equals, or lies inside or above, a file of a `running` job.

`python tools/routing/next_jobs.py PLAN.md --free N` prints the ids of up to `N` ready jobs, in
list order, one per line. A job picked earlier in the same run counts as running for the next, so
two printed jobs never clash. Exit 0 when it prints at least one id, 1 when none is ready and jobs
remain, 2 when every job is `done`. A malformed table, an unknown id in `Waits on` or a cycle is
reported as `path:line: rule: message` and exits 3.

The tool never writes. It sits in `tools/routing/` beside `summarize_dispatches.py`, which also
reads `docs/agent`.

## Open for the owner

1. The tool name, its place and the table columns above are a public shape. They stand unless the
   owner changes them.
2. How the plan runs, inline or in parallel, is the owner's choice (`multi-agent-work`).

## Not in scope

Starting subagents, recording status by itself and enforcing the list from a hook. The orchestrator
does these.
