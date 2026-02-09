<!-- markdownlint-disable MD046 -->

# MCP APIs

Model Context Protocol (MCP) bindings expose capabilities as tools that
agents can call directly. MCP is best for AI-driven workflows and structured
tool invocation.

## Protocol Fundamentals

### Discovery

Businesses advertise MCP transport support in the UCP profile at
`/.well-known/ucp`. The MCP service entry supplies the `endpoint` for the
server and optionally an OpenRPC schema reference.

```json
{
  "ucp": {
    "version": "YYYY-MM-DD",
    "services": {
      "dev.example.local": [
        {
          "version": "YYYY-MM-DD",
          "spec": "https://example.com/specs/local-protocol",
          "transport": "mcp",
          "schema": "https://example.com/schemas/local-protocol/openrpc.json",
          "endpoint": "https://business.example.com/mcp"
        }
      ]
    }
  }
}
```

### Request Metadata

MCP requests should include a `meta` object with protocol metadata:

- `ucp-agent.profile`: the caller profile URI for capability negotiation.
- `idempotency-key`: required for non-idempotent operations.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_delivery_request",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://platform.example/profiles/delivery-agent.json"
        },
        "idempotency-key": "550e8400-e29b-41d4-a716-446655440000"
      },
      "request": {
        "id": "request_123",
        "nonce": "request-nonce-123",
        "pickup_location": { "postal_address": {} },
        "dropoff_location": { "postal_address": {} },
        "pickup_time": "2026-02-12T18:30:00Z",
        "dropoff_time": "2026-02-12T19:00:00Z"
      }
    }
  }
}
```

## Tool Mapping

Capabilities map to MCP tools. A typical pattern is:

| Tool Name              | Operation | Description                     |
| :--------------------- | :-------- | :------------------------------ |
| `create_<resource>`    | Create    | Create a new resource.          |
| `get_<resource>`       | Get       | Retrieve a resource by id.      |
| `update_<resource>`    | Update    | Replace or modify a resource.   |
| `cancel_<resource>`    | Cancel    | Cancel a resource or workflow.  |
| `complete_<resource>`  | Complete  | Finalize a workflow.            |

## Example (Create Delivery Request)

=== "Request"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "create_delivery_request",
        "arguments": {
          "meta": {
            "ucp-agent": {
              "profile": "https://platform.example/profiles/delivery-agent.json"
            }
          },
          "request": {
            "id": "request_123",
            "nonce": "request-nonce-123",
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
                "street_address": "555 Mission St",
                "address_locality": "San Francisco",
                "address_region": "CA",
                "postal_code": "94105",
                "address_country": "US"
              }
            },
            "pickup_time": "2026-02-12T18:30:00Z",
            "dropoff_time": "2026-02-12T19:00:00Z"
          }
        }
      }
    }
    ```

=== "Response"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "request": {
          "id": "request_123",
          "nonce": "request-nonce-123",
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
              "street_address": "555 Mission St",
              "address_locality": "San Francisco",
              "address_region": "CA",
              "postal_code": "94105",
              "address_country": "US"
            }
          },
          "pickup_time": "2026-02-12T18:30:00Z",
          "dropoff_time": "2026-02-12T19:00:00Z"
        }
      }
    }
    ```
