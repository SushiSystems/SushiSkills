---
name: sushisystems-specific
description: Use when working in a Sushi Systems repository, for the products, tools, licence, brand and install scheme that belong to Sushi Systems alone and that the sushiskills doctrine leaves out.
---

# Sushi Systems specific

The `sushiskills` doctrine names no product, company or machine. This skill holds what it
leaves out: the things true of Sushi Systems and of no other organisation. Load `sushiskills`
first; this skill extends its rules and never replaces one.

## The direction of the dependency

This skill depends on the doctrine. The doctrine names nothing here, and
`tools/layering/check_agnostic.py` fails when a doctrine file does. A fact about Sushi Systems is
written in this folder, once. A rule that any organisation could follow is written in the doctrine.

## Where things are

Each topic is a folder beside this file. Read the folder when the task touches its subject.

| Folder | Read when |
| --- | --- |
| `../logging/LOGGER.md`, `../logging/INTERFACE.md` | Adding or changing a log call, a front, a category, a sink or a host join; SushiLog is the logger |
| `../module-install/MODULE_INSTALL.md` | A module's install path, manifest, dependency declaration or catalog entry; SushiHub and `sushicore` fill the roles |
| `../dependencies/DEPENDENCIES.md` | Pinning, finding or upgrading a Sushi library, or the shared logger's runtime file |
| `../licence/LICENCE.md` | Writing or checking a licence block; the holder, the licence and the addresses |
| `../brand/LICENCE_WORDING.md` | Writing copy that names a Sushi product's licence |
| `terms.txt` | Changing which names the doctrine must not carry; the checker reads it |
