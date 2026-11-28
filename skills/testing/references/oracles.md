# Testing: oracles and tolerances

Read this when choosing where an expected value comes from, comparing floating-point results, or
picking the shapes and special values a routine is tested on. The rules are in `../SKILL.md`.

## Oracles and tolerances

Strongest and cheapest first. A test uses the first that applies.

1. **Exact by construction.** Integer-valued or dyadic inputs whose result is exact in the type,
   compared bitwise. The default for BLAS, DSP and tensor kernels.
2. **A host reference.** The naive host implementation of the same routine, accumulating in a wider
   type. A device result is always checked against the host reference, never against values captured
   from a device run.
3. **A specified value** with its derivation in a comment beside it.
4. **A metamorphic relation** where no reference exists: a transposed product, a scaled input, a
   permuted batch, a serializer round trip.
5. **An implicit oracle,** no crash and no sanitizer finding, only for a fuzz target or a stress test.
6. **A golden file,** only when nothing above works.

**Tolerances are derived, never typed.** A floating-point comparison that is not exact goes through
the repository's tolerance helper, which computes `c · f(n) · u · gauge` (for a dot product or GEMM,
`n · u · Σ|aᵢbᵢ|`) and fails when error over bound exceeds the repository's one threshold. The C++
helper is `tests/support/tolerance.hpp`, taken unchanged from the tooling library's
`tools/testing/support/`. A bare `==` is kept only where the value is copied, not computed, or exactly
representable, and the name says so. A name does not derive a tolerance: a named constant that holds a
hand-typed epsilon keeps its name and is defined through the helper.

An acceptance band that a module promises, such as a physical fidelity bound, is a constant in the
module's header with its source beside it, and the test compares against it through the helper. A
statistical bound runs on a fixed seed, and is derived from the sample count and a stated false-failure
rate written beside it.

**Small shapes.** A routine is tested on the sizes {0, 1, 2, 3, 5, 9}, on tile size ± 1, on every
transpose and layout, on alpha and beta in {0, 1, another value}, with strides and leading dimensions
larger than the extent, and with aliased arguments where the interface allows them. Large shapes are
`large` tests and run nightly.

**Special values have their own tests:** NaN, Inf, −0, subnormals, empty extents.

**Rows, not copies.** The same promise over many inputs is one parametrised test (`TEST_P`,
`TYPED_TEST`, `pytest.mark.parametrize`, `it.each`, `[TestCase]`).
