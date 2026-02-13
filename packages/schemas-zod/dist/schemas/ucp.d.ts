import * as z from "zod";
export declare const PostalAddress: z.ZodObject<{
    extended_address: z.ZodOptional<z.ZodString>;
    street_address: z.ZodOptional<z.ZodString>;
    address_locality: z.ZodOptional<z.ZodString>;
    address_region: z.ZodOptional<z.ZodString>;
    address_country: z.ZodOptional<z.ZodString>;
    postal_code: z.ZodOptional<z.ZodString>;
    first_name: z.ZodOptional<z.ZodString>;
    last_name: z.ZodOptional<z.ZodString>;
    phone_number: z.ZodOptional<z.ZodString>;
}, z.core.$strip>;
export declare const PaymentCredential: z.ZodObject<{
    type: z.ZodString;
}, z.core.$loose>;
export declare const PaymentInstrument: z.ZodObject<{
    id: z.ZodString;
    handler_id: z.ZodString;
    type: z.ZodString;
    billing_address: z.ZodOptional<z.ZodObject<{
        extended_address: z.ZodOptional<z.ZodString>;
        street_address: z.ZodOptional<z.ZodString>;
        address_locality: z.ZodOptional<z.ZodString>;
        address_region: z.ZodOptional<z.ZodString>;
        address_country: z.ZodOptional<z.ZodString>;
        postal_code: z.ZodOptional<z.ZodString>;
        first_name: z.ZodOptional<z.ZodString>;
        last_name: z.ZodOptional<z.ZodString>;
        phone_number: z.ZodOptional<z.ZodString>;
    }, z.core.$strip>>;
    credential: z.ZodOptional<z.ZodObject<{
        type: z.ZodString;
    }, z.core.$loose>>;
    display: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
}, z.core.$loose>;
export declare const Payment: z.ZodObject<{
    instruments: z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        handler_id: z.ZodString;
        type: z.ZodString;
        billing_address: z.ZodOptional<z.ZodObject<{
            extended_address: z.ZodOptional<z.ZodString>;
            street_address: z.ZodOptional<z.ZodString>;
            address_locality: z.ZodOptional<z.ZodString>;
            address_region: z.ZodOptional<z.ZodString>;
            address_country: z.ZodOptional<z.ZodString>;
            postal_code: z.ZodOptional<z.ZodString>;
            first_name: z.ZodOptional<z.ZodString>;
            last_name: z.ZodOptional<z.ZodString>;
            phone_number: z.ZodOptional<z.ZodString>;
        }, z.core.$strip>>;
        credential: z.ZodOptional<z.ZodObject<{
            type: z.ZodString;
        }, z.core.$loose>>;
        display: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodUnknown>>;
    }, z.core.$loose>>;
}, z.core.$strip>;
/** JSON Schema for Payment: instruments items ref payment_instrument#/$defs/selected_payment_instrument (Zod cannot emit cross-schema $defs ref). */
export declare function paymentJsonSchema(): Record<string, unknown>;
/** JSON Schema for Payment Instrument with $defs/selected_payment_instrument (Zod cannot emit $defs with self-ref). */
export declare function paymentInstrumentJsonSchema(): Record<string, unknown>;
//# sourceMappingURL=ucp.d.ts.map