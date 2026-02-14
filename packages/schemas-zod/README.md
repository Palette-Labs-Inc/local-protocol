# @local-protocol/schemas-zod

Define **Zod** schemas as the source of truth and use **`z.toJSONSchema()`** to generate JSON Schemas

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


This writes one `.json` file per schema under `local-protocol/schemas/`, with `$ref` values relativized so they match the existing multi-file layout.

### Adding new schemas

1. Add a Zod schema in `src/schemas/` (e.g. `src/schemas/order.ts`) using `.meta({ id: "order/request.json", title: "...", description: "..." })`.
2. Export it from `src/index.ts` and import the module in `src/generate.ts` so it is registered.
3. Run `yarn generate` to emit the JSON file.

Use `.strict()` on objects to get `additionalProperties: false`. Use `.describe()` for property descriptions. Use `z.union([...])` for `oneOf` / `anyOf`.
