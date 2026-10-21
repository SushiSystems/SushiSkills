# Design document format

Read from the `documentation` skill before writing or reshaping a document under `docs/design/`,
and before closing a work folder whose work made a decision.

A design document and a work folder record different things, and neither holds what the other
does. A reader opens a design document to learn what is being built and why. A reader opens a work
folder to learn what one piece of work did.

| | `docs/design/<TOPIC>.md` | `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/` |
| --- | --- | --- |
| Answers | What are we building, and why this way? | What did this piece of work do and find? |
| Holds | The ruling, its reason, the shape, the phases, the open questions | Commit hashes, measurements, review findings, the working record |
| Never holds | A commit hash, a measurement log, a dated narrative of who built what | A decision that outlives the work |
| Lives | As long as the topic | Until closed, then 90 days |

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
modules (`WEATHER`). A topic has one home, `docs/design/<TOPIC>.md` or `docs/design/<TOPIC>/`. A new
idea about an existing topic is a page and a phase in that topic, never a second document. Two
documents on one subject are merged into one topic.

Under the status line, one field to a line, a design document may carry:

| Field | Holds |
| --- | --- |
| `**About:**` | One sentence saying what the topic is, for the topic map |
| `**Modules:**` | The paths of the modules the topic governs, separated by commas, or `none` |

`check_design_topics.py` reads each path and fails one that is not in the repository. A repository
that sets `K_DESIGN_TOPICS` in `tools/settings.py` also requires the line on every topic and a term
in `docs/reference/GLOSSARY.md` for each topic name.

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

## Size

A design document has at most 400 lines. Above it, the topic becomes `<TOPIC>/`: a `README.md`
with the five sections and the status, and one file per phase for the detail the Design section
would otherwise hold. The phase files carry no status and no fixed sections.

`tools/documentation/check_design_topics.py` enforces the metadata above. `tools/documentation/check_design_format.py` enforces the sections, the status length, the phase
table, the hash rule and the dated-work rule; `check_docs_layout.py` enforces the size. The two
content rules read form only: a hash anywhere in prose, and a line outside the status that sets a
verb such as built, merged or reviewed beside an ISO date. A narrative with no date and no hash
passes them; only a reader catches it.
