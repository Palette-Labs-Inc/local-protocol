# DiscoveryResponse

Service discovery metadata.


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `version`                         | *string*                          | :heavy_check_mark:                | Protocol version.                 |
| `name`                            | *string*                          | :heavy_check_mark:                | Server name.                      |
| `capabilities`                    | array<string, *mixed*>            | :heavy_check_mark:                | Supported capabilities by domain. |
| `endpoints`                       | array<string, *string*>           | :heavy_check_mark:                | Endpoint path map.                |