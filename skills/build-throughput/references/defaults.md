# Build throughput: defaults in full

The full text of each default that [`../SKILL.md`](../SKILL.md) lists. Read the entry before
setting up or changing the part of a build it names. Each holds unless its "not when" applies;
why each exists is in [`rationale.md`](rationale.md).

## Measure first

The CLI can report a build: per kind of edge (compile, link, and any other step the build has)
the count, the total and longest wall time and the peak working set, the lowest free memory of
the run, and the slowest edges. Time traces (`-ftime-trace` or the compiler's equivalent) are
taken on the slowest units before any header or template is trimmed.

**Not when:** a repository whose full build takes under two minutes.

## Admission by measured peak

The job count is the hardware threads, and every compile and link runs through a launcher that
admits it only when its expected peak, added to the peaks reserved by the edges already running,
fits in the memory free at the start of the build less the reserve. The expected peak is the one
measured for that unit on its last build, or the largest of its kind for a unit not seen before.
Edges are admitted in arrival order, with a short window in which a lighter edge may pass a
waiting heavy one; after it the queue drains, so no unit is starved. Per-kind pools are the
fallback where no launcher can be set.

**Not when:** every unit peaks within a factor of two of the others and the build always fits.

## Heavy code compiled once, where it is owned

A large template instantiation set or any unit that needs a second compilation pass is
instantiated in the module that owns it, for the types it supports, and exposed through plain
functions. Its consumers, tests above all, include declarations, not the body.

**Not when:** the body is a template over a user's type that the module cannot list.

## Debug information sized to its use

The Debug configuration compiles without optimisation and with debug information at the level
the repository measured as the best trade between build time, memory, disk and debugging.
RelWithDebInfo carries full debug information on optimised code.

**Not when:** a debugging session needs variable-level information on a module; that module's
debugger build is its own tree.

## Debug links what Release links

On Windows every configuration takes the release C runtime, `_ITERATOR_DEBUG_LEVEL` is 0, and a
Debug tree links the Release build of every imported package.

**Not when:** the repository has no imported C++ packages and links nothing across a DLL edge.

## A compiler cache for units that are deterministic

Units compile through a compiler cache inside the build directory, capped in size and keyed on
the compiler's content. A unit whose object bundles several outputs enters the cache only after
a trial shows two cached builds produce identical outputs.

**Not when:** the repository has no generated or repeated builds to hit.

## Batches for test targets

Test targets compile in unity batches of about eight files; a name clash in an anonymous
namespace is fixed, not excluded.

**Not when:** the units are heavy, so that their memory peak grows with the batch.

## Secondary products share the engine's tree

An editor, a player or a tool whose option only adds targets is built inside the tree that
already compiled the libraries it links.

**Not when:** the product needs different compile flags; then it is another configuration,
boundary 1.

## The platform's own costs

On Windows, the build directory, the cache directory and the toolchain directory are excluded
from real-time malware scanning, by the machine's owner.

**Not when:** policy on the machine forbids exclusions.
