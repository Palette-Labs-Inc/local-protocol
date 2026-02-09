# UpdateEventRequest

Body for updating a delivery event.

## Example Usage

```typescript
import { UpdateEventRequest } from "@localprotocol/sdk/models/components";

let value: UpdateEventRequest = {
  event: "<value>",
  eventDescription: "<value>",
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `event`                                                | *string*                                               | :heavy_check_mark:                                     | Event identifier from the delivery's event vocabulary. |
| `eventDescription`                                     | *string*                                               | :heavy_check_mark:                                     | Human-readable event description.                      |