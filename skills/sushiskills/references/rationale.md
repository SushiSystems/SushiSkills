# Why the doctrine holds

Read this when a case is one a rule in `../SKILL.md` did not foresee and you must judge it by
the rule's purpose.

## The whole doctrine

Every rule exists because its absence made a repository more expensive to change. Maintenance
cost is the thing being minimised.

## Boundary 4: maintainability before performance

A wasted cycle is a real cost, in money and in energy; a hack that saves one is a larger one.

## Default 1: grow without reshaping

A switch over kinds that every new kind must extend is the edit that spreads.

In the "not when" case, a closed and small set such as the states of one machine or a
`std::variant` visited in one place, a switch is clearer and faster, and an interface with a
factory around it is a cost with no return.

## Default 2: the CLI is the only door

Only the CLI sets up the runtime search path, so a binary launched any other way fails to find
its DLLs or shared objects.

## Default 3: act on the known step

Precision comes from the check that follows an action, which a test, a hook or CI supplies.
Waiting before the action adds hours and no information.
