# Backlog format

**Status:** Open — part 1 built on 2026-10-19; the migrations are `RW-14`.

The `documentation` skill says where `REMAINING_WORK.md` and `KNOWN_ISSUES.md` live and that
each repository has one of each. It says nothing about what goes inside them, and
`check_docs_layout.py` only checks that they exist. Every rule this work adds is written for any
repository; the repositories below are the evidence, not the subject.

## What the estate showed

A survey of the twelve estate repositories on 2026-10-19 found:

- Three ways of grouping the backlog: by area (sushiblas), by programme (sushistack, sushicore)
  and by the date a batch was opened (sushidsp).
- Two shapes of known issue: a table of rows up to 260 characters (sushiblas, sushiai,
  sushicore, sushitrack) and a heading per issue with prose up to 60 lines (sushiengine,
  sushiweb, sushidsp). The largest file is 928 lines.
- A third kind of record with no home: built but never measured or verified. sushiblas files it
  under known issues ("Verification state"), sushiengine under the backlog ("Unmeasured"),
  sushiruntime as "Verification not yet run", sushidsp as "Waiting on the maintainer's ears".
- Finished work kept in place: 24 `Done:` lines in project-mobilerts-legacy, a "What a build has
  confirmed" section in sushiai, test counts of a past run in sushiblas.
- Work owned by another repository. sushiblas lists "Migrate SushiAI onto the views", "Tag
  SushiRuntime v0.4.0" and "Document colour, theme and exit codes once in sushicore". No commit
  in sushiblas can close any of them.
- Paths that resolve nowhere: `docs/CLAUDE.md`, `docs/agent/specs/...`, `docs/superpowers/...`
  from an older layout, and paths shortened below the module (`blas/sparse.hpp`).
- Design phases copied into the backlog in detail, so a phase is described in two places. One
  repository, sushiengine, keeps its backlog as an index over design documents instead, with a
  `State` column and a local checker that fails when a design document is missing from it.
- An order file beside the backlog that rotted. sushiengine's `PRIORITY_ORDER.md` had no content
  change after 2026-09-19 while 533 commits landed: it counts 18 unmeasured rows against 51 in
  the backlog, calls R3 unblocked while the backlog lists it `blocked`, and keeps finished items
  struck through. Nothing failed when an item it named closed.
- Roadmap, journal, handover and milestone files that repeat the backlog or the changelog:
  sushiengine's `ROADMAP.md` ("Milestones", what has landed), `ROADMAP_JOURNAL.md` (dated
  entries) and `ROADMAP_HANDOVER.md`.
- Status lines a tool cannot read. Of sushiengine's 67 design documents, 4 use the `Open` or
  `Shipped` form `AGENT_WORK.md` gives; the rest are prose ("in progress; ...", "designed ...,
  not started", "living; ..."). One reads "approved and executed 2026-08-22" and is still open.
  sushiai's `ROADMAP.md` reads "Shipped ... superseded on 2026-10-07" and is still under
  `design/`.
- Bulk edits hiding age. Em dash and rename passes on 2026-10-16 and 2026-10-17 touched every
  design document, so every one looks fresh. Counting only commits that touch eight or fewer
  Markdown files, 29 of sushiengine's open design documents have had no change of content for
  three to eight weeks. `rule_archive_candidates` measures idleness by commit date, so a
  shipped document touched by such a pass never becomes a candidate.

## Owner decisions this spec rests on

All taken on 2026-10-19.

| # | Decision |
| --- | --- |
| D1 | An entry lives in the repository whose commit closes it. A repository that depends on it cites it by ID and does not copy it. |
| D2 | A programme that spans repositories lives in the backlog of the repository that coordinates the others. Its entry lists the entries in other repositories it waits on. |
| D3 | IDs are `RW-<n>` and `KI-<n>` inside a repository and `<repository> RW-<n>` from outside it. A `Next id:` line at the top of each file holds the counter; an ID is never reused. |
| D4 | The checker knows the other repositories without a list kept by hand (see section 5). |
| D5 | A sibling repository named in an entry's title or body is listed by `--report` and is not a failure. Paths and ID references are failures. |
| D6 | A backlog entry has a state: `decision`, `open`, `blocked` or `unmeasured`. A claim withdrawn from a design document leaves its work `open`. |
| D7 | `KNOWN_ISSUES.md` holds defects only. Each names its origin; a defect whose cause is in a sibling repository has an entry there too, and the affected repository cites it. |
| D8 | Neither file records finished work. A closed entry is deleted; the changelog records the change and the root README's `## Status` records what works. |
| D9 | A backlog entry for a design phase is one entry that cites the design document. The detail stays in the design document. Every open design document is cited by at least one entry. |
| D10 | The work runs inline in this session. |
| D11 | No order or priority file sits beside the backlog. The owner's order lives in an optional `## Next` section of the backlog, as IDs the checker resolves. |
| D12 | A status line has one of four forms a tool reads, and the archive clock runs from the date in it, not from commit dates. |
| D13 | No roadmap, journal, handover, milestone or priority file is kept under `docs/` outside `agent/` and `archive/`. Phases live in their design document, order in `## Next`, finished work in the changelog, a journal or a handover in the work folder that wrote it. |

D4 was taken as "a shared list of repositories". The owner then ruled that nothing in this
repository names a particular repository, so the list is replaced by discovery.

The engineer decided the field names, the ceilings, the rule names and the discovery.

## Design

### 1. `skills/documentation/BACKLOG_FORMAT.md`

A new file beside `CHANGELOG_FORMAT.md`, read before writing an entry in either file. It holds
sections 2 to 4, with examples that name no real repository. `SKILL.md` gains a row in its "Read
before" table.

### 2. `REMAINING_WORK.md`

```
# Remaining work

Next id: RW-016

## Next

- RW-014 Every speed figure in the design rests on these runs

## Decisions waiting for the owner

### RW-003 Choose whether contributions from outside are accepted
- State: decision
- Done when: the owner has named the contributor agreement, or ruled contributions out

## Kernels

### RW-014 Run the benchmark programs that have not run
- State: unmeasured
- Done when: each program has a recorded run on every device the build supports
- Source: `docs/design/KERNELS.md` §4

### RW-015 Bind a late operand address in the recorder
- State: blocked
- Blocked by: runtime RW-022
- Done when: the recorder accepts an address bound at run time
```

| Part | Rule |
| --- | --- |
| Title | `# Remaining work` |
| Counter | `Next id: RW-<n>` before the first section; every ID in the file is below it |
| `## Next` | Optional, before every other section. The owner's order: at most ten lines `- RW-<n> <why it comes here>`, each ID an entry of this file |
| Decisions section | `## Decisions waiting for the owner`, present when any entry has `State: decision`, and holding only those |
| Other sections | `## <Area>`, a module or a subject. No date, no programme of another repository, no section of finished work |
| Entry heading | `### RW-<n> <what is to be done>`, an imperative sentence |
| `State:` | Required. `decision`, `open`, `blocked` or `unmeasured`. `unmeasured` is built work whose acceptance is a run or a measurement, not a commit |
| `Done when:` | Required. One acceptance criterion, the one `multi-agent-work` asks of a task |
| `Blocked by:` | Required when the state is `blocked`, absent otherwise. IDs (`RW-<n>`, `<repository> RW-<n>`, `<repository> KI-<n>`) or `external: <reason>` for a block outside the estate |
| `Source:` | Optional. A design document, with `§<n>` when it names a section, or a file of a work folder |
| Body | Optional prose under the fields |
| Size | An entry is at most 25 lines, heading included |

An ID in `## Next` that loses its entry fails `rule_references`, so the commit that closes an
item also updates the order. A separate order file has no such tie, which is why one rots.

### 3. `KNOWN_ISSUES.md`

```
# Known issues

Next id: KI-008

## Storage

### KI-007 The host faults when it reads a shared buffer while a kernel runs
- Origin: runtime
- Upstream: runtime KI-004
- Where: `modules/io/source/io.cpp`
- Recognise: the process exits with an access fault during a print or a save
- Workaround: finish the queue before a host read
```

| Part | Rule |
| --- | --- |
| Title, counter, sections | As in the backlog, with `KI-<n>`. No `## Next`, no decisions section |
| Entry heading | `### KI-<n> <the symptom as seen>` |
| `Origin:` | Required. `own`, `toolchain`, `dependency` or the name of a sibling repository |
| `Upstream:` | Required when the origin is a sibling, absent otherwise. That repository's `KI-<n>` |
| `Where:` | Required when the origin is `own`. Paths from the repository root, at most five |
| `Cause:` | Required unless the origin is a sibling, whose entry holds it; `unknown` is a value |
| `Recognise:` | Required. How a reader tells this issue from another |
| `Workaround:` | Required; `none` is a value |
| `Fix:` | Required when the origin is `own`. `RW-<n>`, or `none, <reason>` for a limitation chosen on purpose |
| `Owner:`, `Fix by:` | Required for a quarantined test, as `testing` rule 5 asks |
| `Source:` | Optional. The investigation, usually a work folder's `REPORT.md` |
| Size | At most 25 lines; a longer investigation goes in the `Source:` file |

Built work that was never measured or verified is not a defect. It is a backlog entry with
`State: unmeasured`.

### 4. Rules common to both files

- A field is a line `- <Name>: <value>`; a value runs on to the next line indented by two
  spaces. A field-shaped line with an unknown name is a finding, which catches `- Done:`.
- A path in `Where:` or `Source:` is written from the repository root and exists.
- An entry is deleted by the commit that closes it, in the same commit as its changelog line.
- An ID that another entry cites is closed only after the citing entry is updated.

### 5. `tools/documentation/check_backlog.py`

A shared checker on the `checking.checker` frame, run by `check_all.py`, copied out by
`copy_shared_tools.py`.

| Rule | Finds |
| --- | --- |
| `rule_shape` | A missing title or counter, a section or an entry heading out of shape, an unknown or missing field, a state outside the four, a `decision` entry outside its section or another state inside it |
| `rule_ids` | A duplicate ID, an ID at or above `Next id:`, a `KI` ID in the backlog or an `RW` ID in the known issues |
| `rule_paths` | A path in `Where:` or `Source:` that does not exist |
| `rule_references` | A local ID in `## Next`, `Blocked by:`, `Fix:` or `Upstream:` with no entry; a sibling ID with no entry when that sibling is found; `Origin:` naming a sibling with no `Upstream:` |
| `rule_entry_size` | An entry above 25 lines |
| `rule_design_coverage` | A design document whose status is `Open` and that no `Source:` cites |

A sibling is a folder beside the repository, `<root>/../<name>`, that holds
`docs/design/REMAINING_WORK.md`. The folder name is the repository name an ID is written with. A
reference to a sibling that is not checked out is counted by `--report`, not checked.

`--report` adds, without failing, every entry whose title or body names a sibling outside
`Origin:`, `Upstream:` and `Blocked by:`. A reader decides whether that entry belongs here (D5).

### 6. Status lines and the archive clock (D12)

`AGENT_WORK.md` gives the status line four forms:

| Form | Meaning |
| --- | --- |
| `**Status:** Open — <where it stands>` | Intent with work left |
| `**Status:** Shipped — <YYYY-MM-DD>` | Built as designed on that date |
| `**Status:** Superseded — <YYYY-MM-DD> by <link>` | Replaced by another document |
| `**Status:** Withdrawn — <YYYY-MM-DD>, <reason>` | Given up by the owner |

Text may follow the date after a full stop. The line is required in every design document and in
the first file of every work folder (`SPEC.md`, else `PLAN.md`, else `REPORT.md`); closing a
piece of work sets its date. A file of a split design topic other than its `README.md` carries
none.

`check_docs_layout.py` changes:

- `rule_status_lines` accepts only the four forms.
- `rule_archive_candidates` measures from the date in a `Shipped`, `Superseded` or `Withdrawn`
  line. An `Open` document is never a candidate; its staleness is caught through
  `rule_design_coverage` and the fact check of the entry that cites it.
- `rule_forbidden_kinds` (new): a file under `docs/` outside `agent/` and `archive/` whose name
  contains `ROADMAP`, `JOURNAL`, `HANDOVER`, `MILESTONE`, `PRIORITY` or `TODO` (D13).

### 7. Rules elsewhere that move into the format

- `debugging`, "Known issues": the four parts of an entry become a citation of
  `BACKLOG_FORMAT.md`.
- `testing` rule 5: the quarantine entry cites the `Owner:` and `Fix by:` fields.
- `AGENT_WORK.md`: the four status forms, the close step setting the date, the archive clock.
- `project-tools`: the checker's row, and a manual audit, "Backlog fact check", run per
  repository: for each entry, read the code it names, search `git log` since the entry's last
  change for a commit that closed it, and record each verdict (true, stale, closed, foreign) in
  the work folder's `REPORT.md`. Each open design document is read the same way.
- `tools/README.md` and `check_all.py`: the new checker.

### 8. Migration

Every estate repository migrates, lower tiers first, so that an `Upstream:` or `Blocked by:`
target exists before it is cited. Each migration is that repository's own work folder, and every
repository-specific decision is taken there, not here. Every migration takes the same steps:

1. Copy the shared tools in.
2. Run the fact check and write the inventory into the work folder: each entry and each open
   design document marked true, stale, closed or foreign, with the owning repository for each
   foreign entry; each order, roadmap, journal, handover or milestone file with where each part
   of it goes.
3. The owner approves the inventory. Deleting or moving an entry, a design document's new
   status and the order in `## Next` are the owner's decisions.
4. Convert both files and every status line; move foreign entries to their owners; delete closed
   entries; fold the files D13 forbids into their homes; move what works into the root README's
   `## Status`; remove any local checker a shared rule replaces.
5. `python tools/check_all.py .` passes.

A foreign entry moves into a repository that comes later in the order when that repository is
migrated, and the citing entry gets its ID then.

## Acceptance

- `BACKLOG_FORMAT.md`, `check_backlog.py`, the `check_docs_layout.py` changes and their tests are
  in sushiskills, and `python tools/check_all.py .` passes there with sushiskills' own files
  converted.
- In each migrated repository, `check_all.py` passes and `check_backlog.py --report` lists no
  foreign entry the owner has not accepted.

## Out of scope

- Order inside a section. It carries no priority; `## Next` does.
- Generating the backlog from the design documents. The coverage rule checks the link and does
  not write entries.
- Repositories outside the estate. ipekweb, mayagaweb and serkangaripweb have no documentation
  tree; sushifx carries upstream documentation. Whether any of them joins is the owner's call,
  and joining is its own build-out.
