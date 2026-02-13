import * as z from "zod";

const META = { id: (path: string) => ({ id: path }) };

// Postal address (UCP)
export const PostalAddress = z
  .object({
    extended_address: z.string().optional().describe("An address extension such as an apartment number, C/O or alternative name."),
    street_address: z.string().optional().describe("The street address."),
    address_locality: z.string().optional().describe("The locality in which the street address is, and which is in the region. For example, Mountain View."),
    address_region: z.string().optional().describe("The region in which the locality is, and which is in the country. Required for applicable countries (i.e. state in US, province in CA). For example, California or another appropriate first-level Administrative division."),
    address_country: z.string().optional().describe('The country. Recommended to be in 2-letter ISO 3166-1 alpha-2 format, for example "US". For backward compatibility, a 3-letter ISO 3166-1 alpha-3 country code such as "SGP" or a full country name such as "Singapore" can also be used.'),
    postal_code: z.string().optional().describe("The postal code. For example, 94043."),
    first_name: z.string().optional().describe("Optional. First name of the contact associated with the address."),
    last_name: z.string().optional().describe("Optional. Last name of the contact associated with the address."),
    phone_number: z.string().optional().describe("Optional. Phone number of the contact associated with the address."),
  })
  .meta({
    ...META.id("ucp/shopping/types/postal_address.json"),
    title: "Postal Address",
  });

// Payment credential base
export const PaymentCredential = z
  .object({
    type: z.string().describe("The credential type discriminator. Specific schemas will constrain this to a constant value."),
  })
  .passthrough()
  .meta({
    ...META.id("ucp/shopping/types/payment_credential.json"),
    title: "Payment Credential",
    description: "The base definition for any payment credential. Handlers define specific credential types.",
  });

// Payment instrument base
export const PaymentInstrument = z
  .object({
    id: z.string().describe("A unique identifier for this instrument instance, assigned by the platform."),
    handler_id: z.string().describe("The unique identifier for the handler instance that produced this instrument. This corresponds to the 'id' field in the Payment Handler definition."),
    type: z.string().describe("The broad category of the instrument (e.g., 'card', 'tokenized_card'). Specific schemas will constrain this to a constant value."),
    billing_address: PostalAddress.optional().describe("The billing address associated with this payment method."),
    credential: PaymentCredential.optional(),
    display: z.record(z.string(), z.unknown()).optional().describe("Display information for this payment instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler."),
  })
  .passthrough()
  .meta({
    ...META.id("ucp/shopping/types/payment_instrument.json"),
    title: "Payment Instrument",
    description: "The base definition for any payment instrument. It links the instrument to a specific payment handler.",
  });

// Payment config. Runtime uses PaymentInstrument; JSON Schema refs selected_payment_instrument (see paymentJsonSchema).
export const Payment = z
  .object({
    instruments: z.array(PaymentInstrument).describe("The payment instruments available for this payment. Each instrument is associated with a specific handler via the handler_id field. Handlers can extend the base payment_instrument schema to add handler-specific fields."),
  })
  .meta({
    ...META.id("ucp/shopping/payment.json"),
    title: "Payment",
    description: "Payment configuration containing handlers.",
  });

/** JSON Schema for Payment: instruments items ref payment_instrument#/$defs/selected_payment_instrument (Zod cannot emit cross-schema $defs ref). */
export function paymentJsonSchema(): Record<string, unknown> {
  return {
    $schema: "https://json-schema.org/draft/2020-12/schema",
    title: "Payment",
    description: "Payment configuration containing handlers.",
    type: "object",
    properties: {
      instruments: {
        type: "array",
        items: { $ref: "types/payment_instrument.json#/$defs/selected_payment_instrument" },
        description:
          "The payment instruments available for this payment. Each instrument is associated with a specific handler via the handler_id field. Handlers can extend the base payment_instrument schema to add handler-specific fields.",
      },
    },
  };
}

/** JSON Schema for Payment Instrument with $defs/selected_payment_instrument (Zod cannot emit $defs with self-ref). */
export function paymentInstrumentJsonSchema(): Record<string, unknown> {
  return {
    $schema: "https://json-schema.org/draft/2020-12/schema",
    title: "Payment Instrument",
    description:
      "The base definition for any payment instrument. It links the instrument to a specific payment handler.",
    type: "object",
    required: ["id", "handler_id", "type"],
    properties: {
      id: {
        type: "string",
        description:
          "A unique identifier for this instrument instance, assigned by the platform.",
      },
      handler_id: {
        type: "string",
        description:
          "The unique identifier for the handler instance that produced this instrument. This corresponds to the 'id' field in the Payment Handler definition.",
      },
      type: {
        type: "string",
        description:
          "The broad category of the instrument (e.g., 'card', 'tokenized_card'). Specific schemas will constrain this to a constant value.",
      },
      billing_address: {
        $ref: "postal_address.json",
        description: "The billing address associated with this payment method.",
      },
      credential: { $ref: "payment_credential.json" },
      display: {
        type: "object",
        description:
          "Display information for this payment instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.",
      },
    },
    additionalProperties: true,
    $defs: {
      selected_payment_instrument: {
        title: "Selected Payment Instrument",
        description: "A payment instrument with selection state.",
        allOf: [
          { $ref: "#" },
          {
            type: "object",
            properties: {
              selected: {
                type: "boolean",
                description: "Whether this instrument is selected by the user.",
              },
            },
          },
        ],
      },
    },
  };
}
