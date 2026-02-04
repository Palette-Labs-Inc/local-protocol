# A2A APIs

Agent2Agent (A2A) bindings expose capabilities through agent communication
rather than direct request-response APIs. A2A is best when the business runs an
interactive agent that can negotiate requirements and orchestrate tools.

## Transport Discovery

Businesses advertise A2A support in the UCP profile at `/.well-known/ucp`.
The `endpoint` points to an agent card that describes available extensions.

```json
{
  "ucp": {
    "version": "YYYY-MM-DD",
    "services": {
      "dev.example.local": [
        {
          "version": "YYYY-MM-DD",
          "spec": "https://example.com/specs/local-protocol",
          "transport": "a2a",
          "endpoint": "https://business.example.com/.well-known/agent-card.json"
        }
      ]
    }
  }
}
```

## Extensions and Capabilities

The agent card should list the extension that represents the Local Protocol
data types and enumerate supported capabilities.

```json
{
  "extensions": [
    {
      "uri": "https://example.com/specs/local-protocol/reference",
      "description": "Local Protocol agent extension",
      "params": {
        "capabilities": {
          "dev.example.delivery": [
            {"version": "YYYY-MM-DD"}
          ]
        }
      }
    }
  ]
}
```

## Interaction Model

A2A exchanges are conversational. The business agent can ask for missing data,
return structured payloads, and drive multi-step workflows. Platforms should
preserve conversation context identifiers and task identifiers provided by the
agent to keep state consistent across turns.

## Idempotency

A2A platforms should include stable message identifiers so the business agent
can detect retries and avoid duplicate operations.

## Example (Delivery Request via A2A Message)

```json
{
  "message": {
    "role": "user",
    "content": "I need a courier from 123 Market St to 555 Mission St"
  },
  "meta": {
    "ucp-agent": {
      "profile": "https://platform.example/profiles/local-agent.json"
    },
    "message_id": "msg_123"
  }
}
```
