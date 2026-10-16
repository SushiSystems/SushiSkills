# SushiLog repository

Status: in progress. Done on 2026-10-17: tasks 0 to 6 (SushiLog v0.1.0, commit `b2dc144`) and
6a (sushicore v0.9.1). Open: 6b and 6c in SushiStack, and the adoptions 7 to 10: 7 and 8
started, 9 waits on 7, 10 waits on 7 and 8.

One logger for every Sushi library, in a repository of its own. SushiRuntime, SushiDSP,
SushiBLAS, SushiAI and SushiEngine link one shared library, so a process holds one queue, one
thread and one sink whatever it loads, and SushiEngine's two lanes log the same way. Each
project keeps its own front: its macros, its `LogProject` and its level variable.

The contract is `skills/logging/INTERFACE.md`; the rules are `skills/logging/SKILL.md`.

## Hierarchy

```
SushiLog (C++ standard library only)
  <- SushiRuntime  <- SushiBLAS <- SushiAI
  <- SushiDSP                         <- SushiEngine (both lanes)
```

SushiLog depends on no Sushi library. Every other repository depends on it directly, never
through SushiRuntime.

## Task 0: owner decisions

1. Name: `SushiLog`, repository `SushiSystems/SushiLog`, CMake package `SushiLog`, target
   `SushiLog::SushiLog`, namespace `SushiLog`, macro prefix `SL`, CLI `sl`.
2. Licence: PolyForm Noncommercial 1.0.0, as the other libraries.
3. Who creates the GitHub repository, the owner or this session.
4. Inline or waves for tasks 1 to 5, and build permission for each task's build.

Acceptance: the four answers are recorded in this file.

Decided on 2026-10-16:

1. `SushiLog`, as proposed.
2. PolyForm Noncommercial 1.0.0.
3. The owner created `SushiSystems/SushiLog`; the checkout is `D:/Projects/sushilog`.
4. Inline: one subagent (opus, low) writes tasks 2 to 5; this session runs every build and test,
   because a subagent starts no build. It may copy from SushiRuntime's logger.

## Task 1: the standard names SushiLog

`skills/logging/SKILL.md`: the Logger row names SushiLog as the one logger; "Meeting another
logger" keeps the host cases and drops the Sushi-to-Sushi forward, which one shared library makes
unneeded. `INTERFACE.md` keeps `log_forward_sink()` for hosts only.

Acceptance: `python tools/check_all.py .` clean in SushiSkills.

## Task 2: skeleton

The repository with the tree of `repository-layout` and `documentation`, the shared tools,
`settings.py` (`K_LOG_PREFIX = "SL"`), the license blocks, a CLI `sl` on sushicore with
`build`, `test` and `check`, and one module `modules/foundation/log/` that builds an empty
shared library.

Acceptance: `sl build` succeeds and `python tools/check_all.py .` is clean.

## Task 3: public interface

The installed headers of `INTERFACE.md`: `log_level.hpp`, `log_project.hpp`,
`log_category.hpp`, `log_record.hpp`, `log_sink.hpp`, `log_calls.hpp`, `log_front.hpp` (the
front macro and the per-translation-unit ceiling) and `log_c_sink.h`, one symbol each, with an
umbrella `SushiLog/SushiLog.hpp`. `Delegate` comes with them as `SushiLog::Delegate`.

Acceptance: small tests of the values and the front macro's two gates pass through `sl test`.

## Task 4: implementation, one brick per responsibility

Sources under `modules/foundation/log/source/`, each one responsibility:

| Brick | Holds |
| --- | --- |
| `level_table` | Levels per project and per category, the atomics the gate reads |
| `level_environment` | Reading and parsing `<PREFIX>_LOG_LEVEL` once per project |
| `record_format` | The record line and the thread numbers |
| `log_queue` | The bounded queue and the drop count |
| `log_writer` | The thread, synchronous delivery, `FATAL` ordering, exit |
| `sink_holder` | The sink, its swap, a sink that throws |
| `c_sink` | The C interface and the `size` rule |
| `forward_sink` | The sink a host's records enter through |

Acceptance: `sl test --label small` and `--label medium` pass; every behaviour `INTERFACE.md`
and the "Sink" table of `SKILL.md` name has a test; `check_logging.py` reports 0.

## Task 5: package and CI

Install and export `SushiLog::SushiLog` as a shared library, and `SushiLog::SushiLogStatic`
with hidden symbols for plug-ins a host may load twice. CI: Linux and Windows, small and medium,
ASan with UBSan, and ThreadSanitizer.

Acceptance: CI green on main; a consumer project in `tests/` finds the package and logs through
both targets.

## Task 5a: user guide

`docs/guides/LOGGING_GUIDE.md` in SushiLog: where records go, how to set levels per project and
module, how to send records to a file or a host's system, and what the ABI check's message
means. Each adopting repository's FAQ links it.

Acceptance: `check_docs_truth.py` clean in SushiLog.

## Task 6: release

Tag `v0.1.0` with the owner's approval.

Acceptance: the tag exists and the package builds from it.

## Task 6a: a Sushi library resolves without a workspace

`dependencies`, "A Sushi library as a dependency", holds the rule. In sushicore: read the
`[sushi.<name>]` pins of a fragment, resolve `<NAME>_DIR`, then the sibling, then the fetched
copy, and add a provisioning step that clones a pinned tag into `<home>/sources/<name>/<version>/`
and checks its commit; `doctor` names the source it used and a sibling off its pin. Release
sushicore with the owner's approval.

Acceptance: in a scratch folder holding only a SushiRuntime clone, `sr setup` fetches SushiLog at
its pin and `sr build` finds it; with a sibling present the sibling is used and the fetch is
skipped.

## Task 6b: a workspace takes over a standalone setup

In SushiStack, rule 6 of the same section: `hub add` clones from a fetched copy at the pinned
version and resets the remote; `hub status` lists fetched copies no module uses; `hub clean`
removes them. It waits on task 6a's folder layout.

Acceptance: a test with a fetched copy and no network adds the module from it, with the
repository's URL as the remote; a second test lists and removes an unused copy.

## Task 6c: pins move together

In SushiStack: `hub pin <name> <version>` rewrites the `[sushi.<name>]` pin in every linked
module's fragment, and SushiLog's CI gains a downstream stage that builds and tests SushiRuntime
against the commit under test.

Acceptance: a test moves a pin in two fragments at once; the downstream stage runs on main.

## Tasks 7 to 10: adoption, one repository each, in its own session

| Task | Repository | Change |
| --- | --- | --- |
| 7 | SushiRuntime | `foundation/log` and `foundation/logging` become the SR front over SushiLog; `logger.cpp` goes; `SR_LOG_*` and the public calls keep their names |
| 8 | SushiDSP | Its logger goes; `SD_LOG_*` becomes a front over SushiLog; plug-ins link `SushiLogStatic` |
| 9 | SushiBLAS, SushiAI | Their fronts move from `SR_LOG_FRONT_AT` to SushiLog's front macro and link SushiLog directly |
| 10 | SushiEngine | Both lanes link SushiLog; the native lane's port and the SushiDSP join go; the binary package ships `sushilog.dll`, lists SushiLog in `NOTICE.md` and names its version |

Each waits on tasks 6, 6a and 6b and on the one above it in the hierarchy, pins SushiLog in its
fragment and resolves it as task 6a does, never by `add_subdirectory` of a fixed path alone. Acceptance per task: the
repository's `check_all` clean, its tests green, and one process loading it with SushiRuntime
shows one stream with both projects' records.
