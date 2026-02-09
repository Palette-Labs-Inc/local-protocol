# DiscoveryResponse

Service discovery metadata.

## Example Usage

```typescript
import { DiscoveryResponse } from "@localprotocol/sdk/models/components";

let value: DiscoveryResponse = {
  version: "<value>",
  name: "<value>",
  capabilities: {
    "key": "<value>",
    "key1": "<value>",
    "key2": "<value>",
  },
  endpoints: {
    "key": "<value>",
  },
};
```

## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `version`                         | *string*                          | :heavy_check_mark:                | Protocol version.                 |
| `name`                            | *string*                          | :heavy_check_mark:                | Server name.                      |
| `capabilities`                    | Record<string, *any*>             | :heavy_check_mark:                | Supported capabilities by domain. |
| `endpoints`                       | Record<string, *string*>          | :heavy_check_mark:                | Endpoint path map.                |