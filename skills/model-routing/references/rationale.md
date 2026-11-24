# Model routing: rationale and detail

Read this when a row of the matrix or a step of the escalation order looks wrong for a task, when a
migration to another model generation starts, or when deciding whether a `sonnet` row stays.
The rules themselves are in `../SKILL.md`.

## Why routing is a rule

Every agent in a session costs money by the token, and the orchestrator costs the most,
because everything a subagent reports is added to its context and is read again on every turn.
The skill makes the choice once, by rule, and corrects it with measurements instead of guesses.

## The stack

Effort levels are calibrated per generation, so a migration re-measures the matrix on this
repository's own tasks before a row moves; the table is not carried over.

Whether the API accepts the effort parameter for Haiku 5.5 is not verified here; the per-model
effort in Claude Code's settings is the place it is read from, and one real dispatch confirms it
before the matrix relies on it.

## The session

Changing the model mid-session resets the prompt cache, so a plan session and an implementation
session are separate sessions when they need different models; with the session table they do not.

## Why each matrix row

| Phase | Work | Why this row |
| --- | --- | --- |
| Plan | Exploring the tree | Reading, no judgment; the area must fit a 200K context |
| Plan | Brainstorming, `SPEC.md`, `PLAN.md` | Design judgment; never dispatched |
| Implement | Spec-complete, one or two files | The plan states the change in sentences |
| Implement | Spec-complete, many files | The same work over a wider area |
| Implement | One module, a local choice open | Judgment over a small area |
| Implement | The same, over several files | Judgment over a wider area |
| Implement | Integration across modules, debugging | Needs judgment, not architecture |
| Review | Spec compliance, checker output | A comparison |
| Review | SOLID shape, public surface, humanizer register | The three items a reviewer names |
| Architecture | Public interface, data ownership, numeric kernel, stream merge | The exception, within the owner's limits |

## Haiku, Sonnet and Opus

`haiku` at `medium` or `high` does work the plan has already decided: it follows sentences,
and it is good at that. `opus` at `low` decides across modules. Between them is work in which the
plan leaves one local choice open, inside one module: which of two patterns, how to split a file,
why a test fails. `haiku` there guesses or stops; `opus` there costs more for judgment the area does
not need. That work is `sonnet`'s.

The `sonnet` rows are not measured yet. The dispatch lines decide whether they stay.

## The escalation order

The cheapest step runs first because the failure signal is cheap too: the checkers and the tests
say whether that step's result passed. Example: a task that failed at step 2 (`haiku` high) is
re-run at step 3 (`sonnet` medium); the orchestrator may decide on step 4 instead.

## Inline or subagent

A subagent pays a fixed opening cost: `claude/CLAUDE.md`, the skills its dispatch names, the
dispatch block, and every file it reads, none of it from the cache. In return the orchestrator's
context stays small.

## Token use

`low` means fewer and more consolidated tool calls and less preamble; for mechanical work it is
the effort the matrix row names; the dispatch lines measure whether it held.

## Recording

The dispatch line keeps the token `rung` before the step number, because
`tools/routing/summarize_dispatches.py` parses that token.

After five pieces of work the dispatch lines show which rows are wrong: a stronger model than
the task needs costs more; a weaker one than it needs fails and is re-run.
