# # DeliveryQuote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique quote identifier. |
**nonce** | **string** | Client-generated idempotency key. |
**price** | **int** | Price in minor currency units. |
**currency** | **string** | ISO 4217 currency code. |
**pickup_location** | [**\LocalProtocolSdk\Model\Location**](Location.md) |  |
**dropoff_location** | [**\LocalProtocolSdk\Model\Location**](Location.md) |  |
**pickup_estimate** | **\DateTime** | Estimated pickup time (RFC 3339). |
**dropoff_estimate** | **\DateTime** | Estimated dropoff time (RFC 3339). |
**expires_at** | **\DateTime** | Time when the quote expires (RFC 3339). | [optional]
**payment** | [**\LocalProtocolSdk\Model\Payment**](Payment.md) | Payment handlers available for accepting this quote. |
**request_id** | **string** | Reference to the parent delivery request. |
**created_at** | **\DateTime** | Server-assigned creation timestamp (RFC 3339). |
**status** | **string** | Quote status. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
