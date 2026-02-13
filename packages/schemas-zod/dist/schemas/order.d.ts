import * as z from "zod";
export declare const CartItem: z.ZodObject<{
    id: z.ZodString;
    quantity: z.ZodInt;
}, z.core.$strict>;
export declare const OrderRequest: z.ZodObject<{
    id: z.ZodString;
    intent_id: z.ZodString;
    nonce: z.ZodString;
}, z.core.$strict>;
export declare const OrderQuote: z.ZodObject<{
    id: z.ZodString;
    intent_id: z.ZodString;
    nonce: z.ZodString;
    price: z.ZodInt;
    ready_at: z.ZodISODateTime;
    expires_at: z.ZodISODateTime;
}, z.core.$strict>;
export declare const Order: z.ZodObject<{
    id: z.ZodString;
    intent_id: z.ZodString;
    nonce: z.ZodString;
    payment_instrument_id: z.ZodString;
}, z.core.$strict>;
export declare const Cart: z.ZodObject<{
    id: z.ZodString;
    intent_id: z.ZodString;
    nonce: z.ZodString;
    items: z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        quantity: z.ZodInt;
    }, z.core.$strict>>;
}, z.core.$strict>;
//# sourceMappingURL=order.d.ts.map