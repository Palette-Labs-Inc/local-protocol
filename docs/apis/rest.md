# REST APIs

REST bindings expose Local Protocol capabilities over conventional HTTP endpoints.
They are best for systems that already speak REST or need predictable caching,
proxying, and observability.

## Protocol Fundamentals

### Base URL

REST endpoints are published in the UCP discovery profile at `/.well-known/ucp`.
The REST service entry provides the `endpoint` used as the base URL for
capability routes.

### Content Types

- Request: `application/json`
- Response: `application/json`

### Transport Security

All endpoints should be served over HTTPS with modern TLS.

## Operations

REST bindings typically expose CRUD-like routes that map to capability actions.
The table below shows a generic pattern.

| Operation        | Method | Example Endpoint                     | Description                     |
| :--------------- | :----- | :----------------------------------- | :------------------------------ |
| Create           | `POST` | `/capabilities/{capability}/objects` | Create a new resource.          |
| Get              | `GET`  | `/capabilities/{capability}/{id}`    | Fetch a resource by id.         |
| Update           | `PUT`  | `/capabilities/{capability}/{id}`    | Replace the resource.           |
| Patch            | `PATCH`| `/capabilities/{capability}/{id}`    | Partially update the resource.  |
| Cancel/Complete  | `POST` | `/capabilities/{capability}/{id}:op` | Execute a capability operation. |

## Idempotency

Write operations should accept an idempotency key to allow safe retries.
The header name and behavior are defined by the service entry or capability
specification.

## Example (Delivery Ask)

=== "Request"

    ```json
    POST /capabilities/delivery/asks HTTP/1.1
    UCP-Agent: profile="https://platform.example/profiles/delivery.json"
    Content-Type: application/json

    {
      "ask": {
        "pickup": {
          "address": "123 Market St, San Francisco, CA"
        },
        "dropoff": {
          "address": "555 Mission St, San Francisco, CA"
        },
        "ready_at": "2026-02-05T18:30:00Z"
      }
    }
    ```

=== "Response"

    ```json
    HTTP/1.1 201 Created
    Content-Type: application/json

    {
      "ask": {
        "id": "ask_123",
        "status": "open",
        "pickup": {
          "address": "123 Market St, San Francisco, CA"
        },
        "dropoff": {
          "address": "555 Mission St, San Francisco, CA"
        }
      }
    }
    ```
