# Model routing: phases and excuses

Read this when a row of the dispatch matrix needs its phase, or when you catch yourself using one
of the excuses below. The
rules themselves are in `../SKILL.md`.

## Phases

| Phase | Rows of the matrix |
| --- | --- |
| Plan | Explore: files, patterns, call sites; `SPEC.md` and `PLAN.md` |
| Implement | The two spec-complete rows and the one-module row; cross-module integration. A local choice open is a pattern, a split or a bug's cause |
| Review | Both review rows |
| Architecture | The architecture row |

## Excuses

Each excuse is followed by the rule that answers it.

- "This one is small, I will leave the model to inherit." → the matrix, and the `model` field set.
- "Haiku failed, I will go straight to Opus high." → the escalation order, one step.
- "The orchestrator can read these twelve files itself." → a `haiku` explorer.
- "I will keep the old table after the migration." → re-measure first.
