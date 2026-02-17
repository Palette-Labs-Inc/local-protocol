# Add UCP Discovery

Publish a UCP discovery profile so platforms can find your services, capabilities, and payment handlers.

## Overview

A UCP discovery profile is a JSON document hosted at `/.well-known/ucp` that tells platforms:

- **What transports your service speaks** (`services`) — REST, MCP, A2A, or embedded
- **What domain capabilities you support** (`capabilities`) — the schemas that describe your data model
- **How you handle payments** (`payment_handlers`) — tokenization, processing, and payment config

Each section is keyed by a reverse-domain identifier (e.g., `xyz.localprotocol.delivery`) and contains an array of versioned entries.

## Steps

1. Create a JSON file with a top-level `ucp` object.
2. Set `ucp.version` to the UCP spec version you conform to (e.g., `"2026-01-23"`).
3. Under `ucp.services`, add an entry for each transport your service supports. Each entry needs `version`, `spec`, `transport`, and `endpoint` (plus `schema` for transports that have a machine-readable contract).
4. Under `ucp.capabilities`, declare the domain schemas your service implements. Use `extends` to express that one capability builds on another.
5. Under `ucp.payment_handlers`, declare any payment processing integrations, including tokenization config.
6. Optionally include `signing_keys` for request/response signing.
7. Host the document at `https://your-domain/.well-known/ucp` and keep it current as capabilities change.

## Example: delivery service profile

This example shows a delivery business advertising its service over two transports (REST and MCP), with a delivery capability referencing the [local-protocol delivery schema](../../schemas/delivery/delivery.json), and a payment handler for card tokenization.

```json
{
  "ucp": {
    "version": "2026-01-23",

    "services": {
      "xyz.localprotocol.delivery": [
        {
          "version": "2026-01-23",
          "spec": "https://localprotocol.xyz/specification/delivery",
          "transport": "rest",
          "endpoint": "https://api.example.com/ucp/v1",
          "schema": "https://localprotocol.xyz/2026-01-23/services/delivery/rest.openapi.json"
        },
        {
          "version": "2026-01-23",
          "spec": "https://localprotocol.xyz/specification/delivery",
          "transport": "mcp",
          "endpoint": "https://api.example.com/ucp/mcp",
          "schema": "https://localprotocol.xyz/2026-01-23/services/delivery/mcp.openrpc.json"
        }
      ]
    },

    "capabilities": {
      "xyz.localprotocol.delivery": [
        {
          "version": "2026-01-23",
          "spec": "https://localprotocol.xyz/specification/delivery",
          "schema": "https://localprotocol.xyz/schemas/delivery/delivery.json"
        }
      ]
    },

    "payment_handlers": {
      "com.example.processor_tokenizer": [
        {
          "id": "processor_tokenizer",
          "version": "2026-01-23",
          "spec": "https://example.com/specs/payments/processor_tokenizer",
          "schema": "https://example.com/specs/payments/processor_tokenizer.json",
          "config": {
            "type": "CARD",
            "tokenization_specification": {
              "type": "PUSH",
              "parameters": {
                "token_retrieval_url": "https://api.psp.example.com/v1/tokens"
              }
            }
          }
        }
      ]
    }
  },

  "signing_keys": [
    {
      "kid": "delivery_2026",
      "kty": "EC",
      "crv": "P-256",
      "x": "WbbXwVYGdJoP4Xm3qCkGvBRcRvKtEfXDbWvPzpPS8LA",
      "y": "sP4jHHxYqC89HBo8TjrtVOAGHfJDflYxw7MFMxuFMPY",
      "use": "sig",
      "alg": "ES256"
    }
  ]
}
```

### What each section does

| Section | Purpose | Keys are |
|---|---|---|
| `services` | Declares how to call your API — one entry per transport | Reverse-domain service identifiers |
| `capabilities` | Declares what domain schemas your service implements | Reverse-domain capability identifiers |
| `payment_handlers` | Declares payment processing integrations | Reverse-domain handler identifiers |
| `signing_keys` | Public keys for verifying signed requests/responses | N/A (top-level array) |

### Transport types

| Transport | `endpoint` required? | `schema` required? | Description |
|---|---|---|---|
| `rest` | Yes | Yes (OpenAPI) | Standard REST API |
| `mcp` | Yes | Yes (OpenRPC) | Model Context Protocol |
| `a2a` | Yes (agent card URL) | No | Agent-to-Agent protocol |
| `embedded` | No | Yes (OpenRPC) | Inline protocol for embedded integrations |

## Next steps

- Review the [delivery schemas](../../schemas/delivery/) to understand the data model referenced by the capabilities above.
- See [Understanding Capabilities](./understanding-capabilities.md) for how capabilities and extensions compose.
- See the [Payment Handler Guide](../capabilities/payment/handler-guide.md) for details on payment handler configuration.
