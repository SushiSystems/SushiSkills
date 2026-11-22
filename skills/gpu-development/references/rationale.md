# GPU development: why each rule holds, and red flags

Read this when a rule looks wrong for a case it did not foresee, or a thought sounds like a red
flag. The rules are in `../SKILL.md`.

## Why

- **Device code linked once per process.** A device link (bitcode link, post-link, device code
  generation, assembler) is the cost of a compile, and a static archive repeats it in every
  executable that links it.
- **Development builds target the machine they run on.** Each extra target is another full device
  pass in every device unit and every device link, for code the developer cannot run.
- **Device code stays optimised.** Unoptimised device code makes the tests that exercise it
  unusable.
- **A kernel is compiled where it is owned.** A header-only kernel is compiled, for every device
  target, in every unit that launches it.
- **A bundled object enters the cache after a trial.** A wrong hit is a missing kernel at run time
  that no build step reports.
- **Heavy device units are not batched.** The memory peak of a device unit grows with the batch.

## Red flags

- "The shared library linked in seconds, so the device link is cheap." → count its device images:
  a device driver that never sees the archives (`/WHOLEARCHIVE` passed through `-Xlinker`) links
  an empty device image, and every kernel is missing at run time.
- "The cache makes it faster, so device objects go in too." → the trial first.
- "No GPU here, so the test counts as passing." → skipped.
