---
name: gpu-development
description: Use when writing, building or testing code that runs on an accelerator - device kernels, device compile and link, device targets, device-code caches, software test devices - in a repository.
---

# GPU development

Code that runs on a device is compiled, linked and tested differently from host code. These rules
extend `build-throughput` and `testing`; where they say nothing, those skills hold.

## Building device code

### Device code linked once per process

**Rule:** code that needs a device link lives in a shared library, so each executable links an
import library instead of repeating the device link over the same code.
**Why:** a device link (bitcode link, post-link, device code generation, assembler) is the cost of
a compile, and a static archive repeats it in every executable that links it.
**Not when:** one executable links the archive.

### Development builds target the machine they run on

**Rule:** a development tree compiles device code for the device architectures of the machine
building it; the package and CI lanes compile every architecture the product ships to.
**Why:** each extra target is another full device pass in every device unit and every device link,
for code the developer cannot run.
**Not when:** the tests select a device of another kind on that machine.

### Device code stays optimised

**Rule:** device code is optimised in every configuration, Debug included.
**Why:** unoptimised device code makes the tests that exercise it unusable.
**Not when:** a debugging session needs a device debugger on one module; that module's debugger
build is its own tree.

### A kernel is compiled where it is owned

**Rule:** a kernel is instantiated in the module that owns it, for the types it supports, and
exposed through plain host functions. Its consumers, tests above all, include declarations, not
the kernel's body.
**Why:** a header-only kernel is compiled, for every device target, in every unit that launches it.
**Not when:** the kernel is a template over a user's type that the module cannot list.

### A bundled object enters the cache after a trial

**Rule:** a unit whose object bundles host and device slices enters the compiler cache only after a
trial shows two cached builds produce identical slices.
**Why:** a wrong hit is a missing kernel at run time that no build step reports.
**Not when:** the unit has no device slice.

### Heavy device units are not batched

**Rule:** a unit that compiles device code stays out of a unity batch.
**Why:** the memory peak of a device unit grows with the batch.
**Not when:** the unit is a small device unit measured to fit.

## Testing device code

- A device backend is tested through the real device, labelled `large`.
- A `medium` test uses a software device: a software implementation of the graphics API, or a CPU
  implementation of the compute API. Examples are Lavapipe for Vulkan and a CPU SYCL device.
- A `large` test whose device is absent is reported as skipped, never as passed.

## Red flags

- "The shared library linked in seconds, so the device link is cheap." → count its device images:
  a device driver that never sees the archives (`/WHOLEARCHIVE` passed through `-Xlinker`) links
  an empty device image, and every kernel is missing at run time.
- "The cache makes it faster, so device objects go in too." → the trial first.
- "No GPU here, so the test counts as passing." → skipped.
