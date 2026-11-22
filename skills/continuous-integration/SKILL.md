---
name: continuous-integration
description: Use when adding or changing a CI workflow, when CI fails, or before proposing a release, in a repository.
---

# Continuous Integration

CI runs the agent's local checks on every supported platform. A case no rule foresaw:
`references/rationale.md`.

## Stages

A stage runs the tests whose `testing` size fits its budget; no `quarantined` test gates.
Read `references/stages.md` before changing a job.

- Pre-merge (pull request): `python tools/check_all.py .`, builds, `small` and `medium` tests of
  changed modules and those above, shuffled with a printed seed, also under ASan and UBSan; fuzz
  corpora. 20 minutes median, 45 at most.
- Post-merge (push to `main`): every module plus TSan, 60 min. Nightly adds fuzzing, coverage,
  benchmarks, 3 hours. A release tag adds packaging.
- A sanitizer job gates, never allowed to fail; no MemorySanitizer. Coverage never gates.
  Unity: EditMode and PlayMode as two jobs. Mutation testing only when the owner asks.
- `large` tests run on no runner; before a release is proposed they run through the CLI on
  hardware, and the proposal shows the output.
- A repository pinning an upstream builds on the tag before merge, upstream `main` after.

## Shape

1. Full-history checkout (`commits` trailer check).
2. CI calls the project CLI only, save where `sushiskills` default 2 allows.
3. One workflow per trigger: `ci.yml` (pull request, push), `nightly.yml`, `release.yml`.
4. One job, `gate`, depends on every pre-merge job; it is the one check `main` requires. `main`
   takes pull requests only.
5. Every job has a timeout; a newer push cancels the older run.
6. Caches key on compiler, flags and build files; dependency caches on the manifest.
7. A job prints its CLI command first.
8. Third-party actions are pinned by commit hash.

## Commits that need no run

A commit pushed straight to `main` that changes only prose (`docs/`, README, changelog) ends its
subject with `[skip ci]`, after `python tools/check_all.py .` passed locally.
**Not when:** it touches source, a test, a build file, the CLI, a checker, a workflow or a
manifest; goes through a pull request; or `check_all.py` ran unclean.

## When CI fails

- Read the first failed log when its job ends; fix per default 3 of `sushiskills`.
- A red `main` is reverted first, then fixed and landed; nothing else lands on it. No release is
  proposed or cut while CI is red.
- Reproduce a CI-only failure locally; an environment fault goes to `backlog add issue`.
- Never disable a job or allow it to fail to get green.
