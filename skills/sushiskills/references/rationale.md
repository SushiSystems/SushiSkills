# Why the doctrine holds

Read this to know why a rule in `../SKILL.md` holds. A purpose explains a rule and never grants
an exception to it: a case no rule foresaw goes to the owner.

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

## Purpose of the doctrine as a whole

One discipline for every repository, so that a person or an agent who knows one repository
knows them all. It minimises maintenance cost. Each rule set is its own skill, and its
description says when it loads. A hook repeats the boundaries and the red flags during long
sessions; see `claude/README.md`. Adding a CLI to a repository without one is the owner's decision.

## Fuller wording of two items

Boundary 2: every report names each SOLID breach and each unneeded dependency met in the work,
the ones it made, the ones it kept and the ones it only saw, with the file and what it costs. A
breach is never called a trade-off to make it sound chosen.

Default 3, "not when": a new file inside the task's module is the agent's; a new module, a
changed public signature or a new package is the owner's. Those wait for the owner, and the agent
says in one line what it needs and what it recommends.

Default 2, rule: never call the build, test or package tools behind the CLI, and never run a
program or a test from the build system (a test driver, a custom target, a post-build step). The
language skills name those tools. A repository with no CLI uses its own scripts, such as
`npm run`, and nothing else behind them.

Default 3, rule: do not wait for a run that cannot change the step, ask leave for what the task
already covers, or answer a fault with a plan. A red check is read, fixed and rerun at once, with
the run it supersedes cancelled.

Boundary 1, fuller: siblings that do the same kind of thing are shaped the same; code depends on
the abstraction it needs, never on a neighbour's internals; a dependency exists because the code
uses it, so a module, link, include or package the code does not need is removed, or reported
when removing it is the owner's decision.

Boundary 5, fuller: naming, internal structure, test shape and work order are the agent's.

Default 1, "not when": the set is closed by its meaning and small, such as the states of one
machine or a `std::variant` visited in one place.

Default 3, "not when": the step is one the owner reserves (a module boundary, a public interface,
an external dependency, deleting what you did not create) or one that cannot be undone (a push, a
release, a deletion). A new file inside the task's module is the agent's; a new module, a changed
public signature or a new package is the owner's.

Language: code, comments, documentation, commits and pull requests are in English unless the
owner says otherwise for a specific piece.
