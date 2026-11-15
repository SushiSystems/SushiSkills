---
name: model-routing
description: Use when choosing the model and the effort for a session or a subagent dispatch, when deciding whether a task runs inline or in a subagent, when a dispatched task fails and must be re-run, or when recording what a dispatch cost, in a repository.
---

# Model Routing

This skill says which model and which effort each kind of work runs on. The owner's limits live
in `claude/CLAUDE.md`, section "Delegation": which models are used at all, the effort cap, and
when `high` needs approval. This skill routes within those limits.

Why each row is where it is, and the detail behind the rules: `references/rationale.md`. Read it
when a row looks wrong for a task, or when a migration starts.

## The stack

The tables hold only when the session runs on a Claude 5.5 model: Opus 5.5 as `opus`, Sonnet 5.5
as `sonnet` and Haiku 5.5 as `haiku`. Another agent, another vendor's model or another Claude
generation does not use them; a migration re-measures the matrix before a row moves.

The dispatch sets the effort on every model.

## The session

| Seat | Model | Effort |
| --- | --- | --- |
| Orchestrator of a session that plans, or runs a plan | `opus` | `medium` |
| Orchestrator of a session without a plan: a question, a review, a small edit, a commit | `opus` | `low` |

The session model is chosen at the start, not changed mid-session.

## The dispatch matrix

| Phase | Work | Model | Effort |
| --- | --- | --- | --- |
| Plan | Exploring the tree: finding files, patterns, call sites | `haiku` | `medium` |
| Plan | Brainstorming, `SPEC.md`, `PLAN.md` | orchestrator, inline | `medium` |
| Implement | Spec-complete, files named, one or two files | `haiku` | `medium` |
| Implement | Spec-complete, many files or much reading | `haiku` | `high` |
| Implement | Inside one module, the plan leaves a local choice open: a pattern, a split, a bug's cause | `sonnet` | `low` |
| Implement | The same, over several files or with much reading | `sonnet` | `medium` |
| Implement | Integration across modules, pattern choice, debugging | `opus` | `low` |
| Review | Spec compliance, checker output, changed files against the assigned set | `haiku` | `high` |
| Review | SOLID shape, public surface, humanizer register | `opus` | `low` |
| Architecture | A public interface, data ownership, a numeric kernel, a merge across streams | `opus` | `high` |

The test is the plan: if it states the change, `haiku`; if it states the goal and leaves the how
inside one module, `sonnet`; if the how crosses a module, `opus`.

A task that does not match a row is split until its parts do. A task matching two rows runs on
the more capable one.

## The escalation ladder

A failed task is re-run by a fresh subagent one rung up. It climbs at most two rungs on the
orchestrator's own authority.

| Rung | Model | Effort | Who decides |
| --- | --- | --- | --- |
| 1 | `haiku` | `medium` | orchestrator |
| 2 | `haiku` | `high` | orchestrator |
| 3 | `sonnet` | `medium` | orchestrator |
| 4 | `opus` | `low` | orchestrator |
| 5 | `opus` | `high` | the limits in `claude/CLAUDE.md` |

A task without a failure signal starts on the row the matrix gives it, not on rung 1.

## Inline or subagent

- Three to five tool calls, or a change the orchestrator can make from what it already read: inline.
- Ten files to read and one to write, or any task whose reading would outlive its usefulness in the orchestrator's context: subagent.

## Token hygiene

- A subagent's reply is short: what was done, what was not, the files changed, the verification
  output. Who writes `REPORT.md` is in `multi-agent-work`.
- A dispatch names only the skills the task needs. Each loaded skill is uncached input.
- A `haiku` dispatch is given an area that fits its context. A sweep over a large tree goes to
  several `haiku` dispatches or to `opus` at `low`.

## Recording

Every `REPORT.md` carries one line per dispatch:

```
dispatch: <task> — <model> <effort>, <N> turns, <passed|failed, rung R>
```

`python tools/routing/summarize_dispatches.py .` sums them per model and effort. The matrix is
changed from those lines, in this skill, with the changelog line naming the measurement.

## Red flags

- "This one is small, I will leave the model to inherit." → the matrix, and the `model` field set.
- "Haiku failed, I will go straight to Opus high." → the ladder, one rung.
- "The orchestrator can read these twelve files itself." → a `haiku` explorer.
- "I will keep the old table after the migration." → re-measure first.
