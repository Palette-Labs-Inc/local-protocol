# Delivery

A delivery resource.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *string*                                                          | :heavy_check_mark:                                                | Unique delivery identifier.                                       |
| `requestId`                                                       | *string*                                                          | :heavy_check_mark:                                                | Reference to the delivery request.                                |
| `quoteId`                                                         | *string*                                                          | :heavy_check_mark:                                                | Reference to the accepted quote.                                  |
| `paymentInstrumentId`                                             | *string*                                                          | :heavy_check_mark:                                                | Reference to the payment instrument used to create this delivery. |
| `event`                                                           | *string*                                                          | :heavy_check_mark:                                                | Current event identifier.                                         |
| `eventDescription`                                                | *string*                                                          | :heavy_check_mark:                                                | Human-readable description of the current event.                  |
| `eventVocabulary`                                                 | *string*                                                          | :heavy_check_mark:                                                | Event vocabulary standard in use.                                 |
| `webhookUrl`                                                      | *?string*                                                         | :heavy_minus_sign:                                                | Registered webhook URL, if any.                                   |
| `createdAt`                                                       | [\DateTime](https://www.php.net/manual/en/class.datetime.php)     | :heavy_check_mark:                                                | Creation timestamp (RFC 3339).                                    |
| `updatedAt`                                                       | [\DateTime](https://www.php.net/manual/en/class.datetime.php)     | :heavy_check_mark:                                                | Last update timestamp (RFC 3339).                                 |