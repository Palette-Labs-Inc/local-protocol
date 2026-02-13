import * as z from "zod";

const META = { id: (path: string) => ({ id: path }) };

// Cart item
export const CartItem = z
  .object({
    id: z.string().describe("Item identifier."),
    quantity: z.int().min(1).describe("Quantity requested."),
  })
  .strict()
  .meta({
    ...META.id("order/types/cart_item.json"),
    title: "Cart Item",
  });

// Order request
export const OrderRequest = z
  .object({
    id: z.string().describe("Unique request identifier."),
    intent_id: z.string().describe("Shared intent identifier for tracing Request → Quote → Order."),
    nonce: z.string().describe("Client-generated idempotency key."),
  })
  .strict()
  .meta({
    ...META.id("order/request.json"),
    title: "OrderRequest",
  });

// Order quote
export const OrderQuote = z
  .object({
    id: z.string().describe("Unique quote identifier."),
    intent_id: z.string().describe("Shared intent identifier for tracing Request → Quote → Order."),
    nonce: z.string().describe("Client-generated idempotency key."),
    price: z.int().describe("Price in minor currency units."),
    ready_at: z.iso.datetime().describe("Estimated readiness time (RFC 3339)."),
    expires_at: z.iso.datetime().describe("Quote expiration time (RFC 3339)."),
  })
  .strict()
  .meta({
    ...META.id("order/quote.json"),
    title: "OrderQuote",
  });

// Order
export const Order = z
  .object({
    id: z.string().describe("Unique order identifier."),
    intent_id: z.string().describe("Shared intent identifier for tracing Request → Quote → Order."),
    nonce: z.string().describe("Client-generated idempotency key."),
    payment_instrument_id: z.string().describe("Reference to the payment instrument used to create this order."),
  })
  .strict()
  .meta({
    ...META.id("order/order.json"),
    title: "Order",
  });

// Cart
export const Cart = z
  .object({
    id: z.string().describe("Unique cart identifier."),
    intent_id: z.string().describe("Shared intent identifier for tracing Request → Quote → Order."),
    nonce: z.string().describe("Client-generated idempotency key."),
    items: z.array(CartItem).describe("Items in the cart."),
  })
  .strict()
  .meta({
    ...META.id("order/cart.json"),
    title: "Cart",
  });
