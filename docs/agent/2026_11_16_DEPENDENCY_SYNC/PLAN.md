# Dependency sync: plan

**Status:** Open — run in parallel by the owner's choice on 2026-11-16; R1 and R2 wait on SushiAI and SushiEngine, whose sessions apply them

The shared checkers live in two trees that have drifted: SushiSkills and SushiCore each hold
files the other lacks and about 25 files whose text differs. `copy_shared_tools.py` reads
SushiSkills at `HEAD`, so no repository can say which version of the tools it runs. Library pins
drift as well: SushiBLAS pins SushiRuntime v0.5.1 and SushiAI pins v0.5.2, and the SushiCore range
in each CLI runs from 0.10 to 0.13. `hub pin` moves one pin across the workspace, but nothing
reports a dependency pinned at two versions, finds a module's latest tag, or carries a release up
the `depends_on` graph.

This work makes SushiCore the one source of the shared tools, read at a release tag and recorded
in a lock file. It gives `hub` a pin report and a `bump` that walks the graph. Every repository is
then brought to one version of each dependency.

## Decisions

- **D1.** SushiCore owns the shared tools under its `tools/`. SushiSkills becomes a consumer like
  every other repository and keeps only `tools/skills/`, `tools/settings.py` and
  `tools/README.md` of its own.
- **D2.** The copier becomes `python -m sushicore.shared_tools sync ROOT --tag vX.Y.Z`. It reads
  the files from that SushiCore tag, never from `HEAD`. It writes `tools/shared_tools.lock`, which
  holds the tag and a hash per file. `--check` exits 1 when a file differs from the lock.
  The tag is the SushiCore release the repository's CLI pins.
- **D3.** `check_all.py` runs the lock check, so a local edit or a stale copy fails the
  repository's own check.
- **D4.** `hub pins` prints, per dependency, each module's pinned version, the latest tag, and
  every dependency pinned at more than one version. It exits 1 on a split.
- **D5.** `hub bump <library> <tag>` moves the pin in every module that depends on the library,
  in `depends_on` order, lowest tier first. For `sushicore` it also runs `shared_tools sync` in
  each repository. It runs each repository's `check_all.py` and prints a pass or fail table.
  It commits nothing; the person commits each module.
- **D6.** A CI fan-out that opens a pull request per dependent on a release tag is out of this
  work. It needs tokens in every repository, which is the owner's decision; it goes to the
  backlog.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| C1 | SushiCore `tools/`: every SushiSkills-only shared file brought in, every differing file merged to the newer text, its tests |  | done |
| C2 | SushiCore `source/sushicore/shared_tools/` (package, `__main__.py`) and `tests/`: sync from a tag, lock file, `--check`; SushiCore `tools/checking/copy_shared_tools.py` and its test removed |  | done |
| H1 | SushiStack `cli/sushihub/services/pin_report.py`, `git_ops.py` (latest tag), `cli.py` (`hub pins`), tests |  | done |
| S1 | SushiSkills `skills/api-stability`, `sushisystems/sushisystems-dependencies`, `sushisystems/sushisystems-tooling`, `skills/project-tools`: the rule |  | done |
| C3 | SushiCore `tools/checking/check_shared_tools.py`, `tools/check_all.py`, test: the lock check in `check_all` | C1, C2 | done |
| H2 | SushiStack `cli/sushihub/services/bump.py`, `cli.py` (`hub bump`), tests | H1, C2 | done |
| C4 | SushiCore release, local tag | C3 | done |
| R1 | Each repository: `hub bump sushicore <C4 tag>`, its red checks fixed; SushiSkills' own copier removed | C4, H2, S1 | running |
| R2 | Each split dependency from `hub pins` bumped to one version, red checks fixed | R1 | running |

## Acceptance

- **C1.** `diff -rq` between SushiSkills `tools/` and SushiCore `tools/` lists only `settings.py`,
  `README.md`, `known_findings.toml` and `tools/skills/`. Build: `python tools/check_all.py .` and
  `python -m pytest tools/tests -q` in SushiCore.
- **C2.** Syncing a scratch repository from a tag writes the lock, and a one-byte edit makes
  `--check` exit 1. Build: `python -m pytest tests -q` in SushiCore.
- **H1.** On a workspace fixture with SushiRuntime pinned at two versions, `hub pins` lists the
  split and exits 1. Build: `python -m pytest cli/tests -q` in SushiStack.
- **S1.** Each skill stays inside its word budget and the rule appears in one file only. Build:
  `python tools/check_all.py .` in SushiSkills.
- **C3.** A repository whose shared file differs from its lock fails `check_all.py`.
- **H2.** On a fixture graph, `bump` moves the pins in tier order, and its dry run changes no file.
- **C4.** The tag exists locally and the changelog section is closed.
- **R1.** In every repository `python -m sushicore.shared_tools sync . --check` exits 0 and
  `python tools/check_all.py .` passes.
- **R2.** `hub pins` exits 0 over the whole workspace.

## Owner steps

Pushing branches and tags, and the CI fan-out of D6.
