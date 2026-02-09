# # OrderQuote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique quote identifier. |
**intent_id** | **string** | Shared intent identifier for tracing Request -&gt; Quote -&gt; Order. |
**nonce** | **string** | Client-generated idempotency key. |
**price** | **int** | Price in minor currency units. |
**ready_at** | **\DateTime** | Estimated readiness time (RFC 3339). |
**expires_at** | **\DateTime** | Quote expiration time (RFC 3339). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
