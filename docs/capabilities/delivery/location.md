# Delivery Location

Location used in delivery bids and asks. A location can include a postal address, coordinates, or both.

## Fields

- `coordinates` (object, required): Coordinates with latitude and longitude.
- `postal_address` (object, optional): Postal address using the UCP `postal_address` schema.

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

## Example (coordinates only)

```json
{
  "coordinates": {
    "lat": 37.7818,
    "lng": -122.4056
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
