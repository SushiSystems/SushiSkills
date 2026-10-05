# Estate audit: sushiskills

**Status:** Complete. Read-only audit of 2026-10-05; nothing in the repository was changed.

One auditing agent per dimension read the tree and a second agent checked each finding against
the files. A finding marked *confirmed* was re-read by the reviewer; *unclear* means the reviewer
could not settle it; *found by review* means the first pass missed it and nobody re-checked it.
Refuted findings are listed and not counted. No build, test or project CLI was run.

| Dimension | High | Medium | Low | Refuted |
| --- | --- | --- | --- | --- |
| Licence | 3 | 6 | 5 | 0 |
| Documentation | 2 | 10 | 3 | 0 |
| Layout and hygiene | 3 | 11 | 4 | 0 |

## Licence

### Facts

- Tracked files: 105 (git ls-files). 52 are Sushi Systems' own, 53 sit under third_party/superpowers/. By extension: 83 md, 6 py, 3 sh, 2 js, 1 cjs, 1 ts, 1 html, 1 dot, 3 extensionless scripts, 2 LICENSE, .gitignore, .gitattributes.
- D:/Projects/sushiskills/LICENSE: unmodified Apache License 2.0 text, 201 lines. Line 189 still holds the template placeholder 'Copyright [yyyy] [name of copyright owner]'; the file names no copyright holder.
- D:/Projects/sushiskills/third_party/superpowers/LICENSE: MIT License, 'Copyright (c) 2025 Jesse Vincent'. It is the only other licence file in the tree. There is no NOTICE, COPYING, docs/LICENSE or per-package licence file.
- Header variant A (the only one in own source), two '#' lines: '# Copyright (c) 2026-present Mustafa Garip & Sushi Systems' / '# Licensed under the Apache License, Version 2.0. See LICENSE.' Carried by 6 of 6 own Python files, e.g. tools/common/checker.py, tools/documentation/check_changelog.py, tools/layering/check_layering.py (also tools/common/__init__.py, tools/documentation/check_docs_layout.py, tools/documentation/check_source_comments.py).
- Own source files with no header: 0. Python is the only own source language; the repository has no own C++, GLSL, TypeScript, shell or JavaScript.
- Own Markdown: 45 files (36 under skills/, plus README.md, claude/CLAUDE.md, tools/README.md, two under docs/). None carries a licence header or front-matter licence field; they are covered only by the root LICENSE.
- Vendored source under third_party/superpowers/: 11 files (3 sh, 2 js, 1 cjs, 1 ts, 1 html, 3 extensionless scripts), none with a licence header, as upstream ships them. Examples: third_party/superpowers/skills/brainstorming/scripts/server.cjs, third_party/superpowers/skills/systematic-debugging/find-polluter.sh, third_party/superpowers/skills/writing-skills/render-graphs.js.
- Machine-readable licence declarations: none. The tree has no pyproject.toml, setup.py, package.json, CMakeLists.txt, sushi-module.toml, Doxyfile, Dockerfile, conda file, plugin manifest or SPDX identifier.
- Prose statements of the outbound licence: README.md lines 72-74 ('## License' / 'Apache License 2.0. See `LICENSE`.') and the six Python headers. No file under docs/ states the licence.
- Prose that fixes Apache-2.0 as the organisation-wide header template: skills/source-comments/SKILL.md line 27 ('/* ... Apache-2.0 notice ... */') inside the canonical licence block that every Sushi repository copies.
- Dependency licence policy: skills/dependencies/SKILL.md lines 25-31 accept MIT, BSD, Apache-2.0, Zlib, ISC and public domain, and reject 'Non-commercial, source-available, field-of-use limits' for inbound dependencies.
- Copyright holder strings in use: 'Mustafa Garip & Sushi Systems' with year '2026-present' (six Python headers); 'Jesse Vincent' 2025 (vendored). The skill template writes '<year>-present <Owner> & <Organisation>'.
- git shortlog -sne HEAD: 19 commits 'Mustafa Garip <mustafa.garip3434@hotmail.com>', 1 commit 'Mustafa Garip <mustafagarip@sushisystems.io>' (the GitHub 'Initial commit', committer GitHub <noreply@github.com>). One person, two addresses. History runs 2026-09-15 to 2026-09-24.
- Commit trailers: 13 commits carry 'Co-Authored-By: Claude Opus 5 / 5.5 (1M context) <noreply@anthropic.com>'. No Signed-off-by lines and no other human co-author.
- Third-party component: superpowers 6.3.0 from https://github.com/obra/superpowers, MIT, vendored unchanged at third_party/superpowers/ (commit 75e0f7c). Its notice is kept in third_party/superpowers/LICENSE and third_party/superpowers/README.md (source, version, licence, 'Local patches: None'); README.md lines 44-45 mention it.
- No fetched dependencies: no FetchContent, vcpkg, pip requirements or npm manifest. The six Python checkers import only the standard library as far as their opening lines show (argparse, sys, re, ast, subprocess, collections).
- Published state: remote origin is https://github.com/SushiSystems/SushiSkills.git; local main tracks origin/main at f5dbf69. Annotated tags v0.1.0 and v0.1.1 exist locally, both dated 2026-09-16. docs/reference/CHANGELOG.md has a 'v0.1.1 — 2026-09-16' section and docs/archive/changelog/v0.1.0.md archives v0.1.0. No PyPI or npm package exists for this repository.
- Working tree is not clean at the time of reading: README.md, claude/CLAUDE.md, docs/reference/CHANGELOG.md and skills/sushiskills/SKILL.md are modified and skills/storage-discipline/ is untracked. All counts above are for tracked files at HEAD.

### Corrections from review

- Own Markdown count: the audit says 45 files, 36 under skills/. The tree has 43 tracked own Markdown files, 38 under skills/ (23 SKILL.md plus 15 language and research files), plus README.md, claude/CLAUDE.md, tools/README.md, docs/reference/CHANGELOG.md and docs/archive/changelog/v0.1.0.md. The audit's own parts (36+1+1+1+2) add to 41, not 45. Check: 52 own files = 43 md + 6 py + LICENSE + .gitignore + .gitattributes. F4 repeats the 45.
- README licence lines: the audit cites README.md lines 72-74 while stating that all counts are for HEAD. Those are working-tree line numbers; at HEAD the heading is line 71 and 'Apache License 2.0. See `LICENSE`.' is line 73.
- Remote state: the audit left tags and visibility unconfirmed. git ls-remote --tags --heads origin returns only refs/heads/main f5dbf69, so v0.1.0 and v0.1.1 are local only. api.github.com/repos/SushiSystems/SushiSkills reports private: false, visibility: public, licence spdx_id Apache-2.0. F6's 'the exposure may be nil' does not hold.
- Machine-readable declarations: 'none' holds for the tree, but GitHub's repository licence field reads Apache-2.0 from LICENSE and is a public declaration the change must update.
- Python imports: the audit lists argparse, sys, re, ast, subprocess, collections 'as far as the opening lines show'. The full import lists are standard library only (also time, pathlib, dataclasses, typing, __future__) plus the local common.checker; no third-party import exists in any of the six files.

### Findings

#### L1. [high] The dependencies skill rejects the licence class the owner is about to adopt

Evidence: D:/Projects/sushiskills/skills/dependencies/SKILL.md line 30: '| Non-commercial, source-available, field-of-use limits | Rejected |', and line 35: 'A dependency's own dependencies are held to the same table.' Every Sushi repository depends on the others (sushicore, hub), so after the relicence each sibling becomes a rejected dependency under this table.

Recommendation: Decide with the owner how the table treats first-party Sushi Systems code, then amend the table in the same change that changes the licence. The row should keep rejecting third-party non-commercial code and state the first-party exception explicitly.

Review: unclear. skills/dependencies/SKILL.md lines 30 and 35 read as quoted. But the skill's own description scopes it to 'a third-party library, SDK or package', so the claim that every Sushi sibling 'becomes a rejected dependency' is an inference, not what the table says. Worth one clarifying sentence in the skill; medium at most, not high.

#### L2. [high] The organisation-wide header template hard-codes Apache-2.0

Evidence: D:/Projects/sushiskills/skills/source-comments/SKILL.md line 27: '/* ... Apache-2.0 notice ...                                              */' inside the canonical licence block (lines 18-29). Line 14 makes this block mandatory for every source file in every repository. The installed copy at C:/Users/sushi/.claude/skills/source-comments/SKILL.md carries the same text.

Recommendation: Rewrite the template block with the new licence's notice and SPDX-style identifier before any repository's headers are changed, so that every header rewrite copies one source. Give the Python two-line form as a second example, since the skill currently shows only the boxed C form.

Review: confirmed. skills/source-comments/SKILL.md line 27 holds '/* ... Apache-2.0 notice ... */' inside the block at lines 18-29; line 14 makes the block mandatory; diff -q against C:/Users/sushi/.claude/skills/source-comments/SKILL.md shows no difference. The recommendation (one template, plus a Python form) is a single-source fix and brick-shaped.

#### L3. [high] The repository is public on GitHub under Apache-2.0, so every commit on main is already granted

Evidence: api.github.com/repos/SushiSystems/SushiSkills returns "private": false, "visibility": "public", licence "spdx_id": "Apache-2.0". git ls-remote origin shows refs/heads/main at f5dbf69, the same commit as local main. The audit listed this under not_checked and let F6 end on 'the exposure may be nil'.

Recommendation: Treat all 20 commits up to f5dbf69 as irrevocably Apache-2.0, including the 23 skills, the checkers and claude/CLAUDE.md. The relicence note in README and CHANGELOG should name the first commit or version under the new licence. The local tags v0.1.0 and v0.1.1 were never pushed; ask the owner whether to push them as the Apache-era markers or leave them local.

Review: found by review.

#### L4. [medium] Six Python headers and the README state Apache-2.0 and must be rewritten

Evidence: Line 2 of tools/common/__init__.py, tools/common/checker.py, tools/documentation/check_changelog.py, tools/documentation/check_docs_layout.py, tools/documentation/check_source_comments.py and tools/layering/check_layering.py: '# Licensed under the Apache License, Version 2.0. See LICENSE.' README.md lines 72-74: 'Apache License 2.0. See `LICENSE`.' LICENSE itself is the full Apache-2.0 text (201 lines).

Recommendation: Replace LICENSE, the six header lines and the README section in one commit, with a changelog entry. The surface is small: 8 files in this repository.

Review: confirmed. All six tools/**/*.py carry the Apache line on line 2; LICENSE is 201 lines of Apache-2.0. README line numbers 72-74 are the modified working tree; at HEAD the sentence is line 73. Eight files is right.

#### L5. [medium] LICENSE names no copyright holder

Evidence: D:/Projects/sushiskills/LICENSE line 189: 'Copyright [yyyy] [name of copyright owner]' is the unfilled Apache appendix template. The holder 'Mustafa Garip & Sushi Systems' appears only in the six Python headers; the 45 own Markdown files, which are the bulk of the work, have no copyright statement anywhere.

Recommendation: The new licence file should open with an explicit copyright line (holder and year). Settle first whether the holder is the individual, the company, or both; see F5.

Review: confirmed. LICENSE line 189 is 'Copyright [yyyy] [name of copyright owner]'. That is the unfilled Apache appendix and normal for Apache, so it is a gap for the new licence rather than a present defect. The Markdown count in the evidence is wrong (43, not 45).

#### L6. [medium] Copyright holder is written as two parties, 'Mustafa Garip & Sushi Systems'

Evidence: Line 1 of all six tools/**/*.py files: '# Copyright (c) 2026-present Mustafa Garip & Sushi Systems'. skills/source-comments/SKILL.md line 26 prescribes '<Owner> & <Organisation>' for every repository. A joint statement leaves open who may grant commercial exceptions under a non-commercial licence; the user request says 'benim olsun' (mine).

Recommendation: Ask the owner which legal person holds the copyright and whether Sushi Systems exists as a registered entity, then write one holder (or a deliberate joint statement) in the template, LICENSE and headers. This is a legal question and needs a lawyer's confirmation, not a repository edit alone.

Review: confirmed. Line 1 of the six Python files and skills/source-comments/SKILL.md line 26 both read as quoted. The holder question is real and is the owner's to answer.

#### L7. [medium] Apache-2.0 grant on published history and on tags v0.1.0 and v0.1.1 cannot be retracted

Evidence: Tags v0.1.0 (2cffd0d) and v0.1.1 (5faf24a), both 2026-09-16; docs/reference/CHANGELOG.md section '## v0.1.1 — 2026-09-16'; docs/archive/changelog/v0.1.0.md. main tracks origin/main at f5dbf69 on https://github.com/SushiSystems/SushiSkills.git. Apache-2.0 section 2 grants a perpetual, irrevocable licence, so anyone holding a copy up to the last Apache commit keeps commercial rights to that snapshot.

Recommendation: State in the changelog and README which version is the first under the new licence, and that v0.1.1 and earlier stay Apache-2.0. Whether the tags are actually on the remote was not confirmed (see not_checked); if the GitHub repository is private and was never shared, the exposure may be nil.

Review: confirmed. Tags v0.1.0 (2cffd0d -> 9312f5c) and v0.1.1 (5faf24a -> 71d7f23) exist locally and LICENSE at v0.1.0 is Apache. I resolved the audit's open point: git ls-remote shows only refs/heads/main at f5dbf69, so the tags are not on the remote, and the GitHub API reports the repository public with spdx_id Apache-2.0. The exposure is real and covers all of main up to f5dbf69, not only the tagged versions.

#### L8. [medium] Humanizer and marketing-copy draw on share-alike and government-licensed sources, with no notice

Evidence: D:/Projects/sushiskills/skills/humanizer/generic_english.md lines 3-6 say the rules come from 'the Wikipedia "Signs of AI writing" catalogue' and line 68 carries a 'GOV.UK replacements' word list; D:/Projects/sushiskills/skills/marketing-copy/english.md line 3 cites the same Wikipedia page; D:/Projects/sushiskills/skills/humanizer/research/generic_english_sources.md line 14 lists it. Wikipedia text is CC BY-SA 4.0 and GOV.UK content is under the Open Government Licence v3.0. CC BY-SA cannot be relicensed under a non-commercial licence. The audit put these files under not_checked, so the one place in the repository where a share-alike conflict could exist was not examined.

Recommendation: Compare the word lists and stock-phrase lists in skills/humanizer/*.md and skills/marketing-copy/*.md against the two sources. Lists of single words taken as facts are probably not protected expression; copied sentences or structure would be. If anything was copied, either rewrite it or keep those passages under their source licence with attribution, and say so beside the root licence. I did not do this comparison; the finding is that it has to be done before the relicence.

Review: found by review.

#### L9. [medium] The Python header in use does not match the template it is supposed to copy, and the template defines no Python form

Evidence: D:/Projects/sushiskills/skills/source-comments/SKILL.md lines 18-29 define a boxed block whose first line is the file name (line 37: 'The first line of the license block is the file name'), with project and organisation URLs. The six files under D:/Projects/sushiskills/tools/ carry a two-line '#' header with no file name and no URL. Lines 99-100 of the skill mention 'the license block' for Python without showing one. The audit touches this only inside F2's recommendation and does not record it as a header inconsistency, which the brief asked for.

Recommendation: Define the Python licence header in the skill as its own example beside the C form, decide whether it carries the file name line, and make the six checkers match it in the same change that rewrites the licence line. Sibling files of one kind should carry one shape.

Review: found by review.

#### L10. [low] Vendored MIT component must keep its own licence after the relicence

Evidence: D:/Projects/sushiskills/third_party/superpowers/LICENSE (MIT, Copyright (c) 2025 Jesse Vincent), 53 tracked files, none with a per-file header. MIT allows redistribution inside a non-commercial work, but the 53 files stay MIT and the new licence cannot restrict them. README.md lines 44-45 already say the library is MIT.

Recommendation: Keep third_party/superpowers/LICENSE and README.md as they are. The new root LICENSE or README should say that third_party/ is excluded from the Sushi Systems licence and carries its own terms. No conflict; no GPL, LGPL or proprietary SDK is present in this repository.

Review: confirmed. third_party/superpowers/LICENSE is MIT, Jesse Vincent 2025; 53 tracked files under third_party/; README.md lines 44-45 as quoted. No GPL, LGPL or SDK found.

#### L11. [low] Vendored tree contains an Anthropic documentation page whose licence is not recorded

Evidence: D:/Projects/sushiskills/third_party/superpowers/skills/writing-skills/anthropic-best-practices.md (title 'Skill authoring best practices', links to platform.claude.com, images from mintcdn.com/anthropic-claude-docs at lines 249, 253, 919). third_party/superpowers/README.md declares the whole folder MIT under Jesse Vincent; this page appears to originate from Anthropic's documentation, and no notice names its source or terms.

Recommendation: Check upstream obra/superpowers for the provenance and terms of that file. If the terms are unclear, ask the owner whether to drop the file from the vendored copy (which would then need a 'Local patches' entry) or record its origin in third_party/superpowers/README.md.

Review: confirmed. third_party/superpowers/skills/writing-skills/anthropic-best-practices.md opens with 'Skill authoring best practices' and lines 249, 253, 919 load images from mintcdn.com/anthropic-claude-docs. No file under third_party/ other than LICENSE and README.md line 9 mentions a licence. Provenance still unverified against upstream.

#### L12. [low] Reference checker does not verify that a licence header exists or what it says

Evidence: D:/Projects/sushiskills/tools/documentation/check_source_comments.py lines 54-67: _license_end_c and _license_end_python only skip a leading run of boxed or '#' lines to find where comments start. No rule requires the block or matches its text, so a file with a missing or stale Apache header passes. This checker is the shape every repository copies.

Recommendation: Add one rule that requires the licence block and matches its licence line against a single expected string, so the header rewrite across all repositories can be verified mechanically. That is a code change for a later task, with owner approval of the expected text.

Review: confirmed. tools/documentation/check_source_comments.py lines 54-67 only skip a leading run of boxed or '#' lines; no rule yields an issue for a missing or wrong licence block. The recommendation is one added rule against one expected string, which is brick-shaped, though the expected text should come from one place the skill template also uses rather than a second copy.

#### L13. [low] No machine-readable licence declaration exists

Evidence: No SPDX-License-Identifier in any tracked file (git grep -i SPDX outside third_party returns nothing); no pyproject.toml, package.json or manifest in the tree. The licence is stated only in prose (README.md line 74) and in the six header comments.

Recommendation: When the new header is defined, include an SPDX identifier line (a standard one such as PolyForm-Noncommercial-1.0.0, or 'LicenseRef-<name>' for a custom text) so tools and GitHub can read the licence.

Review: confirmed. git grep for SPDX outside third_party and LICENSE returns nothing; git ls-files has no pyproject, package.json, toml, json or yaml. Low is right: nothing in this repository is packaged.

#### L14. [low] 13 of 20 commits carry an AI co-author trailer; no human contributor other than the owner

Evidence: git log bodies: 12 x 'Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>', 1 x 'Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>'. git shortlog -sne lists only Mustafa Garip under two addresses (mustafa.garip3434@hotmail.com x19, mustafagarip@sushisystems.io x1).

Recommendation: No third-party human consent is needed to relicense this repository. The owner may want a lawyer's view on how far AI-assisted text is protected by copyright in his jurisdiction, since a non-commercial restriction rests on copyright; that is outside what the repository can show.

Review: confirmed. git shortlog -sne HEAD and --all both give 19 + 1 for Mustafa Garip under two addresses; trailers are 12 x Opus 5 and 1 x Opus 5.5; 20 commits; the one other committer is GitHub noreply on the initial commit.

### Not checked

- Whether tags v0.1.0 and v0.1.1 and any GitHub Release exist on the remote: 'git ls-remote --tags origin' returned no output within 20 s (no error text either), so remote state is unconfirmed. Whether the GitHub repository is public or private was not checked.
- The GitHub repository's licence field and any GitHub Release notes (no gh call made).
- Upstream obra/superpowers at 6.3.0 was not fetched; the claim 'copied unchanged' in third_party/superpowers/README.md and the provenance of anthropic-best-practices.md were not verified against upstream.
- Full bodies of the six Python checkers were not read for third-party imports; only their opening lines and the licence-handling functions of check_source_comments.py were read.
- Quoted third-party text inside skills/humanizer/research/*.md and skills/marketing-copy/research/*.md (source lists) was not reviewed for copied passages that would carry their own copyright.
- The untracked folder skills/storage-discipline/ and the four uncommitted modifications were not reviewed; counts cover tracked files at HEAD only.
- Installed copies of the skills under C:/Users/sushi/.claude/skills/ were not compared file by file with the repository; only source-comments and dependencies were seen as loaded.
- Legal questions: enforceability of a non-commercial licence, copyright in AI-assisted text, and whether Sushi Systems is a registered entity able to hold copyright.

## Documentation

### Facts

- Repository holds 105 tracked files: root README.md, LICENSE, claude/CLAUDE.md, 24 skill folders under skills/ (23 tracked, skills/storage-discipline untracked), tools/ with four checkers, third_party/superpowers, and two documents under docs/.
- Working tree is dirty: README.md, claude/CLAUDE.md, docs/reference/CHANGELOG.md and skills/sushiskills/SKILL.md are modified and skills/storage-discipline/ is untracked (git status --short).
- EXISTS: README.md (75 lines), docs/reference/CHANGELOG.md, docs/archive/ (only docs/archive/changelog/v0.1.0.md), tools/README.md, third_party/superpowers/README.md.
- MISSING: docs/README.md, docs/CONTRIBUTING.md, docs/DOCUMENTATION_STYLE_GUIDE.md.
- MISSING: docs/getting_started/, docs/architecture/, docs/modules/, docs/guides/.
- MISSING: docs/reference/GLOSSARY.md, docs/reference/KNOWN_ISSUES.md.
- MISSING: docs/design/ entirely (no README.md topic map, no REMAINING_WORK.md, no design documents).
- MISSING: docs/agent/ entirely (no specs, plans, reports, and no dated work folders).
- MISSING per-module READMEs: skills/README.md and claude/README.md do not exist; each skill folder carries SKILL.md instead of README.md.
- MISSING root AGENTS.md and CLAUDE.md, which skills/repository-layout/SKILL.md line 15 lists in every repository root.
- Nothing under docs/ falls outside the architecture: no docs/superpowers, no docs/slop, no loose top-level guides, no duplicate CHANGELOG or LICENSE in the root. third_party/superpowers/LICENSE is the vendored MIT licence, correctly placed.
- No backlog exists anywhere, so there is no duplicate backlog; there is also no single one.
- No design documents exist, so no status-line violations exist.
- No Markdown link of the form [text](relative path) exists in README.md, docs/, skills/, tools/ or claude/; all references are backticked paths. Every backticked repository path I checked in README.md, tools/README.md and claude/CLAUDE.md resolves.
- Changelog entries: 5 in docs/reference/CHANGELOG.md, 6 in docs/archive/changelog/v0.1.0.md; none exceeds 240 characters, none is nested, none has a second sentence, all carry a scope.
- Git tags are v0.1.0 and v0.1.1; the live changelog keeps Unreleased and v0.1.1, v0.1.0 is archived, matching the documentation skill.
- README.md skill table lists 24 skills and matches the 24 folders under skills/; the map in skills/sushiskills/SKILL.md lists the 23 others. third_party/superpowers/README.md says fourteen skills and the folder holds fourteen.
- The installed copy C:/Users/sushi/.claude/skills/documentation/SKILL.md is byte-identical to skills/documentation/SKILL.md.
- README.md line 74 declares Apache License 2.0 and both checker files open with an Apache header; the owner's request asks for a licence that forbids commercial products, so these lines will change with the licence decision.

### Corrections from review

- README.md length: the audit says 75 lines; the file has 74 (grep -c '' README.md = 74, licence line is 74 as the audit itself cites).
- Apache headers: the audit says 'both checker files open with an Apache header'; six tracked Python files under tools/ carry it (check_changelog.py, check_docs_layout.py, check_source_comments.py, check_layering.py, common/checker.py, common/__init__.py).
- Installed copy: the audit calls C:/Users/sushi/.claude/skills/documentation/SKILL.md a 'byte-identical copy'; it is a symlink to D:/Projects/sushiskills/skills/documentation, as are all 24 skill entries there, so the diff proves nothing and uncommitted edits in the repository are live for every session.
- repository-layout line reference: the README.md definition ('a link to docs/README.md') is on line 22 of skills/repository-layout/SKILL.md, not line 23.
- Commit count for v0.1.0: 15 commits are reachable from the tag (git rev-list --count v0.1.0); the audit's 14 holds only if the release commit is excluded.

### Findings

#### D1. [high] The repository that defines the documentation architecture does not carry it

Evidence: D:/Projects/sushiskills/docs/ contains only reference/CHANGELOG.md and archive/changelog/v0.1.0.md. Absent: docs/README.md, docs/CONTRIBUTING.md, docs/DOCUMENTATION_STYLE_GUIDE.md, docs/getting_started/, architecture/, modules/, guides/, docs/reference/GLOSSARY.md, docs/reference/KNOWN_ISSUES.md, docs/design/ (README.md, REMAINING_WORK.md), docs/agent/. claude/CLAUDE.md line 25 says 'Every repository, whatever its size, carries the same documentation architecture'.

Recommendation: Build the skeleton as its own approved task: docs/README.md as index, CONTRIBUTING.md (how a rule change lands), DOCUMENTATION_STYLE_GUIDE.md, getting_started (install into ~/.claude/skills and ~/.agents/skills), reference/GLOSSARY.md and KNOWN_ISSUES.md, design/README.md and design/REMAINING_WORK.md, docs/agent/.

Review: confirmed. find docs -type f returns only docs/reference/CHANGELOG.md and docs/archive/changelog/v0.1.0.md; claude/CLAUDE.md line 25 reads as quoted. Note docs/design/README.md is required by the skill only, not by CLAUDE.md.

#### D2. [high] claude/CLAUDE.md and the documentation skill describe two different docs trees

Evidence: claude/CLAUDE.md line 33 lists 'docs/getting_started/ architecture/ modules/ guides/ reference/' and line 37 'docs/agent/specs|plans|reports'. skills/documentation/SKILL.md has no docs/modules/ and defines docs/agent/<YYYY_MM_DD>_<WORK_NAME>/ with SPEC.md, PLAN.md, REPORT.md, adding 'No other folder under docs/'. tools/documentation/check_docs_layout.py lines 22-26 (K_DOCS_ENTRIES) omits 'modules' and line 120 rejects anything in docs/agent/ that is not a dated folder, so a repository built to CLAUDE.md fails the checker.

Recommendation: Owner decides one shape (the skill and checker agree with each other; CLAUDE.md is the outlier), then CLAUDE.md, the skill and K_DOCS_ENTRIES are made to say the same thing in one commit.

Review: confirmed. claude/CLAUDE.md lines 33 and 37, skills/documentation/SKILL.md tree, check_docs_layout.py K_DOCS_ENTRIES (lines 22-27, no 'modules') and line 120 all read as cited; skills/multi-agent-work/SKILL.md lines 17 and 49 also use the work-folder form, so CLAUDE.md is the outlier. The recommendation (one owner decision, three files, one commit) is brick-shaped.

#### D3. [medium] Placement questions are ordered differently in the two sources

Evidence: claude/CLAUDE.md lines 42-44: module, agent, 'work with nothing open -> docs/archive/', then 'intent with an open phase -> docs/design/', then manual. skills/documentation/SKILL.md Placement: module, agent, design (question 3), then archive only for 'finished and untouched for 90 days' (question 4), then manual. A shipped design document less than 90 days old lands in archive by CLAUDE.md and stays in design by the skill.

Recommendation: Keep one ordering and one archive criterion (with or without the 90-day rule) and copy it into the other file.

Review: confirmed. CLAUDE.md lines 42-44 order archive before design with 'work with nothing open'; SKILL.md lines 40-44 order design before archive with the 90-day rule, and K_ARCHIVE_AFTER_DAYS = 90 in the checker sides with the skill.

#### D4. [medium] The changelog example in CLAUDE.md fails the repository's own changelog checker

Evidence: claude/CLAUDE.md line 47: '- 2026-08-28 — Fixed the star field's exposure (`star.vert`, `StarPass`).' has no scope. skills/documentation/SKILL.md requires '- <YYYY-MM-DD> — <scope>: <Past-tense verb> ...' and tools/documentation/check_changelog.py line 24 K_ENTRY_SHAPE requires '[a-z0-9_-]+: ' after the dash. CLAUDE.md lines 46-47 also describe the entry as 'the date, a past-tense verb, what changed, and where' with no scope.

Recommendation: Add the scope to the CLAUDE.md description and example ('render: Fixed ...').

Review: confirmed. CLAUDE.md line 47 example has no scope; K_ENTRY_SHAPE at check_changelog.py line 24 requires '[a-z0-9_-]+: ' after the dash, so the example fails rule_entry_shape.

#### D5. [medium] No backlog and no design record for a repository with open work

Evidence: docs/design/REMAINING_WORK.md does not exist. Open items are visible only elsewhere: tools/README.md lines 22-27 ('Not checked': @brief per symbol, Python imports across modules, past-tense verb, newest-first order) is a list of unbuilt checks living in a module README, and skills/documentation/SKILL.md says 'REMAINING_WORK.md is the only backlog. No TODO lists anywhere else'.

Recommendation: Create docs/design/REMAINING_WORK.md and move the four unbuilt checks there as backlog items; tools/README.md keeps a one-line statement of what the checkers cover.

Review: confirmed. docs/design/REMAINING_WORK.md is absent and tools/README.md lines 22-27 read as cited. The recommendation is weaker than the finding: those four lines state the checkers' limits, which are facts about the tools module (placement question 1), so they should stay in tools/README.md; only a decision to build them makes a backlog item.

#### D6. [medium] README front door has no link to the manual and no pointer to the changelog or version

Evidence: D:/Projects/sushiskills/README.md (75 lines) never mentions docs/, the changelog, the current release (tags v0.1.0, v0.1.1) or how a rule change lands beyond lines 67-70. skills/repository-layout/SKILL.md line 23 defines README.md as 'What the project is, one build line, a link to docs/README.md'.

Recommendation: After docs/README.md exists, add the link and move the install instructions (lines 48-65) to docs/getting_started/, leaving a short pointer.

Review: confirmed. README.md has no mention of docs/, the changelog or a version; repository-layout/SKILL.md line 22 (not 23) defines README.md as carrying a link to docs/README.md.

#### D7. [medium] README states that AGENTS.md and CLAUDE.md live at a Sushi repository root; this repository has neither

Evidence: README.md lines 64-65: 'Inside a Sushi Systems repository, `AGENTS.md` and `CLAUDE.md` live at the repository root, naming the skills the repository follows.' skills/repository-layout/SKILL.md lines 15 and 24 say the same. D:/Projects/sushiskills/ root holds only .gitattributes, .gitignore, LICENSE, README.md, claude/, docs/, skills/, third_party/, tools/. The only CLAUDE.md is claude/CLAUDE.md, the owner's global file, which is not a repository instruction file.

Recommendation: Add root AGENTS.md and CLAUDE.md naming the skills this repository follows, or state in README.md why the source repository is exempt.

Review: confirmed. README.md lines 64-65 and repository-layout/SKILL.md lines 15 and 24 read as cited; root listing has no AGENTS.md or CLAUDE.md, and git log shows neither was ever tracked at the root.

#### D8. [medium] Modules without their own README

Evidence: skills/ (24 folders) has no skills/README.md and claude/ has no claude/README.md; only tools/README.md and third_party/superpowers/README.md exist. The skill table that would be skills/README.md sits in the root README.md lines 15-40, and the facts about claude/CLAUDE.md (import line, per-OS path) sit in root README.md lines 55-59. Placement question 1: a fact about one module goes in that module's README.

Recommendation: Owner confirms whether skills/ and claude/ count as modules; if so add skills/README.md (the table, the SKILL.md front-matter contract, companion files such as humanizer's language files and research/) and claude/README.md, and shorten the root README.

Review: confirmed. No skills/README.md or claude/README.md; only tools/README.md and third_party/superpowers/README.md exist. Whether skills/ and claude/ are modules is an owner call, as the audit says.

#### D9. [medium] Changelog history does not cover the commits it claims to

Evidence: docs/archive/changelog/v0.1.0.md has 6 entries for 14 commits up to 9312f5c. No entry for 9f4f351 'feat(skills): add the shared discipline as atomic skills' (the initial skill set) or 910646b 'feat(skills): add the TypeScript code style'; line 5 says 'Added nine engineering discipline skills (`skills/`)' while 24 exist. In the working tree, claude/CLAUDE.md gained delegation rule 6 and the '1, 2, 5 and 6' evidence rule (git diff claude/CLAUDE.md) with no Unreleased entry, while CHANGELOG.md line 5 records only the skill folder.

Recommendation: Add a 'claude:' Unreleased entry for the CLAUDE.md change before committing. The archive is frozen, so the v0.1.0 gap is recorded as a known issue rather than edited.

Review: confirmed. v0.1.0.md has 6 entries; git rev-list --count v0.1.0 is 15 (14 plus the release commit). No entry covers 9f4f351 or 910646b. git diff claude/CLAUDE.md shows rule 6 and the '1, 2, 5 and 6' line with no 'claude:' Unreleased entry. The '24 exist' comparison is loose: line 5 records commit 6a2766c, which did add nine.

#### D10. [medium] check_docs_layout.py has no rule for a missing required document, so this repository's two-file docs/ passes it

Evidence: D:/Projects/sushiskills/tools/documentation/check_docs_layout.py lines 188-200 register eight rules; rule_docs_entries (lines 102-106) only rejects entries outside K_DOCS_ENTRIES and nothing requires docs/README.md, CONTRIBUTING.md, DOCUMENTATION_STYLE_GUIDE.md, reference/GLOSSARY.md, KNOWN_ISSUES.md, design/README.md or design/REMAINING_WORK.md to exist. No rule checks 'every document reachable from here' (skills/documentation/SKILL.md line 17). Read from the code, not run: docs/ here holds only 'reference' and 'archive', both allowed, so F1's gap is invisible to the checker. D:/Projects/sushiskills/tools/README.md lines 22-27 ('Not checked') do not list either limit.

Recommendation: Add one rule per concern (rule_required_entries, rule_reachable_from_index), each one function and one table row as project-tools prescribes, or list both under 'Not checked' in tools/README.md until the owner decides.

Review: found by review.

#### D11. [medium] tools/README.md claims module READMEs and links are checked; the rules cover a narrower set

Evidence: tools/README.md line 10 lists 'links, module READMEs'. rule_module_readmes (check_docs_layout.py lines 163-172) returns at once unless modules/<tier>/<module>/ exists, so a single-module repository (skills/repository-layout/SKILL.md lines 41-47) and this repository's skills/, claude/ and tools/ are never checked. rule_links (lines 146-160) walks live_documents(), which is docs/**/*.md only, so the root README.md and module READMEs are skipped, and backticked cited paths are never resolved although the skill says 'Every link and cited path resolves'.

Recommendation: State the real coverage in tools/README.md (links under docs/ only, READMEs under modules/<tier>/ only, cited paths unchecked), and let the owner decide whether to widen the rules.

Review: found by review.

#### D12. [medium] Installed skills are symlinks into a dirty working tree, and the README offers 'link or copy' without saying which state is published

Evidence: ls -la C:/Users/sushi/.claude/skills shows all 24 entries as symlinks to /d/Projects/sushiskills/skills/<name>, including storage-discipline (untracked, linked 2026-10-03). claude/CLAUDE.md rule 6 already cites that skill. README.md lines 50-53 say 'Link or copy each folder'; a machine that copies from a clone of main gets 23 skills and a CLAUDE.md with five delegation lines, while this machine runs 24 and six.

Recommendation: Commit the pending set (F11) and have the getting_started page name one installation method per tool, so every machine reads the same revision.

Review: found by review.

#### D13. [low] Archived release section was not moved unchanged

Evidence: docs/archive/changelog/v0.1.0.md line 1 is '# v0.1.0'. skills/documentation/SKILL.md: 'every older release section moves, unchanged, to docs/archive/changelog/vX.Y.Z.md' and the heading form is '## vX.Y.Z — YYYY-MM-DD'. The release date (tag commit 9312f5c, 2026-09-16) is lost from the file.

Recommendation: Owner rules whether the archive rule allows a one-time correction to '## v0.1.0 — 2026-09-16'; otherwise state in the skill what the archived file's heading is, since the current file and the rule disagree.

Review: confirmed. docs/archive/changelog/v0.1.0.md line 1 is '# v0.1.0'; tag v0.1.0 is 9312f5c dated 2026-09-16; the skill says the section moves unchanged under '## vX.Y.Z — YYYY-MM-DD'.

#### D14. [low] A changelog entry cites a path that is not in the repository history

Evidence: docs/reference/CHANGELOG.md line 5 cites `skills/storage-discipline`; git status shows '?? skills/storage-discipline/' and the README.md row (line 40), skills/sushiskills/SKILL.md row (line 65) and the changelog line are all uncommitted. On a fresh clone of main the skill named in claude/CLAUDE.md rule 6 does not exist.

Recommendation: Commit the skill, its README row, its map row, the CLAUDE.md change and the changelog lines together.

Review: confirmed. git status shows '?? skills/storage-discipline/' and the three rows naming it are uncommitted modifications; the path exists on disk, so it resolves in the working tree only.

#### D15. [low] project-tools understates what check_changelog.py enforces, and tools/README.md is the only accurate description

Evidence: skills/project-tools/SKILL.md check_changelog row: 'One line, 240 characters, one sentence, no nesting'. tools/documentation/check_changelog.py lines 112-123 also registers rule_entry_shape (headings and scope shape), rule_live_releases (older releases must be archived) and rule_cited_paths (five-place ceiling), as tools/README.md line 11 states. The skill's example signature 'rule_block_ceiling(lines) -> Iterator[Finding]' differs from the code, where rules yield Issue (tools/common/checker.py lines 25-31, 52).

Recommendation: Bring the skill's table row and example in line with the checker: list the six rules and use Issue.

Review: confirmed. project-tools/SKILL.md line 17 lists four properties; check_changelog.py lines 112-123 register six rules. SKILL.md line 38 uses 'lines: list[str]) -> Iterator[Finding]' while checker.py line 52 defines Rule as returning Iterator[Issue].

### Not checked

- Prose register (humanizer) of the 24 SKILL.md files and their companion files (humanizer/*.md, marketing-copy/*.md, research/*.md): only README.md, tools/README.md, skills/sushiskills, documentation, project-tools, and parts of versioning-and-release and repository-layout were read. In those I found no passage needing a rewrite.
- claude/CLAUDE.md was read in full only through the copy injected as global instructions plus lines 20-50 and the working-tree diff; the Planning and Delegation sections were not compared against skills/multi-agent-work/SKILL.md line by line.
- Whether every SKILL.md front matter description matches its body, and whether cross-references between skills (for example 'see commits') all name existing skills, beyond the README and sushiskills tables.
- Content of skills/storage-discipline/ (untracked) was not read.
- tools/documentation/check_source_comments.py and tools/layering/check_layering.py were not compared rule by rule against tools/README.md and the source-comments skill; only the suffix constants were looked at.
- third_party/superpowers was not reviewed beyond its README.md and skill count; its version 6.3.0 was not verified against upstream.
- No checker was run (read-only task forbids running project tools), so check_docs_layout.py and check_changelog.py output is not available; changelog length was measured with awk instead.
- Whether C:/Users/sushi/.claude/skills copies other than documentation match the repository (the 'synced' entry there was not inspected).
- Whether a release is due under versioning-and-release was only estimated (three Unreleased entries, last tag 2026-09-16, 30-day mark not yet reached on 2026-10-05).
- Licence text and licence headers: left to the licence dimension.

## Layout and hygiene

### Facts

- Top-level tree of D:/Projects/sushiskills: .gitattributes, .gitignore, LICENSE (Apache-2.0, 11558 bytes), README.md, claude/ (CLAUDE.md, the global instructions), docs/, skills/ (24 skill folders), third_party/superpowers/ (vendored MIT skill library 6.3.0), tools/ (four checkers plus common/).
- docs/ holds two files only: docs/reference/CHANGELOG.md and docs/archive/changelog/v0.1.0.md.
- git tracks 105 files; 20 commits on main; main is level with origin/main (0 ahead, 0 behind). Last commit f5dbf69, 2026-09-24.
- Remote: origin https://github.com/SushiSystems/SushiSkills.git. The name matches the product name in README.md line 1.
- Tags: v0.1.0 (9312f5c, 2026-09-16) and v0.1.1 (71d7f23, 2026-09-16), both annotated.
- Version numbers: none declared in any file. There is no pyproject.toml, package.json, CMakeLists.txt or sushi-module.toml. The only version carriers are the two tags and the changelog headings (live file: Unreleased and v0.1.1; archive: v0.1.0). Tags and headings agree.
- Unreleased holds three entries (storage-discipline 2026-10-03, claude 2026-09-24, marketing-copy 2026-09-17), all additions. By the versioning table the next release is v0.1.2 (patch, pre-1.0 feat). 19 days since the last tag, so the 30-day trigger has not fired.
- CI workflows: none. There is no .github directory.
- Checkers under tools/: documentation/check_source_comments.py (248 lines; rules file_header, block_ceiling, comment_runs, separators, history, no_date), documentation/check_docs_layout.py (203 lines; docs_entries, document_names, work_folders, status_lines, design_ceiling, links, module_readmes, archive_candidates), documentation/check_changelog.py (126 lines; entry_shape, live_releases, length, single_sentence, no_nesting, cited_paths), layering/check_layering.py (127 lines; declared_tiers, upward_includes, private_reach; K_TIER_ORDER is empty so it does nothing here), common/checker.py (107 lines, the shared runner).
- .gitignore is two lines: `__pycache__/` and `*.pyc`. .gitattributes sets `* text=auto eol=lf`, CRLF for bat/cmd/ps1, binary for png/jpg/pdf.
- git status: four modified tracked files (README.md +1, claude/CLAUDE.md +4/-2, docs/reference/CHANGELOG.md +1, skills/sushiskills/SKILL.md +1) and one untracked folder skills/storage-discipline/ (SKILL.md, 71 lines, 3747 bytes, dated 2026-10-03). All five belong to one change: adding the storage-discipline skill.
- No tracked binary, image, generated file, egg-info, imgui.ini, cmake discovery JSON or compiler probe header. Largest tracked file is third_party/superpowers/skills/writing-skills/anthropic-best-practices.md at 46 KB. The only generated content on disk is tools/common/__pycache__, which is ignored.
- Every folder under skills/ is symlinked from C:/Users/sushi/.claude/skills/ (24 links, contents identical), so the working tree, not the last commit, is what every repository runs on. C:/Users/sushi/.claude/skills/ also holds a non-link folder `synced`. C:/Users/sushi/.agents/skills does not exist.
- Sibling layouts seen: sushistack has cli/ contract/ dependencies/ docs/ gui/ tools/ and .github/workflows/{ci.yml,release.yml}; sushicore has pyproject.toml and sushicore.egg-info at its root and ci.yml, release.yml; sushiengine has ci.yml only. None uses the push.yml name the continuous-integration skill prescribes.

### Corrections from review

- F1 recommendation says a fresh clone gets 'a CLAUDE.md with four dispatch lines'. git show HEAD:claude/CLAUDE.md lists five numbered lines (1-5) under a sentence that says 'the same four lines'; the committed file contradicts itself, and the clone lacks only line 6 and the '1, 2, 5 and 6' evidence rule.
- F11 title says Apache-2.0 is hard-coded in 'six places'. The evidence it lists is nine files: LICENSE, README.md line 74, skills/source-comments/SKILL.md line 27, and six files under tools/ (common/__init__.py, common/checker.py, three under documentation/, layering/check_layering.py).
- F15 cites third_party/superpowers/skills/brainstorming/scripts/server.cjs as the writer of .superpowers/. The string does not appear in server.cjs; it is start-server.sh lines 9 and 117-121.
- F10 cites repository-layout/SKILL.md line 87 for 'It is not allowed'. That row is line 88; line 87 is the 'second CLI or script folder' row.
- Recomputed and correct: 105 tracked files, 20 commits, HEAD f5dbf69 2026-09-24, 24 skill folders, tags v0.1.0 -> 9312f5c and v0.1.1 -> 71d7f23 (both annotated, 2026-09-16), checker line counts 248/203/126/127/107, 19 days since the last tag, 24 symlinks plus 'synced' in ~/.claude/skills, sibling workflows ci.yml/release.yml (sushistack, sushicore) and ci.yml (sushiengine).

### Findings

#### L1. [high] The live rule set runs from an uncommitted working tree

Evidence: git status: `M README.md`, `M claude/CLAUDE.md`, `M docs/reference/CHANGELOG.md`, `M skills/sushiskills/SKILL.md`, `?? skills/storage-discipline/`. The untracked D:/Projects/sushiskills/skills/storage-discipline/SKILL.md (2026-10-03) is already linked at C:/Users/sushi/.claude/skills/storage-discipline, and C:/Users/sushi/.claude/CLAUDE.md imports the modified D:/Projects/sushiskills/claude/CLAUDE.md (line 6 of the delegation block and the `1, 2, 5 and 6` evidence rule exist only in the working copy). Nothing in git or on the remote holds this skill.

Recommendation: Commit the five paths as one change (`feat(storage-discipline): ...`), staged by path, before any other edit to this repository. A second machine cloning the remote today gets a CLAUDE.md with four dispatch lines and no storage skill.

Review: confirmed. git status shows the four modified files and untracked skills/storage-discipline/; ~/.claude/skills/storage-discipline is a symlink into the working tree and ~/.claude/CLAUDE.md imports claude/CLAUDE.md. One detail is wrong: the committed CLAUDE.md lists five dispatch lines under a sentence that says 'four' (see wrong_facts).

#### L2. [high] The dispatch block is defined twice, both 'verbatim', with different text

Evidence: D:/Projects/sushiskills/claude/CLAUDE.md lines 80-96: six lines; line 3 bans `se`, `cmake`, `ninja`, `ctest` outright; line 5 requires `clang -fsyntax-only`; line 6 is the scratchpad rule. D:/Projects/sushiskills/skills/multi-agent-work/SKILL.md lines 41-51: `Every dispatch opens with this block, verbatim` and gives five lines; line 1 drops `Engineer it once carefully...`; line 3 reads `Do not run the build system ... unless this task says so`; line 4 `Write only to the files listed below and to docs/agent/<work folder>/` has no counterpart in CLAUDE.md; no syntax-check line and no storage line. D:/Projects/sushiskills/skills/storage-discipline/SKILL.md lines 60-63 require a storage line in every dispatch, which the multi-agent-work block lacks.

Recommendation: Keep the block in one place. Either multi-agent-work holds the text and CLAUDE.md cites it, or the reverse; the other file says `see ...` and repeats nothing. Carry the file-set line (multi-agent-work line 4) into the surviving block, since CLAUDE.md lost it.

Review: confirmed. claude/CLAUDE.md lines 80-95 (six lines) against skills/multi-agent-work/SKILL.md lines 41-51 (five lines, different wording, file-set line 4, no syntax-check or storage line); storage-discipline lines 60-63 require the storage line. Recommendation is brick-shaped (one owner of the text, the other cites it).

#### L3. [high] CLAUDE.md and the documentation skill describe different docs/ trees, and the checker enforces the skill's

Evidence: CLAUDE.md line 33: `docs/getting_started/ architecture/ modules/ guides/ reference/`. skills/documentation/SKILL.md line 20 lists `getting_started/ architecture/ guides/` and line 34 says `No other folder under docs/`; tools/documentation/check_docs_layout.py lines 22-27 (K_DOCS_ENTRIES) has no `modules`, so a repository following CLAUDE.md fails rule_docs_entries. CLAUDE.md line 37: `docs/agent/specs|plans|reports`. Skill lines 28-29 and 58-60: `docs/agent/<YYYY_MM_DD>_<WORK_NAME>/` holding SPEC.md, PLAN.md, REPORT.md, enforced by K_WORK_FOLDER and K_WORK_FILES (check_docs_layout.py lines 29-30).

Recommendation: Owner decision: one tree. Then make CLAUDE.md, skills/documentation/SKILL.md and K_DOCS_ENTRIES/K_WORK_FOLDER say the same thing in one commit. Sibling repositories built to either version will need the same pass.

Review: confirmed. CLAUDE.md line 33 lists modules/ and line 37 specs|plans|reports; documentation/SKILL.md lines 20, 28-29, 34 and K_DOCS_ENTRIES, K_WORK_FILES, K_WORK_FOLDER in check_docs_layout.py (lines 22-30) have no modules/ and use dated work folders.

#### L4. [medium] Placement order and archive condition differ between CLAUDE.md and the documentation skill

Evidence: CLAUDE.md lines 42-44: module README, docs/agent, `work with nothing open → docs/archive/`, then `intent with an open phase → docs/design/`. skills/documentation/SKILL.md lines 40-44: module README, docs/agent, design (question 3), then archive (question 4) and only for work `finished and untouched for 90 days`. A shipped design document one week old goes to archive under CLAUDE.md and stays in design/ under the skill (lines 66-68).

Recommendation: Adopt the skill's wording (it is the one the checker's K_ARCHIVE_AFTER_DAYS = 90 implements) and rewrite CLAUDE.md lines 42-44 to match, or drop the placement list from CLAUDE.md and cite the skill.

Review: confirmed. CLAUDE.md lines 42-44 put archive before design with no age condition; documentation/SKILL.md lines 40-44 and 66-68 put design first and archive after 90 days; K_ARCHIVE_AFTER_DAYS = 90 is in the checker.

#### L5. [medium] CLAUDE.md's changelog example fails the repository's own changelog checker

Evidence: CLAUDE.md lines 46-47: entry is `the date, a past-tense verb, what changed, and where`, example `- 2026-08-28 — Fixed the star field's exposure (...)`. skills/documentation/SKILL.md line 100 requires `- <YYYY-MM-DD> — <scope>: <Past-tense verb> ...`, and tools/documentation/check_changelog.py line 24 (K_ENTRY_SHAPE) requires `[a-z0-9_-]+: ` after the dash. The CLAUDE.md example has no scope and would be reported by rule_entry_shape.

Recommendation: Add the scope to the CLAUDE.md sentence and example (`— render: Fixed ...`).

Review: confirmed. CLAUDE.md line 47 example has no scope; K_ENTRY_SHAPE in check_changelog.py line 24 requires '[a-z0-9_-]+: ' after the dash; documentation/SKILL.md line 100 states the scope.

#### L6. [medium] Model selection is stated two ways

Evidence: CLAUDE.md lines 97-105: every subagent on `opus`; only effort varies (low for implementers, medium for reviewers, high for architects after owner approval); `sonnet` and `fable` not used. skills/multi-agent-work/SKILL.md lines 59-66: implementation on a `Fast, capable model`, review and architecture on the `Strongest reasoning model`. The skill puts reviewers on the top tier; CLAUDE.md puts them at medium and reserves high for approved work.

Recommendation: Rewrite the skill's table in terms of effort on one model, or delete the table and cite CLAUDE.md. Keep `set on every dispatch` in one place.

Review: confirmed. CLAUDE.md lines 97-105 (one model, effort varies, reviewer at medium) against multi-agent-work/SKILL.md lines 59-66 (two model tiers, review on the strongest).

#### L7. [medium] No version source of truth

Evidence: skills/versioning-and-release/SKILL.md lines 12-22 name one source per stack (CMake, pyproject.toml, package.json) and state `The version lives in one place per repository`. This repository has none of the three files; v0.1.0 and v0.1.1 exist only as tags and changelog headings. The skill has no row for a repository without a build manifest.

Recommendation: Add a row to the skill for documentation-only repositories (source of truth: the latest `## vX.Y.Z` heading, checked against the tag) or add a one-line VERSION carrier; the owner picks. Have check_changelog.py compare the latest heading with `git describe --tags --abbrev=0`.

Review: confirmed. versioning-and-release/SKILL.md lines 12-23 name three manifest sources; the root has no CMakeLists.txt, pyproject.toml or package.json. The recommended tag comparison fits the existing shape (one rule function; check_docs_layout.py already calls git through subprocess), but it gives check_changelog.py a second input (git tags), so it should be its own rule and fail soft when git is absent.

#### L8. [medium] No CI, although the skill this repository publishes requires it

Evidence: No D:/Projects/sushiskills/.github directory. skills/continuous-integration/SKILL.md lines 13-16 require the four checkers on every push and pull request, on Windows and Linux, in `push.yml` and `release.yml`. tools/ here is the reference copy every repository takes (tools/README.md lines 3-4), and nothing runs it against this tree.

Recommendation: Add push.yml running the four checkers over this repository on both platforms. The repository has no project CLI, so the skill's rule 1 (`CI calls the project CLI and nothing else`, line 23) cannot be met as written; the skill needs an exception for repositories without a CLI, or this repository needs a thin one.

Review: confirmed. No .github directory; continuous-integration/SKILL.md lines 13-18 and 23-26 read as quoted; tools/README.md lines 3-4 call this the reference copy. The audit correctly flags that its own push.yml recommendation breaks rule 1 without a CLI or an exception.

#### L9. [medium] The repository does not carry the documentation architecture it prescribes

Evidence: Present: docs/reference/CHANGELOG.md, docs/archive/changelog/v0.1.0.md. Missing against CLAUDE.md lines 28-39 and skills/documentation/SKILL.md lines 15-31: docs/README.md, docs/CONTRIBUTING.md, docs/DOCUMENTATION_STYLE_GUIDE.md, docs/reference/GLOSSARY.md, docs/reference/KNOWN_ISSUES.md, docs/design/README.md, docs/design/REMAINING_WORK.md, docs/agent/, and getting_started/, architecture/, guides/. CLAUDE.md line 26 says `Every repository, whatever its size`. README.md has no link to docs/README.md, which skills/repository-layout/SKILL.md line 22 requires.

Recommendation: Build the skeleton as its own approved task (CLAUDE.md lines 56-57). Much of README.md lines 48-70 (installation, changing a rule) is manual content that belongs under docs/getting_started/ and docs/CONTRIBUTING.md.

Review: confirmed. find docs -type f returns only docs/reference/CHANGELOG.md and docs/archive/changelog/v0.1.0.md; README.md has no link to docs/README.md (repository-layout line 22).

#### L10. [medium] Root layout departs from repository-layout: no AGENTS.md or CLAUDE.md at the root, two top-level folders the table does not allow

Evidence: skills/repository-layout/SKILL.md lines 14-18 list the permitted root entries and line 24 requires root `AGENTS.md` and `CLAUDE.md`; line 87 says a new top-level folder `is not allowed`. The root here has `skills/` and `claude/`, neither in the table, and no AGENTS.md, CLAUDE.md, .editorconfig. README.md lines 64-65 repeat that AGENTS.md and CLAUDE.md `live at the repository root`, and line 61 tells other agents to reach skills/sushiskills/SKILL.md `from the repository's AGENTS.md`, a file this repository lacks. The only CLAUDE.md is claude/CLAUDE.md, which is the global file, not this repository's own.

Recommendation: Add root AGENTS.md and CLAUDE.md naming the skills this repository follows. Record `skills/` and `claude/` in repository-layout as the root entries of a skills repository, or state in the skill that this repository is the named exception; the owner decides which.

Review: confirmed. Root holds claude/ and skills/, no AGENTS.md, CLAUDE.md or .editorconfig; repository-layout lines 14-18, 24 match. The 'not allowed' row is line 88, not 87. README.md lines 61-65 read as quoted.

#### L11. [medium] Apache-2.0 is hard-coded in six places that a licence change must reach, and the dependency table rejects the licence class the owner now wants

Evidence: D:/Projects/sushiskills/LICENSE (Apache 2.0); README.md line 74 `Apache License 2.0`; skills/source-comments/SKILL.md line 27 `/* ... Apache-2.0 notice ... */` in the mandated file header; line 2 of each of the six files under tools/ (`# Licensed under the Apache License, Version 2.0. See LICENSE.`, e.g. tools/documentation/check_docs_layout.py line 2), which every repository copies whole. skills/dependencies/SKILL.md line 30: `Non-commercial, source-available, field-of-use limits | Rejected`, and line 33 applies the table to transitive dependencies. Once Sushi repositories carry a non-commercial licence, one Sushi repository depending on another (sushistack on sushicore) is rejected by that row as written.

Recommendation: When the licence is chosen: change LICENSE, README.md, the header template in source-comments, and the tools/ headers together, then let the sibling repositories copy tools/ again. Add a row to the dependencies table that accepts Sushi Systems' own licence for first-party repositories. Note that third_party/superpowers stays MIT with its own LICENSE.

Review: confirmed. LICENSE, README.md line 74, source-comments/SKILL.md line 27, and line 2 of all six files under tools/ carry Apache; dependencies/SKILL.md line 30 rejects non-commercial licences and line 33 extends that to transitive ones. The title's 'six places' undercounts: it is nine files (see wrong_facts).

#### L12. [medium] The CI workflow name the skill prescribes is used by no repository

Evidence: skills/continuous-integration/SKILL.md lines 25-26 require 'push.yml' and 'release.yml'. D:/Projects/sushistack/.github/workflows and D:/Projects/sushicore/.github/workflows hold ci.yml and release.yml; D:/Projects/sushiengine/.github/workflows holds ci.yml only. The audit records this under facts and raises no finding, while F8 recommends adding push.yml here, which would make sushiskills the one repository that differs from its three siblings.

Recommendation: Owner picks one name. Either change the skill to ci.yml, or rename the three sibling workflows; then add this repository's workflow under the chosen name. sushiengine also lacks release.yml against the same skill line.

Review: found by review.

#### L13. [medium] Vendored superpowers skills write to docs/ paths the documentation skill and its checker forbid

Evidence: third_party/superpowers/skills/brainstorming/SKILL.md lines 100 and 206 save specs to docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md; third_party/superpowers/skills/writing-plans/SKILL.md lines 18 and 157 save plans to docs/superpowers/plans/. skills/documentation/SKILL.md line 34 says 'No other folder under docs/', K_DOCS_ENTRIES (tools/documentation/check_docs_layout.py lines 22-27) has no 'superpowers', and K_DOCUMENT_NAME requires UPPER_SNAKE_CASE.md. README.md lines 44-46 cover this only with a general 'the skill above wins' sentence, and the superpowers skills are loaded in every session (they tell the agent they must be used before any creative work). The audit checked the vendored library for the worktree conflict only.

Recommendation: State the mapping in one place, skills/sushiskills/SKILL.md or skills/documentation/SKILL.md: a superpowers spec or plan is written as SPEC.md or PLAN.md in docs/agent/<YYYY_MM_DD>_<WORK_NAME>/. Do not patch the vendored copy; its README says 'Local patches: None'.

Review: found by review.

#### L14. [medium] The committed CLAUDE.md contradicts itself on the dispatch block

Evidence: git show HEAD:claude/CLAUDE.md line 80 says 'opens with the same four lines, verbatim' and then lists five numbered lines (1-5). The working copy fixes the count to six. This is what origin/main serves today, and the audit described it as 'four dispatch lines'.

Recommendation: Covered by committing the working tree (F1); record it there so the commit is not read as a pure addition. A checker rule that counts the numbered lines against the stated number would be over-engineering; one source for the block (F2) removes the count.

Review: found by review.

#### L15. [low] Subagent ban on the project CLI conflicts with skills that require checks through the CLI

Evidence: CLAUDE.md line 88-89 (dispatch line 3): `Do not start any process that runs se, cmake, ninja or ctest`. skills/testing/SKILL.md line 66: `Tests run through the project CLI only ... A claim that tests pass carries` its output; skills/sushiskills/SKILL.md lines 32-35: `Build, test and run through the repository's own CLI`; skills/versioning-and-release/SKILL.md lines 61-62: run the full suite through the CLI before a release. The CLAUDE.md line names `se`, sushiengine's CLI, in a block that is sent to subagents in every repository, including Python and TypeScript ones where `clang -fsyntax-only` and `shader_compiler.exe` (line 5) do not apply.

Recommendation: Word lines 3 and 5 by role rather than by sushiengine's tool names: `do not run the project CLI's build or test commands` and `syntax-check without building, with the checker the stack provides`. State in testing and versioning-and-release that the orchestrator or owner, not a worker, runs the suite.

Review: confirmed. CLAUDE.md lines 88-93 name se, clang and shader_compiler.exe; testing/SKILL.md line 66, sushiskills/SKILL.md lines 32-35 and versioning-and-release lines 63-64 require the CLI. The fix rewords the owner's verbatim dispatch lines, so it is an owner decision, which the audit does not say.

#### L16. [low] tools/README.md and the checker omit what project-tools promises; skills disagree on the worktree rule

Evidence: skills/project-tools/SKILL.md line 15 says check_source_comments.py enforces `Every rule in source-comments`; tools/README.md lines 24-27 list `every symbol carries a @brief` as not checked, and the checker has no rule for the licence block's first line (source-comments line 37). skills/git-workflow/SKILL.md lines 26-27 forbid `git worktree`, `git stash`, `git add -A` only `when another session may share the working tree`; skills/multi-agent-work/SKILL.md line 81 forbids them `unless the owner asks`; skills/commits/SKILL.md line 49 forbids `git add -A` `never`. README.md line 46 lets vendored third_party/superpowers/skills/using-git-worktrees stand with a general override clause only.

Recommendation: Change project-tools line 15 to name what the checker covers and point at tools/README.md for the gaps. Pick one wording for the stash/worktree/add -A rule and keep it in git-workflow; the other two skills cite it.

Review: confirmed. project-tools line 15 against tools/README.md lines 22-27; git-workflow lines 26-27, multi-agent-work line 81 and commits line 49 give three different conditions for the same ban. Two unrelated defects sit under one id; they should be two findings.

#### L17. [low] Three working copies have CRLF line endings against the repository's eol=lf rule

Evidence: `git diff --stat` prints `warning: in the working copy of 'README.md', CRLF will be replaced by LF the next time Git touches it`, and the same for claude/CLAUDE.md and docs/reference/CHANGELOG.md. .gitattributes line 1: `* text=auto eol=lf`. There is no .editorconfig, which skills/repository-layout/SKILL.md line 16 lists among the root files.

Recommendation: Add .editorconfig with `end_of_line = lf` and renormalise the three files in the commit from F1.

Review: confirmed. git diff --stat prints the CRLF warning for README.md, claude/CLAUDE.md and docs/reference/CHANGELOG.md; .gitattributes line 1 is '* text=auto eol=lf'; no .editorconfig.

#### L18. [low] .gitignore covers Python caches only

Evidence: D:/Projects/sushiskills/.gitignore holds `__pycache__/` and `*.pyc`. Nothing ignores editor and OS residue (.vscode/, .idea/, Thumbs.db, .DS_Store) or agent residue (.claude/settings.local.json, .superpowers/ which third_party/superpowers/skills/brainstorming/scripts/server.cjs writes session files into). None of these exist in the tree today; the working tree is otherwise clean.

Recommendation: Add those patterns so a stray file cannot be staged. The same baseline .gitignore should be the one every sibling repository starts from.

Review: confirmed. .gitignore is the two Python lines. The .superpowers/ path is written by third_party/superpowers/skills/brainstorming/scripts/start-server.sh (lines 117-121), not server.cjs. Low severity is right; none of the residue exists today.

### Not checked

- The four checkers were not run against this repository (the task forbids running project tools); whether tools/*.py and docs/ pass them is unverified.
- The bodies of the checkers were not read line by line; only their headers, K_ constants and rule names. Their SOLID shape and correctness were not reviewed.
- Skills read in full: sushiskills, storage-discipline, multi-agent-work, documentation, commits, git-workflow, repository-layout, project-tools, continuous-integration, versioning-and-release, humanizer SKILL.md. Read in part: source-comments (lines 1-80), dependencies (lines 1-60). Only grepped for keywords: api-stability, cpp-code-style, python-code-style, typescript-code-style, logging, testing, performance, debugging, file-formats, platform-portability, marketing-copy. Contradictions inside those eleven may exist and were not looked for.
- The humanizer and marketing-copy language and research files (16 files) were not read.
- third_party/superpowers was not compared against upstream 6.3.0 to confirm `copied unchanged`, and its 14 skills were not checked for conflicts with Sushi skills beyond the worktree case.
- CLAUDE.md lines 60-73 (source comments, honesty) and 108-125 (planning) were compared with the skills only for the points listed in the findings.
- The remote's state on GitHub (default branch, pushed tags, repository description, visibility) was not queried; only the local remote URL and the local tracking ref.
- C:/Users/sushi/.claude/skills/synced was seen but not opened.
- Sibling repositories were only listed at root level for comparison; their layouts are other agents' dimensions.
- Git history was not scanned for large or binary blobs removed in earlier commits.
