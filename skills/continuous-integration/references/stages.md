# Stages, trigger by trigger

Read this when adding or changing a stage, a job or a budget. `../SKILL.md` holds the short form.

## Stages

| Stage | Trigger | Runs |
| --- | --- | --- |
| Pre-merge | Every pull request | the check command of `project-tools`; the build on Windows and on a hosted Linux runner; the `small` and `medium` tests of the changed modules and of every module above them, shuffled with a printed seed; the same tests again under AddressSanitizer and UndefinedBehaviorSanitizer on Linux; each fuzz target over its corpus, as a regression test |
| Post-merge | Every push to `main` | Everything pre-merge runs, over every module; ThreadSanitizer over the tests that start threads; the repositories downstream built against this commit |
| Nightly | Once a day | Everything post-merge runs; each fuzz target for a fixed time; line and branch coverage; benchmarks against the last nightly; `quarantined` tests, reported and never gating |
| Release | A `vX.Y.Z` tag | Everything nightly runs, then the packaging build |

- A change selects its modules by reverse dependency in the module graph the build declares;
  post-merge runs every module, so a module the selection missed is seen within one merge.
- The diff's line and branch coverage is printed in the pre-merge summary.
- Mutation testing runs over the changed and covered lines of one module.
- A repository that pins an upstream at a tag sees an upstream change that breaks it before the
  pin moves.
- The `commits` trailer check needs the full-history checkout.
- Prose, for `[skip ci]`, is `docs/`, README and changelog.
