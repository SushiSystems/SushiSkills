# Contributing

## Changing a rule

A rule changes here first, in its own skill, and every repository follows it from then on.

1. Edit the skill that holds the rule. If no skill holds it, add a folder; do not add a section
   to a skill about something else.
2. If a checker under `tools/` enforces the rule, change the checker and its test in the same
   commit.
3. Add one changelog line under `## Unreleased`, with the skill's folder name as its scope.
4. Run the four checkers and the tests; see [`tools/README.md`](../tools/README.md).

Sibling repositories copy `tools/` whole after a checker changes.

A rule is stated in one file. `claude/CLAUDE.md` and a skill never restate each other; the one
that does not hold the rule names the one that does.

## Contributions from outside

Contributions from outside Sushi Systems are not accepted yet.
