---
name: gpu-development
description: Use when writing, building or testing code that runs on an accelerator - device kernels, device compile and link, device targets, device-code caches, software test devices - in a repository.
---

# GPU development

Device code is compiled, linked and tested differently from host code. These rules extend
`build-throughput` and `testing`; where silent, those hold. Reasons and red flags:
`references/rationale.md`.

## Building device code

- **Link once per process.** Code needing a device link lives in a shared library, so each
  executable links an import library. *Not when:* one executable links the archive.
- **Development builds target the building machine's device architectures;** package and CI lanes
  compile every shipped architecture. *Not when:* the tests select a device of another kind on that
  machine.
- **Device code is optimised in every configuration,** Debug included. *Not when:* a debugging
  session needs a device debugger on one module; that module's debugger build is its own tree.
- **A kernel is instantiated in the module that owns it,** for the types it supports, and exposed
  through plain host functions; consumers, tests above all, include declarations, not its body.
  *Not when:* the kernel is a template over a user's type the module cannot list.
- **A bundled host-and-device object enters the compiler cache only after a trial** shows two
  cached builds produce identical slices. *Not when:* the unit has no device slice.
- **A unit that compiles device code stays out of a unity batch.** *Not when:* it is a small device
  unit measured to fit.

## Testing device code

- A device backend is tested through the real device, labelled `large`.
- A `medium` test uses a software device: a software graphics API (Lavapipe for Vulkan) or a CPU
  compute implementation (a CPU SYCL device).
- A `large` test whose device is absent is reported as skipped, never passed.
- A kernel is checked against its host reference, with a derived tolerance, as "Oracles and tolerances" in `testing` (`references/oracles.md`) says.
