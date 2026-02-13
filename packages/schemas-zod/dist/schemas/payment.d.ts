import * as z from "zod";
export declare const EvmToken: z.ZodObject<{
    address: z.ZodOptional<z.ZodString>;
    symbol: z.ZodString;
    decimals: z.ZodInt;
}, z.core.$strict>;
export declare const EvmAuthCaptureEscrowConfig: z.ZodObject<{
    chain_id: z.ZodInt;
    contract: z.ZodString;
    operator: z.ZodString;
    receiver: z.ZodString;
    accepted_tokens: z.ZodArray<z.ZodObject<{
        address: z.ZodOptional<z.ZodString>;
        symbol: z.ZodString;
        decimals: z.ZodInt;
    }, z.core.$strict>>;
}, z.core.$loose>;
export declare const EvmAuthCaptureEscrowInstrument: z.ZodIntersection<z.ZodIntersection<z.ZodObject<{
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
}, z.core.$loose>, z.ZodObject<{
    payment_info_hash: z.ZodString;
    operator: z.ZodString;
    payer: z.ZodString;
    receiver: z.ZodString;
    token: z.ZodObject<{
        address: z.ZodOptional<z.ZodString>;
        symbol: z.ZodString;
        decimals: z.ZodInt;
    }, z.core.$strict>;
    max_amount: z.ZodObject<{
        value: z.ZodString;
        currency: z.ZodObject<{
            chain_id: z.ZodInt;
            address: z.ZodString;
            decimals: z.ZodInt;
        }, z.core.$strict>;
    }, z.core.$strict>;
    preapproval_expires_at: z.ZodISODateTime;
    authorization_expires_at: z.ZodISODateTime;
    refund_expires_at: z.ZodISODateTime;
    nonce: z.ZodString;
    chain_id: z.ZodInt;
    contract: z.ZodString;
    amount: z.ZodObject<{
        value: z.ZodString;
        currency: z.ZodObject<{
            chain_id: z.ZodInt;
            address: z.ZodString;
            decimals: z.ZodInt;
        }, z.core.$strict>;
    }, z.core.$strict>;
}, z.core.$loose>>, z.ZodObject<{
    type: z.ZodLiteral<"evm_auth_capture_escrow">;
}, z.core.$strip>>;
//# sourceMappingURL=payment.d.ts.map