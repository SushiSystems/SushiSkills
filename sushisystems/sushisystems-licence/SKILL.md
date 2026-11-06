---
name: sushisystems-licence
description: Use in a Sushi Systems repository together with the source-comments skill, when writing or checking a licence block: the holder, the licence, the addresses and the block in each language.
---

# The Sushi Systems licence block

The `source-comments` skill gives the shape of the licence block. This page holds what fills it at
Sushi Systems.

## The values

| Value | Sushi Systems |
| --- | --- |
| Holder | `Mustafa Garip & Sushi Systems` |
| Website | `https://sushisystems.io` |
| Repository URL | `https://github.com/SushiSystems/<Project>` |
| Licence of an open repository | Apache License 2.0, `https://www.apache.org/licenses/LICENSE-2.0` |

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
/* Licensed under the Apache License, Version 2.0 (the "License"); you    */
/* may not use this file except in compliance with the License. You may   */
/* obtain a copy of the License at                                        */
/*                                                                        */
/*     https://www.apache.org/licenses/LICENSE-2.0                        */
/*                                                                        */
/* Unless required by applicable law or agreed to in writing, software    */
/* distributed under the License is distributed on an "AS IS" BASIS,      */
/* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or        */
/* implied. See the License for the specific language governing           */
/* permissions and limitations under the License.                         */
/**************************************************************************/
```

## The block in Python, shell and CMake

```python
# graph.py
# SushiRuntime - https://github.com/SushiSystems/SushiRuntime
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under the Apache License 2.0. See LICENSE.
```

## The writer

`tools/licensing/write_license_block.py` writes the block, and `check_source_comments.py` checks it.
A repository ported from third-party code keeps the upstream copyright line and licence name inside
the box, below the lines above; see the `sushisystems-dependencies` skill.
