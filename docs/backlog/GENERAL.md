# General

## Remaining work

| ID | Pri | State | Title | Done when | Blocked by | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RW-2 | P2 | decision | Decide whether contributions from outside are accepted | the owner has named a contributor agreement, or ruled contributions out |  |  | 2026-10-19 |
| RW-3 | P2 | decision | Decide where C++ tests live | the owner has kept the `tests/` mirror, or moved C++ tests into their module at `modules/<tier>/<module>/tests/` |  |  | 2026-10-19 |
| RW-4 | P2 | decision | Decide whether the release tags are pushed | `v0.1.0` and `v0.1.1` are on the remote, or the owner has ruled them local |  |  | 2026-10-19 |
| RW-19 | P2 | decision | Name the licence of the shared code of conduct text | `NOTICE.md` names the licence of the Contributor Covenant text that `.github/CODE_OF_CONDUCT.md` adapts, or the owner replaces the text |  |  | 2026-10-19 |
| RW-35 | P1 | open | Carry the industrial testing design into every repository, wave by wave | every repository named in the Rework table of the testing design has measured, reworked and remeasured its suite, each in its own work folder |  | `docs/design/TEST_PIPELINE/README.md` | 2026-10-30 |
| RW-37 | P1 | decision | Run one repository's small and medium tests with JUnit and approve the time limits | the owner has run one measured baseline and the testing Time table holds limits calibrated from it, so the time lines can gate |  | `docs/agent/2026_11_03_INDUSTRIAL_TESTING/REPORT.md` | 2026-10-30 |
| RW-40 | P2 | blocked | Run sr test through the shared test options of sushicore once its gate is green | sr test takes the shared options and prints a time line from a real JUnit file | external: SushiRuntime's check_all is red on its feature branch |  | 2026-11-01 |
| RW-42 | P1 | open | Split the checkers into a pure core and a file-walking shell so their tests are small | every checker's rules pass the purity run, each test file keeps the shell in at most one medium class, and no mutant survives on the changed lines |  | `docs/design/TEST_PIPELINE/README.md` | 2026-11-03 |
| RW-45 | P2 | open | Pilot mutation testing of the diff on host-compiled code in one repository | one repository prints surviving mutants on changed lines from its test command, and its time is recorded |  | `docs/design/TEST_PIPELINE/README.md` | 2026-11-03 |
| RW-53 | P1 | blocked | Make the closed-product licence drafts the LICENSE of SushiEngine and Project mobileRTS | both repositories carry the lawyer-reviewed licence with the repair right and the sunset clause, and a Trustee holds the deposit | external: a lawyer's review of the drafts | `docs/agent/2026_11_06_LICENCE_CHANGE/SPEC.md` | 2026-11-06 |
| RW-70 | P2 | open | Replace every figure of speech in the skills with its literal rule and an example | no skill, claude or sushisystems file holds a metaphor; SOLID has a literal definition with examples |  | `docs/agent/2026_11_24_LITERAL_WORDING/PLAN.md` | 2026-11-24 |
| RW-71 | P3 | open | Measure with a fixed task set whether sessions follow the doctrine and storage rules | a task set with a checklist per task runs before and after a hook change and the results are compared |  |  | 2026-11-24 |
| RW-72 | P2 | decision | Decide whether a PreToolUse hook blocks writes outside the repository and scratchpad | the owner rules yes or no; a yes lists the paths and the size limit the hook enforces |  |  | 2026-11-24 |
| RW-73 | P1 | open | Print the doctrine and storage skills verbatim at session start; stop caches in the tree | session_start.txt holds the five source files verbatim; env stops bytecode and pytest caches; tests pass |  | `docs/agent/2026_11_24_LITERAL_WORDING/PLAN.md` | 2026-11-24 |

## Known issues

| ID | Origin | Symptom | Workaround | Fix | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- |
