# Location1

## Example Usage

```typescript
import { Location1 } from "@localprotocol/sdk/models/components";

let value: Location1 = {
  coordinates: {
    latitude: 1526.08,
    longitude: 5253.35,
  },
};
```

## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `coordinates`                                                         | [components.Coordinates](../../models/components/coordinates.md)      | :heavy_check_mark:                                                    | Geographic coordinates.                                               |
| `postalAddress`                                                       | [components.PostalAddress](../../models/components/postal-address.md) | :heavy_minus_sign:                                                    | N/A                                                                   |