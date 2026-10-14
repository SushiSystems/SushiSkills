# Contributing

## Changing a rule

A rule changes here first, in its own skill, and every repository follows it from then on.

1. Edit the skill that holds the rule. If no skill holds it, add a folder; do not add a section
   to a skill about something else.
2. If a checker under `tools/` enforces the rule, change the checker and its test in the same
   commit.
3. Add one changelog line under `## Unreleased`, with the skill's folder name as its scope.
4. Run `python tools/check_all.py .`; see [`tools/README.md`](../tools/README.md).

Sibling repositories copy the shared tools after a checker changes, as "Shared and own tools" in
`skills/project-tools/SKILL.md` says.

A rule is stated in one file. Every other file that needs it names that file and stops there:
it never restates the rule, not even shortened. `check_docs_truth.py` reports a long paragraph
copied between skills; a rule said twice in other words is caught only by a reader, so before
each release a subagent reads `skills/`, `claude/` and this file for rules stated twice, and
each finding becomes a citation.

## Boundaries and defaults

Every rule is one of two kinds, and its text shows which.

- A **boundary** holds without exception. It is written as "never" or "always", and a checker
  enforces it when a checker can.
- A **default** carries three lines: **Rule**, **Why** and **Not when**. The "not when" line names
  the cases where following the rule costs more than it saves. A default without one is either
  a boundary or not yet thought through.

See the doctrine in [`skills/sushiskills/SKILL.md`](../skills/sushiskills/SKILL.md) for both kinds.

## Contributions from outside

Contributions from outside Sushi Systems are not accepted yet.
