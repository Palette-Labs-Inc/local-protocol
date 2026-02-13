import * as z from "zod";
const META = {
    id: (path) => ({ id: path }),
    idAnd$id: (path, fullUrl) => ({ id: path, $id: fullUrl }),
};
const BASE = "https://localprotocol.xyz/schemas";
// Fiat currency descriptor
export const FiatCurrency = z
    .object({
    symbol: z
        .string()
        .regex(/^[A-Z0-9_]+$/)
        .describe("ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY')."),
})
    .strict()
    .meta({
    ...META.idAnd$id("shared/fiat_currency.json", `${BASE}/shared/fiat_currency.json`),
    title: "FiatCurrency",
    description: "Fiat currency descriptor.",
});
// EVM token currency descriptor
export const EvmCurrency = z
    .object({
    chain_id: z.int().min(1).describe("EVM chain id."),
    address: z
        .string()
        .regex(/^0x[a-fA-F0-9]{40}$/)
        .describe("Token contract address."),
    decimals: z.int().min(0).max(255).describe("Decimal places for the token."),
})
    .strict()
    .meta({
    ...META.idAnd$id("shared/evm_currency.json", `${BASE}/shared/evm_currency.json`),
    title: "EvmCurrency",
    description: "EVM token currency descriptor.",
});
// Amount with explicit currency
export const Amount = z
    .object({
    value: z
        .string()
        .regex(/^[0-9]+$/)
        .describe('Value in minor currency units as an integer string (e.g., "1000" = $10.00 USD, or atomic units for EVM tokens). Use "0" for free items.'),
    currency: z.union([FiatCurrency, EvmCurrency]).describe("Currency descriptor (fiat or EVM token)."),
})
    .strict()
    .meta({
    ...META.idAnd$id("shared/amount.json", `${BASE}/shared/amount.json`),
    title: "Amount",
    description: "Amount with explicit currency. Value is always in minor units (e.g., cents for USD).",
});
// Product media item
export const Media = z
    .object({
    type: z.enum(["image", "video", "model_3d"]).describe("Media type discriminator."),
    url: z.string().url().describe("URL to the media resource."),
    alt_text: z.string().optional().describe("Accessibility text describing the media."),
    width: z.int().min(1).optional().describe("Width in pixels (for images/video)."),
    height: z.int().min(1).optional().describe("Height in pixels (for images/video)."),
})
    .strict()
    .meta({
    ...META.idAnd$id("shared/media.json", `${BASE}/shared/media.json`),
    title: "Media",
    description: "Product media item (image, video, etc.).",
});
// EVM amount
export const EvmAmount = z
    .object({
    value: z
        .string()
        .regex(/^[0-9]+$/)
        .describe("Value in atomic token units as an integer string."),
    currency: EvmCurrency.describe("EVM token currency."),
})
    .strict()
    .meta({
    ...META.idAnd$id("shared/evm_amount.json", `${BASE}/shared/evm_amount.json`),
    title: "EVM Amount",
    description: "Amount denominated in an EVM token. Value is in atomic token units.",
});
