# Order API

Minimal endpoints for the Order capability. All create endpoints are idempotent by `nonce`.

## Endpoints

### Create Cart

`POST /order/carts`

- Request body: `Cart`
- Response: `Cart`
- Errors: `409` if `nonce` was reused with different payload.

### Create Request

`POST /order/requests`

- Request body: `OrderRequest`
- Response: `OrderRequest`
- Errors: `409` if `nonce` was reused with different payload.

### Create Quote

`POST /order/quotes`

- Request body: `OrderQuote`
- Response: `OrderQuote`
- Errors:
  - `404` if no matching `intent_id` exists.
  - `409` if `nonce` was reused with different payload.

### Create Order

`POST /order/orders`

- Request body: `Order`
- Response: `Order`
- Errors:
  - `404` if no matching `quote_id` exists.
  - `409` if `nonce` was reused with different payload.
  - `422` if the quote is expired.

## Idempotency

`nonce` is a client-generated idempotency key. Reusing a `nonce` with a
different payload MUST return `409`.
