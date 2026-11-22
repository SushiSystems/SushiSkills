---
name: testing
description: Use when fixing a bug, adding behaviour, writing or changing a test, updating a golden file, seeing a test fail intermittently, deciding whether a change is tested enough, making code testable, or when a test run is slow or the number of tests has grown, in a repository.
---

# Testing

A test checks one promise of a public interface against a named oracle, at the smallest size that
sees it, and fails when the promise breaks. `REVIEWING.md` gives verdicts.

## A test

- One promise, one when; the name is the promise as a sentence opening with the unit:
  `GemmWithBetaZeroIgnoresNanInC`.
- The expected value never comes from running the code under test.
- It kills a mutant or reproduces its commit's defect; a refactor never breaks it.
- Public interface only; a private function that needs a test wants its own module.
- Straight line: no `if`, loop or `try` outside a row table.

Forbidden kinds, with examples: `references/test-shape.md`.

## Sizes

Every test writes its size. `small`: own memory, one thread, injected clock and seed; 1 s; every
build. `medium`: one machine; 10 s; pre-merge. `large`: anything; 120 s; nightly. Test at the
smallest size that sees the promise; logic only a medium test sees lacks a seam, built first.
`references/sizes.md`.

## Time

The test command fails a run over one.

| Limit | Value |
| --- | --- |
| A `small` test | 100 ms |
| A `medium` test after the shared fixture | 5 s |
| A `large` test | 30 s |
| A repository's pre-merge run (`small` and `medium`), wall | 600 s |

## Oracles, seams, running

Oracles, tolerances and seams: `references/oracles.md`, `references/architecture.md`. Running,
shuffling and proof of value: `references/running.md`. Flaky tests, quarantine and golden files:
`references/determinism.md`. A golden file changes only with the owner's approval; when one fails,
report the difference and stop.

## The agent

List the promises first; take the smallest size; name the oracle; run the module's tests through
the project's test command; report each test added (`tools/testing/added_tests.py`); never run the
whole `large` tier. A bug fix writes the regression test, named for the defect, before the fix; it
runs once, in the single run after the single build (`build-throughput`, boundary 8).
`references/workflow.md`, `references/programs.md`.
