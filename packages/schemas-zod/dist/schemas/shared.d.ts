import * as z from "zod";
export declare const FiatCurrency: z.ZodObject<{
    symbol: z.ZodString;
}, z.core.$strict>;
export declare const EvmCurrency: z.ZodObject<{
    chain_id: z.ZodInt;
    address: z.ZodString;
    decimals: z.ZodInt;
}, z.core.$strict>;
export declare const Amount: z.ZodObject<{
    value: z.ZodString;
    currency: z.ZodUnion<readonly [z.ZodObject<{
        symbol: z.ZodString;
    }, z.core.$strict>, z.ZodObject<{
        chain_id: z.ZodInt;
        address: z.ZodString;
        decimals: z.ZodInt;
    }, z.core.$strict>]>;
}, z.core.$strict>;
export declare const Media: z.ZodObject<{
    type: z.ZodEnum<{
        image: "image";
        video: "video";
        model_3d: "model_3d";
    }>;
    url: z.ZodString;
    alt_text: z.ZodOptional<z.ZodString>;
    width: z.ZodOptional<z.ZodInt>;
    height: z.ZodOptional<z.ZodInt>;
}, z.core.$strict>;
export declare const EvmAmount: z.ZodObject<{
    value: z.ZodString;
    currency: z.ZodObject<{
        chain_id: z.ZodInt;
        address: z.ZodString;
        decimals: z.ZodInt;
    }, z.core.$strict>;
}, z.core.$strict>;
//# sourceMappingURL=shared.d.ts.map