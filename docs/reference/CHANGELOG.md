# Changelog

## Unreleased

- 2026-10-08 — repository-layout: Added the Unity tree, the feature assembly rules, the large-file folder and PascalCase names (`skills/repository-layout/UNITY.md`, `skills/repository-layout/SKILL.md`).
- 2026-10-08 — model-routing: Named Haiku 5.5 as the haiku seat and marked the effort on Haiku as unverified (`skills/model-routing/SKILL.md`).
- 2026-10-08 — model-routing: Added the skill that routes each session seat and dispatch to a model and an effort on the 5.5 stack, with the escalation ladder and the report line (`skills/model-routing/SKILL.md`).
- 2026-10-08 — claude: Replaced the Opus-everywhere rule with the owner's limits and a citation of `model-routing` (`claude/CLAUDE.md`).
- 2026-10-08 — multi-agent-work: Pointed model choice at `model-routing` (`skills/multi-agent-work/SKILL.md`, `skills/sushiskills/SKILL.md`, `skills/README.md`).
- 2026-10-07 — documentation: Named `docs/publish.toml` in the docs tree and accepted it in the layout checker (`skills/documentation/SKILL.md`, `check_docs_layout.py`, `K_DOCS_ENTRIES`).
- 2026-10-07 — licence: Named Mustafa Garip and Sushi Systems as the copyright holders in the licence and notice files (`LICENSE`, `NOTICE.md`).
- 2026-10-06 — licence: Restored the three-section license box and named both holders in the copyright line of every source file (`tools/licensing/write_license_block.py`, `tools/documentation/check_source_comments.py`).
- 2026-10-05 — tools: Stopped reading a `#` line inside a Python string literal as a comment (`check_source_comments.py`, `_python_comment_indexes`).
- 2026-10-05 — tools: Covered files that are staged and not yet committed in the license block writer (`write_license_block.py`).
- 2026-10-05 — tools: Covered configure templates, include fragments and indented old boxes in the license block writer, and skipped tracked files that are deleted (`write_license_block.py`).
- 2026-10-05 — tools: Kept a ported file's upstream lines when the writer runs again without naming them (`write_license_block.py`, `Header.kept_rows`).
- 2026-10-05 — tools: Added the writer that puts the license block into every tracked source file (`tools/licensing/write_license_block.py`, `skills/project-tools/SKILL.md`, `skills/source-comments/SKILL.md`).
- 2026-10-05 — tools: Rejected foreign licence lines in the license block, read byte order marks and encoding lines, and kept reachability inside the manual (`rule_license_block`, `_relative_links`, `_reachable`).
- 2026-10-05 — multi-agent-work: Moved report acceptance to the global instructions and said where a wave worker's report goes (`skills/multi-agent-work/SKILL.md`, `skills/storage-discipline/SKILL.md`).
- 2026-10-05 — documentation: Named the required documents and exempted work folders and the archive from index reachability (`skills/documentation/SKILL.md`).
- 2026-10-05 — licence: Named v0.2.0 as the first version under the new licence and pointed the commercial page at the licence text (`README.md`, `NOTICE.md`, `COMMERCIAL.md`).
- 2026-10-05 — ci: Added the workflow that runs the four checkers and the checker tests on Windows and Linux (`.github/workflows/ci.yml`).
- 2026-10-05 — marketing-copy: Named the licence wording copy must use and removed the open source claim from the examples (`skills/marketing-copy/SKILL.md`, `english.md`).
- 2026-10-05 — docs: Built the documentation skeleton and moved install and rule-change text out of the front door (`docs/README.md`, `docs/getting_started/INSTALL.md`, `skills/README.md`, `AGENTS.md`).
- 2026-10-05 — continuous-integration: Named the push workflow `ci.yml` and allowed direct checker calls in a repository without a CLI (`skills/continuous-integration/SKILL.md`).
- 2026-10-05 — versioning-and-release: Gave a repository without a build manifest its version source (`skills/versioning-and-release/SKILL.md`).
- 2026-10-05 — tools: Added the required-document and reachability rules to the docs layout checker (`check_docs_layout.py`, `rule_required_entries`, `rule_reachable_from_index`, `skills/project-tools/SKILL.md`).
- 2026-10-05 — licence: Moved the repository from Apache-2.0 to PolyForm Noncommercial 1.0.0 (`LICENSE`, `COMMERCIAL.md`, `NOTICE.md`, `README.md`).
- 2026-10-05 — dependencies: Accepted first-party repositories and added the ported code and notices rules (`skills/dependencies/SKILL.md`, `skills/repository-layout/SKILL.md`).
- 2026-10-05 — source-comments: Replaced the Apache license block with the PolyForm Noncommercial block and added the rule that checks it (`skills/source-comments/SKILL.md`, `check_source_comments.py`, `rule_license_block`).
- 2026-10-05 — claude: Reduced the documentation, source comment and planning sections to citations of their skills and added the file-set line to the dispatch block (`claude/CLAUDE.md`).
- 2026-10-05 — multi-agent-work: Removed the second dispatch block and the model table in favour of the global instructions (`skills/multi-agent-work/SKILL.md`).
- 2026-10-05 — sushiskills: Mapped superpowers specs and plans onto the work folder (`skills/sushiskills/SKILL.md`).
- 2026-10-03 — claude: Added the scratch rule as the sixth dispatch line and to the report evidence rule (`claude/CLAUDE.md`).
- 2026-10-03 — storage-discipline: Added the skill that caps agent scratch space and bans binaries and copies in it (`skills/storage-discipline`).
- 2026-09-24 — claude: Added the global Claude Code instructions (`claude/CLAUDE.md`).
- 2026-09-17 — marketing-copy: Added the skill banning AI-style marketing copy, with English and Turkish files (`skills/marketing-copy`).

## v0.1.1 — 2026-09-16

- 2026-09-16 — humanizer: Renamed the language files to `generic_english.md` and `generic_turkish.md`.
- 2026-09-16 — humanizer: Added the `plain_english`, `hood_english` and `hood_turkish` registers (`skills/humanizer`).
