# Testing: architecture for small tests

Read this when a promise can only be checked by a `medium` test and the code needs a seam. The rules are
in `../SKILL.md`.

## Architecture for small tests

Code is shaped so that most promises can be tested small. When it is not, the seam is built before
the test, and building it is part of the task. A new or changed public interface is the owner's
decision; an internal one is yours.

1. **Functional core, imperative shell.** A module keeps its decisions in code that takes values and
   returns values. Device launch, file access, threads, sockets and the clock are in a thin shell
   around it.
2. **Ports with in-memory adapters.** Every outside dependency is reached through an interface the
   module owns, with a host or in-memory implementation beside the real one: clock, random seed, file
   system or stream, executor, transport, device queue, logger and profiler sink. Both pass the same
   contract tests. The in-memory one is the fake every other module's tests use; nobody mocks it.
   The contract tests are one typed or parametrised suite, `<Port>Contract`, in the test file of the
   port's own module, instantiated once per implementation: `small` for the in-memory one, the size
   its boundary needs for the real one. Only the adapter ships in the module; case tables, builders
   and fixtures are under `tests/support/` in a target only the tests link.
3. **Kernels call host-callable functions.** The arithmetic and index math of a device kernel is a
   function compiled for host and device. Small tests call it on the host; one medium test per kernel
   family checks the launch against the host reference.
4. **No logic reaches a process-wide instance.** A singleton or a global context is passed in at the
   shell.
5. **Edges hold no logic.** `main`, a MonoBehaviour, a React page, a kernel launcher and a CLI command only
   call the parts they connect. Logic in them moves into the core.
6. **Concurrency runs on an executor the code is given.** Tests pass a single-threaded executor that
   runs a seeded schedule, so a race reproduces from its seed. Real threads are tested `medium`,
   under ThreadSanitizer.
7. **Waiting takes a clock.** A component that waits takes a clock the test advances. Absence is
   proved by advancing the clock and asserting, never by sleeping.

Mocks are for an out-of-process dependency the repository does not own, in the test of the adapter
that reaches it. Everything else uses the real code or its in-memory port.
