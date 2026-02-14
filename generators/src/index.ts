/**
 * Zod schema definitions that generate JSON Schema identical to local-protocol/schemas
 * via z.toJSONSchema(). Define schemas in Zod here; use toJSONSchema() or the generate
 * script to emit draft-2020-12 JSON Schema files.
 *
 * @see https://zod.dev/json-schema
 */

export { toJSONSchema, toJSONSchemaFromRegistry } from "./to-json-schema";
export type { ToJSONSchemaOptions } from "./to-json-schema";

export { FiatCurrency, EvmCurrency, Amount, Media, EvmAmount } from "./schemas/shared";
export { PostalAddress, PaymentCredential, PaymentInstrument, Payment } from "./schemas/ucp";
export { Coordinates, Location, DeliveryRequest, DeliveryQuote, Delivery } from "./schemas/delivery";
export { DeliveryEventVocabulary } from "./schemas/delivery-events";
export { CartItem, OrderRequest, OrderQuote, Order, Cart } from "./schemas/order";
export { EvmToken, EvmAuthCaptureEscrowConfig, EvmAuthCaptureEscrowInstrument } from "./schemas/payment";
export {
  Interval,
  Availability,
  ModifierItem,
  ModifierGroup,
  ModifierOption,
  CatalogItem,
  CatalogCategory,
  Catalog,
  Merchant,
} from "./schemas/catalog";
