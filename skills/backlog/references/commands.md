# Backlog commands and line forms

Read when you need the command for a question, the forms of the `Backlog:` line, the
work-or-issue choice.

## State comes from the command

A question about state is answered by a command, never by a file, the git log or memory.
`<cli>` is the repository's CLI. A repository with none runs the module form of the same
commands, named by the tooling role.

| Question | Command |
| --- | --- |
| What do I do next? | `<cli> backlog next`, with `--json` for an agent |
| What is open, blocked or late in one area? | `<cli> backlog list`, filtered |
| What waits for the owner? | `<cli> backlog decisions` |
| What does one entry say? | `<cli> backlog show <ID>` |
| Is the store well-formed? | `<cli> backlog check` |
| Which entry does my commit serve? | The ID from `backlog next`, or the one `backlog add` printed |

A markdown file under `docs/backlog/` is output of the tool. Reading it to learn what is left
answers from a stale copy; running the command answers from the store.

`backlog next` gives the owner's pins, then the ready entries by priority and age. The command
`backlog close` takes no commit hash; the changelog line it prints names the ID. A plan's job
serves its work folder's entry (`AGENT_WORK.md` in `documentation`). A commit that serves no
entry ends with `Backlog: none (<reason>)`, and the reason says why no entry exists.

## The Backlog line

The line, last in the message, takes one of these forms:

<!-- quote:begin backlog-line -->
```
Backlog: RW-123
Backlog: RW-123, KI-4
Backlog: SushiSkills RW-38
Backlog: none (typo in a comment)
```
<!-- quote:end backlog-line -->

## Work or issue

| What was found | Entry |
| --- | --- |
| Something to build, fix or check, with a scheduled fix and no workaround | `backlog add work` |
| A condition a reader can meet that has a workaround, or a limitation chosen on purpose | `backlog add issue` |
| A fault of a dependency, a toolchain or a sibling that is not the repository's to close | `backlog add issue`, with its origin |
| Something only the owner can rule on | `backlog add work --decision` |

The columns and the rule for a known issue are in `BACKLOG_FORMAT.md`.

## Choosing a priority

The priorities and their limits are in `SKILL.md`, section "Priority", the one home of the
limits.

## Red flags, in full

- "I will read `docs/backlog/` to see what is left." -> `backlog next` or `backlog list`.
- "I will note it in the commit message, a TODO or memory." -> `backlog add`.
- "I will close it in a later commit." -> the same commit.
- "I will edit the row." -> `backlog set`; nobody edits a row by hand.
- "I will pick the next task myself." -> with no task from the owner, `backlog next`.
- "This commit carries out a plan job, so it has no entry." -> it serves the work folder's entry.
- "This commit is too small for an ID." -> `Backlog: none (<reason>)`, and the reason is written.
