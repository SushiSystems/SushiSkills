---
name: model-routing
description: Use when choosing the model and the effort for a session or a subagent dispatch, when deciding whether a task runs inline or in a subagent, when a dispatched task fails and must be re-run, or when recording what a dispatch cost, in a repository.
---

# Model Routing

Which model and effort each kind of work runs on, within the owner's limits in
`claude/CLAUDE.md`, "Delegation". Read `references/rationale.md` when a row looks wrong or a
migration starts, and `references/matrix-tables.md` for the tables and red flags.

## The stack

The rows hold only on Claude 5.5 models: `opus`, `sonnet`, `haiku`. Another agent, vendor or
Claude generation does not use them; a migration re-measures the matrix before a row moves. The
dispatch sets the effort on every model.

## The session

The model is chosen at the start, never changed mid-session. The orchestrator is `opus`:
`medium` when the session plans or runs a plan; `low` otherwise.

## The dispatch matrix

| Work | Model, effort |
| --- | --- |
| Explore: files, patterns, call sites | `haiku` medium |
| Brainstorm, `SPEC.md`, `PLAN.md` | orchestrator inline, medium |
| Spec-complete, one or two files | `haiku` medium |
| Spec-complete, many files or much reading | `haiku` high |
| One module, a local choice open (pattern, split, bug's cause) | `sonnet` low; several files or much reading: medium |
| Integration across modules, pattern choice, debugging | `opus` low |
| Review: spec compliance, checker output, files against the set | `haiku` high |
| Review: SOLID shape, public surface, humanizer register | `opus` low |
| Architecture: public interface, data ownership, numeric kernel, merge across streams | `opus` high |

The plan decides: it states the change, `haiku`; the goal with the how inside one module,
`sonnet`; the how crossing a module, `opus`. A task matching no row is split until its parts do;
one matching two runs on the more capable.

## The escalation ladder

A failed task is re-run by a fresh subagent one rung up, at most two rungs on the orchestrator's
authority: 1 `haiku` medium, 2 `haiku` high, 3 `sonnet` medium, 4 `opus` low, 5 `opus` high
(decided by the limits in `claude/CLAUDE.md`). A task without a failure signal starts on its
matrix row.

## Inline or subagent

- Three to five tool calls, or a change made from what is already read: inline.
- Ten files to read and one to write, or reading that would outlive its use in the
  orchestrator's context: subagent.

## Token hygiene

- A reply is short: done, not done, files changed, verification output (`REPORT.md`:
  `multi-agent-work`).
- A dispatch names only the skills the task needs.
- A `haiku` area fits its context; a sweep over a large tree goes to several `haiku` or `opus` low.

## Recording

Every `REPORT.md` carries one line per dispatch:

```
dispatch: <task> — <model> <effort>, <N> turns, <passed|failed, rung R>
```

`python tools/routing/summarize_dispatches.py .` sums them. The matrix changes only from those
lines, in this skill, with a changelog line naming the measurement.
