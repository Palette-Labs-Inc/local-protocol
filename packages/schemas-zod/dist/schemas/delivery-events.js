import * as z from "zod";
const META = {
    id: (path) => ({ id: path }),
    idAnd$id: (path, fullUrl) => ({ id: path, $id: fullUrl }),
};
const BASE = "https://localprotocol.xyz/schemas";
// Event definition inside a vocabulary
const EventDef = z.object({
    description: z.string().describe("Human-readable description of the event."),
}).strict();
// Delivery event vocabulary. Runtime uses z.record(EventDef); JSON Schema uses events.additionalProperties: { $ref: "#/$defs/event" } (see deliveryEventsJsonSchema).
export const DeliveryEventVocabulary = z
    .object({
    name: z.string().regex(/^[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+$/).describe("Standard identifier in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier)."),
    version: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).describe("Version in YYYY-MM-DD format."),
    extends: z.array(z.string().regex(/^[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+@\d{4}-\d{2}-\d{2}$/)).min(1).max(1).optional().describe("Parent standard this standard extends (optional). Only one parent is allowed; the reference must include a version date. Used for lineage and discovery."),
    title: z.string().describe("Human-readable title for the standard."),
    description: z.string().describe("Human-readable description of the standard."),
    spec: z.string().url().optional().describe("URL to human-readable specification document."),
    events: z.record(z.string(), EventDef).refine((o) => Object.keys(o).length >= 1, { message: "At least one event required" }).describe("Map of all event IDs supported by this standard, including inherited events."),
})
    .strict()
    .meta({
    ...META.idAnd$id("delivery/events.json", `${BASE}/delivery/events.json`),
    title: "Delivery Event Vocabulary",
    description: "Schema for delivery event vocabularies.",
});
/** JSON Schema for Delivery Event Vocabulary with $defs/event and additionalProperties ref (Zod record inlines value schema). */
export function deliveryEventsJsonSchema() {
    return {
        $schema: "https://json-schema.org/draft/2020-12/schema",
        $id: "https://localprotocol.xyz/schemas/delivery/events.json",
        title: "Delivery Event Vocabulary",
        description: "Schema for delivery event vocabularies.",
        type: "object",
        additionalProperties: false,
        required: ["name", "version", "title", "events"],
        properties: {
            name: {
                type: "string",
                pattern: "^[a-z][a-z0-9-]*(\\.[a-z][a-z0-9-]*)+$",
                description: "Standard identifier in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier).",
            },
            version: {
                type: "string",
                pattern: "^\\d{4}-\\d{2}-\\d{2}$",
                description: "Version in YYYY-MM-DD format.",
            },
            extends: {
                type: "array",
                minItems: 1,
                maxItems: 1,
                uniqueItems: true,
                items: {
                    type: "string",
                    pattern: "^[a-z][a-z0-9-]*(\\.[a-z][a-z0-9-]*)+@\\d{4}-\\d{2}-\\d{2}$",
                    description: "Standard reference with version (e.g., xyz.localprotocol.delivery.courier@2026-01-30).",
                },
                description: "Parent standard this standard extends (optional). Only one parent is allowed; the reference must include a version date. Used for lineage and discovery.",
            },
            title: {
                type: "string",
                description: "Human-readable title for the standard.",
            },
            description: {
                type: "string",
                description: "Human-readable description of the standard.",
            },
            spec: {
                type: "string",
                format: "uri",
                description: "URL to human-readable specification document.",
            },
            events: {
                type: "object",
                minProperties: 1,
                additionalProperties: { $ref: "#/$defs/event" },
                description: "Map of all event IDs supported by this standard, including inherited events.",
            },
        },
        $defs: {
            event: {
                type: "object",
                additionalProperties: false,
                required: ["description"],
                properties: {
                    description: {
                        type: "string",
                        description: "Human-readable description of the event.",
                    },
                },
            },
        },
    };
}
/** Courier delivery vocabulary instance (data, not a schema). */
export function courierVocabularyData() {
    return {
        name: "xyz.localprotocol.delivery.courier",
        version: "2026-01-30",
        title: "Courier Delivery Standard",
        description: "Event vocabulary for courier-based pickup and delivery.",
        spec: "https://localprotocol.xyz/spec/delivery/courier",
        events: {
            created: { description: "Delivery created" },
            assigned: { description: "Courier assigned" },
            enroute_pickup: { description: "Courier heading to pickup" },
            arrived_pickup: { description: "Courier at pickup location" },
            collected: { description: "Courier picked up" },
            arrived_dropoff: { description: "Courier at dropoff location" },
            delivered: { description: "Courier completed dropoff" },
            canceled: { description: "Delivery canceled" },
        },
    };
}
