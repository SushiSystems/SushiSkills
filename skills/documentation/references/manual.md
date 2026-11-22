# Keeping the manual true: detail

Read this when a documentation checker reports a finding you do not understand, when a page passes
its ceiling, when writing a source example, a `Describes:` line or a fact marker, or when tempted
to leave a page as it is.

## What the manual is

The manual is the root `README.md`, every document under `docs/` outside `agent/`, `archive/`
and the changelog, and every `.md` page under the source folders: each `README.md`, and each page
named after the file it describes (`test_tensor.md` beside `test_tensor.cpp`), which its folder's
README links.

## What the truth checker sees

`tools/documentation/check_docs_truth.py` sees what a tool can: every name and path a page
writes in code exists in the source, and every example comes from a file. A sentence that
describes behaviour the code has lost is caught only by a reader. A design document states
intent, so its names are not looked up.

A name the source cannot hold, such as a third-party type or a target the build generates, goes in
`docs/.docs_truth_allow`: one regular expression per line, ` # reason` after it. An entry without
a reason, or one that excuses nothing, is a finding.

## Editing is replacing

A page does not say `previously`, `no longer`, `used to`, `was renamed`, `formerly`, `as of v`,
`new in v`, `up to v` or `deprecated since`. What changed is in the changelog; a defect that still
bites is a known issue in the backlog.

## Above the ceiling

| Page | Above its ceiling |
| --- | --- |
| Root `README.md` | Move the detail into the manual and link it |
| Manual page | Split by subject into pages the index links |
| Module README | Move each part to the README of the folder it describes, or to a page beside the file it describes |
| Design document | Pages beside its `README.md`, one per phase |

## Duplicated passages, examples, dashes

- A repeated paragraph of 300 characters or more is the one that must become a sentence and a
  link.
- A source example in a manual page is taken from a file the build compiles, and a line within
  three lines after it cites that file: ``Source: `applications/examples/quickstart.cpp` ``.
  Every line of the example is a line of that file; `// ...` marks an omission.
- An example no file can back carries `Source: not compiled`. `--report` counts those; drive the
  count down.
- No em dash in the prose of a page; `humanizer` gives the repair. The changelog entry and the
  design status line keep theirs.

## Pages follow what they describe

- A path in a `Describes:` line is a file or a folder, and a folder covers everything below it.
- A README also describes the entries of its own folder. A commit that adds an entry to that
  folder, or removes one whole, needs the README in the same commit. Editing a file inside an entry
  does not.
- `Docs: none (<reason>)` waives every page of the commit. A reason of no words is a refusal.
- `docs/agent/`, `docs/design/`, `docs/backlog/` and `docs/archive/` are not followed; they are
  written by their own commands or end with the work.
- `tools/documentation/check_docs_follow.py` checks the commits after `K_DOCS_FOLLOW_SINCE` in
  `tools/settings.py`, and the `commit-msg` hook of `commits` refuses the commit before it exists.

## Facts with one home

- An id is lower-case words joined by `-`, and unique in the repository. The id is the fact's
  identity; a line number or a heading is not.
- Nobody types a quote's text: `python tools/documentation/facts_cli.py apply` rewrites it from the
  home, and the checker fails a quote that differs by one character.
- A paraphrase's `<!-- follows: ID -->` line is indented when it sits in a list item.
- `facts_cli.py cited-by ID` lists every quote and follow of a fact, `where ID` names its home and
  `list` shows them all. The map is computed from the markers on every run and is never stored.
- `tools/documentation/check_docs_facts.py` checks the markers, the ids and the quotes.

## Red flags

- "I will write a quick note in a new file so the next agent sees it." → the work folder.
- "This review deserves its own file." → replace `REPORT.md`.
- "I will read the backlog or the design map to see what is left or designed." → ask the
  repository's commands, as `backlog` and `design` say.
- "I will update the changelog at the end of the week." → it is part of the commit.
- "`docs/` is outside my write list, so I reported it." → `AGENT_WORK.md`, on a reported page.
- "The manual is a later stage of the plan." → the page is part of the change that made it false.
- "The module README is updated, that is enough." → `git grep` the name over `README.md` and
  `docs/`; every hit belongs to this change.
- "I will add a note that this changed." → replace the text; the changelog holds the change.
- "I will keep the old paragraph in case." → delete it; git keeps it.
- "The page is long because the subject is large." → a subject that large is more than one page.
- "I will copy the sentence into the other page." → give it a home and quote it, or link it.
- "The page still reads true, so I leave it." → add `Docs: <page> unchanged (<reason>)`; the
  reason is the proof.

## Detail beyond the skill page

- Documentation is split by what it records, and each kind has one home: a fact in two places is
  a fact that will disagree with itself.
- Placement, item 5: version history keeps a page about finished work.
- Which format to read: opening or extending a design document, or opening or closing a work
  folder under `docs/agent/`, is `AGENT_WORK.md`; writing or reshaping a design document
  (sections, status line, phase table) is `DESIGN_FORMAT.md`; a changelog entry or moving a release
  section is `CHANGELOG_FORMAT.md`; reading, writing or closing a backlog entry in `docs/backlog/`
  is `BACKLOG_FORMAT.md`. What is left or next, what a module is meant to be or who owns it, a
  defect found, work finished, a decision made: the `backlog` and `design` skills.
- Architecture and guide pages are never a stage at the end of a plan.
- A page is written for the reader who arrives cold: what the thing is, how to use it, then the
  detail.
- A fact earns a home when two pages must say the same thing.
