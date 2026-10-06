---
name: source-comments
description: Use when writing or reviewing a comment, a Doxygen block, a file header, a docstring or a license block in C++, GLSL, TypeScript or Python source in a Sushi Systems repository.
---

# Source Comments

A comment says what a thing does, in Doxygen form, and nothing else. The reason for a design
lives in a design document; a comment may cite its path. Documentation generated from the
source is the API reference, so every symbol carries its sentence.

## File opening

Every source file opens with the license block, a blank line, then the `@file` block. The file
block is at most six lines and has exactly these tags.

```cpp
/**************************************************************************/
/* graph.hpp                                                              */
/**************************************************************************/
/*                          This file is part of:                         */
/*                              SushiRuntime                              */
/*              https://github.com/SushiSystems/SushiRuntime              */
/*                         https://sushisystems.io                        */
/**************************************************************************/
/* Copyright (c) 2026-present Mustafa Garip & Sushi Systems               */
/*                                                                        */
/* Licensed under the PolyForm Noncommercial License 1.0.0 (the           */
/* "License"); you may not use this file except in compliance with the    */
/* License. You may obtain a copy of the License at                       */
/*                                                                        */
/*     https://polyformproject.org/licenses/noncommercial/1.0.0           */
/*                                                                        */
/* Noncommercial use is free. Commercial use requires a separate licence  */
/* from Sushi Systems; see COMMERCIAL.md. The software is provided        */
/* "as is", without warranty of any kind.                                 */
/**************************************************************************/

/**
 * @file graph.hpp
 * @brief Declares the task graph and the nodes it owns.
 * @author <Full Name>
 */
```

- The box is 76 columns wide and has three sections: the file name; `This file is part of:`,
  the project and its addresses, centred; the copyright line and the licence text.
- The holder is `Mustafa Garip & Sushi Systems`. The year is the year the file was first
  written, followed by `-present`.
- A closed repository replaces the licence text with `All rights reserved.` and the paragraph
  the writer's `--closed` flag produces, and names `https://sushisystems.io` alone.
- A file ported from third-party code keeps the upstream copyright line and licence name inside
  the box, below the Sushi licence text. See `dependencies`.
- Nobody types the box. `tools/licensing/write_license_block.py` writes it.
- `@file` repeats the file name; `@brief` is one sentence starting with a verb; `@author` names
  a person. No `@date`, no version, no history.

## Symbol blocks

Every symbol carries a block: namespaces, types, functions, members, enumerators, private ones
included.

```cpp
/**
 * @brief Advances every body by one fixed step.
 * @param seconds Step length; must be positive.
 * @pre finalize() has been called.
 */
void step(double seconds);

/// @brief Bodies registered since the last finalize().
std::vector<RigidBody> pending_bodies_;

enum class WaveReadStatus : std::uint8_t
{
    Ok,             /**< The file parsed. */
    FileUnreadable, /**< The path could not be opened, or holds no bytes. */
};
```

| Tag | When |
| --- | --- |
| `@brief` | Always. One sentence, starting with its verb: Declares, Returns, Advances, Holds |
| `@param` | Only when it states a rule the caller must keep (range, ownership, lifetime) |
| `@tparam` | Only when the template parameter has a requirement |
| `@return` | Only when the value's meaning is not obvious from `@brief` |
| `@pre` | A precondition the caller must establish |
| `/**< */` | Enumerators and aligned struct fields |

A block is at most eight lines.

## Inside a body

A `//` comment is one line, alone, stating an invariant the code relies on.

```cpp
// bodies_ is sorted by id; the binary search below depends on it.
auto it = std::lower_bound(bodies_.begin(), bodies_.end(), id);
```

Two `//` lines in a row are a paragraph, and a paragraph belongs in a document.

## Forbidden in source

| Forbidden | Where it goes instead |
| --- | --- |
| Why a design was chosen | `docs/design/<TOPIC>.md`, cited by path |
| History: "previously", "was changed", "fixed in" | The commit message |
| `TODO`, `FIXME`, `HACK`, `XXX` | `docs/design/REMAINING_WORK.md` |
| Separator lines (`-----`, `=====`, `*****`) outside the license block | Nothing; split the file |
| Commented-out code | Delete it; git keeps it |
| `@date` | Git |

## Python

A module docstring of at most six lines opens every file after the license block. The license
block is five `#` lines with no box: the file name, the project and its address, the copyright
line of the box, and two licence lines. A shebang, when present, comes first. Shell and CMake
files carry the same `#` lines.

```python
# graph.py
# SushiRuntime - https://github.com/SushiSystems/SushiRuntime
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Builds the task graph from a module manifest."""
```

Functions and classes carry Google-style docstrings: a one-sentence summary starting with its verb, then
`Args:`, `Returns:`, `Raises:` only when they state a rule. `#` follows the `//` rule: one line,
alone, an invariant.

## Checking

`tools/documentation/check_source_comments.py` enforces every rule above, and
`tools/licensing/write_license_block.py` writes the license block. See `project-tools`.
