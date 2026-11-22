# Build throughput: detail of the boundaries

What the boundaries of [`../SKILL.md`](../SKILL.md) leave open. `SKILL.md` holds the rules; read
this when the short form leaves a case open. The defaults are in [defaults.md](defaults.md), the
reasons in [rationale.md](rationale.md).

## Boundaries

1. Each execution lane or platform has its own build directory beside each configuration. The CLI
   refuses to configure an existing tree with another build type or other compile flags.
2. The plain build command builds the development configuration. `versioning-and-release` and
   `performance` build Release.
3. What runs at once is decided from the peaks measured on earlier builds and the memory free when
   the build starts.
4. The measuring rule of `performance` applies: same tree and machine, before and after.
5. Every knob is a CLI option or a machine-local CLI setting.
6. The shared tooling library supplies `build_tree`, `build_admission`, `build_gate` and
   `build_report`; a CLI built on it keeps no copy of its own.
7. A public header needs the whole type when it holds it by value or as a member, derives from it
   or uses it in an inline body. A type it only names by reference or pointer is forward-declared
   there; a caller that builds such an argument includes and links it itself.
8. The size of the piece of work changes nothing. Structural build errors are fixed at the single
   build like any other.
9. A single permission lapses after its run. A standing one lasts until revoked.

## Red flags

- "A quick build now will catch a mistake early." / "This module is done, so I build it." /
  "The build is green, so I test this part now." → boundary 8.
- "I will set `-j` to what worked last time." → admission by measured peak.
- "I will switch this tree to Release for one measurement." → the Release tree.
- "The test needs the template set, so the test compiles it." → the module compiles it.
- "The cache makes it faster, so bundled objects go in too." → the trial first.
- "The header names its type, so the dependency is public." → forward-declare; keep it private.
