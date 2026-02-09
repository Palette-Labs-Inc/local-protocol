# Coordinates

Geographic coordinates.

## Example Usage

```typescript
import { Coordinates } from "@localprotocol/sdk/models/components";

let value: Coordinates = {
  latitude: 601.54,
  longitude: 4028.75,
};
```

## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `latitude`                    | *number*                      | :heavy_check_mark:            | Latitude in decimal degrees.  |
| `longitude`                   | *number*                      | :heavy_check_mark:            | Longitude in decimal degrees. |