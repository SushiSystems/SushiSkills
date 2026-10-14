# Contributing

## Changing a rule

A rule changes here first, in its own skill, and every repository follows it from then on.

1. Edit the skill that holds the rule. If no skill holds it, add a folder; do not add a section
   to a skill about something else.
2. If a checker under `tools/` enforces the rule, change the checker and its test in the same
   commit.
3. Add one changelog line under `## Unreleased`, with the skill's folder name as its scope.
4. Run the five checkers and the tests; see [`tools/README.md`](../tools/README.md).

Sibling repositories copy `tools/` whole after a checker changes.

A rule is stated in one file. `claude/CLAUDE.md` and a skill never restate each other; the one
that does not hold the rule names the one that does.

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
