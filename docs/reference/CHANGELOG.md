# Changelog

## Unreleased

- 2026-10-05 — docs: Built the documentation skeleton and moved install and rule-change text out of the front door (`docs/README.md`, `docs/getting_started/INSTALL.md`, `skills/README.md`, `AGENTS.md`).
- 2026-10-05 — continuous-integration: Named the push workflow `ci.yml` and allowed direct checker calls in a repository without a CLI (`skills/continuous-integration/SKILL.md`).
- 2026-10-05 — versioning-and-release: Gave a repository without a build manifest its version source (`skills/versioning-and-release/SKILL.md`).
- 2026-10-05 — tools: Added the required-document and reachability rules to the docs layout checker (`check_docs_layout.py`, `rule_required_entries`, `rule_reachable_from_index`).
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
