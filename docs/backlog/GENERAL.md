# General

## Remaining work

| ID | Pri | State | Title | Done when | Blocked by | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RW-2 | P2 | decision | Decide whether contributions from outside are accepted | the owner has named a contributor agreement, or ruled contributions out |  |  | 2026-10-19 |
| RW-3 | P2 | decision | Decide where C++ tests live | the owner has kept the `tests/` mirror, or moved C++ tests into their module at `modules/<tier>/<module>/tests/` |  |  | 2026-10-19 |
| RW-4 | P2 | decision | Decide whether the release tags are pushed | `v0.1.0` and `v0.1.1` are on the remote, or the owner has ruled them local |  |  | 2026-10-19 |
| RW-19 | P2 | decision | Name the licence of the shared code of conduct text | `NOTICE.md` names the licence of the Contributor Covenant text that `.github/CODE_OF_CONDUCT.md` adapts, or the owner replaces the text |  |  | 2026-10-19 |
| RW-35 | P1 | open | Finish the test budget: the shared command, a measured run and the gate | the limits are set from a measured SushiEngine run, the budget line gates in report mode then in gate mode, and SushiEngine runs the shared test command |  | `docs/design/TEST_BUDGET/README.md` | 2026-10-30 |
| RW-37 | P1 | decision | Run the SushiEngine tests with a JUnit file and approve the budget limits | the owner has run small, medium and one large module with --output-junit, and REPORT.md holds the numbers and the limits the owner approved |  | `docs/agent/2026_10_30_TEST_BUDGET/REPORT.md` | 2026-10-30 |
| RW-40 | P2 | blocked | Run sr test through the shared test options of sushicore once its gate is green | sr test takes the shared options and prints a budget line from a real JUnit file | external: SushiRuntime's check_all is red on its feature branch |  | 2026-11-01 |

## Known issues

| ID | Origin | Symptom | Workaround | Fix | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- |
