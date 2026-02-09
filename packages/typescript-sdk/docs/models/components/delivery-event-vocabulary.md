# DeliveryEventVocabulary

Schema for delivery event vocabularies.

## Example Usage

```typescript
import { DeliveryEventVocabulary } from "@localprotocol/sdk/models/components";

let value: DeliveryEventVocabulary = {
  name: "<value>",
  version: "<value>",
  title: "<value>",
  events: {
    "key": {
      description: "furthermore mmm possession but since along each of yahoo",
    },
  },
};
```

## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `name`                                                                                | *string*                                                                              | :heavy_check_mark:                                                                    | Standard identifier in reverse-domain notation.                                       |
| `version`                                                                             | *string*                                                                              | :heavy_check_mark:                                                                    | Version in YYYY-MM-DD format.                                                         |
| `extends`                                                                             | *string*[]                                                                            | :heavy_minus_sign:                                                                    | Parent standard this extends (optional, max one).                                     |
| `title`                                                                               | *string*                                                                              | :heavy_check_mark:                                                                    | Human-readable title.                                                                 |
| `description`                                                                         | *string*                                                                              | :heavy_minus_sign:                                                                    | Human-readable description.                                                           |
| `spec`                                                                                | *string*                                                                              | :heavy_minus_sign:                                                                    | URL to specification document.                                                        |
| `events`                                                                              | Record<string, [components.DeliveryEvent](../../models/components/delivery-event.md)> | :heavy_check_mark:                                                                    | Map of event IDs to event definitions.                                                |