---
name: typescript-code-style
description: Use when writing, reviewing or refactoring TypeScript in a Sushi Systems repository - a web application, a package, a service or tests - including its layout, brace symmetry, naming, class shape, errors and logging.
---

# TypeScript Code Style

The same brick discipline and the same visual symmetry as the C++: every opening brace sits on
its own line in the column of its closing brace.

## Layout

The module-count predicate from `repository-layout` holds unchanged.

```
modules/<tier>/<module>/
    README.md
    package.json          name: @<organisation>/<module>
    source/
        index.ts          re-exports the public surface, nothing else
        <name>.ts
    tests/
        <name>.test.ts
```

A single-module project puts `source/` and `tests/` at the root. A module imports another
module only through its package name, never through a relative path into its `source/`.

## Formatting

`dprint` with the TypeScript plugin formats; ESLint with `@stylistic` checks. Prettier cannot
place braces on their own line and is not used.

| Rule | Value |
| --- | --- |
| Indent | 4 spaces |
| Line length | 100 |
| Quotes | Double |
| Semicolons | Always |
| Braces | Own line, same column as the closing brace: classes, functions, methods, control flow, enums, lambdas with bodies, multi-line object literals |
| Single-statement bodies | Braces optional; the statement goes on its own line |
| Empty bodies | `{` and `}` on their own lines with one blank line between them |
| Single-expression arrow | Stays on one line: `(record) => record.id` |

Settings that encode this: dprint `"bracePosition": "nextLine"`, ESLint
`@stylistic/brace-style: ["error", "allman"]` and `no-unexpected-multiline`.

## The return rule

JavaScript inserts a semicolon after a bare `return`. An object literal therefore never follows
`return` in the same statement; it is bound to a `const` first.

```ts
// Wrong: returns undefined.
return
{
    status: LookupStatus.Unknown,
};

// Right.
const missing: LookupResult =
{
    status: LookupStatus.Unknown,
};
return missing;
```

## Example

```ts
export enum LookupStatus
{
    Ok,
    Unknown,
}

export class AssetRegistry
{
    private readonly records_ = new Map<AssetId, AssetRecord>();

    public constructor(private readonly capacity_: number = K_MAX_ASSETS)
    {

    }

    public add(record: AssetRecord): void
    {
        if (this.records_.size >= this.capacity_)
            this.evictOldest();

        this.records_.set(record.id, record);
    }
}

export function findOversized(records: AssetRecord[], limit: number): AssetId[]
{
    return records
        .filter((record) =>
        {
            return record.bytes > limit;
        })
        .map((record) => record.id);
}
```

## Naming

| Kind | Form | Example |
| --- | --- | --- |
| File, folder | `snake_case` | `asset_registry.ts` |
| Package | `@<organisation>/<kebab-case>` | `@acme/asset-registry` |
| Class, interface, type, enum | `PascalCase` | `AssetRegistry`, `LookupResult` |
| Enum member | `PascalCase` | `LookupStatus.Unknown` |
| Function, method | `camelCase`, verb first | `findOversized`, `evictOldest` |
| Variable, parameter | `camelCase` | `sampleRate` |
| Private member | `camelCase_` with `private` | `records_` |
| Module constant | `K_UPPER_SNAKE` | `K_MAX_ASSETS` |
| Component (JSX) | `PascalCase` file and symbol | `AssetList` in `asset_list.tsx` |

No `I` prefix on interfaces, no `any`, no default exports.

## Class shape

1. Public members first, in the order a caller uses them; private after; fields at the top.
2. Dependencies arrive through the constructor; no module-level mutable state.
3. Every member states its visibility: `public`, `protected` or `private`.
4. `readonly` on every field that is not reassigned.
5. Interfaces hold no implementation; each implementation is its own class in its own file.

## Errors

- An operation that can fail for a reason outside the program returns a discriminated union
  carrying a status enum, as `LookupResult` does above.
- `throw` is reserved for programmer errors and for boundaries where a framework requires it.
- A caught error is converted to a status or logged at its boundary. `catch {}` that swallows is
  forbidden.

## Logging

The rules in `logging` apply. Each module creates one logger for its category at module level,
`const K_LOGGER = Logger.forCategory("assets");`, and passes values as arguments, never through
template strings built at the call site.

## Comments

The file header and symbol blocks follow `source-comments`: `/** @file ... @brief ... */` after
the license block, `@brief` on every symbol.

## Tests

`vitest`. One test file per source file, `tests/<name>.test.ts`. Test names read as behaviour:
`it("evicts the oldest record when full")`.
