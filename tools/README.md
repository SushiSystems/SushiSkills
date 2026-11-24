# tools

This repository's side of the shared checkers, which run from the sushicore package with
`python -m sushicore.tools check .`:

| Path | Holds |
| --- | --- |
| `settings.py` | The settings the checkers read for this repository |
| `known_findings.toml` | The findings the checkers accept for now, each with its backlog ID |
| `hooks/pre-commit`, `hooks/commit-msg` | The git hooks; `python -m sushicore.tools install-hooks .` points git at them |

The repository's own tools:

| Path | Does | Runs from |
| --- | --- | --- |
| `tests/test_test_times_settings.py` | The Time table of the testing skill and `K_TEST_TIMES` agree | Repository root |
| `skills/check_skill_budget.py` | Every `SKILL.md` outside `third_party/`: its body, front matter left out, holds at most 800 words, or no more than its entry in `K_SKILL_WORD_CEILINGS`; an entry is lowered as its skill shrinks and removed once the skill fits the budget | Repository root |
