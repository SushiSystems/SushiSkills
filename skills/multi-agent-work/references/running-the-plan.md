# Multi-agent work: running the plan

Read this when writing the job list of a plan, when running a plan in parallel mode, or when a
report has done something other than its instruction said. The rules themselves are in
`../SKILL.md`.

## Why one orchestrator

Parallel agents multiply output and also multiply conflicting edits and unchecked work by the same factor. One session orchestrates so
that every other agent works on a fixed file set and reports with its evidence.

## The job list

Both modes start from the same job list: the jobs in hierarchy order, and per job its files, what
it waits on and its acceptance criterion. The list is a table under `## Jobs` in `PLAN.md`, with
the columns `Job`, `Files`, `Waits on` and `Status`; the status is `todo`, `running`, `done` or
`failed`, and the orchestrator edits it. The tasks are rows of the plan; `AGENT_WORK.md` in
`documentation` says which backlog entry serves the work folder.

## Parallel mode

`python -m <library>.tools.routing.next_jobs PLAN.md --free N` prints the ids of up to `N` jobs that may
start now. The orchestrator runs the list like this:

- It decides which subagent takes which job, and hands the jobs out without waiting for any to finish.
- When a subagent finishes a job it is free, and the orchestrator gives it the next job at once.
  A subagent that is still working gets nothing.
- The hierarchy is strict. A job starts only when everything it waits on is done. If the next job
  is blocked, the orchestrator does not wait: it gives the free subagent the next job that is ready.

A worker returns its report as its reply and the orchestrator writes `REPORT.md`; the work folder
holds one report.

## Reading instructions literally: examples

- A record that says "resize to small" ends with a small test. A ruling that says "build the
  seam" ends with the seam built.
- "Stays medium for a missing seam" (a seam is a place where a test replaces a dependency) is a reading put in place of an instruction that could not be
  done as written. It is reported as not done instead.
- "It cannot be checked without a build": the build comes once, at the end (`build-throughput`,
  boundary 8), and the change it needs, a production seam included, is part of the job.
- An instruction not done as written leaves its job `todo` or `failed`, never `done`.
