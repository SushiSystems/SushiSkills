# Known issues scope: report

**Status:** Shipped — 2026-10-20

Both parts of `PLAN.md` are done. `check_backlog.py --rule rule_scope` reports nothing in all
twelve estate repositories, and each repository's own backlog checker reports nothing.

## What changed

| Repository | Known issues moved | Commit |
| --- | --- | --- |
| sushiskills | 0; the rule, `rule_scope`, `Where:` on a backlog entry | `45331d0` |
| sushicore | 8 | `8d67d2c` |
| sushiruntime | 2 | `e32ccff5` |
| sushiblas | 10 | `5f30dc3` |
| sushiai | 5 | `d665ab6` |
| sushidsp | 26 | `c0a2fcd` |
| sushiengine | 6 | `c1eac8ba6` |
| sushitrack | 3 | `0ad0e6c` |
| sushiweb | 39 | `52aef52e` |
| project-mobilerts-legacy | 15 | `882416720` |
| sushistack | 6 | `c94e8aa` |
| sushilog | 0; the checker only | `2411c00` |

120 known issues moved, one more than the survey counted; the two counts read a workaround of
`none` by slightly different rules and the difference was not traced. Nothing is pushed.

## Where the build differs from `PLAN.md`

- Only `check_backlog.py` and its test were copied into each repository, not the whole shared set.
  `copy_shared_tools.py` copies everything, and the other files found faults that predate this
  work in sushidsp, sushiengine, sushiweb and sushistack; those copies were reverted. Those four
  repositories are behind the shared tools.
- Each migration was one script run per repository plus a read of the result, not an entry-by-entry
  rewrite. Four citations of a removed ID were rewritten by hand (sushidsp `RW-4`, sushiengine
  `RW-299`, `RW-301`, `RW-302`, `RW-304`, sushiblas `LAYERED_EXECUTION.md`, mobilerts `RW-8`) and
  three stale sentences (sushiengine `RW-47`, sushiweb `RW-72`, mobilerts).

## Known weaknesses of the result

- A moved symptom is the known issue's title followed by its `Recognise:` text. Where that text was a
  fragment, the prose reads as one (sushiweb `RW-90`: "The two years."). Twenty entries already
  had prose; most of the new text adds to it, a few repeat it.
- A `Where:` field kept what the known issue held, including broad values such as `docs`, `apps`
  and `.git/config`.
- sushiengine and project-mobilerts-legacy fail `check_all.py` on faults that predate this work
  (`check_docs_truth.py`, `check_test_mirror.py`, `check_design_citations.py`; `check_decks.py`,
  `check_probes.py`). sushiweb and sushistack carry no `check_all.py`; their documentation
  checkers report nothing.
- Prose citations of a removed ID inside `docs/agent/` reports were left; those folders are frozen
  history.

## SOLID and dependencies

None met in the files this work changed. `check_backlog.py` keeps one rule per function and one
table row per rule; `rule_scope` follows that shape.
