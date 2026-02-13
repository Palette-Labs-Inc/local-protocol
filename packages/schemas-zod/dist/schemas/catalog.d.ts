import * as z from "zod";
export declare const Interval: z.ZodObject<{
    day: z.ZodOptional<z.ZodString>;
    date: z.ZodOptional<z.ZodString>;
    from_hour: z.ZodInt;
    from_minute: z.ZodInt;
    to_hour: z.ZodInt;
    to_minute: z.ZodInt;
}, z.core.$strict>;
export declare const Availability: z.ZodObject<{
    timezone: z.ZodOptional<z.ZodString>;
    intervals: z.ZodArray<z.ZodObject<{
        day: z.ZodOptional<z.ZodString>;
        date: z.ZodOptional<z.ZodString>;
        from_hour: z.ZodInt;
        from_minute: z.ZodInt;
        to_hour: z.ZodInt;
        to_minute: z.ZodInt;
    }, z.core.$strict>>;
}, z.core.$strict>;
export declare const ModifierItem: z.ZodObject<{
    id: z.ZodString;
    name: z.ZodString;
    description: z.ZodOptional<z.ZodString>;
    price: z.ZodObject<{
        value: z.ZodString;
        currency: z.ZodUnion<readonly [z.ZodObject<{
            symbol: z.ZodString;
        }, z.core.$strict>, z.ZodObject<{
            chain_id: z.ZodInt;
            address: z.ZodString;
            decimals: z.ZodInt;
        }, z.core.$strict>]>;
    }, z.core.$strict>;
    metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
}, z.core.$strict>;
export declare const ModifierGroup: z.ZodType<{
    id: string;
    name: string;
    description?: string;
    minimum_selections?: number;
    maximum_selections?: number;
    allow_quantities?: boolean;
    max_per_modifier?: number;
    modifier_options: unknown[];
    type?: string;
    metadata?: Record<string, unknown>;
}>;
/** Modifier option (lazy for circular ref with ModifierGroup). */
export declare const ModifierOption: z.ZodType<{
    id: string;
    modifier_item: unknown;
    child_modifier_groups?: unknown[];
    is_default?: boolean;
    metadata?: Record<string, unknown>;
}>;
/** Catalog item. Matches schemas/catalog/types/item.json */
export declare const CatalogItem: z.ZodObject<{
    id: z.ZodString;
    name: z.ZodString;
    description: z.ZodString;
    price: z.ZodObject<{
        value: z.ZodString;
        currency: z.ZodUnion<readonly [z.ZodObject<{
            symbol: z.ZodString;
        }, z.core.$strict>, z.ZodObject<{
            chain_id: z.ZodInt;
            address: z.ZodString;
            decimals: z.ZodInt;
        }, z.core.$strict>]>;
    }, z.core.$strict>;
    media: z.ZodOptional<z.ZodArray<z.ZodObject<{
        type: z.ZodEnum<{
            image: "image";
            video: "video";
            model_3d: "model_3d";
        }>;
        url: z.ZodString;
        alt_text: z.ZodOptional<z.ZodString>;
        width: z.ZodOptional<z.ZodInt>;
        height: z.ZodOptional<z.ZodInt>;
    }, z.core.$strict>>>;
    modifier_groups: z.ZodOptional<z.ZodArray<z.ZodType<{
        id: string;
        name: string;
        description?: string;
        minimum_selections?: number;
        maximum_selections?: number;
        allow_quantities?: boolean;
        max_per_modifier?: number;
        modifier_options: unknown[];
        type?: string;
        metadata?: Record<string, unknown>;
    }, unknown, z.core.$ZodTypeInternals<{
        id: string;
        name: string;
        description?: string;
        minimum_selections?: number;
        maximum_selections?: number;
        allow_quantities?: boolean;
        max_per_modifier?: number;
        modifier_options: unknown[];
        type?: string;
        metadata?: Record<string, unknown>;
    }, unknown>>>>;
    availability: z.ZodOptional<z.ZodObject<{
        timezone: z.ZodOptional<z.ZodString>;
        intervals: z.ZodArray<z.ZodObject<{
            day: z.ZodOptional<z.ZodString>;
            date: z.ZodOptional<z.ZodString>;
            from_hour: z.ZodInt;
            from_minute: z.ZodInt;
            to_hour: z.ZodInt;
            to_minute: z.ZodInt;
        }, z.core.$strict>>;
    }, z.core.$strict>>;
    metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
}, z.core.$strict>;
/** Catalog category (lazy for self and Item). */
export declare const CatalogCategory: z.ZodType<{
    id: string;
    name: string;
    description?: string;
    categories?: unknown[];
    items: unknown[];
    availability?: unknown;
    metadata?: Record<string, unknown>;
}>;
/** Catalog. Matches schemas/catalog/catalog.json */
export declare const Catalog: z.ZodObject<{
    id: z.ZodString;
    name: z.ZodString;
    description: z.ZodOptional<z.ZodString>;
    categories: z.ZodArray<z.ZodType<{
        id: string;
        name: string;
        description?: string;
        categories?: unknown[];
        items: unknown[];
        availability?: unknown;
        metadata?: Record<string, unknown>;
    }, unknown, z.core.$ZodTypeInternals<{
        id: string;
        name: string;
        description?: string;
        categories?: unknown[];
        items: unknown[];
        availability?: unknown;
        metadata?: Record<string, unknown>;
    }, unknown>>>;
    items: z.ZodOptional<z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        name: z.ZodString;
        description: z.ZodString;
        price: z.ZodObject<{
            value: z.ZodString;
            currency: z.ZodUnion<readonly [z.ZodObject<{
                symbol: z.ZodString;
            }, z.core.$strict>, z.ZodObject<{
                chain_id: z.ZodInt;
                address: z.ZodString;
                decimals: z.ZodInt;
            }, z.core.$strict>]>;
        }, z.core.$strict>;
        media: z.ZodOptional<z.ZodArray<z.ZodObject<{
            type: z.ZodEnum<{
                image: "image";
                video: "video";
                model_3d: "model_3d";
            }>;
            url: z.ZodString;
            alt_text: z.ZodOptional<z.ZodString>;
            width: z.ZodOptional<z.ZodInt>;
            height: z.ZodOptional<z.ZodInt>;
        }, z.core.$strict>>>;
        modifier_groups: z.ZodOptional<z.ZodArray<z.ZodType<{
            id: string;
            name: string;
            description?: string;
            minimum_selections?: number;
            maximum_selections?: number;
            allow_quantities?: boolean;
            max_per_modifier?: number;
            modifier_options: unknown[];
            type?: string;
            metadata?: Record<string, unknown>;
        }, unknown, z.core.$ZodTypeInternals<{
            id: string;
            name: string;
            description?: string;
            minimum_selections?: number;
            maximum_selections?: number;
            allow_quantities?: boolean;
            max_per_modifier?: number;
            modifier_options: unknown[];
            type?: string;
            metadata?: Record<string, unknown>;
        }, unknown>>>>;
        availability: z.ZodOptional<z.ZodObject<{
            timezone: z.ZodOptional<z.ZodString>;
            intervals: z.ZodArray<z.ZodObject<{
                day: z.ZodOptional<z.ZodString>;
                date: z.ZodOptional<z.ZodString>;
                from_hour: z.ZodInt;
                from_minute: z.ZodInt;
                to_hour: z.ZodInt;
                to_minute: z.ZodInt;
            }, z.core.$strict>>;
        }, z.core.$strict>>;
        metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
    }, z.core.$strict>>>;
    availability: z.ZodOptional<z.ZodObject<{
        timezone: z.ZodOptional<z.ZodString>;
        intervals: z.ZodArray<z.ZodObject<{
            day: z.ZodOptional<z.ZodString>;
            date: z.ZodOptional<z.ZodString>;
            from_hour: z.ZodInt;
            from_minute: z.ZodInt;
            to_hour: z.ZodInt;
            to_minute: z.ZodInt;
        }, z.core.$strict>>;
    }, z.core.$strict>>;
    metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
}, z.core.$strict>;
/** Merchant. Matches schemas/catalog/merchant.json */
export declare const Merchant: z.ZodObject<{
    id: z.ZodString;
    name: z.ZodString;
    timezone: z.ZodString;
    last_updated: z.ZodOptional<z.ZodISODateTime>;
    catalogs: z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        name: z.ZodString;
        description: z.ZodOptional<z.ZodString>;
        categories: z.ZodArray<z.ZodType<{
            id: string;
            name: string;
            description?: string;
            categories?: unknown[];
            items: unknown[];
            availability?: unknown;
            metadata?: Record<string, unknown>;
        }, unknown, z.core.$ZodTypeInternals<{
            id: string;
            name: string;
            description?: string;
            categories?: unknown[];
            items: unknown[];
            availability?: unknown;
            metadata?: Record<string, unknown>;
        }, unknown>>>;
        items: z.ZodOptional<z.ZodArray<z.ZodObject<{
            id: z.ZodString;
            name: z.ZodString;
            description: z.ZodString;
            price: z.ZodObject<{
                value: z.ZodString;
                currency: z.ZodUnion<readonly [z.ZodObject<{
                    symbol: z.ZodString;
                }, z.core.$strict>, z.ZodObject<{
                    chain_id: z.ZodInt;
                    address: z.ZodString;
                    decimals: z.ZodInt;
                }, z.core.$strict>]>;
            }, z.core.$strict>;
            media: z.ZodOptional<z.ZodArray<z.ZodObject<{
                type: z.ZodEnum<{
                    image: "image";
                    video: "video";
                    model_3d: "model_3d";
                }>;
                url: z.ZodString;
                alt_text: z.ZodOptional<z.ZodString>;
                width: z.ZodOptional<z.ZodInt>;
                height: z.ZodOptional<z.ZodInt>;
            }, z.core.$strict>>>;
            modifier_groups: z.ZodOptional<z.ZodArray<z.ZodType<{
                id: string;
                name: string;
                description?: string;
                minimum_selections?: number;
                maximum_selections?: number;
                allow_quantities?: boolean;
                max_per_modifier?: number;
                modifier_options: unknown[];
                type?: string;
                metadata?: Record<string, unknown>;
            }, unknown, z.core.$ZodTypeInternals<{
                id: string;
                name: string;
                description?: string;
                minimum_selections?: number;
                maximum_selections?: number;
                allow_quantities?: boolean;
                max_per_modifier?: number;
                modifier_options: unknown[];
                type?: string;
                metadata?: Record<string, unknown>;
            }, unknown>>>>;
            availability: z.ZodOptional<z.ZodObject<{
                timezone: z.ZodOptional<z.ZodString>;
                intervals: z.ZodArray<z.ZodObject<{
                    day: z.ZodOptional<z.ZodString>;
                    date: z.ZodOptional<z.ZodString>;
                    from_hour: z.ZodInt;
                    from_minute: z.ZodInt;
                    to_hour: z.ZodInt;
                    to_minute: z.ZodInt;
                }, z.core.$strict>>;
            }, z.core.$strict>>;
            metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
        }, z.core.$strict>>>;
        availability: z.ZodOptional<z.ZodObject<{
            timezone: z.ZodOptional<z.ZodString>;
            intervals: z.ZodArray<z.ZodObject<{
                day: z.ZodOptional<z.ZodString>;
                date: z.ZodOptional<z.ZodString>;
                from_hour: z.ZodInt;
                from_minute: z.ZodInt;
                to_hour: z.ZodInt;
                to_minute: z.ZodInt;
            }, z.core.$strict>>;
        }, z.core.$strict>>;
        metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
    }, z.core.$strict>>;
    metadata: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
}, z.core.$strict>;
//# sourceMappingURL=catalog.d.ts.map