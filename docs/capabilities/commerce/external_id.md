# External ID

Provider-specific identifier mapping for a Local Protocol object.

## Fields

- `provider` (string, required): Provider name (e.g., toast, square, google).
- `id` (string, required): Identifier value in the provider system.
- `type` (string, optional): Identifier type or role (e.g., guid, reference_id).
- `location_id` (string, optional): Provider-specific location or merchant context.
- `metadata` (object, optional): Provider-specific attributes for this identifier.

## Example

```json
{ "provider": "toast", "id": "f2c8...", "type": "guid", "location_id": "loc_1" }
```
