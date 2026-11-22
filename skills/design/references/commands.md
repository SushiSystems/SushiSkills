# Design commands

Read when you need the command for a design question.

A design topic holds the intent of one subject: the ruling, its reason, the shape and the
phases. Its sections, status line and phase table are in `DESIGN_FORMAT.md` of `documentation`;
the work folders that carry out its phases are in `AGENT_WORK.md`.

`<cli>` is the repository's CLI. A repository with none runs the module form of the same
commands, named by the tooling role.

| Question | Command |
| --- | --- |
| What topics exist, and which phases are open? | `<cli> design list` |
| What does one topic say? | `<cli> design show <TOPIC>` |
| Which topic owns this module or path? | `<cli> design owner <path>` |
| Do two topics overlap? | `<cli> design overlap` |
| Is every topic well-formed? | `<cli> design check` |

The topic map in `docs/design/README.md` is generated. Reading it, or the git log, to learn what
is designed answers from a stale copy.
