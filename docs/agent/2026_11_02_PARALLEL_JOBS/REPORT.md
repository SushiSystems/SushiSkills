# Parallel jobs: report

**Status:** Open — built and tested; the backlog entry RW-41 closes in the next commit

Ran inline, in the order A, B, C, D, in one commit.

| Job | Result |
| --- | --- |
| A | `tools/routing/job_table.py` reads the `## Jobs` table; 7 tests cover a bad status, a repeated id, a short row, a wrong header, a missing table and the table's position |
| B | `tools/routing/ready_jobs.py` picks the ready jobs and reports unknown waits and cycles; 11 tests |
| C | `tools/routing/next_jobs.py` prints the ids and sets exit codes 0 to 3; 5 tests |
| D | Row in `tools/README.md`, the table format and the command in `multi-agent-work`, the changelog line |

Evidence: `python tools/check_all.py .` printed `clean: 20 checkers, tests`. Run on this plan's
`PLAN.md` while A to C were done and D was `todo`, the command printed `D` and exited 0; with all
four `done` it exits 2.

Breaches and dependencies met: none found in the files touched. `graph_problems` sits in
`ready_jobs.py` beside the choice of jobs; both read the same job graph, so they stay together.

Not done: nothing starts subagents or writes status. The orchestrator does both.
