---
name: platform-portability
description: Use when writing code that differs between Windows and Linux, adding a preprocessor platform check, exporting symbols from a shared library, handling file paths, or touching DLL and shared-object loading, in a Sushi Systems repository.
---

# Platform Portability

Windows and Linux are both first-class. Platform differences live behind one interface in one
place; everything else is written once.

## Where platform code lives

1. `#ifdef _WIN32`, `#ifdef __linux__` and their relatives appear only in the platform module, or
   in adapter files named for their platform: `<name>_windows.cpp`, `<name>_linux.cpp`.
2. Every other module calls the platform module's interface and contains no platform checks.
3. Adding a platform adds adapter files. It never adds branches to shared code.

## Shared libraries

- Every exported symbol carries `<PREFIX>_API`, defined once per library:

```cpp
#if defined(_WIN32)
    #if defined(PR_BUILDING_LIBRARY)
        #define PR_API __declspec(dllexport)
    #else
        #define PR_API __declspec(dllimport)
    #endif
#else
    #define PR_API __attribute__((visibility("default")))
#endif
```

- Default symbol visibility is hidden on every platform; only `<PREFIX>_API` symbols export.
- The runtime search path for DLLs and shared objects is set by the project CLI, never by copying
  binaries next to each other by hand and never by running from CMake.

## Paths and text

- Paths are `std::filesystem::path` in C++, `pathlib.Path` in Python, `node:path` in TypeScript.
  No hand-written separators, no string concatenation of paths.
- Paths shown to people or written to files use forward slashes.
- Text files are UTF-8, LF line endings, pinned by `.gitattributes`; only `.bat`, `.cmd` and
  `.ps1` are CRLF.
- File names are compared case-sensitively, as Linux does, even on Windows.

## Types and behaviour

- Fixed-width integers (`std::uint32_t`) wherever size matters; never `long`.
- No reliance on the order of directory listings; sort them.
- No reliance on the platform's default locale or encoding; state them.

## Red flags

- "A small `#ifdef` here is simpler than an adapter." → the adapter.
- "It works on Windows; Linux can wait." → both, or it is not finished.
- "I copied the DLL next to the executable to make it run." → the CLI sets the path.
