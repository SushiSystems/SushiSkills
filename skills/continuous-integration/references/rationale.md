# Continuous integration: rationale

Read this when a rule in `../SKILL.md` looks wrong for a case it did not foresee. The rules
themselves are in `../SKILL.md`; this file holds only why they exist.

## MemorySanitizer

MemorySanitizer is not run because it needs every library in the process instrumented.

## Commits that need no run

A commit that changes only prose cannot change what the build, the tests or the sanitizers see.
A run for it holds the runners for an hour while it waits behind the run before it.

## A red run

The rest of a red run is not waited for because its remaining jobs cannot change the fix made
from the first failed job.
