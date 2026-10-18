# Backlog format: report

Part 1 of `PLAN.md`, the work in this repository, is done. Part 2, the migration of every other
estate repository, has not started; it is `RW-14` in the backlog.

## What changed

| Task | Files |
| --- | --- |
| 1. The format in the skills | `skills/documentation/BACKLOG_FORMAT.md` (new), `skills/documentation/SKILL.md`, `skills/documentation/AGENT_WORK.md`, `skills/debugging/SKILL.md`, `skills/testing/SKILL.md` |
| 2. Status lines, archive clock, forbidden kinds | `tools/documentation/check_docs_layout.py`, `tools/documentation/design_status.py` (new), `tools/tests/test_check_docs_layout.py`, the status lines of the four older work folders |
| 3. The backlog checker | `tools/documentation/check_backlog.py` (new), `tools/tests/test_check_backlog.py` (new) |
| 4. This repository on the format | `docs/design/REMAINING_WORK.md`, `docs/reference/KNOWN_ISSUES.md`, `tools/check_all.py`, `tools/README.md`, `skills/project-tools/SKILL.md`, `skills/README.md` |

Where the build differs from `SPEC.md`:

- IDs carry no leading zeros: `RW-14`, not `RW-014`.
- The status reader moved out of `check_docs_layout.py` into `design_status.py`, which both
  checkers import, so the four forms are written once.
- `--report` of `check_backlog.py` also prints each sibling it read and the branch it is on, the
  risk `PLAN.md` names.

## Fact check of this repository

Every entry was read against the code and `git log` on 2026-10-19.

| Entry | Verdict |
| --- | --- |
| RW-1, the archive clock in the gate | True. The clock now reads the status date; the oldest work folder is dated 2026-10-05, so the first failing push is on 2027-01-04 |
| RW-2, RW-3 | True; owner decisions |
| RW-4, pushing the tags | True. `git ls-remote --tags origin` lists no tag |
| RW-5 | True. `check_source_comments.py` checks `@brief` in the file block only |
| RW-6 | True. `check_layering.py` reads C-family suffixes only |
| RW-7, RW-8 | True. `check_changelog.py` checks a capital letter and no order |
| RW-9, RW-13 | True. `live_documents` reads `docs/` only; `K_LINK` reads inline links, not images |
| RW-10 | True. `rule_module_readmes` reads `modules/<tier>/<module>/` only |
| RW-11, RW-12 | True. `rule_license_block` takes C-family and Python suffixes |
| RW-14 | New. Foreign under D1: closed by commits in the other repositories |
| RW-15, the estate programmes | Foreign under D2. The section held no task; it is now the task of handing them over |
| KI-1 | True |
| KI-2 | True; the fix is `RW-4` |

## Checks

```
$ python tools/check_all.py .
clean: 10 checkers, tests
$ python tools/documentation/check_backlog.py . --report
rule_shape: 0
rule_ids: 0
rule_paths: 0
rule_references: 0
rule_entry_size: 0
rule_design_coverage: 0
total: 0
siblings read: project-mobilerts-legacy (main), sushiai (main), sushiblas (main), sushicore (main), sushidsp (main), sushiengine (main), sushilog (main), sushiruntime (main), sushistack (main), sushitrack (main), sushiweb (main)
sibling references not checked: 0
entries naming a sibling: 0
```

The new tests of `test_check_docs_layout.py` were run red before the rules existed (an import
error on the missing rules). Those of `test_check_backlog.py` were written before the checker
but first run against it, so they were never seen failing for the right reason; one failed on
the first run and found a fault reported twice.

## SOLID and dependencies

- `check_backlog.py`, `Repository`: it holds the two parsed files, resolves references and finds
  sibling mentions. Three jobs in one class; each is a few lines and all read the same parsed
  files, so they were kept together. Splitting the reference resolver out is the repair if the
  class grows.
- `check_backlog.py` and `check_docs_layout.py` each define a code-span and a fence pattern. The
  two copies are one line each and match different needs (a span's content, a fence's opener),
  but they are the same knowledge in two files.
- `Kind` carries a function for the fields each file needs. The set of kinds is closed at two,
  so this is not an interface for growth.
- No dependency was added. `check_backlog.py` uses `subprocess` for one `git rev-parse` under
  `--report`.

## Not done

- Part 2, the migrations: `RW-14`.
- Repositories outside the estate (ipekweb, mayagaweb, serkangaripweb) stay out of scope until
  the owner decides.
