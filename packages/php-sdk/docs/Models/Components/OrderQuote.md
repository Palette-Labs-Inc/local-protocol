# OrderQuote

An order quote.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *string*                                                        | :heavy_check_mark:                                              | Unique quote identifier.                                        |
| `intentId`                                                      | *string*                                                        | :heavy_check_mark:                                              | Shared intent identifier for tracing Request -> Quote -> Order. |
| `nonce`                                                         | *string*                                                        | :heavy_check_mark:                                              | Client-generated idempotency key.                               |
| `price`                                                         | *int*                                                           | :heavy_check_mark:                                              | Price in minor currency units.                                  |
| `readyAt`                                                       | [\DateTime](https://www.php.net/manual/en/class.datetime.php)   | :heavy_check_mark:                                              | Estimated readiness time (RFC 3339).                            |
| `expiresAt`                                                     | [\DateTime](https://www.php.net/manual/en/class.datetime.php)   | :heavy_check_mark:                                              | Quote expiration time (RFC 3339).                               |