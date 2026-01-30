# Delivery Location

Location used in delivery bids and asks. A location requires a postal address and can include optional coordinates.

## Fields

- `postal_address` (object, required): Postal address using the UCP `postal_address` schema.
- `coordinates` (object, optional): Coordinates with latitude and longitude.

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
    "lat": 37.7897,
    "lng": -122.3961
  }
}
```
