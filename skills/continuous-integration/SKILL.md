---
name: continuous-integration
description: Use when adding or changing a CI workflow, when CI fails, or before proposing a release, in a repository.
---

# Continuous Integration

CI runs the local checks on every supported platform. Why: `references/rationale.md`.

## Stages

Read `references/stages.md` before changing a job. A stage runs the tests whose `testing` size fits its budget; no `quarantined` test gates.

- Pre-merge (pull request): the check command of `project-tools`, builds, `small` and `medium` tests of
  changed modules and those above, shuffled with a printed seed, also under ASan and UBSan; fuzz
  corpora. 20 min median, 45 max.
- Post-merge (push to `main`): every module plus TSan, 60 min. Nightly adds fuzzing, coverage,
  benchmarks, 3 hours. A release tag adds packaging.
- A sanitizer job gates, never allowed to fail; no MemorySanitizer; coverage never gates. Unity:
  EditMode and PlayMode as two jobs. Mutation testing only when the owner asks.
- `large` tests run on no runner; before a release is proposed they run through the CLI on
  hardware and the proposal shows the output.
- A repository pinning an upstream builds on the tag before merge, upstream `main` after.

## Workflow rules

1. Full-history checkout.
2. CI calls only the project CLI, save where `sushiskills` default 2 allows.
3. One workflow per trigger: `ci.yml` (pull request, push), `nightly.yml`, `release.yml`.
4. `gate` depends on every pre-merge job and is the only check `main` requires; `main` takes
   pull requests only.
5. Every job has a timeout; a newer push cancels the older run.
6. Caches key on compiler, flags and build files; dependency caches on the manifest.
7. A job prints its CLI command first.
8. Third-party actions are pinned by commit hash.

## Commits that need no run

A commit pushed straight to `main` that changes only prose ends its subject with `[skip ci]`,
after the check command passed locally.
**Not when:** it touches source, a test, a build file, the CLI, a checker, a workflow or a
manifest; goes through a pull request; or the check command was not clean.

## When CI fails

- Read the first failed log as its job ends; fix per `sushiskills` default 3.
- A failing `main` is reverted, then fixed and merged again; nothing else is merged into it. No
  release is proposed or cut while CI fails.
- Reproduce a CI-only failure locally; file an environment fault with `backlog add issue`.
- Never disable a job or allow it to fail so that CI reports success.
