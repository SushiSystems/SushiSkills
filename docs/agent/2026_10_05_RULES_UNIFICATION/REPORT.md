# Rules unification report

**Status:** Implemented on 2026-10-05, inline, on `main`; independent review pending. Nothing is pushed.

## What was done

| Task | Commit | Result |
| --- | --- | --- |
| Precondition: pending rule changes | `ef442df` | Committed as they were |
| 1. One home per rule | `22d40da` | Dispatch block in `claude/CLAUDE.md` only, seven lines |
| 2. License block template and rule | `8000083` | `rule_license_block`, 7 tests |
| 3. Licence, notices, dependency rules | `36c0c4c` | PolyForm Noncommercial 1.0.0 text fetched from the PolyForm repository |
| 4. Required documents and reachability | `50325a6` | Two rules, 7 tests |
| 5. CI and versioning rules | `c9bf405` | `ci.yml`, version source without a manifest |
| 6. Documentation skeleton | `592e4e7` | `check_docs_layout.py` exits 0 |
| 7. Source comparison | none | No copied passage found; no skill file changed for this task |
| 8. CI workflow and close | this commit | Acceptance output below |

## Task 7: comparison with the cited sources

Fetched on 2026-10-05: the wikitext of "Wikipedia:Signs of AI writing" (32 223 words) and the
GOV.UK A to Z style page (11 562 words). Every Markdown file under `skills/humanizer/` and
`skills/marketing-copy/` (ten files, `research/` excluded) was compared with both for runs of
eight or more consecutive words in common, case and punctuation ignored. Result: no shared run
in any file.

`generic_english.md` carries a "GOV.UK replacements" line of word pairs. Its source words
appear in the GOV.UK "words to avoid" list; the replacements and the order are the skill's own.
`NOTICE.md` credits both sources with their licences. The comparison does not detect paraphrase
or copied structure; it was not read side by side by a person.

## Rulings

- Ledger kept here, not in a `.superpowers/` folder: the work folder is the one place an agent
  writes. Cost if wrong: none; the superpowers scripts were not used.
- Work done on `main`, not a branch or worktree: `git-workflow` puts everyday work on `main`
  and forbids worktrees unless the owner asks. Cost if wrong: eight commits to move.
- Test command is `python -m unittest discover -s tools/tests`, without `-t tools`: the plan's
  form needs `tools/tests` to be a package. Cost if wrong: none; all 14 tests run.
- The licence notice names `8000083` as the last Apache-2.0 commit, not `ef442df` as the plan
  said: `LICENSE` held the Apache text through `8000083`. Cost if wrong: one sentence in
  `README.md` and `NOTICE.md`.
- The `claude:` changelog line for the sixth dispatch line landed in Task 1, not in the
  precondition commit. Cost if wrong: none.
- The Task 5 changelog entry was 254 characters and was committed in `c9bf405` before the
  checker ran; Task 6 split it into two entries. The history holds one commit with an
  over-long line.
- Added beyond the plan: `skills/marketing-copy` now names the licence wording, and its two
  example sentences no longer call the libraries open source. The spec's rule against "open
  source" reached a file the plan did not list.
- The spec said `rule_license_block` would read the expected lines from `LICENSE`; it reads
  `K_` constants, as the `project-tools` contract requires. The spec was updated.
- "Apache" remains in five files: the changelog, `NOTICE.md` and `README.md` (the sentence
  about earlier commits), `skills/dependencies/SKILL.md` (accepted inbound licences) and the
  test that proves the old header is rejected.

## What was not done

- No sibling repository was touched. Each still carries the old `tools/`, the Apache header
  and, in most cases, `docs/agent/specs|plans|reports`; all of them fail the new rules until
  programmes 2 and 4 reach them.
- The commercial licence agreement is not drafted. `COMMERCIAL.md` gives a contact address.
- No contributor agreement text exists; `docs/CONTRIBUTING.md` states that one is required.
- The CI workflow was not run; it runs on the first push.
- Nothing was pushed. The public remote still shows Apache-2.0 at `f5dbf69`.
- A lawyer has not confirmed the licence choice or the Turkish written-form question.

## Acceptance output

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
Ran 14 tests in 0.032s

OK
$ grep -rln "re-attachable without touching" --include=*.md . | grep -v -e third_party -e docs/archive -e docs/agent
./claude/CLAUDE.md
./skills/sushiskills/SKILL.md
$ grep -rIl "Apache" . --exclude-dir=.git --exclude-dir=third_party --exclude-dir=archive --exclude-dir=agent
./docs/reference/CHANGELOG.md
./NOTICE.md
./README.md
./skills/dependencies/SKILL.md
./tools/tests/test_check_source_comments.py
$ ls ~/.claude/skills | wc -l
25
```

The skill count is 25, not the 24 the plan expected; every entry resolves.
