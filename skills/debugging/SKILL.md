---
name: debugging
description: Use when a bug, crash, wrong image, wrong number or unexpected behaviour appears, when a failure looks impossible given the code, or when tempted to theorise about a cause without data, in a Sushi Systems repository.
---

# Debugging

Data before theory. A cause is found by measuring the running program, not by reading code until
a story fits.

## Order

1. **Check the known issues.** When a failure looks impossible given the code, look it up in
   `docs/reference/KNOWN_ISSUES.md` first. Some failures belong to a toolchain, a driver or a
   vendor library, not to this repository.
2. **Reproduce.** State the smallest input and steps that show it.
3. **Instrument.** Add one temporary readout that prints the values the next decision depends
   on, behind a single flag or in a single block, and hand the command to the owner to run when
   the program needs their machine or their eyes.
4. **Narrow.** Each readout halves the space of causes. Move it, do not multiply it.
5. **Fix at the root** with a regression test, following `testing`.
6. **Remove the instrumentation** in the same piece of work. No readout survives the fix.

## Temporary instrumentation

- Writes to standard error with a fixed, searchable prefix: `[DIAG <topic>]`.
- Prints values with units and frame or step numbers, one line per sample.
- Is the only uncommitted change while it exists, or lives in a commit that the fix removes.

## Known issues

A failure that turns out not to be this repository's fault gets an entry in
`docs/reference/KNOWN_ISSUES.md`: the symptom as seen, the real cause, how to recognise it, and
the workaround. One entry per cause.

## Red flags

- "It is probably the shader." → measure which stage the value goes wrong in.
- "Could you tell me what the panel shows?" asked five times in a row → ship one readout that
  prints everything needed at once.
- "I added a second workaround on top of the first." → find the root.
- "The diagnostics might be useful later." → remove them.
