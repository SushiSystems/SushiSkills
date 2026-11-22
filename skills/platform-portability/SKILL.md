---
name: platform-portability
description: Use when writing code that differs between Windows and Linux, adding a preprocessor platform check, exporting symbols from a shared library, handling file paths, or touching DLL and shared-object loading, in a repository.
---

# Platform Portability

Windows and Linux are both first-class. Platform differences live behind one interface in one
place; everything else is written once. Read `references/export-macro.md` for the export macro
and red flags.

## Where platform code lives

1. `#ifdef _WIN32`, `#ifdef __linux__` and relatives appear only in the platform module or in
   adapter files `<name>_windows.cpp`, `<name>_linux.cpp`.
2. Every other module calls the platform module's interface and has no platform checks.
3. A new platform adds adapter files, never branches in shared code.

## Shared libraries

- Every exported symbol carries `<PREFIX>_API`, defined once per library.
- Default symbol visibility is hidden everywhere; only `<PREFIX>_API` symbols export.
- The DLL and shared-object search path is set by the project CLI, never by copying binaries
  together by hand or running from the build system.

## Paths and text

- Paths are `std::filesystem::path`, `pathlib.Path` or `node:path`; no hand-written separators
  or string concatenation.
- Paths shown to people or written to files use forward slashes.
- Text files are UTF-8, LF, pinned by `.gitattributes`; only `.bat`, `.cmd` and `.ps1` are CRLF.
- File names are compared case-sensitively, even on Windows.

## Types and behaviour

- Fixed-width integers (`std::uint32_t`) wherever size matters; never `long`.
- Sort directory listings; never rely on their order.
- State locale and encoding; never rely on the platform default.
