# Stages, trigger by trigger

Read this when adding or changing a stage, a job or a budget. `../SKILL.md` holds the short form.

## Stages

Each stage runs the tests whose size, from `testing`, fits its budget. No test carrying
`quarantined` runs in a stage that gates.

| Stage | Trigger | Runs | Budget |
| --- | --- | --- | --- |
| Pre-merge | Every pull request | `python tools/check_all.py .` from `project-tools`; the build on Windows and on a hosted Linux runner; the `small` and `medium` tests of the changed modules and of every module above them, shuffled with a printed seed; the same tests again under AddressSanitizer and UndefinedBehaviorSanitizer on Linux; each fuzz target over its corpus, as a regression test | 20 minutes median, 45 at most |
| Post-merge | Every push to `main` | Everything pre-merge runs, over every module; ThreadSanitizer over the tests that start threads; the repositories downstream built against this commit | 60 minutes |
| Nightly | Once a day | Everything post-merge runs; each fuzz target for a fixed time; line and branch coverage; benchmarks against the last nightly; `quarantined` tests, reported and never gating | 3 hours |
| Release | A `vX.Y.Z` tag | Everything nightly runs, then the packaging build | None |

- A change selects its modules by reverse dependency in the module graph the build declares;
  post-merge runs every module, so a module the selection missed is seen within one merge.
- A sanitizer job gates like any other; it is never marked allowed to fail. MemorySanitizer is not
  run.
- The diff's line and branch coverage is printed in the pre-merge summary and never gates.
- A Unity project runs its EditMode and PlayMode tests as two jobs.
- Mutation testing runs only when the owner asks, over the changed and covered lines of one module.
- `large` tests run on no runner. Before a release is proposed they are run through the CLI on a
  machine that has the hardware, and the proposal carries the command and its output.
- A repository that pins an upstream at a tag builds against the tag before merge and against the
  upstream's `main` after merge, so an upstream change that breaks it is seen before the pin
  moves.

