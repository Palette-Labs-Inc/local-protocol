import * as z from "zod";
const DRAFT_2020_12 = "draft-2020-12";
const SCHEMA_META = "https://json-schema.org/draft/2020-12/schema";
/**
 * Generate a JSON Schema object from a Zod schema, matching the format used in
 * local-protocol/schemas (draft 2020-12, strict objects, descriptions).
 * Use this to keep Zod as the source of truth and emit schemas identical to
 * the ones in schemas/*.json.
 *
 * @see https://zod.dev/json-schema
 */
export function toJSONSchema(schema, options = {}) {
    const { target = DRAFT_2020_12, reused = "ref" } = options;
    const raw = z.toJSONSchema(schema, { target, reused });
    const out = raw;
    if (!out.$schema) {
        out.$schema = SCHEMA_META;
    }
    return out;
}
/**
 * Generate JSON Schema for all schemas registered in the given registry (e.g. z.globalRegistry).
 * Schemas must be registered with .meta({ id: "path/to/schema.json" }). Returns a map of
 * id -> JSON Schema object. Add $schema to each; use with generate script to write files
 * and optionally rewrite $ref to relative paths.
 */
export function toJSONSchemaFromRegistry(registry, options = {}) {
    const { target = DRAFT_2020_12 } = options;
    const result = z.toJSONSchema(registry, { target });
    const schemas = result?.schemas ?? {};
    const withMeta = {};
    for (const [id, schema] of Object.entries(schemas)) {
        const copy = { ...schema };
        if (!copy.$schema)
            copy.$schema = SCHEMA_META;
        withMeta[id] = copy;
    }
    return withMeta;
}
