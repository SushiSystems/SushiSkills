---
name: model-routing
description: Use when choosing the model and the effort for a session or a subagent dispatch, when deciding whether a task runs inline or in a subagent, when a dispatched task fails and must be re-run, or when recording what a dispatch cost, in a repository.
---

# Model Routing

Model and effort per work, within the limits in `claude/CLAUDE.md`, "Delegation".
Detail: `references/`.

## Stack and session

The rows hold only on Claude 5.5 models (`opus`, `sonnet`, `haiku`); others re-measure first.
Every dispatch sets effort. The session model is fixed at the start: the orchestrator is `opus`,
`medium` when it plans or runs a plan, `low` otherwise.

## The dispatch matrix

| Work | Model, effort |
| --- | --- |
| Explore: files, patterns, calls | `haiku` medium |
| `SPEC.md`, `PLAN.md` | orchestrator, medium |
| Spec-complete, one or two files | `haiku` medium |
| Spec-complete, many files | `haiku` high |
| One module, a local choice open (pattern, split, cause) | `sonnet` low; several files: medium |
| Cross-module integration, pattern choice, debugging | `opus` low |
| Review: spec compliance, checker output | `haiku` high |
| Review: SOLID shape, public surface, humanizer register | `opus` low |
| Architecture: public interface, data ownership, numeric kernel, merge | `opus` high |

The plan decides: it states the change, `haiku`; the how inside one module is open, `sonnet`;
the how crosses a module, `opus`. A task matching no row is split; one matching two takes the
more capable.

## The escalation order

A failed task is re-run by a fresh subagent the next step, two at most if the orchestrator
says so: 1 `haiku` medium, 2 `haiku` high, 3 `sonnet` medium, 4 `opus` low, 5 `opus` high
(owner's limits). A task not yet failed starts on its row.

## Inline or subagent

Three to five tool calls, or a change from what is read: inline. Ten files to read and one to
write, or reading that would fill the orchestrator's context: subagent.

## Token use

A reply is short: done, not done, files changed, verification output. A dispatch names only
needed skills. A `haiku` area fits its context; a large tree goes to several `haiku` or `opus` low.

## Recording

Every `REPORT.md` carries one line per dispatch:

```
dispatch: <task> — <model> <effort>, <N> turns, <passed|failed, rung R>
```

`R`: step number. `python -m <library>.tools.routing.summarize_dispatches .` sums them. The matrix changes only from those
lines, with a changelog line naming it.
