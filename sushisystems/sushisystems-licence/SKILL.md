---
name: sushisystems-licence
description: Use in a Sushi Systems repository together with the source-comments skill, when writing or checking a licence block (the holder, the licence, the addresses and the block in each language), or together with the marketing-copy skill when copy names the licence of a Sushi Systems product.
---

# The Sushi Systems licence block

The `source-comments` skill gives the layout of the licence block. This page holds the values
written into it at Sushi Systems.

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
the block, below its copyright line; see the `sushisystems-dependencies` skill.

## In copy

`marketing-copy` says copy names a licence exactly. Sushi Systems libraries are open source under
the Apache License 2.0, and copy may say "open source" or "açık kaynak" about them. SushiEngine,
Project mobileRTS and the website are closed, and copy that mentions their source says so.
