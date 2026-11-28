# Backlog commands and line forms

Read when you need the command for a question, the forms of the `Backlog:` line, the
work-or-issue choice.

## State comes from the command

`<cli>` is the repository's CLI. A repository with none runs the module form of the same
commands, named by the tooling role.

| Question | Command |
| --- | --- |
| What do I do next? | `<cli> backlog next`, with `--json` for an agent |
| What is open, blocked or late in one area? | `<cli> backlog list`, filtered |
| What waits for the owner? | `<cli> backlog decisions` |
| What does one entry say? | `<cli> backlog show <ID>` |
| Which open entries sit on the file I am about to change? | `<cli> backlog here <path>` |
| Does work close, or pile up? (the owner's) | `<cli> backlog flow` |
| Which work has outlived its first two weeks? (the owner triages it) | `<cli> backlog stale` |
| Is the store well-formed? | `<cli> backlog check` |
| Which entry does my commit serve? | The ID from `backlog next`, or the one `backlog add` printed |

A markdown file under `docs/backlog/` is a copy of the tool's output that can be out of date; the
command answers from the store.

`backlog next` gives the owner's pins, then the ready entries by priority and age. The command
`backlog close` takes no commit hash; the changelog line it prints names the ID. The work folder
of a plan's job is described in `AGENT_WORK.md` in `documentation`.

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

The priorities and their limits are in `SKILL.md`, section "Priority", the one location of the
limits.
