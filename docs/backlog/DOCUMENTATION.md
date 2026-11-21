# Documentation

## Remaining work

| ID | Pri | State | Title | Done when | Blocked by | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RW-26 | P2 | open | Write bulk edits through a temporary file and the changelog as fragments | a tool that rewrites many files refuses to shrink one past a set share and copies it first, and an entry is added as a file beside the changelog and joined at… |  | `docs/agent/2026_10_21_DOCS_SCALABILITY/SPEC.md` | 2026-10-22 |
| RW-27 | P2 | open | Check a built phase against a test and make a shipped design shrink | a phase marked built may name an existing test or command that a checker verifies, and a shipped design above a set size is a finding |  | `docs/agent/2026_10_21_DOCS_SCALABILITY/SPEC.md` | 2026-10-22 |
| RW-28 | P2 | blocked | Land the topic model in the main checkout of sushiengine | commit `0dcf60dc7` of sushiengine is merged into the working tree of its main checkout and `git status` shows only the other session's files | external: another session holds uncommitted edits in eight files the commit changes |  | 2026-10-22 |

## Known issues

| ID | Origin | Symptom | Workaround | Fix | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- |
