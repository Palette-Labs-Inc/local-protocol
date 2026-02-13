import * as z from "zod";
export type ToJSONSchemaOptions = {
    /** JSON Schema target. Default: draft-2020-12 to match local-protocol/schemas */
    target?: "draft-04" | "draft-07" | "draft-2020-12" | "openapi-3.0";
    /** Emit $defs for reused schemas. Default: "ref" */
    reused?: "ref" | "inline";
};
/**
 * Generate a JSON Schema object from a Zod schema, matching the format used in
 * local-protocol/schemas (draft 2020-12, strict objects, descriptions).
 * Use this to keep Zod as the source of truth and emit schemas identical to
 * the ones in schemas/*.json.
 *
 * @see https://zod.dev/json-schema
 */
export declare function toJSONSchema<T extends z.ZodTypeAny>(schema: T, options?: ToJSONSchemaOptions): Record<string, unknown>;
/**
 * Generate JSON Schema for all schemas registered in the given registry (e.g. z.globalRegistry).
 * Schemas must be registered with .meta({ id: "path/to/schema.json" }). Returns a map of
 * id -> JSON Schema object. Add $schema to each; use with generate script to write files
 * and optionally rewrite $ref to relative paths.
 */
export declare function toJSONSchemaFromRegistry(registry: Parameters<typeof z.toJSONSchema>[0], options?: ToJSONSchemaOptions): Record<string, Record<string, unknown>>;
//# sourceMappingURL=to-json-schema.d.ts.map