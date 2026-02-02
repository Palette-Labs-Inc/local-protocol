# Add UCP Discovery

Publish a UCP discovery profile so platforms can find your services and capabilities.

## Steps

1. Create a business discovery profile at `/.well-known/ucp`.
2. Include `ucp.version`, `ucp.services`, `ucp.capabilities`, and `ucp.payment_handlers` in the profile.
3. For each service, list its `version`, `spec`, `transport`, and `endpoint` (and `schema` when applicable).
4. For each capability, list its `name`, `version`, `spec`, and `schema` (and `extends` if it is an extension).
5. Host the discovery document at `https://your-domain/.well-known/ucp` and keep it updated as capabilities change.

## Minimal example (business profile)

```json
{
  "ucp": {
    "version": "YYYY-MM-DD",
    "services": {
      "dev.example.delivery": [
        {
          "version": "YYYY-MM-DD",
          "spec": "https://example.com/specs/delivery",
          "transport": "rest",
          "endpoint": "https://api.example.com/delivery",
          "schema": "https://example.com/schemas/delivery/openapi.json"
        }
      ]
    },
    "capabilities": [
      {
        "name": "com.example.delivery",
        "version": "YYYY-MM-DD",
        "spec": "https://example.com/specs/local-protocol/delivery",
        "schema": "https://example.com/schemas/local-protocol/delivery/bid.json"
      }
    ],
    "payment_handlers": {}
  }
}
```

## Next steps

- Review the UCP documentation for discovery and registration details (well-known file format, required fields).
