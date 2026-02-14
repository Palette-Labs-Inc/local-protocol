# @local-protocol/schemas-zod

Define **Zod** schemas as the source of truth and use **`z.toJSONSchema()`** to generate JSON Schema identical to the ones in [local-protocol/schemas](../schemas).

- [Zod JSON Schema docs](https://zod.dev/json-schema)

## Usage

### Generate JSON Schema from a single Zod schema

```ts
import { toJSONSchema, Amount } from "@local-protocol/schemas-zod";

const jsonSchema = toJSONSchema(Amount);
// => draft-2020-12 JSON Schema object (matches schemas/shared/amount.json)
```

### Generate all schemas and write to `schemas/test/`

All schemas under `local-protocol/schemas/` are generated from Zod (no copying). Run:

```bash
yarn generate
```

No build step is required; the script runs TypeScript via `tsx`. From repo root: `yarn workspace @local-protocol/schemas-zod generate`.

This writes one `.json` file per schema under `local-protocol/schemas/`, with `$ref` values relativized so they match the existing multi-file layout.

### Adding new schemas

1. Add a Zod schema in `src/schemas/` (e.g. `src/schemas/order.ts`) using `.meta({ id: "order/request.json", title: "...", description: "..." })`.
2. Export it from `src/index.ts` and import the module in `src/generate.ts` so it is registered.
3. Run `yarn generate` to emit the JSON file.

Use `.strict()` on objects to get `additionalProperties: false`. Use `.describe()` for property descriptions. Use `z.union([...])` for `oneOf` / `anyOf`.

### Generate OpenAPI 3.1 spec

The same Zod schemas are used to generate the OpenAPI spec via [@asteasolutions/zod-to-openapi](https://github.com/asteasolutions/zod-to-openapi). Run:

```bash
yarn generate:openapi
```

No build step is required. This writes `openapi/specs/local-protocol.v1.openapi.json`. A **post-processing** step merges `x-codeSamples` from the existing spec and reorders keys so the output matches the previous format. The generator imports `openapi/zod-extend.ts` first so the global Zod module is extended with `.openapi()` before any schemas load.
