# Literal wording: plan

**Status:** Open — every job ran and R1 reviewed the diff; the owner commits and closes RW-70 and RW-73

The skills, `claude/` and `sushisystems/` are read by AI models, which need the rule stated
exactly. Several rules are taught through an image instead: SOLID as "a brick", the CLI rule as
"the only door", the model order as "a ladder", a documentation layout as a "skeleton", storage as
"a byte it owes back". A model has to guess what the image maps to; a literal definition with an
example leaves nothing to guess.

This work replaces every figure of speech in those files with the literal rule and, where the image
taught something, one concrete example from this repository. It adds no rule and drops none.

## Decisions

- **D1.** A metaphor is a word or phrase used in a non-literal sense to describe a rule, a tool,
  a structure or a process. Each one is replaced by what it means, in the form "the rule, then an
  example" when the image carried an idea.
- **D2.** A term stays when a software engineering dictionary defines it with the meaning the text
  uses: pipeline, thread, tree, branch, merge, layer, tier, module, hook, seam (in a test), leak,
  bug, gate (naming a real pass or fail check). A quoted example of wording the text forbids stays
  as written; `humanizer` lists such wording on purpose.
- **D3.** These words are fixed, so that every file names a rule the same way:

  | Was | Becomes |
  | --- | --- |
  | a unit is a brick; brick discipline; a brick of the repository | unit, meaning a function, class, file or module; "the unit rules of `sushiskills`" |
  | The CLI is the only door | Run everything through the CLI |
  | Grow without reshaping | Add a kind without editing existing code |
  | ladder, rung | escalation order, step |
  | skeleton, build-out | initial layout, creation |
  | every byte a session writes is a byte it owes back | a session deletes every file it created outside the repository before it ends |
  | red flag, red flags; `red-flags.md` | excuse, excuses; `excuses.md`; the heading `## Excuses` |
  | one home | one location |

- **D4.** SOLID is defined once, literally, with an example for each of its five principles, in
  `skills/sushiskills/references/solid.md`. Every other file says "SOLID" or "the unit rules of
  `sushiskills`" and links there; none restates the definition.
- **D5.** Each `SKILL.md` stays at or under 2500 bytes and 800 words. Detail moves to the skill's
  own `references/`.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| A0 | `skills/sushiskills/` (all files; adds `references/solid.md`, renames `red-flags.md`), `claude/CLAUDE.md`, `claude/DISPATCH.md`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `skills/README.md`, `docs/CONTRIBUTING.md` |  | done |
| A1 | `skills/testing/`, `skills/performance/`, `skills/debugging/` (renames `red-flags.md`), `skills/platform-portability/`, `sushisystems/sushisystems-testing/` |  | done |
| A2 | `skills/documentation/`, `skills/file-formats/`, `skills/commits/`, `docs/DOCUMENTATION_STYLE_GUIDE.md` |  | done |
| A3 | `skills/humanizer/` English files and `SKILL.md`, `references/` (not `research/`) |  | done |
| A4 | `skills/humanizer/generic_turkish.md`, `skills/humanizer/hood_turkish.md` |  | done |
| A5 | `skills/repository-layout/`, `skills/build-throughput/`, `skills/project-tools/`, `skills/unity-project-layout/` |  | done |
| A6 | `skills/logging/`, `sushisystems/sushisystems-logging/`, `skills/marketing-copy/`, `skills/source-comments/`, `skills/model-routing/`, `skills/multi-agent-work/` |  | done |
| A7 | `skills/module-install/` (renames `red-flags.md`), `skills/cpp-code-style/`, `skills/dependencies/`, `skills/typescript-code-style/`, `skills/continuous-integration/`, `skills/backlog/`, `skills/python-code-style/`, `skills/unlinked-cleanup/` (renames `red-flags.md`), `sushisystems/sushisystems-tooling/` |  | done |
| A8 | `skills/versioning-and-release/`, `skills/storage-discipline/`, `sushisystems/sushisystems-licence/`, `skills/gpu-development/`, `skills/design/`, `skills/api-stability/` (renames `red-flags.md`), `skills/git-workflow/`, `sushisystems/sushisystems-dependencies/`, `sushisystems/sushisystems-specific/`, `sushisystems/sushisystems-module-install/` |  | done |
| R1 | Read-only review of the diff of A0 to A8: meaning kept, SOLID shape, humanizer register, no figure left | A0, A1, A2, A3, A4, A5, A6, A7, A8 | done |

## Acceptance

One criterion per job. A0 to A8: a Grep of the job's files finds no word of the "Was" column of
D3 and no figure of speech, and the job's report lists each replacement as old and new text. R1:
the report names, for each changed rule, that its meaning is the same as before, or names the file
and line where it is not.
