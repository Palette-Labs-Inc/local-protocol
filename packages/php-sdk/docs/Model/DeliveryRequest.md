# # DeliveryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique request identifier. |
**nonce** | **string** | Client-generated idempotency key. |
**pickup_location** | [**\LocalProtocolSdk\Model\Location**](Location.md) |  |
**dropoff_location** | [**\LocalProtocolSdk\Model\Location**](Location.md) |  |
**pickup_time** | **\DateTime** | Requested pickup time (RFC 3339). |
**dropoff_time** | **\DateTime** | Requested dropoff time (RFC 3339). |
**pickup_instructions** | **string** | Pickup directions, access codes, or handling notes. | [optional]
**dropoff_instructions** | **string** | Dropoff directions, access codes, or delivery notes. | [optional]
**created_at** | **\DateTime** | Server-assigned creation timestamp (RFC 3339). |
**status** | **string** | Request status. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
