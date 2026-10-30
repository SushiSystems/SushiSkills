---
name: continuous-integration
description: Use when adding or changing a CI workflow, when CI fails, or before proposing a release, in a repository.
---

# Continuous Integration

CI runs the same checks the agent runs locally, on every platform the repository supports, so
that "it works here" is not the only evidence.

## Stages

Each stage runs the tests whose size, from `testing`, fits its budget. No test carrying
`quarantined` runs in a stage that gates.

| Stage | Trigger | Runs | Budget |
| --- | --- | --- | --- |
| Pre-merge | Every pull request | `python tools/check_all.py .` from `project-tools`; the build on Windows and Linux; `small` and `medium` tests; `small` tests again under AddressSanitizer and UndefinedBehaviorSanitizer on Linux | 20 minutes median, 45 at most |
| Post-merge | Every push to `main` | Everything pre-merge runs; ThreadSanitizer; the repositories downstream built against this commit | 60 minutes |
| Nightly | Once a day | Everything post-merge runs; benchmarks; `quarantined` tests, reported and never gating | 3 hours |
| Release | A `vX.Y.Z` tag | Everything nightly runs, then the packaging build | None |

- `large` tests run on no runner. Before a release is proposed they are run through the CLI on a
  machine that has the hardware, and the proposal carries the command and its output.
- A repository that pins an upstream at a tag builds against the tag before merge and against the
  upstream's `main` after merge, so an upstream change that breaks it is seen before the pin
  moves.

## Shape

1. CI calls the project CLI and nothing else: no build, test or package tool invoked directly in
   the workflow file, except where the doctrine's default 2 in `sushiskills` allows a direct call.
2. One workflow file per trigger under the forge's workflow folder: `ci.yml` for pull requests
   and pushes, `nightly.yml` for the schedule, `release.yml` for tags.
3. One job, `gate`, depends on every pre-merge job, and is the one check `main` requires. `main`
   takes changes through pull requests only.
4. Every job sets a timeout. A newer push to a pull request cancels the run before it.
5. Compiler output is cached by compiler, flags and build-file hash; dependency caches are keyed
   on the dependency manifest's hash.
6. A job prints the CLI command it ran as its first line.
7. Third-party actions are pinned to a commit hash.

## Commits that need no run

- **Rule:** a commit pushed straight to `main` that changes only prose (a page under `docs/`, a
  README, the changelog) carries `[skip ci]` at the end of its subject line, after
  `python tools/check_all.py .` has passed locally.
- **Why:** such a commit cannot change what the build, the tests or the sanitizers see, and a run
  for it holds the runners for an hour while it waits behind the run before it.
- **Not when:** the commit touches source, a test, a build file, the CLI, a checker, a workflow
  or a dependency manifest; the commit goes through a pull request, whose `gate` must report; or
  `check_all.py` was not run clean, since CI then runs the checkers the commit skipped.

## When CI fails

- A red `main` is fixed, or the change that broke it reverted, before any other work lands.
- No release is proposed or cut while CI is red.
- A failure that only CI shows is reproduced locally before it is fixed; if it is an environment
  fault, it becomes a known issue through `backlog add issue`.
- A job is never disabled or marked allowed-to-fail to get green.
