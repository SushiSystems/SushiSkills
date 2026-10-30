# Agnostic doctrine plan

**Status:** Open — inline; P1 to P7 built, P8 is rolling out to the other repositories, P9 waits for the design talk.

Carries out `SPEC.md` and the topic `docs/design/DOCTRINE_SPLIT/`. One session runs every task in
order. Each task has one acceptance criterion and one build, `python tools/check_all.py .` unless
the task says otherwise, and ends in one commit that carries its `Backlog:` line once P6 exists.

## Hierarchy

```
P1 checker -> P2 skeleton -> P3 company content moves -> P4 technology split -> P5 tools decoupled
                                                                                       |
                                    P6 backlog and design, commit rule, hook -> P7 memory -> P8 rollout
```

The checker comes first, so every later task has a red test to turn green. The skeleton exists
before content moves into it. Moves come before cleanup, so no sentence is deleted before its new
home exists. Rollout is last, because it ships the finished shape to the other repositories.

## Task 0: owner decisions

Recorded in `SPEC.md` and the design topic. The run mode is inline, decided on 2026-10-30.

Acceptance: both files carry the decisions. Done.

## P1: the boundary checker

`tools/layering/check_agnostic.py`, with `K_SPECIFIC_TERMS` in `tools/settings.py`: patterns for
product names, company tool names, the licence holder, the docs host, drive letters and home paths.
It scans `skills/` and `claude/` and fails on a match. `sushiskills` is allowed. Tests in
`tools/tests/` cover a hit, a clean file and the allowed name. It runs standalone until P5.

Acceptance: the tests pass, and a standalone run lists every hit of the inventory in `SPEC.md`.

## P2: the skeleton

- `sushisystems/sushisystems-specific/SKILL.md`: name, a description that triggers inside a
  Sushi Systems repository, a table of topic folders, and the line that it extends `sushiskills`.
- `repository-layout` and `check_docs_layout.py` accept `sushisystems/` as a top-level folder.
- `docs/getting_started/INSTALL.md` says how the skill links into a machine's skills folder.

Acceptance: `check_all.py` clean with the folder present.

## P3: company content moves

One sub-task per skill, each owning its files. The company text moves to `sushisystems/<topic>/`;
the doctrine file keeps the neutral rule.

| Task | Doctrine files | Moves to |
| --- | --- | --- |
| 3a | `logging/SKILL.md`, `logging/INTERFACE.md` | `sushisystems/logging/` |
| 3b | `module-install/SKILL.md` | `sushisystems/module-install/` |
| 3c | `marketing-copy/` | `sushisystems/brand/` |
| 3d | `source-comments` licence block, `dependencies` library section | `sushisystems/licence/`, `sushisystems/dependencies/` |
| 3e | `project-tools`, `documentation/*_FORMAT.md`, `build-throughput` | `sushisystems/tooling/` |
| 3f | `repository-layout`, `cpp-code-style`, `api-stability`, `continuous-integration`, `commits`, every `description:` | in place, neutral wording |

`module-install` and `logging/INTERFACE.md` are near-rewrites; the rest are extractions.

Acceptance per sub-task: the standalone checker reports no hit in its files, and the moved text is
in its new home unless the neutral rule needed a sentence.

## P4: technology split

The doctrine's general skills name no engine, vendor, device or build tool. Each technology gets a
skill of its own, named for it; the general skill refers to it by role.

| From | To |
| --- | --- |
| `repository-layout/UNITY.md` | a `unity-project-layout` skill |
| GPU and device-class passages in `testing` and `build-throughput` | a `gpu-development` skill |
| The build tools named in the doctrine's second default (cmake, ninja, ctest, npm, uv) | the language and build skills that own them; the default says "the repository's own CLI" |

Acceptance: `check_agnostic.py` finds no technology term in a general skill, and the new skills are
listed in `sushiskills` and `skills/README.md`.

## P5: tools decoupled

- `tools/documentation/sushicore_bridge.py`, and the calls in `check_backlog.py`,
  `check_design_format.py` and `check_design_topics.py`: the command comes from a setting
  (`K_BACKLOG_COMMAND`, `K_DESIGN_COMMAND`), with no default naming a product.
- `check_module_install.py` and the module-install checks move to `sushisystems/`.
- `check_agnostic.py` joins `check_all.py` and also scans `tools/`.

Acceptance: `check_all.py` clean, including the new checker, in this repository and in a temporary
copy configured with different commands.

## P6: strict backlog and design

- `skills/backlog/SKILL.md` and `skills/design/SKILL.md`, each small, each with a table of
  "state question, repository CLI command", the operation order for a session (start, find a
  defect, finish) and the rule that nothing is read from markdown or the git log.
- The same table appears as a row set in `documentation` and `project-tools`, where a reader
  looks first. `documentation` loses the overlapping red flags and links the new skills.
- A `CLAUDE.md` template with the operation order as commands, in `sushisystems/tooling/`.
- The state vocabulary in `BACKLOG_FORMAT.md` names the state of built work that is committed but
  not verified. RW-475 in SushiEngine shows it as `unverified`; the state set belongs to sushicore,
  so this repository records the wording and opens an entry for sushicore and one for SushiEngine.
- A trailer `Backlog: <ID>` or `Backlog: none (<reason>)` on every commit. A checker passes an ID
  that is open or closed by the same commit and fails any other. `commits` states it.
- A tracked hooks folder, set with `core.hooksPath` by the repository's setup, runs the fast checks.

Acceptance: a commit without a trailer is refused by the hook, a valid one passes, and
`check_all.py` is clean.

## P7: memory rule

`claude/CLAUDE.md` and `claude/DISPATCH.md` state that no agent writes to memory unless the owner
asks for it in that message. A report that wrote memory is sent back.

Acceptance: both files carry the rule; `check_all.py` clean.

## P8: rollout to the other repositories

Needs RW-29 first: `copy_shared_tools.py` must refuse or report a shared checker whose copy
differs from every version here. Then one repository at a time (SushiRuntime, SushiDSP,
SushiTrack, SushiBLAS, SushiEngine): copy the shared tools, add the `CLAUDE.md` operation order,
run its own checks. Each repository is its own commit in its own checkout, shown to the owner
before it is pushed.

Two backlog entries for sushicore go in with the rest: its command-group names exported, and a
shared surface-test helper, so a repository stops writing the list into its tests.

Acceptance: `RW-29` closed here; each repository passes its own `check_all` after the copy.

## Close

The orchestrator writes the changelog line, dates the status lines of the topic and this folder,
and closes or opens the backlog entries with the `backlog` commands. Nothing is deleted before the
grace period.

## P9: documentation that cannot go stale

Added on 2026-10-30 at the owner's request. Agents sometimes change or add documentation and
forget the places that link or quote it, so a project's documentation goes stale. The owner wants
strict rules against it. The rules are designed with the owner when P8 closes, then built; this
phase stays the last in the queue.

Acceptance: the design is written into the topic and agreed with the owner before any rule is built.
