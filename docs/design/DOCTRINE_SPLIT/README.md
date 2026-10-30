# Doctrine split

**Status:** Open — P1 to P6 built, P7 to P9 planned
**About:** The doctrine in skills/ names no product, company, person or machine; everything specific to Sushi Systems lives under sushisystems/.
**Modules:** `skills`, `claude`

## Problem

The skills in `skills/` are meant to be a global engineering doctrine, but about 145 passages in
34 files name Sushi products (SushiLog, SushiHub, SushiEngine), a company tool (sushicore and its
backlog and design commands), the licence holder, the docs host or a drive path. Technology rules
(Unity layout, GPU test devices, build tools) sit inside general skills. The shared checkers under
`tools/` call sushicore. A reader or an agent outside Sushi Systems cannot use the doctrine without
carrying the company with it, and a company rule changes the doctrine's files.

## Decision

Decided by the owner on 2026-10-30.

1. The doctrine keeps the name `sushiskills` and names nothing specific.
2. Everything specific to Sushi Systems lives under `sushisystems/`, in this repository, tracked.
   Its skill is `sushisystems/sushisystems-specific/`. It is not git-ignored and not a second
   repository.
3. The dependency runs one way: the specific skill builds on the doctrine, the doctrine never names it.
   A checker enforces it.
4. Backlog and design are used strictly: state from the repository's CLI, entries written only
   through it, a backlog trailer on every commit, a tracked hook.
5. An agent writes nothing to memory unless the owner asks in that message.

## Design

Two layers in one repository.

| Layer | Folder | Holds |
| --- | --- | --- |
| Doctrine | `skills/` | Rules any repository can follow. It speaks of "the project's logger", "the project's licence block", "the repository's backlog CLI". |
| Company | `sushisystems/` | Product names, the company CLI and its commands, the licence holder, the brand copy, the module install scheme, the checkers that enforce them. |

Technology rules are a third kind: not company-specific, but not general either. A language already
has its own skill (`cpp-code-style`, `python-code-style`, `typescript-code-style`). An engine, a
device class or a build tool follows the same shape: a skill of its own, named for the technology,
and a general skill refers to it by role only. The general skills name no engine, vendor or device.

The shared checkers under `tools/` take the backlog and design command from a setting. A checker
that enforces a company rule moves to `sushisystems/` with the rule.

`check_agnostic.py` scans `skills/` against a list of patterns kept in `tools/settings.py`; the name
`sushiskills` is allowed.

### Rollout

A change to a shared tool or skill reaches the other repositories through `copy_shared_tools.py`.
It must not erase a checker a repository changed for itself (backlog entry RW-29), so P8 follows it.

## Phases

| Id | Phase | State |
| --- | --- | --- |
| P1 | A checker fails when skills/ names a product, company tool, person, host or machine path | built |
| P2 | The sushisystems/ folder and the sushisystems-specific skill exist and the layout accepts them | built |
| P3 | Every Sushi Systems rule moved out of skills/ into sushisystems/, the doctrine keeping the neutral rule | built |
| P4 | Technology rules (Unity, GPU devices, build tools) sit in skills of their own, not inside general skills | built |
| P5 | tools/ holds no company-specific checker; the repository's backlog and design CLI is a setting | built |
| P6 | Backlog and design skills, the status-to-command table, the commit trailer and the tracked hook | built |
| P7 | Memory is written only on the owner's request, stated in claude/CLAUDE.md and DISPATCH.md | planned |
| P8 | The shared tools and skills reach the other repositories without erasing their local rules | planned |
| P9 | Documentation cannot go stale: a change to a documented fact updates every page that links or cites it, enforced by rule, to be designed with the owner | planned |

## Open questions

- Where the neutral rule ends and a technology skill begins for the build tools the doctrine's
  second default names (cmake, ninja, ctest, npm, uv).
