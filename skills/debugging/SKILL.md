---
name: debugging
description: Use when a bug, crash, wrong image, wrong number or unexpected behaviour appears, when a failure looks impossible given the code, or when tempted to theorise about a cause without data, in a repository.
---

# Debugging

Data before theory: a cause is found by measuring the running program, not by reading code until
a story fits.

## Order

1. **Check the known issues.** When a failure looks impossible given the code, run
   `backlog list --kind issue` first; some failures belong to a toolchain, driver or vendor library.
2. **Reproduce** with the smallest input and steps.
3. **Instrument** with one temporary readout of the values the next decision depends on, behind
   one flag or in one block. Hand the command to the owner when the program needs their machine
   or eyes.
4. **Narrow.** Each readout halves the causes; move it, do not multiply it.
5. **Fix at the root** with a regression test, following `testing`.
6. **Remove the instrumentation** in the same piece of work; no readout survives the fix.

## Instrumentation

Writes to standard error with the prefix `[DIAG <topic>]`; prints values with units and frame or
step numbers, one line per sample; is the only uncommitted change while it exists, or lives in a
commit that the fix removes.

## Known issues

A failure that is not this repository's fault, or that it lives with and has a workaround for, is
a known issue: `backlog add issue`, one entry per cause, as `BACKLOG_FORMAT.md` in `documentation`
gives. A defect to fix with no workaround yet is `backlog add work`.

Red flags (a theory with no data, repeated questions, stacked workarounds): `references/red-flags.md`.
