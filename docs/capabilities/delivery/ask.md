# Delivery Ask

Delivery ask posted by a requester, including route and requested timing.

## Fields

- `id` (string, required): Unique ask identifier.
- `pickup_location` (object, required): Pickup location (postal address or coordinates).
- `dropoff_location` (object, required): Dropoff location (postal address or coordinates).
- `pickup_time` (string, required): Requested pickup time (RFC 3339).
- `dropoff_time` (string, required): Requested dropoff time (RFC 3339).

## Example

```json
{
  "id": "ask_456",
  "pickup_location": {
    "coordinates": {
      "lat": 37.7765,
      "lng": -122.4167
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
      "lat": 37.7897,
      "lng": -122.3961
    }
  },
  "pickup_time": "2026-01-30T19:00:00Z",
  "dropoff_time": "2026-01-30T19:30:00Z"
}
```
