import * as z from "zod";
export declare const DeliveryEventVocabulary: z.ZodObject<{
    name: z.ZodString;
    version: z.ZodString;
    extends: z.ZodOptional<z.ZodArray<z.ZodString>>;
    title: z.ZodString;
    description: z.ZodString;
    spec: z.ZodOptional<z.ZodString>;
    events: z.ZodRecord<z.ZodString, z.ZodObject<{
        description: z.ZodString;
    }, z.core.$strict>>;
}, z.core.$strict>;
/** JSON Schema for Delivery Event Vocabulary with $defs/event and additionalProperties ref (Zod record inlines value schema). */
export declare function deliveryEventsJsonSchema(): Record<string, unknown>;
/** Courier delivery vocabulary instance (data, not a schema). */
export declare function courierVocabularyData(): Record<string, unknown>;
//# sourceMappingURL=delivery-events.d.ts.map