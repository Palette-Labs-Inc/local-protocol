import z from "zod";

export const DiscoveryResponse = z
  .object({
    version: z.string().describe("Protocol version."),
    name: z.string().describe("Server name."),
    capabilities: z.record(z.string(), z.record(z.string(), z.unknown())).describe("Supported capabilities by domain."),
    endpoints: z.record(z.string(), z.string()).describe("Endpoint path map."),
  })
  .strict();

export const HealthResponse = z
  .object({
    status: z.literal("ok"),
  })
  .strict();

export const ErrorResponse = z.object({
  detail: z.string().describe("Error message."),
});

export const ValidationErrorResponse = z.object({
  detail: z.object({
    errors: z.array(z.string()).describe("List of validation error messages."),
  }),
});

export const CreateDeliveryRequest = z
  .object({
    request_id: z.string().describe("The delivery request to fulfill."),
    quote_id: z.string().describe("The accepted quote."),
    nonce: z.string().describe("Client-generated idempotency key."),
    webhook_url: z.string().url().nullable().optional().describe("Optional URL to receive delivery event webhook notifications."),
    event_vocabulary: z.string().default("xyz.localprotocol.delivery.courier@2026-01-30").describe("Event vocabulary standard to use."),
  })
  .strict();

export const UpdateEventRequest = z
  .object({
    event: z.string().describe("Event identifier from the delivery's event vocabulary."),
    event_description: z.string().describe("Human-readable event description."),
  })
  .strict();

export const CreateOrderRequest = z
  .object({
    order_request_id: z.string().describe("The order request to fulfill."),
    order_quote_id: z.string().describe("The accepted quote."),
    nonce: z.string().describe("Client-generated idempotency key."),
    payment_instrument_id: z.string().describe("Reference to the registered payment instrument."),
  })
  .strict();
