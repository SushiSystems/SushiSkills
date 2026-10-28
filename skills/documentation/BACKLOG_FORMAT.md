# Backlog format

Read from the `documentation` skill before reading, writing or closing an entry of the backlog.

The backlog holds what is to be done: the remaining work, and the known issues, conditions a
reader can meet and act on, such as a defect that has a workaround, a limitation chosen on
purpose, or a fault of the toolchain, a dependency or a sibling. Neither holds finished work: the
commit that closes an entry deletes it and writes its changelog line, and what works is in the
root README's `## Status`.

## The store

```
docs/backlog/
    README.md          generated: each area counted by state and priority, and the pins
    backlog.toml       the areas and the owner's pins
    ids.toml           the next number of each kind and every number ever closed
    <AREA>.md          one area, holding a table of remaining work and a table of known issues
    detail/<ID>.md     the explanation of an entry that does not fit its row
```

Every file here is written by the `backlog` commands of sushicore: `<cli> backlog ...` in a
repository with a module CLI, `python -m sushicore.backlog ...` in one without. Nobody edits a
row by hand; `backlog check` fails a file out of the shape the tool writes. A detail file is
prose the author writes, and `backlog close` deletes it with its entry.

The columns, their values, the ceilings and the commands are in sushicore's
`docs/reference/BACKLOG.md`. In short:

| Kind | Columns |
| --- | --- |
| Remaining work, `RW-<n>` | `ID`, `Pri`, `State`, `Title`, `Done when`, `Blocked by`, `Source`, `Opened` |
| Known issue, `KI-<n>` | `ID`, `Origin`, `Symptom`, `Workaround`, `Fix`, `Source`, `Opened` |

## Which repository owns an entry

An entry lives in the repository whose commit closes it. A repository that waits on it cites it
by ID and does not copy its text, written `<repository> RW-<n>`, the repository being its folder
name. A programme that spans repositories lives in the backlog of the repository that
coordinates the others, and its entry lists the entries it waits on in `Blocked by`.

## Areas

An area is a module or a subject of the repository, named in upper case words joined by `_` and
listed in `backlog.toml`; `backlog area add` adds one. An area is never a date, a programme of
another repository, a design topic's phase or finished work. Areas are few: a subject with two
entries belongs in the area of the module it changes, and `backlog area merge` joins two.

## States

| State | Means |
| --- | --- |
| `open` | Work to be done |
| `blocked` | Waits on the entries or the external reason in `Blocked by` |
| `unmeasured` | Built work whose acceptance is a run or a measurement rather than a commit |
| `decision` | Waits on the owner's ruling; never given to an agent |

Work whose claim was withdrawn from a design document is `open`. Built work that was never
measured or verified is not a defect; it is `unmeasured` work.

## Priority and order

`P0` is data loss, a broken gate, a regression in a release or a security fix after disclosure,
late after 2 days. `P1` is a defect with no workaround or work that blocks other work, late after
14. `P2` is a defect with a workaround or a missing check that let a defect through, late after
90. `P3` is an improvement, reviewed after 180.

The order is computed, never kept by hand. `backlog next` gives an agent its work: the owner's
pins first, then the ready entries by priority and age. The owner pins at most ten entries with
`backlog pin`; `backlog decisions` lists what waits on the owner.

## Remaining work or a known issue

A known issue of origin `own` carries a workaround, or a `Fix` of the form `none, <reason>` for a
limitation chosen on purpose. A defect with a scheduled fix and no workaround is work: it lives in
the remaining work table alone, its symptom and cause in its detail. Once a workaround exists it
may become an issue with `Fix: RW-<n>`, and `backlog promote` opens the work of an issue. An
origin that is not `own` is never the repository's to close, so it is not remaining work whatever
its workaround.

An open design phase gets one work entry whose `Source` cites its topic; the phase's detail stays
there. Every design topic whose status is `Open` is cited by at least one entry.

## A quarantined test

A test taken out of the gating stages has a known issue whose detail file names the test, its
owner and the date it is fixed by. The issue's `Fix` names the work that brings it back.

## An agent and the backlog

- Read the work to take with `backlog next --json`, never by reading the area files.
- Add what the work found with `backlog add`, and close what it finished with `backlog close`,
  writing the changelog line it prints.
- A longer explanation goes in the entry's detail file or in the work folder its `Source` cites.
- Two branches that took one ID are resolved with `backlog renumber` after the merge.

`tools/documentation/check_backlog.py` runs `backlog check`, so a repository's checkers enforce
every rule above that a tool can see. Whether an entry is still true is the fact check in
`project-tools`.
