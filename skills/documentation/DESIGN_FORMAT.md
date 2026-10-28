# Design document format

Read from the `documentation` skill before writing or reshaping a document under `docs/design/`,
and before closing a work folder whose work made a decision.

A design document and a work folder record different things, and neither holds what the other
does. A reader opens a design document to learn what is being built and why. A reader opens a work
folder to learn what one piece of work did.

| | `docs/design/<TOPIC>/README.md` | `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/` |
| --- | --- | --- |
| Answers | What are we building, and why this way? | What did this piece of work do and find? |
| Holds | The ruling, its reason, the shape, the phases, the open questions | Commit hashes, measurements, review findings, the working record |
| Never holds | A commit hash, a measurement log, a dated narrative of who built what | A decision that outlives the work |
| Lives | As long as the topic | Until closed, then deleted |

When a piece of work makes a decision, its closing commit writes that decision into the design
document and leaves the evidence in `REPORT.md`. The document links the work folder; it does not
copy it.

## The document

```
# <Title>

**Status:** <one of the four forms of AGENT_WORK.md>

## Problem
## Decision
## Design
## Phases
## Open questions
```

- Exactly these five `##` sections, in this order. A section with nothing to say says `None.`
- Headings below `##` are free. A `##` section of any other name is a finding: its content belongs
  under one of the five, or in a work folder.
- **Problem** is what is wrong or missing, as a cold reader meets it.
- **Decision** is the ruling and the reason for it, in a few lines. The owner's words go here.
- **Design** is the shape: interfaces, data, flows, the alternatives set aside and why.
- **Open questions** are what is undecided. An answered question moves into Decision or Design.

## The status line

One line, at most 160 characters. It says where the document stands, never how it got there. A
phase is named by its id in the table below, not described in the status.

## The phase table

`## Phases` holds one table with the columns `Id`, `Phase` and `State`.

| State | Meaning |
| --- | --- |
| `planned` | Not started |
| `building` | Work is under way |
| `built` | Merged and working as designed |
| `withdrawn` | Given up by the owner |

When every phase is `built` or `withdrawn`, the document's status becomes `Shipped`.

## The topic and its metadata

The unit of design is the topic: a name that is a module (`AUDIO`, `ECS`) or a subject that spans
modules (`WEATHER`). A topic has one home, the folder `docs/design/<TOPIC>/`, whose `README.md` is
the design document. Nothing but `README.md` sits loose in `docs/design/`.

Topics have two levels: the topic, and the pages and phases under it. A new idea about an
existing topic is a page and a phase in that topic, never a second topic. Clouds are a page of
`ATMOSPHERE`; a matter solver is a page of `MATTER`.

Under the status line, one field to a line, a design document carries:

| Field | Holds |
| --- | --- |
| `**About:**` | One sentence saying what the topic is, for the topic map |
| `**Modules:**` | Required: the paths of the modules the topic owns, separated by commas, or `none` |

**A module belongs to one topic.** A module path is named on the `**Modules:**` line of at most
one topic, and a path inside a module belongs to the topic that names the deepest module holding
it; `design owner <path>` says which. A topic of no module, such as a release, writes `none` and
carries `**About:**` to say why.

The `design` commands of sushicore write the frame: the title, the status line, the metadata
lines, the five headings and the phase table. `design new <TOPIC> --modules <paths> --about
<text>` is the only way to open a topic; it refuses a module another topic owns, or one inside or
around it, and names that topic. `design page` and `design phase` grow a topic, and `design
phase-state` moves a phase and ships the topic when the last one is built. Two topics on one
subject are found with `design overlap` and joined with `design merge <INTO> <FROM>`, which makes
`FROM` a page of `INTO`, joins the phases and the modules, and rewrites every citation. The prose
inside the sections is the author's. The commands are in sushicore's `docs/reference/DESIGN.md`.

A repository that sets `K_DESIGN_TOPICS` in `tools/settings.py` also requires a term in
`docs/reference/GLOSSARY.md` for each topic name, and the topic map.

Three views are generated from this metadata and the phase tables, each between a begin and an end
marker (`<!-- topics:begin -->` and `<!-- topics:end -->`, and the same for `designs` and `work`):
the topic map in `docs/design/README.md`, a list of the topics that govern a module at the end of
its README, and the open work that names a topic's phases, at the end of its `Phases` section.
Nobody edits text between markers. `tools/documentation/generate_design_views.py` writes the views,
`--init` adds the markers, and `check_design_topics.py` fails a block that is out of date.

Work reaches a topic through its phase ids; see `AGENT_WORK.md`.

When a topic becomes a folder, or a folder a file, `tools/documentation/repair_design_citations.py
--apply` rewrites every citation of it in the manual and the source and reports the ones it cannot
place. A repair is never done by hand.

## A topic under revision

When an audit grades a topic insufficient and the owner keeps it to be revised, its folder moves
whole to `docs/design/_REVISION/<TOPIC>/` and its text stays as it was; the audit's report says
what is wrong with it. The topic map lists it with the state `Revision`. Nothing new is written
into it and no work carries out its phases. It leaves in one of two ways: rewritten into
`docs/design/<TOPIC>/` in the format above, or deleted. After either move, and after the move in,
`repair_design_citations.py --apply` relinks it, reading each link inside it from its former place.

## Size

A design document, the `README.md` of a topic folder, has at most 400 lines. Above it, the detail
moves into one page per phase beside it, where the Design section would otherwise hold it. The pages carry
no status and no fixed sections. `fold_design_topics.py --apply` gives a loose document its folder.

`tools/documentation/check_design_topics.py` enforces the metadata, the ownership rule and the
generated views; `tools/documentation/check_design_format.py` enforces the sections, the status
length, the phase table, the hash rule and the dated-work rule; both run sushicore's `design
check`. `check_docs_layout.py` enforces the size. The two
content rules read form only: a hash anywhere in prose, and a line outside the status that sets a
verb such as built, merged or reviewed beside an ISO date. A narrative with no date and no hash
passes them; only a reader catches it.
