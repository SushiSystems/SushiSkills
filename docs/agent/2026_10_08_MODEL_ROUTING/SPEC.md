# Model routing

**Status:** Shipped — implemented on 2026-10-08; see `REPORT.md`.

The global instructions set one model for every dispatch, `opus`, and vary only the effort.
They name no phase, and the orchestrator itself ran on `fable`, the most expensive seat in the
session, because nothing said otherwise. This work gives model and effort choice its own skill,
`model-routing`, and reduces the "Delegation" section of `claude/CLAUDE.md` to the owner's
limits plus a citation.

## Owner decisions this spec rests on

All taken on 2026-10-08.

| # | Decision |
| --- | --- |
| D1 | `fable` is not used anywhere, the orchestrator included. |
| D2 | The orchestrator session runs on `opus` at `medium`. |
| D3 | Every `opus` dispatch runs at `low`. |
| D4 | `high` on `opus` is the exception, about five dispatches in a hundred, and only with the owner's approval. |
| D5 | `haiku` takes the spec-complete and mechanical work, at `medium` or `high` by task. `sonnet` is not used. |
| D6 | The table holds only for Claude 5.5 models: Opus 5.5, with Haiku 5.5 in the Haiku seat. Another agent or generation does not use it; a migration re-measures before the table moves. |

The engineer decided where the rule lives: a new skill, so that the limits (owner) and the
routing (engineer, tuned with data) sit in different files.

## Design

### 1. The `model-routing` skill

Holds, for Claude 5.5 models: the session seat, the dispatch matrix by phase and kind of work, the
escalation ladder for a failed task, the inline-or-subagent rule, the token hygiene rules, and
the line every `REPORT.md` records per dispatch so the matrix can be tuned with measurements.

### 2. `claude/CLAUDE.md`, section "Delegation"

The model paragraph becomes the owner's limits (D1 to D6) and a citation of the skill. The
dispatch block, the report evidence rule and the effort cap stay as they are.

### 3. Citations

`multi-agent-work` "Choosing a model" points at the skill. `skills/sushiskills/SKILL.md` and
`skills/README.md` gain one row each.

## Acceptance

- The skill exists, its front matter names it, and its description starts with "Use when".
- `claude/CLAUDE.md` names no model that the skill does not, and no effort above `high`.
- The four checkers and the unit tests pass.
- Three changelog lines: `model-routing`, `claude`, `multi-agent-work`.
