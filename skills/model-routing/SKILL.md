---
name: model-routing
description: Use when choosing the model and the effort for a session or a subagent dispatch, when deciding whether a task runs inline or in a subagent, when a dispatched task fails and must be re-run, or when recording what a dispatch cost, in a Sushi Systems repository.
---

# Model Routing

Every seat in a session costs money by the token, and the orchestrator's seat costs the most,
because everything a subagent reports lands in its context and is read again on every turn.
This skill says which model and which effort each kind of work runs on, so that the choice is
made once, by rule, and corrected with measurements instead of guesses.

The owner's limits live in `claude/CLAUDE.md`, section "Delegation": which models are used at
all, the effort cap, and when `high` needs approval. This skill routes within those limits.

## The stack

The tables below hold only when the session runs on a Claude 5.5 model: Opus 5.5 as `opus`,
with Haiku 5.5 in the `haiku` seat. Another agent, another vendor's model or
another Claude generation does not use this table. Effort levels are calibrated per generation,
so a migration re-measures the matrix on this repository's own tasks before a row moves; the
table is not carried over.

The dispatch sets the effort on every model. Whether the API accepts the effort parameter for
Haiku 5.5 is not verified here; the per-model effort in Claude Code's settings is the place it is
read from, and one real dispatch confirms it before the matrix relies on it.

## The session

| Seat | Model | Effort |
| --- | --- | --- |
| Orchestrator: plans, dispatches, accepts reports, integrates, commits | `opus` | `medium` |

The session model is chosen at the start. Changing it mid-session resets the prompt cache, so a
plan session and an implementation session are separate sessions when they need different
seats; with this table they do not.

## The dispatch matrix

| Phase | Work | Model | Effort | Why this row |
| --- | --- | --- | --- | --- |
| Plan | Exploring the tree: finding files, patterns, call sites | `haiku` | `medium` | Reading, no judgment; the area must fit a 200K context |
| Plan | Brainstorming, `SPEC.md`, `PLAN.md` | orchestrator, inline | `medium` | Design judgment; never dispatched |
| Implement | Spec-complete, files named, one or two files | `haiku` | `medium` | The plan states the change in sentences |
| Implement | Spec-complete, many files or much reading | `haiku` | `high` | The same work over a wider area |
| Implement | Integration across modules, pattern choice, debugging | `opus` | `low` | Needs judgment, not architecture |
| Review | Spec compliance, checker output, changed files against the assigned set | `haiku` | `high` | A comparison |
| Review | SOLID shape, public surface, humanizer register | `opus` | `low` | The three items a reviewer names |
| Architecture | A public interface, data ownership, a numeric kernel, a merge across streams | `opus` | `high` | The exception; owner approval first |

A task that does not match a row is split until its parts do. A task matching two rows runs on
the more capable one.

## The escalation ladder

A failed task is re-run by a fresh subagent one rung up. It climbs at most two rungs on the
orchestrator's own authority.

| Rung | Model | Effort | Who decides |
| --- | --- | --- | --- |
| 1 | `haiku` | `medium` | orchestrator |
| 2 | `haiku` | `high` | orchestrator |
| 3 | `opus` | `low` | orchestrator |
| 4 | `opus` | `high` | owner |

The cheap run comes first because the failure signal is cheap too: the checkers and the tests
say whether the rung held. A task without a failure signal starts on the row the matrix gives
it, not on rung 1.

## Inline or subagent

A subagent pays a fixed opening cost: `claude/CLAUDE.md`, the skills its dispatch names, the
dispatch block, and every file it reads, none of it from the cache. In return the orchestrator's
context stays clean. The rule:

- Three to five tool calls, or a change the orchestrator can make from what it already read: inline.
- Ten files to read and one to write, or any task whose reading would outlive its usefulness in the orchestrator's context: subagent.

## Token hygiene

- A subagent's reply is short: what was done, what was not, the files changed, the verification
  output. Everything else goes to `REPORT.md` in the work folder, which the orchestrator reads
  once.
- A dispatch names only the skills the task needs. Each loaded skill is uncached input.
- `low` means fewer and more consolidated tool calls and less preamble. On `opus` it is the
  default for every dispatch, not a compromise.
- A `haiku` dispatch is given an area that fits its context. A sweep over a large tree goes to
  several `haiku` dispatches or to `opus` at `low`.

## Recording

Every `REPORT.md` carries one line per dispatch:

```
dispatch: <task> — <model> <effort>, <N> turns, <passed|failed, rung R>
```

After a handful of pieces of work these lines say which rows are over- or under-provisioned.
The matrix is changed from those lines, in this skill, with the changelog line naming the
measurement.

## Red flags

- "This one is small, I will leave the model to inherit." → the matrix, and the `model` field set.
- "Haiku failed, I will go straight to Opus high." → the ladder, one rung.
- "The orchestrator can read these twelve files itself." → a `haiku` explorer.
- "I will keep the old table after the migration." → re-measure first.
