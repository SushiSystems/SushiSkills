# Parallel jobs: plan

**Spec:** `SPEC.md` in this folder. **Rules:** the `multi-agent-work`, `python-code-style`,
`project-tools` and `documentation` skills. **Runs:** inline until the owner chooses otherwise.

## Global constraints

- Tests and checkers run through `python tools/check_all.py .`.
- A change to the tool changes its test and its row in `tools/README.md` in the same commit.
- Prose is written under `humanizer`; the changelog line carries the scope `multi-agent-work`.
- Each finished job is written into `REPORT.md` at once, with its commit.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| A | `tools/routing/job_table.py`, `tools/tests/test_job_table.py` | - | done |
| B | `tools/routing/ready_jobs.py`, `tools/tests/test_ready_jobs.py` | A | done |
| C | `tools/routing/next_jobs.py`, `tools/tests/test_next_jobs.py` | B | done |
| D | `tools/README.md`, `skills/multi-agent-work/SKILL.md`, `docs/reference/CHANGELOG.md` | C | done |

## A. Read the table

`job_table.py` reads the `Jobs` table of a plan into `Job` records (id, files, waits on, status)
and reports a malformed row with its line.

**Acceptance:** a table with a bad status, a repeated id or a missing column yields findings with
line numbers; a good table yields its jobs in order.

## B. Choose the ready jobs

`ready_jobs.py` takes the jobs and a count and returns the ids that may start, by the three rules
of `SPEC.md`, treating each pick as running.

**Acceptance:** tests cover a blocked job being skipped for a later ready one, a failed dependency,
a file inside a running job's folder, two ready jobs that share a file, and a cycle.

## C. The command

`next_jobs.py` parses `PLAN.md` and `--free`, calls A and B, prints the ids and sets the exit code
of `SPEC.md`.

**Acceptance:** the four exit codes each have a test, and a run on this `PLAN.md` prints `A`.

## D. Rules and manual

The row in `tools/README.md`, the sentence in `multi-agent-work` that names the command, and the
changelog line.

**Acceptance:** `python tools/check_all.py .` is clean.
