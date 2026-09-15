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
/* physics_world.hpp                                                      */
/**************************************************************************/
/*                          This file is part of:                         */
/*                                <Project>                               */
/*              https://github.com/<organisation>/<Project>               */
/*                          https://<organisation site>                   */
/**************************************************************************/
/* Copyright (c) <year>-present <Owner> & <Organisation>                  */
/* ... Apache-2.0 notice ...                                              */
/**************************************************************************/

/**
 * @file physics_world.hpp
 * @brief Declares the world that owns rigid bodies and advances them in time.
 * @author <Full Name>
 */
```

- The first line of the license block is the file name.
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

A module docstring of at most six lines opens every file after the license block. Functions
and classes carry Google-style docstrings: a one-sentence summary starting with its verb, then
`Args:`, `Returns:`, `Raises:` only when they state a rule. `#` follows the `//` rule: one line,
alone, an invariant.

## Checking

`tools/documentation/check_source_comments.py` enforces every rule above. See `project-tools`.
