# SDKs

Local Protocol provides generated SDKs for TypeScript, Python, and PHP.

## Where they are hosted

SDKs are generated in this repo and pushed to their language-specific repos. Releases are published to language registries.

- TypeScript: npm package `local-protocol` ([npm](https://www.npmjs.com/package/local-protocol))
- Python: PyPI package `local_protocol` ([PyPI](https://pypi.org/project/local_protocol/))
- PHP: Packagist package `local-protocol/local-protocol` ([Packagist](https://packagist.org/packages/local-protocol/local-protocol))

## Install

### TypeScript

```sh
npm install local-protocol
```

### Python

```sh
pip install local_protocol
```

### PHP

Install via Composer:

```sh
composer require local-protocol/local-protocol
```

## From GitHub (development)

If you need the latest unreleased changes, install directly from the SDK repos:

- TypeScript: `git+ssh://git@github.com:Palette-Labs-Inc/local-protocol-typescript.git`
- Python: `git+ssh://git@github.com/Palette-Labs-Inc/local-protocol-python.git`
- PHP: add a VCS repo in `composer.json` pointing to `git@github.com:Palette-Labs-Inc/local-protocol-php.git`

## Quick usage

### TypeScript

```ts
import LocalProtocol from 'local-protocol';

const client = new LocalProtocol();

const request = await client.requests.create({
  id: 'req_demo_123',
  nonce: 'nonce_demo_123',
  pickup_location: { coordinates: { latitude: 37.7751, longitude: -122.4193 } },
  dropoff_location: { coordinates: { latitude: 37.7875, longitude: -122.4073 } },
  pickup_time: '2026-02-10T17:00:00Z',
  dropoff_time: '2026-02-10T17:30:00Z',
});

console.log(request.id);
```

### Python

```python
from datetime import datetime
from local_protocol import LocalProtocol

client = LocalProtocol()

request = client.requests.create(
    id="req_demo_123",
    nonce="nonce_demo_123",
    pickup_location={"coordinates": {"latitude": 37.7751, "longitude": -122.4193}},
    dropoff_location={"coordinates": {"latitude": 37.7875, "longitude": -122.4073}},
    pickup_time=datetime.fromisoformat("2026-02-10T17:00:00"),
    dropoff_time=datetime.fromisoformat("2026-02-10T17:30:00"),
)

print(request.id)
```

### PHP

```php
<?php

use LocalProtocol\Client;

$client = new Client();

$request = $client->requests->create(
  id: 'req_demo_123',
  nonce: 'nonce_demo_123',
  pickupLocation: [
    'coordinates' => ['latitude' => 37.7751, 'longitude' => -122.4193]
  ],
  dropoffLocation: [
    'coordinates' => ['latitude' => 37.7875, 'longitude' => -122.4073]
  ],
  pickupTime: new \DateTimeImmutable('2026-02-10T17:00:00Z'),
  dropoffTime: new \DateTimeImmutable('2026-02-10T17:30:00Z'),
);

var_dump($request->id);
```

## Reference

Each SDK repo includes a full API reference and more examples:

- TypeScript: `sdks/local-protocol-typescript/README.md`
- Python: `sdks/local-protocol-python/README.md`
- PHP: `sdks/local-protocol-php/README.md`
