# Platform portability: export macro and red flags

Read this when defining `<PREFIX>_API` for a new shared library, or when a red flag applies. The
rules themselves are in `../SKILL.md`.

## The export macro

Defined once per library:

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

## Red flags

- "A small `#ifdef` here is simpler than an adapter." → the adapter.
- "It works on Windows; Linux can wait." → both, or it is not finished.
- "I copied the DLL next to the executable to make it run." → the CLI sets the path.
