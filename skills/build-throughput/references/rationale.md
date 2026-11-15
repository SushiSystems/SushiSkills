# Build throughput: rationale

Why each rule in [`../SKILL.md`](../SKILL.md) exists. Read this when a case is not covered there,
or when a rule seems to cost more than it saves. The rules themselves live only in `SKILL.md`.

## Why the setup is engineered

A build is run thousands of times for every time its setup is designed, so the setup is
engineered once, carefully, and measured. A build that spills to the page file, or is stopped
for memory, is slower than one that ran fewer jobs.

## Boundaries

- **One tree per configuration.** Switching configurations never recompiles a tree, and never
  leaves one half-built under the other's flags.
- **Memory decides parallelism.** A constant tuned on a quiet machine runs out of memory on a
  busy one.
- **A build change carries its numbers.** A change made to build faster or lighter is a
  performance claim.
- **A public dependency.** A public edge hands its include directories to every module above,
  transitively. A change to the lower module's headers then recompiles all of them, and the
  first build after the edge lands recompiles most of the tree.
- **Build once.** A design that adds a million lines changes nothing in this rule. An error costs
  the same to fix whenever it is found, and each build in the middle costs a full compile and
  link, so a build run early is paid for again by every later one.

## Defaults

- **Measure first.** The edge that costs the most is rarely the one that looks heavy, and every
  other decision is sized from these numbers. `-ftime-trace` or the compiler's equivalent gives
  the time traces.
- **Admission by measured peak.** Units of one kind differ by a factor of three or more in
  memory, so any fixed job count or pool depth is set for the worst unit and idles the machine
  the rest of the time. After the passing window the queue drains, so no unit is starved.
- **Heavy code compiled once.** A header-only body is compiled, for every target, in every unit
  that uses it; a test file then costs minutes and gigabytes.
- **Debug information sized to its use.** Full debug information multiplies object size,
  compile memory and link time on template-heavy code.
- **Debug links what Release links.** The libraries below a repository are consumed as Release
  packages; a debug C runtime would need a debug build of the whole stack beneath it and would
  mismatch the packages' heaps. Memory errors are the sanitizer tree's job.
- **A compiler cache.** Branch switches, reconfigures and clean builds then pay only for what
  changed; a wrong hit on a bundled object is a defect at run time that no build step reports.
- **Batches for test targets.** Each test file reparses the test framework and the headers it
  tests; batching removes most of that.
- **Secondary products share the tree.** A second tree recompiles every library for nothing and
  doubles the disk the trees take.
- **The platform's own costs.** The scanner opens every object and executable the build writes.

## More red flags

- "Full debug information costs nothing." → measure its memory and link time first.
- "Release is the default because that is what ships." → Debug is the default; Release ships.
