# Industrial testing: plan

**Status:** Open — triage done; phase D's split built, J2b2 left; J10 next

Carries out phase D of `SPEC.md` and clears the working trees the 2026-11-02 rollout left
uncommitted, so wave 1 starts from clean branches. Parallel mode, at most four subagents at once (the owner, 2026-11-04), sharing one checkout as `git-workflow`
says (no worktree unless the owner asks, no stash), models from `model-routing`. Work is accepted on proof, never on a share of sizes.

## Jobs

| Job | Files | Waits on | Status |
| --- | --- | --- | --- |
| J1 | `tools/checking/`, `tools/testing/check_test_sizes.py`, `tools/tests/test_check_test_sizes.py`, `tools/tests/test_checker.py` | | done |
| J1b | `tools/checking/tests_tree.py` (new), `tools/testing/check_test_sizes.py`, `tools/testing/check_test_value.py`, `tools/testing/added_tests.py`, `tools/README.md` | J1 | done |
| J2 | `tools/testing/` (rest), `tools/tests/test_*` of those checkers | J1b | done |
| J3 | `tools/documentation/check_docs_truth.py` and its tests (the rest split below) | J1b | done |
| J3a | `tools/documentation/check_docs_layout.py` and its tests | J3 | done |
| J3b | `tools/documentation/check_docs_follow.py`, `docs_follow.py` and their tests | J3 | done |
| J3c | `tools/documentation/check_source_comments.py` and its tests | J3 | done |
| J3d | `tools/documentation/check_docs_facts.py`, `facts.py`, `facts_cli.py` and their tests | J3 | done |
| J3e | `tools/documentation/check_design_topics.py`, `check_design_format.py` and their helpers and tests | J3 | done |
| J3e2 | `tools/documentation/repair_design_citations.py`, `fold_design_topics.py`, `retire_archive.py`, a test module for `design_status.py` and `citation_files.py`, line numbers asserted in `test_check_design_topics.py` | J3e | done |
| J4c2 | `tools/tests/test_check_all.py`: the three shell lines of `check_all.py` no test reaches | J4c | done |
| J3f | `tools/documentation/check_module_install.py`, `check_changelog.py` and their tests | J3 | done |
| J2b1 | `tools/testing/case_reader.py`, `check_test_sizes.py`, `tools/tests/conftest.py` and their tests: every `TestCase` class read (KI-3), and a class-level `K_TEST_SIZE` | J2 | done |
| J2b2 | the size marks of every `tools/tests/test_*`: `pytest.mark` replaced by the class-level `K_TEST_SIZE`, so the checker tests run without pytest | J2b1, J3a to J3f, J4a to J4d | done |
| J4 | `tools/licensing/write_license_block.py`, `tools/commits/check_backlog_trailer.py` and their tests (the rest split below) | J1b | done |
| J4a | `tools/layering/` and its tests | J4 | done |
| J4b | `tools/logs/`, `tools/ci/` and their tests | J4 | done |
| J4c | `tools/routing/`, `tools/check_all.py` and their tests | J4 | done |
| J4d | `tools/commits/history.py`, `tools/hooks/` and their tests, with the injection seam the hook tests need, and `trailer_problems` given its pattern | J4 | done |
| J10 | the copied `tools/` of every repository in the rework table, through `checking/copy_shared_tools.py`, its commit hooks installed, and the Skills block of `CLAUDE_TEMPLATE.md` in its `CLAUDE.md`; project-mobilerts by the session working there | J2b2, J10a | todo |
| J10c | `tools/checking/copy_shared_tools.py`: copy what upstream committed, never its working tree; the target's own licence block on every copied source file | J10b | done |
| J10a | `tools/layering/check_layering.py` and its tests: `rule_declared_libraries` and `rule_restricted_includes` moved up from sushiengine's copy, read from settings and silent where a repository sets none | J2b2 | done |
| J11 | `tools/testing/mutate_diff.py` (new) and its tests: mutation of the changed Python lines, standard library only | J1b | done |
| J12 | sushicore `source/sushicore/testing/`: read-only map of what the shared test command already does against `Running fast` and `Time` in `testing` | | done |
| J13 | `PLAN.md` of phase F in sushicore, written by the orchestrator from J12 | J12 | done |
| J14 | sushiengine: the 13 red checkers, triaged into fixes and backlog entries | J10 | todo |
| J10b | `tools/checking/known_findings.py` (new), `tools/check_all.py` and their tests: a known-findings baseline that only shrinks, so the commit that brings the tools into a red repository lands | J10a | done |
| J16 | `skills/testing/SKILL.md` and a new `skills/testing/REVIEWING.md`: how the promises of an interface are found, one good test whole beside a bad one, the signs of a long test, and the verdict table of a suite review | J10 | todo |
| J15 | the full review of every repository's tests, wave by wave of `PIPELINE.md`: per repository a read-only survey writes the promise list and a verdict per test into its work folder, then module workers apply it; the orchestrator builds and runs every repository's tests itself | J10, J10b, J11, J13, J16 | todo |
| J5 | sushicore working tree | | done |
| J6 | sushiruntime working tree | | done |
| J7 | sushiengine working tree | | done |
| J8 | sushiweb working tree | | done |
| J9 | project-mobilerts working tree | | done |

## Acceptance

- **J1.** One checker split into a pure core (strings and paths in, findings out) and a shell that
  walks files; its tests are `small` and touch no file or subprocess; the pattern is the one J2 to
  J4 copy. Build: `python tools/check_all.py .` green.
- **J1b.** Test-tree discovery (`TestTree`, `discover`, `K_TEST_FOLDERS`) lives in
  `tools/checking/tests_tree.py`; no checker imports another checker. Build: `check_all` green.
- **J10a.** sushiengine's two layering rules run upstream with their tests, and a repository that sets
  none of their settings gets no finding from them. Build: `check_all` green, and sushiengine's
  `check_layering.py` output equal before and after the copy.
- **J10.** Every repository's copies equal SushiSkills's, local forks reported before they are
  overwritten (sushicore's uncommitted `test_budget.py` fork is committed first, so history keeps it;
  sushidsp's skip list is dropped, as `TESTS.md` forbids one, and its findings become backlog
  entries). Build: each repository's checkers.
- **J11.** Given a base commit, it mutates each changed Python line once (comparison, boolean,
  constant, return), runs that module's tests per mutant and prints the survivors; it needs no
  package outside the standard library. Pulled ahead of the waves so the triage of every repository
  has machine evidence that a test can fail. C++ mutation stays RW-45 and needs the owner's choice of
  tool. Build: `check_all` green and one run on this repository's last commit recorded.
- **J12, J13.** The gap between sushicore's test command and the skill is listed per rule; the phase F
  plan closes each gap with one job.
- **J14.** Every red line is fixed or has an open backlog entry. Build: sushiengine's checkers.
- **J10b.** On a red repository the written baseline makes `check_all` pass, a new finding makes it fail,
  and a fixed one makes it fail until its count is lowered. Build: a scratch repository and `check_all`.
- **J16.** A reviewer given only the skill reaches the same verdict on a test as the table gives. Build:
  `check_docs_truth.py`; the owner reads the draft before it is committed.
- **J15.** Every test of a repository has a recorded verdict, and the kept and new tests pass the proof of
  RW-42's done-when. Build: the repository's own test command, run by the orchestrator. Paused by the
  owner on 2026-11-05 at the checkpoint; it starts after J16.
- **J2 to J4.** The same split for their checkers. Build: `python tools/check_all.py .` green.
  Accepted on proof, not on a share: the rules pass the purity run, the shell sits in one `medium`
  class, outputs equal the old checker's, and `mutate_diff.py` leaves no survivor unexplained (RW-42).
- **J5 to J9.** Every uncommitted change is either committed on the repository's feature branch,
  because it agrees with the `testing` skill as it stands, or listed in the report with the reason
  it was left. Nothing is discarded and nothing is pushed. Build: the repository's own check.
</content>
</invoke>
