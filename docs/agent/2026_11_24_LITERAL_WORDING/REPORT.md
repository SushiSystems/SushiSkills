# Literal wording: report

**Status:** Every job A0 to A9 and the reviews R1 and R2 ran; three rounds of fixes followed. `check_all.py` is clean and every SKILL.md is at or under 2500 bytes. Open items are listed below.

## What was built

- Every figure of speech in the skills, `claude/` and `sushisystems/` is replaced by the literal rule
  (plan decisions D1 to D5). SOLID has a definition, a correct example and a violation with its fix
  for each of its five principles in `skills/sushiskills/references/solid.md`.
- `red-flags.md` became `excuses.md` in five skills, and `licences-and-flags.md` and
  `tables-and-flags.md` became `licences-and-excuses.md` and `tables-and-excuses.md`.
- The session hook prints the doctrine, `solid.md`, the skill map, the excuses and the storage skill
  verbatim (12 422 bytes); the prompt hook is one line of 408 bytes (RW-73).
- `storage-discipline` forbids notes, plans, summaries and tool caches in a tree, makes a download
  of any size wait for the owner, and caps the scratchpad at 20 MB and a file at 1 MB. `settings.json`
  sets `PYTHONDONTWRITEBYTECODE=1` and `PYTEST_ADDOPTS=-p no:cacheprovider`.

## Defects found and fixed on the way

- Workers shortened rules to meet the byte limit and dropped words (`SKILL.md` default 2 lost the ban
  on running a program or test from the build system; `module-install` boundary 3 lost "on a clean
  machine"). Both are restored.
- `solid.md` showed dependency inversion with a concrete dataclass; it now uses a `Protocol`.
- Nine `SKILL.md` files were over 2500 bytes after round 1; all fit now.
- The `check_agnostic.py` checker caught a Sushi product name in a doctrine example.

## Deviations of the workers

- Rule 11 (compare each change with HEAD): A1, A2, A5, A6, A7 and A8 first reported that they did
  not; after a return each ran `git diff -U0` against HEAD, except A7, whose second report restates
  the comparison for four rules only. R1 compared the changes independently.
- Rule 1 (skills invoked): A1 invoked two of five, A2 and A5 three, A6 three, A8 four at the start
  and `documentation` later, A3 four after its edits. No finding of R1 traces to a missing skill.
- Rule 12: A5 and A7 ran a recursive `grep` from a shell; both reported it.

## Open

- RW-74: the shared tools of SushiCore keep `rung` and "one home" (`summarize_dispatches.py`,
  `check_docs_facts.py`, `facts.py`, `tools/README.md`, `test_check_docs_truth.py`).
- RW-71: no fixed task set yet measures whether sessions follow the rules. RW-72 waits for the
  owner: a `PreToolUse` hook that blocks writes outside the repository and scratchpad.
- Read by the owner: `build-throughput` boundary 1 says "CI job" for what HEAD called "execution
  lane", which is A5's reading; "pins", "folded in", "sibling", "front", "quarantined", the
  Turkish `tik` and `imza`, and the renamed tier label `Hafif küfür` were kept as terms or renamed
  on the worker's judgement.
- R2 reviewed rounds 2 and the A9 edits; round 3 fixed its findings and nobody reviewed round 3.
- `unlinked-cleanup` says an interface with one implementation "is replaced by that implementation, or asked about"; HEAD said "folded in", and A7 chose the reading.
- Lines over 100 columns that were already over it at HEAD remain in `INTERFACE.md`, `AGENT_WORK.md` and `manual.md`.

## Dispatches

dispatch: A0 core doctrine — opus low, 51 turns, passed after 1 return, rung 4
dispatch: A1 testing group — sonnet medium, 87 turns, passed after 1 return, rung 3
dispatch: A2 documentation group — sonnet medium, 133 turns, passed after 3 returns, rung 3
dispatch: A3 humanizer English — sonnet medium, 127 turns, passed after 2 returns, rung 3
dispatch: A4 humanizer Turkish — sonnet medium, 24 turns, passed, rung 3
dispatch: A5 layout and build group — sonnet medium, 108 turns, passed after 2 returns, rung 3
dispatch: A6 logging and routing group — sonnet medium, 105 turns, passed after 2 returns, rung 3
dispatch: A7 language styles group — sonnet medium, 213 turns, passed after 2 returns, rung 3
dispatch: A8 remaining skills — sonnet medium, 103 turns, passed after 2 returns, rung 3
dispatch: R1 review of the diff — opus low, 31 turns, passed, rung 4
dispatch: A9 last figures of speech — haiku high, 40 turns, passed, rung 2
dispatch: R2 review of the fix rounds — opus low, 26 turns, passed, rung 4
