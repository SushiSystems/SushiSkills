# Backlog and design tool: specification

**Status:** Shipped — 2026-10-28

The owner asked on 2026-10-28 for the backlog, the known issues and the design documents to stay
Markdown in git, behind a command line that reads and writes them as if they were a database. The
owner delegated every ruling below to the orchestrator and approved them the same day.

## 1. Problem

Measured on `sushiengine` on 2026-10-28:

| Measure | Value |
| --- | --- |
| `docs/backlog/README.md` | 1 670 lines, `Next id: RW-475` |
| `docs/backlog/README.md` | 399 lines |
| Design topics | 45, and 14 more under `_REVISION/` |
| Work folders in `docs/agent/` | 19 |
| `## Next` | 9 lines and a blank line; several are status notes, not an order |

Four failures follow.

1. **Entries are free text.** The format allows prose after the fields, so each agent adds a
   paragraph. `RW-461` carries a summary of a solver comparison; the heading of `RW-2` is
   `§3.3–§3.7` and says nothing about what is to be done.
2. **Nothing computes an order.** `## Next` is kept by hand and drifts. There is no priority and
   no age.
3. **One file per kind.** Two branches that each add an entry edit the same file and take the same
   `Next id`.
4. **One subject, many topics.** The atmosphere is described in `ATMOSPHERE_SYSTEM`,
   `PLANETARY_APPEARANCE`, `VOLUMETRIC_CLOUDS` and `_REVISION/SOLAR_SYSTEM_OVERHAUL`. Every design
   carries `**Modules:**`, but nothing stops two topics from naming the same module, so each new
   agent opens a new topic.

The trial of moving these records into Work at `company.sushisystems.io` (sushiweb, `WORK` design)
did not hold: the records left the place where agents and commits are. That application becomes a
light board; the records stay in the repositories.

## 2. Rulings

| Question | Ruling |
| --- | --- |
| Where the tool lives | In sushicore, as two command groups, `backlog` and `design`, that every module CLI registers: `se backlog next`, `sr design new` |
| Who writes the files | The tool. A person or an agent reads and writes through it; `check` fails a file edited by hand into a shape the tool would not write |
| Output | Every command takes `--json`; agents use it |
| Store | `docs/backlog/<AREA>.md`, one file per area, one table row per entry |
| Areas | A fixed set in the repository's configuration; an entry in an unknown area is refused |
| Priority | `P0` to `P3`, with the age limits of section 4 |
| Order | Computed by `backlog next`. `## Next` is retired; the owner's pins sit in the configuration |
| Prose | None in the store. A cell has a length ceiling; a longer explanation goes in the file `Source` names |
| `Where` | Retired. The paths a piece of work changes are read from its source |
| Design ownership | A module belongs to exactly one topic. `**Modules:**` is required on every topic |
| New topic | Only through `design new`, which refuses a module another topic owns |
| Topic depth | Two levels: a topic, and pages and phases under it. A subject such as clouds is a page of `ATMOSPHERE`, not a topic |
| Work folders | Unchanged: `SPEC.md`, `PLAN.md`, `REPORT.md`. A later piece of work reviews them |

## 3. The store

### Layout

```
docs/backlog/
    README.md          generated index: areas, counts by state and priority, late entries
    ids.toml           the next id of each kind, and every id ever closed
    <AREA>.md          one file per area, both kinds
```

`docs/backlog/README.md` and `docs/backlog/README.md` are retired. A migration
command, `backlog import`, reads both into the new store and rewrites every citation.

### An area file

```
# Physics

## Remaining work

| ID | Pri | State | Title | Done when | Blocked by | Source | Opened |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RW-461 | P1 | decision | Choose the matter solver route | The owner has chosen AVBD or XPBD and the other route is deleted | | `docs/design/PHYSICS/README.md` §4 | 2026-10-21 |

## Known issues

| ID | Origin | Symptom | Workaround | Fix | Opened |
| --- | --- | --- | --- | --- | --- |
| KI-31 | own | The cantilever wave runs 1.83 times too fast on AVBD | none | RW-461 | 2026-10-21 |
```

| Column | Rule |
| --- | --- |
| `ID` | `RW-<n>` or `KI-<n>`, from `ids.toml`; never reused |
| `Pri` | `P0`, `P1`, `P2` or `P3` |
| `State` | `decision`, `open`, `blocked` or `unmeasured`, with the meanings of `BACKLOG_FORMAT.md` |
| `Title` | An imperative sentence for work, the symptom as seen for an issue; at most 90 characters |
| `Done when` | One acceptance criterion; at most 160 characters |
| `Blocked by` | Empty unless `blocked`: IDs, `<repository> RW-<n>`, or `external: <reason>` |
| `Source` | Empty, or a path from the repository root with an optional `§<n>`; the path exists |
| `Origin` | `own`, `toolchain`, `dependency` or a sibling repository |
| `Workaround` | Text, or `none` |
| `Fix` | `RW-<n>`, or `none, <reason>`; required when the origin is `own` |
| `Opened` | ISO date the entry was written |

Rows are sorted by ID. A pipe inside a cell is escaped as `\|`. A change to one entry is a one-line
diff.

The fields `Cause`, `Recognise`, `Upstream`, `Owner` and `Fix by` of `BACKLOG_FORMAT.md` leave the
row: `Cause` and `Recognise` go in the source, `Upstream` is written in `Origin` as
`<repository> KI-<n>`, and a quarantined test's owner and date go in the source.

### Identifiers across branches

`ids.toml` holds the next number of each kind. Two branches that each add an entry take the same
number; the merge conflicts in `ids.toml` alone, one line. `backlog renumber` resolves it: it keeps
the entries of the target branch and gives the others the next free numbers, rewriting their
citations. `check` fails a number used twice.

## 4. Priority and order

| Priority | Means | Age limit |
| --- | --- | --- |
| P0 | Data loss, a broken gate, a regression in a release, a security fix after disclosure | 2 days |
| P1 | A defect with no workaround, or work that blocks other work | 14 days |
| P2 | A defect with a workaround, or a missing check that let a defect through | 90 days |
| P3 | An improvement | reviewed every 180 days |

An entry past its limit is late. `backlog next` prints the work an agent should take, in this
order: the owner's pins in their listed order; then entries that are `open` or `unmeasured` and
whose blocks are all closed, by priority, then by age, the oldest first. `decision` entries are
never returned to an agent; `backlog decisions` lists them for the owner.

The pins are a list of at most ten IDs under `[backlog]` in the repository's sushicore
configuration. A pin whose entry is closed fails `check`.

## 5. The backlog commands

```
<cli> backlog list [--area A] [--state S] [--priority P0..P1] [--late] [--json]
<cli> backlog show <ID> [--json]
<cli> backlog next [--count n] [--json]
<cli> backlog decisions [--json]
<cli> backlog add work  --area A --priority P --title T --done-when D [--source S] [--blocked-by IDS]
<cli> backlog add issue --area A --origin O --symptom T --workaround W [--fix F] [--source S]
<cli> backlog promote <KI-n> --priority P --title T --done-when D
<cli> backlog set <ID> <column> <value>
<cli> backlog close <ID> --commit <hash>
<cli> backlog renumber
<cli> backlog import
<cli> backlog check [--report]
```

- `add` prints the new ID and regenerates `docs/backlog/README.md`.
- `promote` opens a work entry from an issue and writes its ID into the issue's `Fix`.
- `close` deletes the row, records the ID as closed in `ids.toml`, and prints the changelog line
  of `CHANGELOG_FORMAT.md` for the caller to write. It refuses an ID that another open entry cites
  in `Blocked by` or `Fix`.
- `check` replaces `tools/documentation/check_backlog.py`: the columns, the values, the ceilings,
  the paths, the IDs, the pins, and that every `Open` design is cited by at least one entry.

## 6. Design control

| Command | Does |
| --- | --- |
| `design list [--json]` | Every topic with its status, its modules and its open phases |
| `design show <TOPIC>` | The topic's document, pages listed |
| `design owner <path>` | The topic that owns the module at that path, or none |
| `design new <TOPIC> --modules <paths> --about <text>` | Writes the topic folder with the five sections and the status line; refuses a module another topic owns and names that topic |
| `design page <TOPIC> <PAGE>` | Adds a page beside the topic's `README.md` |
| `design phase <TOPIC> <Id> <text>` / `design phase-state <TOPIC> <Id> <state>` | Adds a phase or moves its state; the status becomes `Shipped` when every phase is `built` or `withdrawn` |
| `design overlap` | Every module that two topics name, and every pair of topics whose names share a word |
| `design merge <INTO> <FROM>` | Moves `FROM`'s sections into pages of `INTO`, joins the phase tables, deletes `FROM` and rewrites every citation, as `repair_design_citations.py` does |
| `design check [--report]` | Replaces `check_design_format.py` and `check_design_topics.py`, and adds the ownership rule |

The ownership rule: every module of the repository is named by at most one topic, and a topic
names at least one module or the word `none`. A topic that names `none` is a subject with no code,
such as a release; `design new` asks for `--about` to say why. `design check` fails a module named
twice.

Text inside a section stays prose the author writes. The tool writes the frame: the title, the
status line, the metadata lines, the five headings and the phase table.

## 7. What changes in SushiSkills

- `BACKLOG_FORMAT.md` is rewritten for the store of section 3 and the commands of section 5.
- `DESIGN_FORMAT.md` gains the ownership rule and names `design new` as the only way to open a
  topic.
- `SKILL.md` of `documentation` moves the backlog from `docs/backlog/README.md` and
  `docs/backlog/README.md` to `docs/backlog/`, and its red flags send an agent to the
  commands.
- `tools/documentation/check_backlog.py`, `check_design_format.py` and `check_design_topics.py`
  become thin calls into sushicore, so a repository without a module CLI still runs them.
- SushiSkills itself moves its backlog with `backlog import`.

## 8. Answered while building

The owner delegated these to the orchestrator on 2026-10-28.

| Question | Answer |
| --- | --- |
| Is a sibling's work read across repositories by `backlog next`? | No. `next` reads this repository; `check` resolves a sibling's ID when the sibling is checked out beside it, and a block on a sibling never counts as closed |
| Does a merge keep the history of the merged file? | The files move on disk and git finds the rename by content; no `git mv` is run |
| Where do the areas and the pins live? | In `docs/backlog/backlog.toml`, because a repository without a module CLI has no sushicore configuration |
| Where does prose that does not fit a row go? | In `docs/backlog/detail/<ID>.md`, which `show` prints and `close` deletes. `import` writes one for every entry whose fields, prose or lengths do not fit |
| Does a known issue cite its source? | Yes: the issue table carries `Source` before `Opened` |
| Does the generated index list late entries? | No: an index that changed every day would fail `check` on a day nothing changed. `list --late` and `check --report` list them |
| Does `renumber` rewrite the prose that cites a renamed ID? | No: which side of a merge a citation meant cannot be read. It prints each rename for the caller |
| Does `design new` accept a module inside another topic's module? | No: it is a page of that topic. `check` fails a module path named twice, and `owner` gives a path to the deepest module named |
| Do the generated design views move into sushicore? | No: the topic map, the glossary rule, the folder ceiling and the archive rule stay in SushiSkills' `check_design_topics.py` |

Commands added beyond section 5: `backlog move`, `backlog pin`, `backlog unpin`, `backlog area
list`, `backlog area add`, `backlog area merge`, `backlog add work --decision` and `backlog list
--kind`. `design check` takes no `--report`.
