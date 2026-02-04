# Delivery Location

Location used in delivery quotes and requests. A location must include a postal address or coordinates (or both).

## Fields

- `postal_address` (object, optional): Postal address using the UCP `postal_address` schema.
- `coordinates` (object, optional): Coordinates with latitude and longitude.
  - At least one of `postal_address` or `coordinates` is required.

## Example (postal address only)

```json
{
  "postal_address": {
    "street_address": "123 Market St",
    "address_locality": "San Francisco",
    "address_region": "CA",
    "postal_code": "94103",
    "address_country": "US"
  }
}
```

## Example (postal address and coordinates)

```json
{
  "postal_address": {
    "street_address": "456 Mission St",
    "address_locality": "San Francisco",
    "address_region": "CA",
    "postal_code": "94105",
    "address_country": "US"
  },
  "coordinates": {
    "latitude": 37.7897,
    "longitude": -122.3961
  }
}
```
