# TypeScript code style: tree, settings and examples

Elaboration of the rules in `../SKILL.md`: the layout tree, the formatter settings, the example
class and the naming examples. Prettier cannot place braces on their own line, which is why
`dprint` formats.

## Layout

```
modules/<tier>/<module>/
    README.md
    package.json          name: @<organisation>/<module>
    source/
        index.ts          re-exports the public surface, nothing else
        <name>.ts
tests/<tier>/<module>/<name>.test.ts
```

## Formatting settings

The dprint TypeScript plugin sets `"bracePosition": "nextLine"`. ESLint sets
`@stylistic/brace-style: ["error", "allman"]` and `no-unexpected-multiline`.

A single-expression arrow stays on one line: `(record) => record.id`.

## The return rule

JavaScript inserts a semicolon after a bare `return`, so an object literal on the next line
returns `undefined`.

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
    private readonly records_ = new Map<AssetID, AssetRecord>();

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

export function findOversized(records: AssetRecord[], limit: number): AssetID[]
{
    return records
        .filter((record) =>
        {
            return record.bytes > limit;
        })
        .map((record) => record.id);
}
```

`LookupResult` is the discriminated union that carries a `LookupStatus`.

## Naming examples

| Kind | Example |
| --- | --- |
| File | `asset_registry.ts` |
| Package | `@acme/asset-registry` |
| Class, type | `AssetRegistry`, `LookupResult` |
| Enum member | `LookupStatus.Unknown` |
| Function, method | `findOversized`, `evictOldest` |
| Variable, parameter | `sampleRate` |
| Private member | `records_` |
| Module constant | `K_MAX_ASSETS` |
| Component (JSX) | `AssetList` in `asset_list.tsx` |

## Test names

`it("evicts the oldest record when full")`.
