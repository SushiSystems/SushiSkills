---
name: design
description: Use when asking what a module is meant to be, who owns a module or what a phase of a design says, before changing a module, when a decision is made, when a design topic is opened or extended, or when a phase starts or finishes, to read and write design topics through the repository's design commands, in a repository.
---

# Design

A design topic holds the intent of one subject: the ruling, its reason, the shape and the phases.
It is read and written through the repository's `design` commands. Its sections, status line and
phase table are in `DESIGN_FORMAT.md` of `documentation`; the work folders that carry out its
phases are in `AGENT_WORK.md`.

## State comes from the command

| Question | Command |
| --- | --- |
| What topics exist, and which phases are open? | `<cli> design list` |
| What does one topic say? | `<cli> design show <TOPIC>` |
| Which topic owns this module or path? | `<cli> design owner <path>` |
| Do two topics overlap? | `<cli> design overlap` |
| Is every topic well-formed? | `<cli> design check` |

The topic map in `docs/design/README.md` is generated. Reading it, or the git log, to learn what
is designed answers from a stale copy.

## The order of work

1. **Before changing a module,** run `design owner <path>`. The topic it names holds the intent the
   change must keep.
2. **A decision is made** while working: write it into that topic's Decision or Design section in
   the same commit as the work.
3. **A new subject** is opened with `design new`, which refuses a module another topic owns. A new
   idea about an existing topic is a page (`design page`) and a phase (`design phase`) of that
   topic, never a second topic.
4. **A phase moves** with `design phase-state`. The topic ships when its last phase is built or
   withdrawn.
   <!-- follows: phase-ships-topic -->
5. **Work that carries out a phase** says so in its work folder's `Implements` line.
6. **The status line** says where the document stands and never how it got there.

## Red flags

- "I will read `docs/design/` to see what is designed." → `design list` or `design show`.
- "This topic is slightly different, so it gets its own document." → extend the owner of the module.
- "I will write the topic's frame by hand." → `design new`, `design page`, `design phase`.
- "I will change the phase table to match what I built." → `design phase-state`.
- "The decision is in the commit message." → in the topic, in the same commit.
