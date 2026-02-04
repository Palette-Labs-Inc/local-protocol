# Delivery Quote

Delivery quote offered by a provider, including price, route, and estimated timing.

## Fields

- `id` (string, required): Unique quote identifier.
- `nonce` (string, required): Client-generated idempotency key.
- `price` (integer, required): Price in minor currency units.
- `currency` (string, required): ISO 4217 currency code.
- `pickup_location` (object, required): Pickup location (postal address or coordinates).
- `dropoff_location` (object, required): Dropoff location (postal address or coordinates).
- `pickup_estimate` (string, required): Estimated pickup time (RFC 3339).
- `dropoff_estimate` (string, required): Estimated dropoff time (RFC 3339).

## Example

```json
{
  "id": "quote_123",
  "nonce": "quote-nonce-123",
  "price": 1299,
  "currency": "USD",
  "pickup_location": {
    "postal_address": {
      "street_address": "123 Market St",
      "address_locality": "San Francisco",
      "address_region": "CA",
      "postal_code": "94103",
      "address_country": "US"
    }
  },
  "dropoff_location": {
    "postal_address": {
      "street_address": "456 Mission St",
      "address_locality": "San Francisco",
      "address_region": "CA",
      "postal_code": "94105",
      "address_country": "US"
    },
    "coordinates": {
      "latitude": 37.7818,
      "longitude": -122.4056
    }
  },
  "pickup_estimate": "2026-01-30T19:15:00Z",
  "dropoff_estimate": "2026-01-30T19:35:00Z"
}
```
