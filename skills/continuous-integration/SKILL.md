---
name: continuous-integration
description: Use when adding or changing a CI workflow, when CI fails, or before proposing a release, in a Sushi Systems repository.
---

# Continuous Integration

CI runs the same checks the agent runs locally, on every platform the repository supports, so
that "it works here" is not the only evidence.

## What runs

| Trigger | Jobs |
| --- | --- |
| Every push and pull request | The four checkers from `project-tools`; build and every test that needs no device, through the project CLI |
| A `vX.Y.Z` tag push | Everything above, then the packaging build |

- Platforms: Windows and Linux, both on every trigger.
- Tests labelled as needing a device are skipped in CI and reported as skipped.

## Shape

1. CI calls the project CLI and nothing else: no cmake, ctest, npm or pytest invoked directly in
   the workflow file.
2. One workflow file per trigger under the forge's workflow folder, named after the trigger:
   `push.yml`, `release.yml`.
3. Dependency caches are keyed on the dependency manifest's hash.
4. A job prints the CLI command it ran as its first line.

## When CI fails

- A red `main` is fixed before any other work lands.
- No release is proposed or cut while CI is red.
- A failure that only CI shows is reproduced locally before it is fixed; if it is an environment
  fault, it goes into `docs/reference/KNOWN_ISSUES.md`.
- A job is never disabled or marked allowed-to-fail to get green.
