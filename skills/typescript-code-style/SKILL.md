---
name: typescript-code-style
description: Use when writing, reviewing or refactoring TypeScript in a repository - a web application, a package, a service or tests - including its layout, brace symmetry, naming, class shape, errors and logging.
---

# TypeScript Code Style

Braces as in C++: every opening brace on its own line, in the column of its closing
brace. Layout tree, examples: [rules](references/rules.md).
- Layout: `repository-layout`'s module-count predicate holds; the tree is in rules.
  `source/index.ts` re-exports the public surface only; tests at
  `tests/<tier>/<module>/<name>.test.ts`. One module: `source/` and `tests/` at the root.
  Import modules by package name, never by relative path into `source/`.
- Formatting: `dprint` formats, ESLint `@stylistic` checks, never Prettier. 4 spaces, 100 columns,
  double quotes, semicolons. Own-line braces for classes, functions, control flow,
  enums, bodied lambdas, multi-line object literals; single-statement bodies optional, on their
  own line; empty body `{` and `}` with a blank line between; a single-expression arrow stays on
  one line. The dprint and ESLint settings that encode it are in rules.
- Return: never an object literal after `return`; bind it to a `const` first.
- Names: `snake_case` files, folders; `@<organisation>/<kebab-case>` packages; `PascalCase`
  classes, interfaces, types, enums, members, components; `camelCase` functions (verb first),
  variables, parameters; `camelCase_` private members with `private`; `K_UPPER_SNAKE`
  constants. No `I` prefix, `any`, default exports.
- Class: public first in caller order, fields on top; dependencies via the constructor, no
  module-level mutable state; every member states visibility; `readonly` unless reassigned;
  interfaces hold no implementation, each implementation its own class and file.
- Errors: external failure returns a discriminated union with a status enum; `throw` only for
  programmer errors and framework-required boundaries; convert or log a caught error at its
  boundary; no empty `catch {}`.
- Logging (`logging`): one `const K_LOGGER = Logger.forCategory("assets");` per module; values
  as arguments, never template strings. Comments: `source-comments`.
- Tests: `vitest`, one `<name>.test.ts` per source file at the path `TESTS.md` in
  `repository-layout` gives; names read as behaviour.
- `npm`, `vitest` run only through the repository's CLI (`sushiskills`, default 2).
