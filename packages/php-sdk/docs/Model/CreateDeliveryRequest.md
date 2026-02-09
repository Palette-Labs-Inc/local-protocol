# # CreateDeliveryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **string** | The delivery request to fulfill. |
**quote_id** | **string** | The accepted quote. |
**nonce** | **string** | Client-generated idempotency key. |
**webhook_url** | **string** | Optional URL to receive delivery event webhook notifications. | [optional]
**event_vocabulary** | **string** | Event vocabulary standard to use. | [optional] [default to 'xyz.localprotocol.delivery.courier@2026-01-30']

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
