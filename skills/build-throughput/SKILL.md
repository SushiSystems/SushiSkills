---
name: build-throughput
description: Use when choosing a build configuration or a build tree, changing how a repository compiles or links (job counts, pools, caches, precompiled headers, unity batches, optimisation or debug-information levels), when a build runs out of memory or takes too long, or when deciding where heavy code such as a large template set is compiled, in a repository.
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
6. **One copy of the machinery.** A CLI built on the shared tooling library takes the tree rule, the gate, its
   launcher entries and the report from it (`build_tree`, `build_admission`,
   `build_gate`, `build_report`) and keeps no copy of its own.
7. **A module dependency is public only when a public header needs the whole type.** That is a
   type held by value or as a member, a base class, or a type used in an inline body. A type a
   public header only names by reference or pointer is forward-declared there, its include
   moves into the module's sources, and the dependency is private. A caller that builds such an
   argument includes its header and links its module itself. Before a dependency is declared
   public, read every public header and name the line that needs it.
   A public edge hands its include directories to every module above, transitively. A change to
   the lower module's headers then recompiles all of them, and the first build after the edge
   lands recompiles most of the tree.

## Defaults

### Measure first

**Rule:** the CLI can report a build: per kind of edge (compile, link, and any other step the
build has) the count, the total and longest wall time and the peak working set, the lowest free
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

**Rule:** a large template instantiation set or any unit that needs a second compilation pass is
instantiated in the module that owns it, for the types it supports, and exposed through plain
functions. Its consumers, tests above all, include declarations, not the body.
**Why:** a header-only body is compiled, for every target, in every unit that uses it; a test
file then costs minutes and gigabytes.
**Not when:** the body is a template over a user's type that the module cannot list.

### Debug information sized to its use

**Rule:** the Debug configuration compiles without optimisation and with debug information at the
level the repository measured as the best trade between build time, memory, disk and debugging.
RelWithDebInfo carries full debug information on optimised code.
**Why:** full debug information multiplies object size, compile memory and link time on
template-heavy code.
**Not when:** a debugging session needs variable-level information on a module; that module's
debugger build is its own tree.

### Debug links what Release links

**Rule:** on Windows every configuration takes the release C runtime, `_ITERATOR_DEBUG_LEVEL` is
0, and a Debug tree links the Release build of every imported package.
**Why:** the libraries below a repository are consumed as Release packages; a debug C runtime
would need a debug build of the whole stack beneath it and would mismatch the packages' heaps.
Memory errors are the sanitizer tree's job.
**Not when:** the repository has no imported C++ packages and links nothing across a DLL edge.

### A compiler cache for units that are deterministic

**Rule:** units compile through a compiler cache inside the build directory, capped in size and
keyed on the compiler's content. A unit whose object bundles several outputs enters the cache
only after a trial shows two cached builds produce identical outputs.
**Why:** branch switches, reconfigures and clean builds then pay for what changed; a wrong hit on
a bundled object is a defect at run time that no build step reports.
**Not when:** the repository has no generated or repeated builds to hit.

### Batches for test targets

**Rule:** test targets compile in unity batches of about eight files; a name clash in an
anonymous namespace is fixed, not excluded.
**Why:** each test file reparses the test framework and the headers it tests; batching removes
most of that.
**Not when:** the units are heavy, so that their memory peak grows with the batch.

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
- "The test needs the template set, so the test compiles it." → the module compiles it.
- "Full debug information costs nothing." → measure its memory and link time first.
- "The cache makes it faster, so bundled objects go in too." → the trial first.
- "Release is the default because that is what ships." → Debug is the default; Release ships.
- "The header names its type, so the dependency is public." → only by reference? Forward-declare
  it and keep the edge private.
