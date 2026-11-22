# Why the doctrine holds

Read this to know why a rule in `../SKILL.md` holds. A purpose explains a rule and never grants
an exception to it.

## The whole doctrine

Every rule exists because its absence made a repository more expensive to change. Maintenance
cost is the thing being minimised.

## Boundary 4: maintainability before performance

Engineer it once carefully; run it a thousand times cheaply. A wasted cycle is a real cost, in
money and in energy; a hack that saves one is a larger one.

## Default 1: grow without reshaping

A new kind then adds a file, not edits. A switch over kinds that every new kind must extend is
the edit that spreads.

In the "not when" case, a closed and small set such as the states of one machine or a
`std::variant` visited in one place, a switch is clearer and faster, and an interface with a
factory around it is a cost with no return.

## Default 2: the CLI is the only door

Only the CLI sets up the runtime search path, so a binary launched any other way fails to find
its DLLs or shared objects. The language skills name the tools behind the CLI.

## Default 3: act on the known step

Precision comes from the check that follows an action, which a test, a hook or CI supplies.
Waiting before the action adds hours and no information.

## Purpose of the doctrine as a whole

One discipline for every repository, so that a person or an agent who knows one repository
knows them all. It minimises maintenance cost. Each rule set is its own skill, and its
description says when it loads. A hook repeats the boundaries and the red flags during long
sessions; see `claude/README.md`.
