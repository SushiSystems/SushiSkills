# Backlog format

Read from the `documentation` skill before writing or closing an entry in
`docs/design/REMAINING_WORK.md` or `docs/reference/KNOWN_ISSUES.md`.

The backlog holds what is to be done. The known issues hold defects that stand in the tree.
Neither holds finished work: the commit that closes an entry deletes it and writes its changelog
line, and what works is in the root README's `## Status`.

## Which repository owns an entry

An entry lives in the repository whose commit closes it. A repository that waits on it cites it
by ID and does not copy its text. A programme that spans repositories lives in the backlog of
the repository that coordinates the others, and its entry lists the entries it waits on.

## IDs

`RW-<n>` in the backlog, `KI-<n>` in the known issues, written `<repository> RW-<n>` from another
repository, the repository being its folder name. Each file opens with a counter line,
`Next id: RW-<n>`, and every ID in the file is below it. An ID is never reused.

## `REMAINING_WORK.md`

```
# Remaining work

Next id: RW-16

## Next

- RW-14 Every speed figure in the design rests on these runs

## Decisions waiting for the owner

### RW-3 Choose whether contributions from outside are accepted
- State: decision
- Done when: the owner has named the contributor agreement, or ruled contributions out

## Kernels

### RW-14 Run the benchmark programs that have not run
- State: unmeasured
- Done when: each program has a recorded run on every device the build supports
- Source: `docs/design/KERNELS.md` §4

### RW-15 Bind a late operand address in the recorder
- State: blocked
- Blocked by: runtime RW-22
- Done when: the recorder accepts an address bound at run time
```

| Part | Rule |
| --- | --- |
| `## Next` | Optional, first. The owner's order: at most ten lines `- RW-<n> <why it comes here>` |
| Decisions | `## Decisions waiting for the owner`, holding every entry with `State: decision` and nothing else |
| Other sections | `## <Area>`, a module or a subject; never a date, a programme of another repository or finished work |
| Heading | `### RW-<n> <what is to be done>`, an imperative sentence |
| `State:` | Required: `decision`, `open`, `blocked` or `unmeasured` |
| `Done when:` | Required: one acceptance criterion |
| `Blocked by:` | Required when `blocked`, absent otherwise: IDs, or `external: <reason>` for a block outside the estate |
| `Source:` | Optional: a design document, with `§<n>` for a section, or a file of a work folder |

`unmeasured` is built work whose acceptance is a run or a measurement rather than a commit. Work
whose claim was withdrawn from a design document is `open`. An open design phase gets one entry
whose `Source:` cites its document; the phase's detail stays there. Every design document whose
status is `Open` is cited by at least one entry.

The order lives in `## Next` and in no other file. An ID there that loses its entry fails the
checker, so the commit that closes an entry also updates the order.

## `KNOWN_ISSUES.md`

```
# Known issues

Next id: KI-8

## Storage

### KI-7 The host faults when it reads a shared buffer while a kernel runs
- Origin: runtime
- Upstream: runtime KI-4
- Where: `modules/io/source/io.cpp`
- Recognise: the process exits with an access fault during a print or a save
- Workaround: finish the queue before a host read
```

| Part | Rule |
| --- | --- |
| Sections | `## <Area>` only |
| Heading | `### KI-<n> <the symptom as seen>` |
| `Origin:` | Required: `own`, `toolchain`, `dependency` or a sibling repository |
| `Upstream:` | Required when the origin is a sibling, absent otherwise: that repository's `KI-<n>` |
| `Where:` | Required when the origin is `own`: at most five paths |
| `Cause:` | Required unless the origin is a sibling, whose entry holds it; `unknown` is a value |
| `Recognise:` | Required: how a reader tells this issue from another |
| `Workaround:` | Required; `none` is a value |
| `Fix:` | Required when the origin is `own`: `RW-<n>`, or `none, <reason>` for a limitation chosen on purpose |
| `Owner:`, `Fix by:` | Required for a quarantined test |
| `Source:` | Optional: the investigation, usually a work folder's `REPORT.md` |

Built work that was never measured or verified is not a defect; it is a backlog entry with
`State: unmeasured`.

## Both files

- A field is a line `- <Name>: <value>`. A value continues on lines indented by two spaces.
  Prose may follow the fields.
- A field-shaped line with any other name is a finding; `- Done:` is one.
- A path in `Where:` or `Source:` is written from the repository root and exists.
- An entry is at most 25 lines, heading included. A longer investigation goes in its `Source:`.
- An ID another entry cites is closed only once the citing entry is updated.

`tools/documentation/check_backlog.py` enforces every rule above that a tool can see. Whether an
entry is still true is the fact check in `project-tools`.
