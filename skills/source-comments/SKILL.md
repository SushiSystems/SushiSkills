---
name: source-comments
description: Use when writing or reviewing a comment, a Doxygen block, a file header, a docstring or a license block in C++, GLSL, TypeScript or Python source in a repository.
---

# Source Comments

A comment says what a thing does, in Doxygen form, and nothing else. A design's reason lives in
a design document; a comment may cite its path. Every symbol carries its sentence. Examples, the
license box and the Python header: [detail](references/detail.md); read it before
writing a file opening.

- File opening: license block, blank line, `@file` block of at most six lines with exactly
  `@file` (the file name), `@brief` (one sentence, starts with a verb), `@author` (a person). No
  `@date`, version or history.
- Nobody types the license box; `tools/licensing/write_license_block.py` writes it. A ported
  third-party file keeps the upstream copyright inside it (`dependencies`).
- Every symbol carries a block, private ones included, at most eight lines. `@brief` always, one
  sentence starting with its verb. `@param` only for a rule the caller keeps, `@tparam` only for
  a requirement, `@return` only when not obvious from `@brief`, `@pre` for a caller's
  precondition, `/**< */` on enumerators and aligned fields.
- A `//` comment in a body is one line, alone, stating an invariant the code relies on. Two in a
  row are a paragraph, which belongs in a document.
- Forbidden in source: why a design was chosen (to `docs/design/<TOPIC>/README.md`); history
  (the commit message); `TODO`, `FIXME`, `HACK`, `XXX` (`backlog add work`); separator lines
  outside the license block (split the file); commented-out code (delete it); `@date`.
- Python: a module docstring of at most six lines after the license block, which is five `#`
  lines without a box; a shebang comes first; shell and CMake carry the same lines. Docstrings
  are Google-style: one summary sentence starting with its verb, `Args:`, `Returns:`, `Raises:`
  only when they state a rule. `#` follows the `//` rule.
- `tools/documentation/check_source_comments.py` enforces all of it; see `project-tools`.
