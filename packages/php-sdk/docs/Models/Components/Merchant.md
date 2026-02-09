# Merchant

Merchant catalog payload containing denormalized catalogs.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *string*                                                        | :heavy_check_mark:                                              | Merchant identifier.                                            |
| `name`                                                          | *string*                                                        | :heavy_check_mark:                                              | Merchant name.                                                  |
| `timezone`                                                      | *string*                                                        | :heavy_check_mark:                                              | IANA timezone for availability schedules.                       |
| `lastUpdated`                                                   | [\DateTime](https://www.php.net/manual/en/class.datetime.php)   | :heavy_minus_sign:                                              | RFC 3339 timestamp of the latest catalog update.                |
| `catalogs`                                                      | array<[Components\Catalog](../../Models/Components/Catalog.md)> | :heavy_check_mark:                                              | Catalogs available for the merchant.                            |
| `metadata`                                                      | array<string, *mixed*>                                          | :heavy_minus_sign:                                              | Business-defined custom data.                                   |