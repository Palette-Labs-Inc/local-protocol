/**
 * Generate JSON Schema files from Zod schemas and write them under local-protocol/schemas/test.
 * Run from repo root: yarn workspace @local-protocol/schemas-zod generate
 * Or from this package: yarn build && yarn generate
 *
 * We register each schema with its id (matching schemas/ paths) and emit one .json per schema.
 * Output is normalized to match the original schemas exactly (key order, no extra keys, oneOf vs anyOf).
 */
export {};
//# sourceMappingURL=generate.d.ts.map