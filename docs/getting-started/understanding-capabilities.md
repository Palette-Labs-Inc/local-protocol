# Understanding Capabilities

Capabilities describe *what* a business supports (catalog, delivery, order, payment) and are activated through transport bindings that describe *how* you call them. The flow is the same regardless of transport:

1. **Discover** the business profile at `/.well-known/ucp`.
2. **Negotiate** capabilities by intersecting the platform profile with the business profile.
3. **Select a transport** from `ucp.services` (REST, MCP, A2A) and use the capability's schema/operations.

Below are minimal examples of the same capability (Catalog) across the three transports.

## REST example

REST is the default transport. Endpoints come from the business profile (`ucp.services["dev.example.local"].transport=rest`). Use `UCP-Agent` to identify the platform profile.

```http
GET /capabilities/catalog/catalogs/cat_1 HTTP/1.1
UCP-Agent: profile="https://platform.example/profiles/catalog-agent.json"
Content-Type: application/json
```

```json
{
  "catalog": {
    "id": "cat_1",
    "name": "Breakfast",
    "description": "Morning menu",
    "categories": [
      {
        "id": "catg_1",
        "name": "Tacos",
        "items": [
          {
            "id": "item_1",
            "name": "Carnitas Taco",
            "description": "Slow-cooked pork with salsa verde.",
            "price": { "value": "450", "currency": { "symbol": "USD" } }
          }
        ]
      }
    ]
  }
}
```

## MCP example

MCP uses JSON-RPC and maps UCP capabilities 1:1 to MCP tools. The business advertises an MCP endpoint in its profile, and clients call `tools/call` with the operation in `params.name`. Every request must include `meta.ucp-agent.profile` for negotiation.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_catalog",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://platform.example/profiles/catalog-agent.json"
        }
      },
      "id": "cat_1"
    }
  }
}
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "catalog": {
      "id": "cat_1",
      "name": "Breakfast",
      "categories": [
        {
          "id": "catg_1",
          "name": "Tacos",
          "items": [
            {
              "id": "item_1",
              "name": "Carnitas Taco",
              "price": { "value": "450", "currency": { "symbol": "USD" } }
            }
          ]
        }
      ]
    }
  }
}
```

## A2A example

A2A uses an Agent Card to advertise the UCP extension. The business profile points at the agent card (`transport: "a2a"`), and the card declares the UCP extension and active capabilities. Platforms include `UCP-Agent` and `X-A2A-Extensions` headers on requests.

**Agent Card (business):**

```json
{
  "extensions": [
    {
      "uri": "https://ucp.dev/specification/reference?v=2026-01-23",
      "description": "Business agent supporting UCP",
      "params": {
        "capabilities": {
          "dev.example.catalog": [{"version": "2026-01-23"}]
        }
      }
    }
  ]
}
```

**Message (platform to business agent):**

```json
{
  "messageId": "msg_001",
  "contextId": "ctx_abc",
  "dataParts": [
    {
      "type": "application/ucp+json",
      "data": {
        "catalog": {
          "id": "cat_1"
        }
      }
    }
  ]
}
```

**Message (business agent response):**

```json
{
  "messageId": "msg_002",
  "contextId": "ctx_abc",
  "dataParts": [
    {
      "type": "application/ucp+json",
      "data": {
        "catalog": {
          "id": "cat_1",
          "name": "Breakfast",
          "categories": [
            {
              "id": "catg_1",
              "name": "Tacos",
              "items": [
                {
                  "id": "item_1",
                  "name": "Carnitas Taco",
                  "price": { "value": "450", "currency": { "symbol": "USD" } }
                }
              ]
            }
          ]
        }
      }
    }
  ]
}
```

## Notes

- Use the business `/.well-known/ucp` profile as the source of truth for transport endpoints and capability schemas.
- Only rely on capabilities that appear in the negotiated intersection.
- Idempotency keys are required for non-idempotent writes (header for REST, `meta.idempotency-key` for MCP).
- MCP tools follow a `create/get/update/cancel/complete` naming pattern by resource.
- A2A exchanges are conversational; preserve `contextId` and any `taskId` returned by the agent, and use stable message IDs for retry detection.
- Error handling and retries follow the transport rules (HTTP status codes for REST, JSON-RPC errors for MCP, `messageId` idempotency for A2A).
