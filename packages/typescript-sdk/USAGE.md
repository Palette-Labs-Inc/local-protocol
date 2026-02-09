<!-- Start SDK Example Usage [usage] -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.discovery.getDiscovery();

  console.log(result);
}

run();

```
<!-- End SDK Example Usage [usage] -->