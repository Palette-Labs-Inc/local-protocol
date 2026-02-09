# GetEventVocabularyRequest

## Example Usage

```typescript
import { GetEventVocabularyRequest } from "@localprotocol/sdk/models/operations";

let value: GetEventVocabularyRequest = {
  name: "<value>",
};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `name`                                                                                       | *string*                                                                                     | :heavy_check_mark:                                                                           | Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier). |