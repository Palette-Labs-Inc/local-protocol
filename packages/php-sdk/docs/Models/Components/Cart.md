# Cart

A shopping cart.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *string*                                                          | :heavy_check_mark:                                                | Unique cart identifier.                                           |
| `intentId`                                                        | *string*                                                          | :heavy_check_mark:                                                | Shared intent identifier for tracing Request -> Quote -> Order.   |
| `nonce`                                                           | *string*                                                          | :heavy_check_mark:                                                | Client-generated idempotency key.                                 |
| `items`                                                           | array<[Components\CartItem](../../Models/Components/CartItem.md)> | :heavy_check_mark:                                                | Items in the cart.                                                |