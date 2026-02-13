import * as z from "zod";
import { EvmAmount } from "./shared.js";
import { PaymentInstrument } from "./ucp.js";
const META = {
    id: (path) => ({ id: path }),
    idAnd$id: (path, fullUrl) => ({ id: path, $id: fullUrl }),
};
const BASE = "https://localprotocol.xyz/schemas";
// EVM token
export const EvmToken = z
    .object({
    address: z.string().regex(/^0x[a-fA-F0-9]{40}$/).optional().describe("ERC-20 contract address. Omit for native gas tokens (e.g., ETH, MATIC)."),
    symbol: z.string().describe("Token symbol (e.g., USDC)."),
    decimals: z.int().min(0).max(255).describe("Token decimals."),
})
    .strict()
    .meta({
    ...META.idAnd$id("payment/types/evm_token.json", `${BASE}/payment/types/evm_token.json`),
    title: "EVM Token",
    description: "EVM token identifier used for auth/capture settlement.",
});
// EVM auth/capture escrow config
export const EvmAuthCaptureEscrowConfig = z
    .object({
    chain_id: z.int().min(1).describe("EVM chain id for the escrow contract."),
    contract: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Escrow contract address on the target chain."),
    operator: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Operator address authorized to drive state transitions."),
    receiver: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Default receiver address for captures."),
    accepted_tokens: z.array(EvmToken).min(1).describe("Tokens accepted on the escrow contract chain."),
})
    .passthrough()
    .meta({
    ...META.idAnd$id("payment/evm_auth_capture_escrow_config.json", `${BASE}/payment/evm_auth_capture_escrow_config.json`),
    title: "EVM Auth/Capture Escrow Config",
    description: "Handler configuration for auth/capture escrow on EVM chains.",
});
// EVM auth/capture escrow instrument: PaymentInstrument + extension + type discriminator (emits allOf[0]=$ref, allOf[1]=object, allOf[2]={ type: const })
const EvmAuthCaptureEscrowExtension = z
    .object({
    payment_info_hash: z.string().regex(/^0x[a-fA-F0-9]{64}$/).describe("Hash that identifies the on-chain payment authorization."),
    operator: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Operator address used to compute the payment info hash."),
    payer: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Payer address used to compute the payment info hash."),
    receiver: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Receiver address used for captures."),
    token: EvmToken.describe("EVM token."),
    max_amount: EvmAmount.describe("Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals."),
    preapproval_expires_at: z.iso.datetime().describe("Pre-approval expiration timestamp (RFC 3339)."),
    authorization_expires_at: z.iso.datetime().describe("Authorization expiration timestamp (RFC 3339)."),
    refund_expires_at: z.iso.datetime().describe("Refund expiration timestamp (RFC 3339)."),
    nonce: z.string().regex(/^[0-9]+$/).describe("Unique nonce used to compute the payment info hash."),
    chain_id: z.int().min(1).describe("EVM chain id for the escrow contract."),
    contract: z.string().regex(/^0x[a-fA-F0-9]{40}$/).describe("Escrow contract address on the target chain."),
    amount: EvmAmount.describe("Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals."),
})
    .passthrough();
export const EvmAuthCaptureEscrowInstrument = PaymentInstrument.and(EvmAuthCaptureEscrowExtension)
    .and(z.object({ type: z.literal("evm_auth_capture_escrow") }))
    .meta({
    ...META.id("payment/evm_auth_capture_escrow_instrument.json"),
    title: "EVM Auth/Capture Escrow Instrument",
    description: "Payment instrument for auth/capture escrow on EVM chains.",
});
