# Model routing: tables and red flags

Read this when the original table form of the session seats, the dispatch matrix or the ladder is
needed, or when a red flag applies. The rules themselves are in `../SKILL.md`.

## The session

| Seat | Model | Effort |
| --- | --- | --- |
| Orchestrator of a session that plans, or runs a plan | `opus` | `medium` |
| Orchestrator of a session without a plan: a question, a review, a small edit, a commit | `opus` | `low` |

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

## The escalation ladder

| Rung | Model | Effort | Who decides |
| --- | --- | --- | --- |
| 1 | `haiku` | `medium` | orchestrator |
| 2 | `haiku` | `high` | orchestrator |
| 3 | `sonnet` | `medium` | orchestrator |
| 4 | `opus` | `low` | orchestrator |
| 5 | `opus` | `high` | the limits in `claude/CLAUDE.md` |

## Red flags

- "This one is small, I will leave the model to inherit." → the matrix, and the `model` field set.
- "Haiku failed, I will go straight to Opus high." → the ladder, one rung.
- "The orchestrator can read these twelve files itself." → a `haiku` explorer.
- "I will keep the old table after the migration." → re-measure first.
