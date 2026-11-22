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

## The blocks

The block in C++, Python, shell and CMake, ready to copy: `references/blocks.md`. Read it before writing one by hand.

## The writer

`tools/licensing/write_license_block.py` writes the block, and `check_source_comments.py` checks it.
A repository ported from third-party code keeps the upstream copyright line and licence name inside
the box, below the copyright line of the block; see the `sushisystems-dependencies` skill.
