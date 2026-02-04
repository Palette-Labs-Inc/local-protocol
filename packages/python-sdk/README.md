# Local Protocol Python SDK

Auto-generated Pydantic models from Local Protocol JSON schemas.

## Installation

```bash
pip install local-protocol-sdk
```

Or for development:

```bash
uv sync
```

## Regenerating Models

To regenerate models from updated schemas:

```bash
./generate_models.sh
```

Or from the repository root:

```bash
make build-python-sdk
```

## Usage

```python
from local_protocol_sdk.models.delivery.request import DeliveryRequest
from local_protocol_sdk.models.delivery.quote import DeliveryQuote

# Create a request
request = DeliveryRequest(
    id="request-123",
    pickup_location={"coordinates": {"latitude": 37.77, "longitude": -122.41}},
    dropoff_location={"coordinates": {"latitude": 37.78, "longitude": -122.40}},
    pickup_time="2024-01-15T10:00:00Z",
    dropoff_time="2024-01-15T11:00:00Z",
)

# Serialize to JSON
request_json = request.model_dump_json()
```

## Requirements

- Python 3.10+
- pydantic >= 2.0.0
