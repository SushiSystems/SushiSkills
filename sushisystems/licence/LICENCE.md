# The Sushi Systems licence block

The `source-comments` skill gives the shape of the licence block. This page holds what fills it at
Sushi Systems.

## The values

| Value | Sushi Systems |
| --- | --- |
| Holder | `Mustafa Garip & Sushi Systems` |
| Website | `https://sushisystems.io` |
| Repository URL | `https://github.com/SushiSystems/<Project>` |
| Licence | PolyForm Noncommercial License 1.0.0, `https://polyformproject.org/licenses/noncommercial/1.0.0` |
| Commercial use | A separate licence from Sushi Systems; see `COMMERCIAL.md` |

A closed repository names `https://sushisystems.io` alone.

## The block in C++

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
```

## The block in Python, shell and CMake

```python
# graph.py
# SushiRuntime - https://github.com/SushiSystems/SushiRuntime
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
```

## The writer

`tools/licensing/write_license_block.py` writes the block, and `check_source_comments.py` checks it.
A repository ported from third-party code keeps the upstream copyright line and licence name inside
the box, below the lines above; see `../dependencies/DEPENDENCIES.md`.
