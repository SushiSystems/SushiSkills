# Agnostic doctrine

**Status:** Open — planned on 2026-10-30, nothing built yet. The plan is `PLAN.md`.
**Implements:** DOCTRINE_SPLIT#P1, DOCTRINE_SPLIT#P2, DOCTRINE_SPLIT#P3, DOCTRINE_SPLIT#P4, DOCTRINE_SPLIT#P5, DOCTRINE_SPLIT#P6, DOCTRINE_SPLIT#P7, DOCTRINE_SPLIT#P8

The `sushiskills` doctrine becomes a global engineering doctrine that names no application, no
company and no machine. Everything specific to Sushi Systems moves into one tracked folder of this
repository, and the doctrine never refers to it.

## Decisions

Made by the owner on 2026-10-30.

1. The doctrine skill keeps the name `sushiskills`.
2. Everything specific to Sushi Systems lives under `sushisystems/` at the repository root. Its
   skill is `sushisystems/sushisystems-specific/`, and the rest of that folder holds the files the
   skill reads, one folder per topic.
3. The folder is tracked in this repository. It is not git-ignored and it is not a second
   repository.
4. The dependency runs one way. `sushisystems-specific` builds on the doctrine; the doctrine names
   nothing under `sushisystems/`. A checker enforces it.
5. An agent writes nothing to memory unless the owner asks for it in that message.
6. Backlog and design are used strictly: state is read from the repository's CLI, never from
   markdown or the git log; entries are written only through the CLI; a commit names the backlog
   entry it serves; a commit hook runs the fast checks.
7. No machine path, drive letter, user name or host name appears in a skill.

## What counts as specific

| Kind | Examples found in `skills/` | Goes to |
| --- | --- | --- |
| A named product or library | SushiLog, SushiHub, SushiStack, SushiEngine, SushiRuntime, SushiAI | `sushisystems/` |
| A named company tool | `sushicore` and its `backlog` and `design` commands, `sushi-module.toml`, `SUSHISTACK_HOME`, `.sushistack` | `sushisystems/` |
| A person or company identity | the licence holder line, the founders' names in copy examples, the docs host, the repository URL | `sushisystems/` |
| A machine path | `D:/Projects/...` in `claude/README.md` | removed; the import path is each machine's own |
| A technology rule, not a company one | the C++ style, Unity layout, Lavapipe and SYCL device names, memory figures | stays; see "Open" |

The doctrine's wording for a moved rule is the neutral one: "the project's logger", "the project's
licence block", "the repository's backlog CLI".

## Out of scope

- Changes inside sushicore and SushiEngine. What they need is recorded as backlog entries: sushicore
  exports its command-group names and a surface-test helper, and carries the state RW-475 shows;
  SushiEngine shows committed but unbuilt work as `unverified`.

## Technology rules

Technology rules are not company-specific, but they do not belong in a general skill. A language
already has a skill of its own. An engine, a device class and a build tool follow it: a skill named
for the technology, referred to by role from the general ones (P4).
