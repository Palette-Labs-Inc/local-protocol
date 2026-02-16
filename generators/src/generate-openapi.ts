/**
 * Generate OpenAPI 3.1 spec from Zod schemas via @asteasolutions/zod-to-openapi.
 * Post-processes to merge x-codeSamples from the existing spec and reorder keys to match.
 *
 * Run: yarn generate:openapi (from generators).
 */
import "./openapi/zod-extend";
import * as fs from "node:fs";
import * as path from "node:path";
import { OpenAPIRegistry, OpenApiGeneratorV31 } from "@asteasolutions/zod-to-openapi";
import z from "zod";

import {
  Coordinates,
  Location,
  DeliveryRequest,
  DeliveryQuote,
  Delivery,
  PostalAddress,
  Payment,
  PaymentInstrument,
  EvmAuthCaptureEscrowInstrument,
  DeliveryEventVocabulary,
  CartItem,
  Cart,
  OrderRequest,
  OrderQuote,
  Order,
  FiatCurrency,
  EvmCurrency,
  Amount,
  Media,
  EvmAmount,
  EvmToken,
  EvmAuthCaptureEscrowConfig,
  Interval,
  Availability,
  ModifierItem,
  ModifierGroup,
  ModifierOption,
  CatalogItem,
  CatalogCategory,
  Catalog,
  Merchant,
  PaymentCredential,
} from "./index";
import {
  DiscoveryResponse,
  HealthResponse,
  ErrorResponse,
  ValidationErrorResponse,
  CreateDeliveryRequest,
  UpdateEventRequest,
  CreateOrderRequest,
} from "./openapi/api-schemas";


const __dirname = path.dirname(process.argv[1] ?? ".");
const REPO_ROOT = path.resolve(__dirname, "..", "..");
const SPEC_PATH = path.join(REPO_ROOT, "openapi", "specs", "local-protocol.v1.openapi.json");

function ensureSpecDir(): string {
  const dir = path.dirname(SPEC_PATH);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  return dir;
}

// Recursively reorder generated to match original key order; use generated values
function reorderToMatch(original: unknown, generated: unknown): unknown {
  if (generated === undefined || generated === null) return generated;
  if (typeof original !== "object" || original === null) return generated;
  if (Array.isArray(original)) {
    const genArr = Array.isArray(generated) ? generated : [];
    return genArr.map((genItem, i) =>
      i < original.length ? reorderToMatch(original[i], genItem) : genItem
    );
  }
  if (typeof generated !== "object" || generated === null || Array.isArray(generated)) {
    return generated;
  }
  const origObj = original as Record<string, unknown>;
  const genObj = generated as Record<string, unknown>;
  const result: Record<string, unknown> = {};
  for (const k of Object.keys(origObj)) {
    if (k in genObj) {
      const reordered = reorderToMatch(origObj[k], genObj[k]);
      if (reordered !== undefined) result[k] = reordered;
    }
  }
  for (const k of Object.keys(genObj)) {
    if (!(k in origObj)) {
      const reordered = reorderToMatch(undefined, genObj[k]);
      if (reordered !== undefined) result[k] = reordered;
    }
  }
  return result;
}

// Map path-style $ref (from Zod schema meta id) to OpenAPI component schema names
const REF_PATH_TO_COMPONENT: Record<string, string> = {
  "delivery/request.json": "DeliveryRequest",
  "delivery/quote.json": "DeliveryQuote",
  "delivery/delivery.json": "Delivery",
  "delivery/events.json": "DeliveryEventVocabulary",
  "delivery/types/coordinates.json": "Coordinates",
  "delivery/types/location.json": "Location",
  "order/request.json": "OrderRequest",
  "order/quote.json": "OrderQuote",
  "order/order.json": "Order",
  "order/cart.json": "Cart",
  "order/types/cart_item.json": "CartItem",
  "catalog/merchant.json": "Merchant",
  "catalog/catalog.json": "Catalog",
  "catalog/types/item.json": "CatalogItem",
  "catalog/types/category.json": "CatalogCategory",
  "catalog/types/interval.json": "Interval",
  "catalog/types/availability.json": "Availability",
  "catalog/types/modifier_item.json": "ModifierItem",
  "catalog/types/modifier_group.json": "ModifierGroup",
  "catalog/types/modifier_option.json": "ModifierOption",
  "shared/media.json": "Media",
  "shared/fiat_currency.json": "FiatCurrency",
  "shared/evm_currency.json": "EvmCurrency",
  "shared/amount.json": "Amount",
  "shared/evm_amount.json": "EvmAmount",
  "payment/evm_auth_capture_escrow_instrument.json": "EvmAuthCaptureEscrowInstrument",
  "payment/types/evm_token.json": "EvmToken",
  "payment/evm_auth_capture_escrow_config.json": "EvmAuthCaptureEscrowConfig",
  "ucp/shopping/types/payment_instrument.json": "PaymentInstrument",
  "ucp/shopping/types/payment_credential.json": "PaymentCredential",
  "ucp/shopping/types/postal_address.json": "PostalAddress",
};

function rewriteSchemaRefs(obj: unknown): unknown {
  if (obj === null || obj === undefined) return obj;
  if (typeof obj === "object" && "$ref" in obj && typeof (obj as { $ref: string }).$ref === "string") {
    const ref = (obj as { $ref: string }).$ref;
    const prefix = "#/components/schemas/";
    if (ref.startsWith(prefix)) {
      const path = ref.slice(prefix.length);
      const component = REF_PATH_TO_COMPONENT[path];
      if (component) {
        return { ...(obj as object), $ref: prefix + component };
      }
    }
    return obj;
  }
  if (Array.isArray(obj)) return obj.map(rewriteSchemaRefs);
  if (typeof obj === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(obj)) out[k] = rewriteSchemaRefs(v);
    return out;
  }
  return obj;
}

/** Rekey components.schemas from path-style keys to component names so $refs resolve. */
function rekeyComponentSchemas(spec: Record<string, unknown>): void {
  const components = spec.components as Record<string, unknown> | undefined;
  const schemas = components?.schemas as Record<string, unknown> | undefined;
  if (!schemas || typeof schemas !== "object") return;
  const rekeyed: Record<string, unknown> = {};
  for (const [key, value] of Object.entries(schemas)) {
    const newKey = REF_PATH_TO_COMPONENT[key] ?? key;
    rekeyed[newKey] = value;
  }
  (components as Record<string, unknown>).schemas = rekeyed;
}

// Copy x-codeSamples from original into generated for every path operation
function mergeCodeSamples(original: Record<string, unknown>, generated: Record<string, unknown>): void {
  const origPaths = original.paths as Record<string, Record<string, unknown>> | undefined;
  const genPaths = generated.paths as Record<string, Record<string, unknown>> | undefined;
  if (!origPaths || !genPaths) return;
  for (const [pathKey, pathItem] of Object.entries(origPaths)) {
    if (typeof pathItem !== "object" || pathItem === null) continue;
    const genPath = genPaths[pathKey] as Record<string, unknown> | undefined;
    if (!genPath) continue;
    for (const method of ["get", "post", "put", "patch", "delete"]) {
      const origOp = pathItem[method] as Record<string, unknown> | undefined;
      const genOp = genPath[method] as Record<string, unknown> | undefined;
      const samples = origOp && "x-codeSamples" in origOp && origOp["x-codeSamples"];
      if (samples && genOp) {
        genOp["x-codeSamples"] = samples;
      }
    }
  }
}

function main(): void {
  const registry = new OpenAPIRegistry();

  // Parameters (must match spec names for $ref)
  const RequestId = registry.registerParameter(
    "RequestId",
    z.string().openapi({ param: { name: "request_id", in: "path" }, description: "Delivery request identifier." })
  );
  const QuoteId = registry.registerParameter(
    "QuoteId",
    z.string().openapi({ param: { name: "quote_id", in: "path" }, description: "Quote identifier." })
  );
  const DeliveryId = registry.registerParameter(
    "DeliveryId",
    z.string().openapi({ param: { name: "delivery_id", in: "path" }, description: "Delivery identifier." })
  );
  const MerchantId = registry.registerParameter(
    "MerchantId",
    z.string().openapi({ param: { name: "merchant_id", in: "path" }, description: "Merchant identifier." })
  );
  const OrderRequestId = registry.registerParameter(
    "OrderRequestId",
    z.string().openapi({ param: { name: "order_request_id", in: "path" }, description: "Order request identifier." })
  );
  const OrderQuoteId = registry.registerParameter(
    "OrderQuoteId",
    z.string().openapi({ param: { name: "order_quote_id", in: "path" }, description: "Order quote identifier." })
  );
  const OrderId = registry.registerParameter(
    "OrderId",
    z.string().openapi({ param: { name: "order_id", in: "path" }, description: "Order identifier." })
  );
  const EventVocabularyName = registry.registerParameter(
    "EventVocabularyName",
    z.string().openapi({
      param: { name: "name", in: "path" },
      description: "Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier).",
    })
  );

  // Schemas – register with OpenAPI component names
  registry.register("Coordinates", Coordinates);
  registry.register("PostalAddress", PostalAddress);
  registry.register("Location", Location);
  registry.register("DeliveryRequest", DeliveryRequest);
  registry.register("DeliveryQuote", DeliveryQuote);
  registry.register("CreateDeliveryRequest", CreateDeliveryRequest);
  registry.register("UpdateEventRequest", UpdateEventRequest);
  registry.register("Delivery", Delivery);
  registry.register("DiscoveryResponse", DiscoveryResponse);
  registry.register("HealthResponse", HealthResponse);
  registry.register("ErrorResponse", ErrorResponse);
  registry.register("ValidationErrorResponse", ValidationErrorResponse);
  registry.register("FiatCurrency", FiatCurrency);
  registry.register("EvmCurrency", EvmCurrency);
  registry.register("EvmAmount", EvmAmount);
  registry.register("Amount", Amount);
  registry.register("Media", Media);
  registry.register("Interval", Interval);
  registry.register("Availability", Availability);
  registry.register("ModifierItem", ModifierItem);
  registry.register("ModifierOption", ModifierOption);
  registry.register("ModifierGroup", ModifierGroup);
  registry.register("CatalogItem", CatalogItem);
  registry.register("CatalogCategory", CatalogCategory);
  registry.register("Catalog", Catalog);
  registry.register("Merchant", Merchant);
  registry.register("CartItem", CartItem);
  registry.register("Cart", Cart);
  registry.register("OrderRequest", OrderRequest);
  registry.register("OrderQuote", OrderQuote);
  registry.register("CreateOrderRequest", CreateOrderRequest);
  registry.register("Order", Order);
  registry.register("EvmToken", EvmToken);
  registry.register("EvmAuthCaptureEscrowConfig", EvmAuthCaptureEscrowConfig);
  registry.register("EvmAuthCaptureEscrowInstrument", EvmAuthCaptureEscrowInstrument);
  registry.register("PaymentCredential", PaymentCredential);
  registry.register("PaymentInstrument", PaymentInstrument);
  registry.register("Payment", Payment);
  registry.register("DeliveryEventVocabulary", DeliveryEventVocabulary);

  // Paths
  registry.registerPath({
    method: "get",
    path: "/.well-known/local-protocol",
    tags: ["discovery"],
    summary: "Service discovery",
    description: "Returns server capabilities, supported standards, and endpoint paths.",
    operationId: "getDiscovery",
    responses: {
      200: { description: "Discovery metadata.", content: { "application/json": { schema: DiscoveryResponse } } },
      500: { description: "Internal server error.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/healthz",
    tags: ["discovery"],
    summary: "Health check",
    description: "Returns server health status.",
    operationId: "getHealth",
    responses: {
      200: { description: "Server is healthy.", content: { "application/json": { schema: HealthResponse } } },
      503: { description: "Service unavailable.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/requests",
    tags: ["requests"],
    summary: "Create delivery request",
    description: "Submit a new delivery request. The `nonce` field provides idempotency.",
    operationId: "createRequest",
    request: { body: { content: { "application/json": { schema: DeliveryRequest } } } },
    responses: {
      201: { description: "Request created.", content: { "application/json": { schema: DeliveryRequest } } },
      400: { description: "Invalid nonce.", content: { "application/json": { schema: ErrorResponse } } },
      409: { description: "Duplicate nonce or request ID.", content: { "application/json": { schema: ErrorResponse } } },
      422: { description: "Validation errors.", content: { "application/json": { schema: ValidationErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/requests",
    tags: ["requests"],
    summary: "List delivery requests",
    description: "Returns all delivery requests.",
    operationId: "listRequests",
    responses: {
      200: {
        description: "List of requests.",
        content: {
          "application/json": {
            schema: z.array(DeliveryRequest),
          },
        },
      },
      500: { description: "Internal server error.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/requests/{request_id}",
    tags: ["requests"],
    summary: "Get delivery request",
    description: "Returns a single delivery request by ID.",
    operationId: "getRequest",
    request: { params: z.object({ request_id: RequestId }) },
    responses: {
      200: { description: "The request.", content: { "application/json": { schema: DeliveryRequest } } },
      404: { description: "Request not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/requests/{request_id}/quotes",
    tags: ["quotes"],
    summary: "Create quote",
    description: "Submit a quote for a delivery request. The `nonce` field provides idempotency.",
    operationId: "createQuote",
    request: {
      params: z.object({ request_id: RequestId }),
      body: { content: { "application/json": { schema: DeliveryQuote } } },
    },
    responses: {
      201: { description: "Quote created.", content: { "application/json": { schema: DeliveryQuote } } },
      400: { description: "Invalid nonce.", content: { "application/json": { schema: ErrorResponse } } },
      404: { description: "Request not found.", content: { "application/json": { schema: ErrorResponse } } },
      409: { description: "Duplicate nonce or quote ID.", content: { "application/json": { schema: ErrorResponse } } },
      422: { description: "Validation errors.", content: { "application/json": { schema: ValidationErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/requests/{request_id}/quotes",
    tags: ["quotes"],
    summary: "List quotes for request",
    description: "Returns all quotes for a delivery request.",
    operationId: "listQuotes",
    request: { params: z.object({ request_id: RequestId }) },
    responses: {
      200: {
        description: "List of quotes.",
        content: { "application/json": { schema: z.array(DeliveryQuote) } },
      },
      404: { description: "Request not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/requests/{request_id}/quotes/{quote_id}",
    tags: ["quotes"],
    summary: "Get quote",
    description: "Returns a single quote by ID.",
    operationId: "getQuote",
    request: { params: z.object({ request_id: RequestId, quote_id: QuoteId }) },
    responses: {
      200: { description: "The quote.", content: { "application/json": { schema: DeliveryQuote } } },
      404: { description: "Request or quote not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/deliveries",
    tags: ["deliveries"],
    summary: "Create delivery",
    description: "Create a delivery from an accepted quote. The `nonce` field provides idempotency.",
    operationId: "createDelivery",
    request: { body: { content: { "application/json": { schema: CreateDeliveryRequest } } } },
    responses: {
      201: { description: "Delivery created.", content: { "application/json": { schema: Delivery } } },
      400: { description: "Invalid request.", content: { "application/json": { schema: ErrorResponse } } },
      404: { description: "Request or quote not found.", content: { "application/json": { schema: ErrorResponse } } },
      409: { description: "Duplicate nonce or nonce reuse with different payload.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/deliveries",
    tags: ["deliveries"],
    summary: "List deliveries",
    description: "Returns all deliveries.",
    operationId: "listDeliveries",
    responses: {
      200: { description: "List of deliveries.", content: { "application/json": { schema: z.array(Delivery) } } },
      500: { description: "Internal server error.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/deliveries/{delivery_id}",
    tags: ["deliveries"],
    summary: "Get delivery",
    description: "Returns a single delivery by ID.",
    operationId: "getDelivery",
    request: { params: z.object({ delivery_id: DeliveryId }) },
    responses: {
      200: { description: "The delivery.", content: { "application/json": { schema: Delivery } } },
      404: { description: "Delivery not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "patch",
    path: "/deliveries/{delivery_id}/event",
    tags: ["deliveries"],
    summary: "Update delivery event",
    description:
      "Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.",
    operationId: "updateDeliveryEvent",
    request: {
      params: z.object({ delivery_id: DeliveryId }),
      body: { content: { "application/json": { schema: UpdateEventRequest } } },
    },
    responses: {
      200: { description: "Delivery event updated.", content: { "application/json": { schema: Delivery } } },
      404: { description: "Delivery not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/merchants/{merchant_id}",
    tags: ["merchants"],
    summary: "Get merchant",
    description: "Returns a merchant with its full denormalized catalog tree.",
    operationId: "getMerchant",
    request: { params: z.object({ merchant_id: MerchantId }) },
    responses: {
      200: { description: "The merchant.", content: { "application/json": { schema: Merchant } } },
      404: { description: "Merchant not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/orders/requests",
    tags: ["orders"],
    summary: "Create order request",
    description: "Submit a new order request with a cart. The `nonce` field provides idempotency.",
    operationId: "createOrderRequest",
    request: { body: { content: { "application/json": { schema: Cart } } } },
    responses: {
      201: { description: "Order request created.", content: { "application/json": { schema: OrderRequest } } },
      400: { description: "Invalid request.", content: { "application/json": { schema: ErrorResponse } } },
      409: { description: "Duplicate nonce or request ID.", content: { "application/json": { schema: ErrorResponse } } },
      422: { description: "Validation errors.", content: { "application/json": { schema: ValidationErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/orders/requests/{order_request_id}/quotes",
    tags: ["orders"],
    summary: "List order quotes",
    description: "Returns all quotes for an order request.",
    operationId: "listOrderQuotes",
    request: { params: z.object({ order_request_id: OrderRequestId }) },
    responses: {
      200: { description: "List of order quotes.", content: { "application/json": { schema: z.array(OrderQuote) } } },
      404: { description: "Order request not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/orders/requests/{order_request_id}/quotes/{order_quote_id}",
    tags: ["orders"],
    summary: "Get order quote",
    description: "Returns a single order quote by ID.",
    operationId: "getOrderQuote",
    request: { params: z.object({ order_request_id: OrderRequestId, order_quote_id: OrderQuoteId }) },
    responses: {
      200: { description: "The order quote.", content: { "application/json": { schema: OrderQuote } } },
      404: { description: "Order request or quote not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/orders",
    tags: ["orders"],
    summary: "Create order",
    description: "Accept a quote and create an order. The `nonce` field provides idempotency.",
    operationId: "createOrder",
    request: { body: { content: { "application/json": { schema: CreateOrderRequest } } } },
    responses: {
      201: { description: "Order created.", content: { "application/json": { schema: Order } } },
      400: { description: "Invalid nonce or quote does not belong to request.", content: { "application/json": { schema: ErrorResponse } } },
      404: { description: "Order request or quote not found.", content: { "application/json": { schema: ErrorResponse } } },
      409: { description: "Duplicate nonce.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/orders/{order_id}",
    tags: ["orders"],
    summary: "Get order",
    description: "Returns a single order by ID.",
    operationId: "getOrder",
    request: { params: z.object({ order_id: OrderId }) },
    responses: {
      200: { description: "The order.", content: { "application/json": { schema: Order } } },
      404: { description: "Order not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "get",
    path: "/event-vocabularies/{name}",
    tags: ["events"],
    summary: "Get event vocabulary",
    description: "Returns a delivery event vocabulary by name.",
    operationId: "getEventVocabulary",
    request: { params: z.object({ name: EventVocabularyName }) },
    responses: {
      200: { description: "The event vocabulary.", content: { "application/json": { schema: DeliveryEventVocabulary } } },
      404: { description: "Event vocabulary not found.", content: { "application/json": { schema: ErrorResponse } } },
    },
  });

  registry.registerPath({
    method: "post",
    path: "/payment-instruments",
    tags: ["payments"],
    summary: "Register payment instrument",
    description: "Register a payment instrument for use in order creation.",
    operationId: "createPaymentInstrument",
    request: { body: { content: { "application/json": { schema: EvmAuthCaptureEscrowInstrument } } } },
    responses: {
      201: { description: "Payment instrument registered.", content: { "application/json": { schema: EvmAuthCaptureEscrowInstrument } } },
      400: { description: "Invalid instrument data.", content: { "application/json": { schema: ErrorResponse } } },
      422: { description: "Validation errors.", content: { "application/json": { schema: ValidationErrorResponse } } },
    },
  });

  const docConfig = {
    openapi: "3.1.0",
    info: {
      title: "Local Protocol",
      description: "Local Protocol delivery API. Covers service discovery, delivery requests, quotes, and deliveries.",
      version: "0.1.0",
    },
    servers: [{ url: "http://localhost:8000", description: "Local development server" }],
    tags: [
      { name: "discovery", description: "Service discovery and health" },
      { name: "requests", description: "Delivery request operations" },
      { name: "quotes", description: "Delivery quote operations" },
      { name: "deliveries", description: "Delivery lifecycle operations" },
      { name: "merchants", description: "Merchant and catalog operations" },
      { name: "orders", description: "Order lifecycle operations" },
      { name: "events", description: "Event vocabulary operations" },
      { name: "payments", description: "Payment instrument operations" },
    ],
  };

  const generator = new OpenApiGeneratorV31(registry.definitions);
  let generated = generator.generateDocument(docConfig) as unknown as Record<string, unknown>;

  generated = rewriteSchemaRefs(generated) as Record<string, unknown>;
  rekeyComponentSchemas(generated);

  // Post-process: merge x-codeSamples from existing spec, then reorder to match
  if (fs.existsSync(SPEC_PATH)) {
    const originalJson = fs.readFileSync(SPEC_PATH, "utf8");
    const original = JSON.parse(originalJson) as Record<string, unknown>;
    mergeCodeSamples(original, generated);
    generated = reorderToMatch(original, generated) as Record<string, unknown>;
  }

  rekeyComponentSchemas(generated);

  ensureSpecDir();
  fs.writeFileSync(SPEC_PATH, JSON.stringify(generated, null, 2) + "\n", "utf8");
  console.log("Generated", SPEC_PATH);
}

main();
