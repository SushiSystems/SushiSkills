# Source comments: examples and detail

Examples and detail for the rules in `../SKILL.md`. Read this before writing a file opening, a
symbol block or a Python header.

## File opening

The license block, a blank line, then the `@file` block:

```cpp
/**************************************************************************/
/* graph.hpp                                                              */
/**************************************************************************/
/*                          This file is part of:                         */
/*                                <Project>                               */
/*                            <repository URL>                            */
/*                              <website URL>                             */
/**************************************************************************/
/* Copyright (c) <year>-present <holder>                                  */
/*                                                                        */
/* <licence text, wrapped to this width>                                  */
/**************************************************************************/

/**
 * @file graph.hpp
 * @brief Declares the task graph and the nodes it owns.
 * @author <Full Name>
 */
```

- The box is 76 columns wide and has three sections: the file name; `This file is part of:`,
  the project and its addresses, centred; the copyright line and the licence text.
- The holder and the licence text are the owner's and are written once, in the writer's
  configuration. The year is the year the file was first written, followed by `-present`.
- A closed repository replaces the licence text with `All rights reserved.` and the paragraph
  the writer's `--closed` flag produces, and names the website alone.
- A file ported from third-party code keeps the upstream copyright line and licence name inside
  the box, below the owner's licence text. See `dependencies`.

## Symbol blocks

Blocks go on namespaces, types, functions, members and enumerators.

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

A `@brief` starts with a verb such as Declares, Returns, Advances or Holds. A `@param` states a
range, ownership or lifetime. A `@tparam` states a requirement.

## Inside a body

A `//` comment is one line, alone, stating an invariant the code relies on.

```cpp
// bodies_ is sorted by id; the binary search below depends on it.
auto it = std::lower_bound(bodies_.begin(), bodies_.end(), id);
```

## Forbidden in source

Separator lines are `-----`, `=====` and `*****`. History is wording such as "previously", "was
changed" or "fixed in". Commented-out code stays in git.

## Python

The license block is five `#` lines with no box: the file name, the project and its address, the
copyright line of the box, and two licence lines.

```python
# graph.py
# <Project> - <repository URL>
# Copyright (c) <year>-present <holder>
# <licence line>
# <licence line>
"""Builds the task graph from a module manifest."""
```
