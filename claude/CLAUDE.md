# Global rules

These hold in every repository, before any project CLAUDE.md.

## Language

Chat in Turkish. Every project artifact — code, comments, documentation, commit messages,
pull requests — in English unless told otherwise for a specific piece. All prose goes through
the `humanizer` skill in the language it is written in.

## Quality

SOLID, without exception. Every unit is a brick: one responsibility, detachable and
re-attachable without touching its neighbours, rebuildable on its own. Siblings that do the
same kind of thing are shaped the same. Engineer it once carefully, run it a thousand times
cheaply. No quick hacks that happen to pass.

Ask before deciding module boundaries, public interface shape, data ownership, external
dependencies, and before deleting or overwriting anything you did not create. Decide naming,
internal structure, test shape and work order yourself. Never pick arbitrarily out of
laziness; if a choice is real, ask.

## Documentation architecture

Every repository, whatever its size, carries the documentation tree the `documentation` skill
defines, so that what exists, what is done, what is left and what is planned can be read from
the tree. Load that skill before writing or moving anything under `docs/` or a module README.
It holds the tree, the placement questions and the changelog entry shape;
`tools/documentation/check_docs_layout.py` and `check_changelog.py` enforce it.

A manual page that stops being true is a defect in the change that made it false. The
documentation update is part of the same commit as the code; a change without its README,
design status or changelog entry is not finished.

On first entering a repository that lacks this shape: measure it, report the gaps, and get
approval before building the skeleton. The build-out is its own task.

## Source comments

A comment says what a thing does, in Doxygen form, and nothing else. Load the `source-comments`
skill before writing or reviewing a comment, a file header or a license block. It holds the
license block, the `@file` block, the tag table and what is forbidden in source;
`tools/documentation/check_source_comments.py` enforces it.

## Honesty

Say what was done and what was not. Never claim completion on partial work. If a task needs a
choice, ask rather than guess.

## Delegation

A subagent reads CLAUDE.md but not my memory, so nothing in memory reaches it unless the prompt
carries it. Every subagent prompt, whatever the task, opens with the same seven lines, verbatim:

1. SOLID, without exception. Every unit is a brick: one responsibility, detachable and
   re-attachable without touching its neighbours, rebuildable on its own. Siblings that do the
   same kind of thing are shaped the same. Engineer it once carefully, run it a thousand times
   cheaply. No quick hacks that happen to pass.
2. Before writing any prose (a comment that explains, a commit message, a report, a reply),
   invoke the `humanizer` skill and apply its rules in the language of the prose.
3. Do not start any process that runs `se`, `cmake`, `ninja` or `ctest`, in the foreground or
   the background, and do not write or edit any build configuration file.
4. Write only to the files listed below and to the work folder under `docs/agent/`.
5. Report what was done and what was not. Paste the output of every verification you claim.
6. Before reporting, syntax-check what you wrote without building: C++ through
   `compile_commands.json` with `clang -fsyntax-only`, GLSL through `shader_compiler.exe`.
   Paste the command and its output.
7. Write scratch only to the scratchpad, never binaries or copies, under 100 MB; delete what you
   made and report the scratchpad size (`storage-discipline` skill).

Model per dispatch: every subagent runs on `opus` (Opus 5.5); only the effort changes. An
implementer, explorer or mechanical checker runs at `low`; a reviewer runs at `medium`; work
that needs real reasoning (an architect, a public interface, data ownership, a numeric kernel,
a merge across streams) runs at `high`, and only after I have approved it: ask me before any
`high` dispatch. `sonnet` and `fable` are not used. The `model` field and the effort are set
on every dispatch, never left to inherit.

Effort caps at `high`; never `xhigh` or `max`. `low` and `medium` are the right choice for
mechanical work and are not a compromise.

A report that comes back without evidence of 1, 2, 6 and 7 is sent back, not accepted. Reviewer
dispatches check SOLID shape and humanizer register explicitly, as named items, not as "quality".

## Planning

The `multi-agent-work` skill holds the planning rules: hierarchy first, one acceptance criterion
and one build per task. I choose how a plan runs, inline or in waves; ask me.
