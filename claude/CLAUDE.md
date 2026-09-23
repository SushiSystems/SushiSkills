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

Every repository, whatever its size, carries the same documentation architecture, so that what
exists, what is done, what is left and what is planned can be read from the tree:

```
README.md                       front door
docs/README.md                  manual index; every document reachable from here
docs/CONTRIBUTING.md            what must be documented, how a change lands
docs/DOCUMENTATION_STYLE_GUIDE.md
docs/getting_started/ architecture/ modules/ guides/ reference/
docs/reference/CHANGELOG.md  GLOSSARY.md  KNOWN_ISSUES.md
docs/design/                    live intent, each document with a status line;
                                REMAINING_WORK.md is the single backlog
docs/agent/specs|plans|reports  everything an agent writes while working
docs/archive/                   frozen; added to, never edited
<module>/README.md              the module's own facts, beside the code
```

Placement, five questions in order, stop at the first yes: a fact about one module → its
README; written by an agent during execution → `docs/agent/`; work with nothing open →
`docs/archive/`; intent with an open phase → `docs/design/`; otherwise the manual.

A changelog entry is one line: the date, a past-tense verb, what changed, and where, in
backticks. `- 2026-08-28 — Fixed the star field's exposure (`star.vert`, `StarPass`).` It never
says why; the reason lives in a design document the entry may link. Never more than 240
characters, never a nested bullet, never a second sentence. An entry that reads as a paragraph
is a violation, whatever it explains.

A manual page that stops being true is a defect in the change that made it false. The
documentation update is part of the same commit as the code; a change without its README,
design status or changelog entry is not finished. Every link and cited path resolves.

On first entering a repository that lacks this shape: measure it, report the gaps, and get
approval before building the skeleton. The build-out is its own task.

## Source comments

A comment says what a thing does, in Doxygen form, and nothing else. Every file opens, after
any license block, with `/** @file <name>`, one `@brief` sentence and `@author`; no `@date`.
Every symbol, private members included, carries `@brief`, one sentence starting with its verb;
`@param`, `@return`, `@pre` only when they state a rule the caller must keep. A block is at
most eight lines, a file header six. `//` appears alone, one line, inside a body, stating an
invariant; two `//` lines in a row are a paragraph and a paragraph belongs in a document.
Separator lines, history, TODO and the reason for a design are forbidden in source; the reason
is a design document the comment cites by path. Python carries the same in a module docstring
and Google-style function docstrings. `tools/documentation/check_source_comments.py` is the
shape of the checker every repository carries.

## Honesty

Say what was done and what was not. Never claim completion on partial work. If a task needs a
choice, ask rather than guess.

## Delegation

A subagent reads CLAUDE.md but not my memory, so nothing in memory reaches it unless the prompt
carries it. Every subagent prompt, whatever the task, opens with the same four lines, verbatim:

1. SOLID, without exception. Every unit is a brick: one responsibility, detachable and
   re-attachable without touching its neighbours, rebuildable on its own. Siblings that do the
   same kind of thing are shaped the same. Engineer it once carefully, run it a thousand times
   cheaply. No quick hacks that happen to pass.
2. Before writing any prose (a comment that explains, a commit message, a report, a reply),
   invoke the `humanizer` skill and apply its rules in the language of the prose.
3. Do not start any process that runs `se`, `cmake`, `ninja` or `ctest`, in the foreground or
   the background, and do not write or edit any build configuration file.
4. Report what was done and what was not. Paste the output of every verification you claim.
5. Before reporting, syntax-check what you wrote without building: C++ through
   `compile_commands.json` with `clang -fsyntax-only`, GLSL through `shader_compiler.exe`.
   Paste the command and its output.

Model per dispatch: every subagent runs on `opus` (Opus 5.5); only the effort changes. An
implementer, explorer or mechanical checker runs at `low`; a reviewer runs at `medium`; work
that needs real reasoning (an architect, a public interface, data ownership, a numeric kernel,
a merge across streams) runs at `high`, and only after I have approved it: ask me before any
`high` dispatch. `sonnet` and `fable` are not used. The `model` field and the effort are set
on every dispatch, never left to inherit.

Effort caps at `high`; never `xhigh` or `max`. `low` and `medium` are the right choice for
mechanical work and are not a compromise.

A report that comes back without evidence of 1, 2 and 5 is sent back, not accepted. Reviewer
dispatches check SOLID shape and humanizer register explicitly, as named items, not as "quality".

## Planning

Every plan puts hierarchy first: interfaces and the bricks they depend on come before their
callers, and a module boundary is fixed before anything on either side of it is written. Each
task closes with one acceptance criterion and one build; a task that needs two builds is two
tasks.

I choose how a plan runs:

- **Inline.** One session implements the tasks in hierarchy order, without subagents. A serial
  chain is correct here.
- **Waves.** Tasks the hierarchy leaves independent are grouped into waves with disjoint file
  sets, so two agents never touch one file. The plan states, per wave: the tasks, their files,
  what each waits on, and the build I run after it.
