import * as z from "zod";

const DRAFT_2020_12 = "draft-2020-12" as const;
const SCHEMA_META = "https://json-schema.org/draft/2020-12/schema";

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
export function toJSONSchema<T extends z.ZodTypeAny>(
  schema: T,
  options: ToJSONSchemaOptions = {}
): Record<string, unknown> {
  const { target = DRAFT_2020_12, reused = "ref" } = options;
  const raw = z.toJSONSchema(schema, { target, reused });
  const out = raw as Record<string, unknown>;
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
export function toJSONSchemaFromRegistry(
  registry: Parameters<typeof z.toJSONSchema>[0],
  options: ToJSONSchemaOptions = {}
): Record<string, Record<string, unknown>> {
  const { target = DRAFT_2020_12 } = options;
  const result = z.toJSONSchema(registry, { target }) as { schemas?: Record<string, Record<string, unknown>> };
  const schemas = result?.schemas ?? {};
  const withMeta: Record<string, Record<string, unknown>> = {};
  for (const [id, schema] of Object.entries(schemas)) {
    const copy = { ...schema } as Record<string, unknown>;
    if (!copy.$schema) copy.$schema = SCHEMA_META;
    withMeta[id] = copy;
  }
  return withMeta;
}
