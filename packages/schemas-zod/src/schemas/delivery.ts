import * as z from "zod";
import { PostalAddress } from "./ucp.js";
import { Payment } from "./ucp.js";

const META = { id: (path: string) => ({ id: path }) };

// Latitude/longitude
export const Coordinates = z
  .object({
    latitude: z.number().min(-90).max(90).describe("Latitude in decimal degrees."),
    longitude: z.number().min(-180).max(180).describe("Longitude in decimal degrees."),
  })
  .strict()
  .meta({
    ...META.id("delivery/types/coordinates.json"),
    title: "Coordinates",
  });

// Location (postal address or coordinates). Runtime union; JSON Schema is single object + anyOf required (see locationJsonSchema).
export const Location = z
  .union([
    z.object({ postal_address: PostalAddress, coordinates: Coordinates.optional() }).strict(),
    z.object({ coordinates: Coordinates, postal_address: PostalAddress.optional() }).strict(),
  ])
  .meta({
    ...META.id("delivery/types/location.json"),
    title: "Location",
  });

/** JSON Schema for Location: single object + anyOf required (Zod union would emit oneOf of two objects). */
export function locationJsonSchema(refs: { postal_address: string; coordinates: string }): Record<string, unknown> {
  return {
    $schema: "https://json-schema.org/draft/2020-12/schema",
    title: "Location",
    type: "object",
    additionalProperties: false,
    properties: {
      postal_address: { $ref: refs.postal_address, description: "Postal address for the location." },
      coordinates: { $ref: refs.coordinates, description: "Coordinates for the location." },
    },
    anyOf: [{ required: ["postal_address"] }, { required: ["coordinates"] }],
  };
}

// Delivery request
export const DeliveryRequest = z
  .object({
    id: z.string().describe("Unique request identifier."),
    nonce: z.string().describe("Client-generated idempotency key."),
    pickup_location: Location.describe("Pickup location for the delivery."),
    dropoff_location: Location.describe("Dropoff location for the delivery."),
    pickup_time: z.iso.datetime().describe("Requested pickup time (RFC 3339)."),
    dropoff_time: z.iso.datetime().describe("Requested dropoff time (RFC 3339)."),
    pickup_instructions: z.string().optional().describe("Pickup directions, access codes, or handling notes."),
    dropoff_instructions: z.string().optional().describe("Dropoff directions, access codes, or delivery notes."),
  })
  .strict()
  .meta({
    ...META.id("delivery/request.json"),
    title: "DeliveryRequest",
  });

// Delivery quote
export const DeliveryQuote = z
  .object({
    id: z.string().describe("Unique quote identifier."),
    nonce: z.string().describe("Client-generated idempotency key."),
    price: z.int().min(0).describe("Price in minor currency units."),
    currency: z.string().regex(/^[A-Z]{3}$/).describe("ISO 4217 currency code."),
    pickup_location: Location.describe("Pickup location for the delivery."),
    dropoff_location: Location.describe("Dropoff location for the delivery."),
    pickup_estimate: z.iso.datetime().describe("Estimated pickup time (RFC 3339)."),
    dropoff_estimate: z.iso.datetime().describe("Estimated dropoff time (RFC 3339)."),
    expires_at: z.iso.datetime().optional().describe("Time when the quote expires (RFC 3339)."),
    payment: Payment.describe("Payment handlers available for accepting this quote."),
  })
  .strict()
  .meta({
    ...META.id("delivery/quote.json"),
    title: "DeliveryQuote",
  });

// Delivery resource
export const Delivery = z
  .object({
    id: z.string().describe("Unique delivery identifier."),
    request_id: z.string().describe("Reference to the original request."),
    quote_id: z.string().describe("Reference to the accepted quote."),
    payment_instrument_id: z.string().describe("Reference to the payment instrument used to create this delivery."),
    event: z.string().describe("Current event identifier."),
    event_description: z.string().describe("Human-readable description of the current event."),
    event_vocabulary: z.string().describe("Event vocabulary standard in use."),
    webhook_url: z.string().nullable().optional().describe("Registered webhook URL, if any."),
    created_at: z.iso.datetime().describe("Delivery creation timestamp (RFC 3339)."),
    updated_at: z.iso.datetime().describe("Last update timestamp (RFC 3339)."),
  })
  .strict()
  .meta({
    ...META.id("delivery/delivery.json"),
    title: "Delivery",
    description: "Delivery resource created when a quote is accepted.",
  });
