# Merchant

Merchant catalog payload containing denormalized catalogs.

## Example Usage

```typescript
import { Merchant } from "@localprotocol/sdk/models/components";

let value: Merchant = {
  id: "<id>",
  name: "<value>",
  timezone: "Europe/Istanbul",
  catalogs: [],
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | Merchant identifier.                                                                          |
| `name`                                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | Merchant name.                                                                                |
| `timezone`                                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | IANA timezone for availability schedules.                                                     |
| `lastUpdated`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_minus_sign:                                                                            | RFC 3339 timestamp of the latest catalog update.                                              |
| `catalogs`                                                                                    | [components.Catalog](../../models/components/catalog.md)[]                                    | :heavy_check_mark:                                                                            | Catalogs available for the merchant.                                                          |
| `metadata`                                                                                    | Record<string, *any*>                                                                         | :heavy_minus_sign:                                                                            | Business-defined custom data.                                                                 |