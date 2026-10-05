# Rules unification report

**Status:** Implemented and reviewed on 2026-10-05, inline, on `main`. Nothing is pushed.

## What was done

| Step | Commit | Result |
| --- | --- | --- |
| Licence text | `78821ac` | `LICENSE` holds PolyForm Noncommercial 1.0.0, fetched from the PolyForm repository |
| Precondition: pending rule changes | `7fef7ae` | Committed as they were |
| 1. One home per rule | `f252f3e` | Dispatch block in `claude/CLAUDE.md` only, seven lines |
| 2. License block template and rule | `17eed89` | `rule_license_block` |
| 3. Notices and dependency rules | `aa6371a` | `COMMERCIAL.md`, `NOTICE.md`, first-party and ported-code rules |
| 4. Required documents and reachability | `ce4375a` | Two rules |
| 5. CI and versioning rules | `1db876b` | `ci.yml`, version source without a manifest |
| 6. Documentation skeleton | `6d1d37b` | `check_docs_layout.py` exits 0 |
| 7. Source comparison | none | No copied passage found |
| 8. CI workflow | `823ba85` | Four checkers and the tests on two platforms |
| Review fix pass | `dfc3d95` | 2 Critical and 15 Important findings closed; 25 tests |

## Review

Three independent reviewers read the range through one lens each: rule consistency, checker
code, and prose and licence accuracy. They returned 2 Critical, 17 Important and 13 Minor
findings after duplicates are merged. The fix pass closed these:

| Finding | Fix | Proof |
| --- | --- | --- |
| Critical: the notice named an unpublished commit as the last Apache-2.0 one, and that commit carried both licences | The unpushed commits were rebuilt so the licence text changes first, in `78821ac`; `README.md` and `NOTICE.md` name `f5dbf69` and v0.2.0 | `git show 7fef7ae:LICENSE` opens with the PolyForm title |
| Critical: `rule_license_block` passed a block that kept an old licence or holder line beside the new ones | The rule rejects a line that names Sushi Systems or states a licence and is not one of the repository's own | `test_reports_second_licence_beside_the_right_one`, `test_reports_old_block`, `test_reports_reserved_rights_beside_a_grant`: failed, then passed |
| The closed-repository setting broke six tests | Tests take their lines from `K_LICENSE_LINES` | suite passes with either setting |
| A byte order mark or an encoding line made a correct block read as missing | `utf-8-sig`; `K_PYTHON_PREAMBLE` | two tests: failed, then passed |
| Titled, wrapped, bracketed and queried links were not read | Whole-text link reader | `test_reads_titled_wrapped_bracketed_and_queried_links`, `test_reports_a_broken_titled_link_on_its_line` |
| Reachability walked out of `docs/` and through work folders | `_reachable` stays inside the manual | `test_does_not_reach_through_a_file_outside_docs`, `test_does_not_reach_through_a_work_folder` |
| Report acceptance stated in three files | One home, `claude/CLAUDE.md`; `multi-agent-work` and `storage-discipline` cite it | text |
| `storage-discipline` restated dispatch line 7 | Citation | text |
| Dispatch line 4 contradicted the worker's README right; wave workers shared one `REPORT.md` | Worker set reworded in two skills; a wave worker reports in its reply | text |
| `claude/CLAUDE.md` kept the same-commit rule | Paragraph removed; `documentation` holds it | text |
| Required documents existed only as a checker constant | `documentation` names them; spec says documents, not folders | text |
| No first version under the new licence was named | v0.2.0, from the versioning table: a breaking change before v1.0.0 | `README.md`, `NOTICE.md` |
| `#` block for shell and CMake files missing from the skill | One sentence in `source-comments`; checker gap in the backlog | text |
| "Each skill folder is a module" owed 24 READMEs | "whose `SKILL.md` is its README" | text |
| `COMMERCIAL.md` summarised the licence more broadly than its text | Points at `LICENSE` as binding; address is `hello@sushisystems.io` | text |
| `CONTRIBUTING.md` promised a contributor agreement nobody decided | "not accepted yet"; listed as an open decision | text |
| Boxed template edges two columns short | 66 columns throughout | `awk` length check |
| Two skill changes had no changelog entry | Entries added | `check_changelog.py` exits 0 |

## Rulings

- Ledger kept here, not in a `.superpowers/` folder: the work folder is the one place an agent
  writes. Cost if wrong: none.
- Work done on `main`: `git-workflow` puts everyday work there and forbids worktrees unless
  the owner asks. Cost if wrong: eleven commits to move.
- Test command is `python -m unittest discover -s tools/tests`, without `-t tools`. Cost if
  wrong: none; all tests run.
- The unpushed commits were rebuilt with `git commit-tree` so that the licence text changes in
  the first commit after `f5dbf69`. Trees, authors and dates are unchanged apart from
  `LICENSE`; one sentence left the message of the notices commit. The earlier hashes are kept
  under the tags `backup/rules-unification-before-review-fixes` and
  `backup/rules-unification-before-reorder`. Cost if wrong: `git reset --soft` to a tag.
- Three commits carry rule changes of a second scope (`aa6371a` also changes `dependencies` and
  `repository-layout`, `1db876b` also `versioning-and-release`, `823ba85` also
  `marketing-copy`), and the fix pass is one commit under `fix(tools)`. They were not split.
  Cost if wrong: `git log` by scope misses those changes; the changelog carries each under its
  own scope.
- `rule_required_entries` demands the eight documents and no folders: git keeps no empty
  folder, and a repository without guides has no guide to put in one. Cost if wrong: one table.
- `ci.yml` still gates on `rule_archive_candidates`. Taking it out needs a new option on the
  shared checker runner, which every repository copies; that is the owner's call. Cost if
  wrong: the first push after 2027-01-03 fails until this folder is archived.
- Added beyond the plan: `skills/marketing-copy` names the licence wording, and its examples
  no longer call the libraries open source.
- `rule_license_block` reads `K_` constants, not `LICENSE`, as the `project-tools` contract
  requires. The spec was updated.

## Deferred minors

- `versioning-and-release`: the release steps still say "through the project CLI" and treat
  the version source and the changelog heading as two acts.
- Three files say a checker "enforces" its skill, while the backlog lists what it does not check.
- `rule_license_block` does not check the project line, the order of upstream lines or the box
  edges.
- `_reachable` does not follow a link to a folder.
- `KNOWN_ISSUES.md` is a two-column table, not the symptom, cause and recognition shape the
  `debugging` skill names.
- Two commit subjects are exactly 72 characters; one has no scope.
- `skills/README.md` and `docs/DOCUMENTATION_STYLE_GUIDE.md` both state the front-matter contract.

## What was not done

- No sibling repository was touched. Each still carries the old `tools/`, the old header and,
  in most cases, `docs/agent/specs|plans|reports`; all fail the new rules until programmes 2
  and 4 reach them.
- The commercial licence agreement is not drafted. `COMMERCIAL.md` gives a contact address.
- Whether outside contributions are accepted is undecided.
- The CI workflow was not run; it runs on the first push.
- Nothing was pushed. The public remote still shows Apache-2.0 at `f5dbf69`.
- A lawyer has not confirmed the licence choice or the Turkish written-form question.
- The source comparison of Task 7 finds shared runs of eight words; it does not find paraphrase.
- Reference-style Markdown links and links around images are not read by the layout checker.

## Task 7: comparison with the cited sources

Fetched on 2026-10-05: the wikitext of "Wikipedia:Signs of AI writing" (32 223 words) and the
GOV.UK A to Z style page (11 562 words). Ten Markdown files under `skills/humanizer/` and
`skills/marketing-copy/`, `research/` excluded, were compared with both for runs of eight or
more consecutive words in common, case and punctuation ignored. No file shares a run with
either source. The "GOV.UK replacements" line in `generic_english.md` takes its source words
from the GOV.UK "words to avoid" list; `NOTICE.md` credits both sources with their licences.

## Acceptance output

Run on `dfc3d95`'s tree, Python 3.13.13, Windows.

```
$ python tools/documentation/check_source_comments.py .
exit 0
$ python tools/documentation/check_docs_layout.py .
exit 0
$ python tools/documentation/check_changelog.py .
exit 0
$ python tools/layering/check_layering.py .
exit 0
$ python -m unittest discover -s tools/tests
Ran 25 tests in 0.048s

OK
$ grep -rln "re-attachable without touching" --include=*.md . | grep -v -e third_party -e docs/archive -e docs/agent
./claude/CLAUDE.md
./skills/sushiskills/SKILL.md
$ git diff backup/rules-unification-before-reorder HEAD --stat
(no output: the rebuilt history ends in the same tree)
$ git show HEAD~9:LICENSE | head -1
# PolyForm Noncommercial License 1.0.0
```

"Apache" remains in the changelog, `NOTICE.md` and `README.md` (the sentence about earlier
versions), `skills/dependencies/SKILL.md` (accepted inbound licences) and the test that proves
the old header is rejected. No 3.11 interpreter is installed here, so the checkers were not run
on the version CI uses.
