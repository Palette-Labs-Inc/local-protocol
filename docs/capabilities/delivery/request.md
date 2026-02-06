# Delivery Request

Delivery request posted by a requester, including route and requested timing.

## Fields

- `id` (string, required): Unique request identifier.
- `nonce` (string, required): Client-generated idempotency key.
- `pickup_location` (object, required): Pickup location (postal address or coordinates).
- `dropoff_location` (object, required): Dropoff location (postal address or coordinates).
- `pickup_time` (string, required): Requested pickup time (RFC 3339).
- `dropoff_time` (string, required): Requested dropoff time (RFC 3339).
- `pickup_instructions` (string, optional): Pickup directions, access codes, or handling notes.
- `dropoff_instructions` (string, optional): Dropoff directions, access codes, or delivery notes.

## Example

```json
{
  "id": "request_456",
  "nonce": "request-nonce-456",
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
      "extended_address": "Suite 500",
      "address_locality": "San Francisco",
      "address_region": "CA",
      "postal_code": "94105",
      "address_country": "US"
    },
    "coordinates": {
      "latitude": 37.7897,
      "longitude": -122.3961
    },
    "contact": {
      "name": "Alex Rivera",
      "phone": "+1-415-555-0123"
    }
  },
  "pickup_time": "2026-01-30T19:00:00Z",
  "dropoff_time": "2026-01-30T19:30:00Z",
  "pickup_instructions": "Back door pickup.",
  "dropoff_instructions": "Leave with front desk."
}
```
