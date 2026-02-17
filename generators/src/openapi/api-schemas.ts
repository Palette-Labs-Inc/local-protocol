import z from "zod";

const UcpServiceEntry = z.object({
  version: z.string().describe("Service version in YYYY-MM-DD format."),
  spec: z.string().describe("URL to service specification document."),
  transport: z.enum(["rest", "mcp", "a2a", "embedded"]).describe("Transport protocol for this service binding."),
  endpoint: z.string().optional().describe("Endpoint URL for this transport binding. Required for rest, mcp, and a2a transports."),
  schema: z.string().optional().describe("URL to transport contract schema (OpenAPI or OpenRPC). Required for rest, mcp, and embedded transports."),
});

const UcpCapabilityEntry = z.object({
  version: z.string().describe("Capability version in YYYY-MM-DD format."),
  spec: z.string().describe("URL to capability specification document."),
  schema: z.string().describe("URL to capability JSON Schema."),
  extends: z.union([z.string(), z.array(z.string())]).optional().describe("Parent capability or capabilities this extends."),
});

const UcpPaymentHandlerEntry = z.object({
  id: z.string().describe("Unique identifier for this handler instance."),
  version: z.string().describe("Handler version in YYYY-MM-DD format."),
  spec: z.string().optional().describe("URL to handler specification document."),
  schema: z.string().optional().describe("URL to handler JSON Schema."),
  config: z.record(z.string(), z.unknown()).optional().describe("Handler-specific configuration."),
});

export const DiscoveryResponse = z.object({
  ucp: z.object({
    version: z.string().describe("UCP protocol version in YYYY-MM-DD format."),
    services: z.record(z.string(), z.array(UcpServiceEntry)).describe("Service registry keyed by reverse-domain name."),
    capabilities: z.record(z.string(), z.array(UcpCapabilityEntry)).describe("Capability registry keyed by reverse-domain name."),
    payment_handlers: z.record(z.string(), z.array(UcpPaymentHandlerEntry)).describe("Payment handler registry keyed by reverse-domain name."),
  }).describe("UCP discovery profile."),
});

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
