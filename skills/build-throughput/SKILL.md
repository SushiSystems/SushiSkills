---
name: build-throughput
description: Use when choosing a build configuration or a build tree, changing how a repository compiles or links (job counts, pools, caches, precompiled headers, unity batches, device targets, optimisation or debug-information levels), when a build runs out of memory or takes too long, or when deciding where heavy code such as GPU kernels is compiled, in a Sushi Systems repository.
---

# Build throughput

A build is run thousands of times for every time its setup is designed, so the setup is
engineered once, carefully, and measured. The machine it is engineered for is the development
machine as it is: a fixed amount of memory shared with everything else running, and a fixed
number of hardware threads. A build that spills to the page file, or is stopped for memory, is
slower than one that ran fewer jobs.

## Boundaries

1. **One tree per configuration.** Debug, RelWithDebInfo and Release each have their own build
   directory, and so does each execution lane or platform. A tree's configuration is fixed when it
   is created; the CLI refuses to configure an existing tree with another build type or another
   set of compile flags. Switching configurations never recompiles a tree, and never leaves one
   half-built under the other's flags.
2. **Debug is the default; Release is built for releases.** The CLI's plain build command builds
   the development configuration. Release is built by the release procedure
   (`versioning-and-release`) and for performance measurement (`performance`, which measures in
   the build type that ships). Nothing else defaults to it.
3. **Memory decides parallelism.** No build is allowed to push free memory under a reserve the
   repository names, 1.5 GB unless it names another. What runs at once is decided from measured
   peaks and the memory free when the build starts, never from a constant tuned on a quiet
   machine.
4. **A build change carries its numbers.** A change made to build faster or lighter is a
   performance claim and follows the measuring rule of `performance`: the same tree, the same
   machine, before and after, wall time and peak memory.
5. **The CLI is the only door.** Every knob below is a CLI option or a machine-local CLI
   setting, never a command typed at the build system (`sushiskills`, default 2).

## Defaults

### Measure first

**Rule:** the CLI can report a build: per kind of edge (host compile, device compile, host link,
device link) the count, the total and longest wall time and the peak working set, the lowest free
memory of the run, and the slowest edges. Time traces (`-ftime-trace` or the compiler's
equivalent) are taken on the slowest units before any header or template is trimmed.
**Why:** the edge that costs the most is rarely the one that looks heavy, and every decision
below is sized from these numbers.
**Not when:** a repository whose full build takes under two minutes.

### Admission by measured peak

**Rule:** the job count is the hardware threads, and every compile and link runs through a
launcher that admits it only when its expected peak, added to the peaks reserved by the edges
already running, fits in the memory free at the start of the build less the reserve. The
expected peak is the one measured for that unit on its last build, or the largest of its kind for
a unit not seen before. Edges are admitted in arrival order, with a short window in which a
lighter edge may pass a waiting heavy one; after it the queue drains, so no unit is starved.
**Why:** units of one kind differ by a factor of three or more in memory, so any fixed job count
or pool depth is set for the worst unit and idles the machine the rest of the time, and a count
tuned on a quiet machine runs out of memory on a busy one. Per-kind pools are the fallback where
no launcher can be set.
**Not when:** every unit peaks within a factor of two of the others and the build always fits.

### Heavy code compiled once, where it is owned

**Rule:** a kernel, a large template instantiation set or any unit that needs a second
compilation pass is instantiated in the module that owns it, for the types it supports, and
exposed through plain host functions. Its consumers, tests above all, include declarations, not
the kernel's body.
**Why:** a header-only kernel is compiled, for every device target, in every unit that launches
it; a test file then costs minutes and gigabytes.
**Not when:** the kernel is a template over a user's type that the module cannot list.

### Device code linked once per process

**Rule:** code that needs a device link lives in a shared library, so each executable links an
import library instead of repeating the device link over the same code.
**Why:** a device link (bitcode link, post-link, device code generation, assembler) is the cost
of a compile, and a static archive repeats it in every executable that links it.
**Not when:** one executable links the archive.

### Development builds target the machine they run on

**Rule:** a development tree compiles device code for the device architectures of the machine
building it; the package and CI lanes compile every architecture the product ships to.
**Why:** each extra target is another full device pass in every device unit and every device
link, for code the developer cannot run.
**Not when:** the tests select a device of another kind on that machine.

### Debug information sized to its use

**Rule:** the Debug configuration compiles host code without optimisation and with debug
information at the level the repository measured as the best trade between build time, memory,
disk and debugging; device code stays optimised in every configuration. RelWithDebInfo carries
full debug information on optimised code.
**Why:** full debug information multiplies object size, compile memory and link time on
template-heavy code; unoptimised device code makes the tests that exercise it unusable.
**Not when:** a debugging session needs variable-level information on a module; that module's
debugger build is its own tree.

### A compiler cache for units that are deterministic

**Rule:** host units compile through a compiler cache inside the build directory, capped in size
and keyed on the compiler's content. A unit whose object bundles several outputs, such as host
and device slices, enters the cache only after a trial shows two cached builds produce identical
slices.
**Why:** branch switches, reconfigures and clean builds then pay for what changed; a wrong hit on
a bundled object is a missing kernel at run time that no build step reports.
**Not when:** the repository has no generated or repeated builds to hit.

### Batches for test targets

**Rule:** host-only test targets compile in unity batches of about eight files; a name clash in
an anonymous namespace is fixed, not excluded.
**Why:** each test file reparses the test framework and the headers it tests; batching removes
most of that.
**Not when:** the units are heavy device units, whose memory peak grows with the batch.

### Secondary products share the engine's tree

**Rule:** an editor, a player or a tool whose option only adds targets is built inside the tree
that already compiled the libraries it links.
**Why:** a second tree recompiles every library for nothing and doubles the disk the trees take.
**Not when:** the product needs different compile flags; then it is another configuration,
boundary 1.

### The platform's own costs

**Rule:** on Windows, the build directory, the cache directory and the toolchain directory are
excluded from real-time malware scanning, by the machine's owner.
**Why:** the scanner opens every object and executable the build writes.
**Not when:** policy on the machine forbids exclusions.

## Red flags

- "I will set `-j` to what worked last time." → admission by measured peak.
- "I will switch this tree to Release for one measurement." → the Release tree.
- "The test needs the kernel, so the test compiles it." → the module compiles it.
- "Full debug information costs nothing." → measure its memory and link time first.
- "The cache makes it faster, so device objects go in too." → the trial first.
- "Release is the default because that is what ships." → Debug is the default; Release ships.
