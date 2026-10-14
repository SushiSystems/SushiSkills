# Global rules

These hold in every repository, before any project CLAUDE.md.

## Language

Chat in Turkish. Every project artifact — code, comments, documentation, commit messages,
pull requests — in English unless told otherwise for a specific piece. All prose goes through
the `humanizer` skill in the language it is written in.

## Quality

The doctrine in the `sushiskills` skill holds the quality rules: its boundaries, SOLID first,
hold without exception, and its defaults hold unless their "not when" line applies. Load it
before any work.

## Documentation architecture

Every repository, whatever its size, carries the documentation tree the `documentation` skill
defines, so that what exists, what is done, what is left and what is planned can be read from
the tree. Load that skill before writing or moving anything under `docs/` or a module README.
It holds the tree, the placement questions and the changelog entry shape;
`tools/documentation/check_docs_layout.py`, `check_changelog.py` and `check_docs_truth.py`
enforce it.

On first entering a repository that lacks this shape: measure it, report the gaps, and get
approval before building the skeleton. The build-out is its own task.

## Source comments

A comment says what a thing does, in Doxygen form, and nothing else. Load the `source-comments`
skill before writing or reviewing a comment, a file header or a license block. It holds the
license block, the `@file` block, the tag table and what is forbidden in source;
`tools/documentation/check_source_comments.py` enforces it.

## Delegation

A subagent reads CLAUDE.md but not my memory, so nothing in memory reaches it unless the prompt
carries it. The rules every subagent follows are in `DISPATCH.md`, in the folder of the file
`~/.claude/CLAUDE.md` imports. Every subagent prompt opens with one line, naming that file by its
absolute path on this machine:

`Read <absolute path>/DISPATCH.md before anything else and follow it.`

Read `DISPATCH.md` once before the first dispatch of a session. A report that does not open with
the line it asks for is sent back unread, whatever its content: the subagent did not read the
rules.

Model per dispatch: the `model-routing` skill chooses the model and the effort for each kind
of dispatch, by phase and by task, and holds the escalation ladder for a failed task. The limits
it works within, for Claude 5.5 models only: the session runs on `opus`, at `medium` when it
plans or runs a plan and at `low` otherwise; `fable` is not used; `sonnet` runs at `low` or
`medium` only; every `opus` dispatch runs at `low`; `haiku` takes spec-complete and mechanical
work at `medium` or `high`, by task; `high` on `opus` is the exception, about five dispatches
in a hundred, and only after I have approved it: ask me before any `high` dispatch. The `model`
field and the effort are set on every dispatch, never left to inherit.

Effort caps at `high`; never `xhigh` or `max`. `low` and `medium` are the right choice for
mechanical work and are not a compromise.

A report that comes back without evidence of rules 1, 2, 6 and 7 of `DISPATCH.md` is sent back, not accepted. Reviewer
dispatches check SOLID shape and humanizer register explicitly, as named items, not as "quality".

## Planning

The `multi-agent-work` skill holds the planning rules: hierarchy first, one acceptance criterion
and one build per task. I choose how a plan runs, inline or in waves; ask me.
