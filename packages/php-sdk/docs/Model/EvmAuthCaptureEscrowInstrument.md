# # EvmAuthCaptureEscrowInstrument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique instrument identifier. |
**handler_id** | **string** | Handler instance identifier. |
**type** | **string** |  |
**billing_address** | [**\LocalProtocolSdk\Model\PostalAddress**](PostalAddress.md) | Billing address. | [optional]
**credential** | [**\LocalProtocolSdk\Model\PaymentCredential**](PaymentCredential.md) |  | [optional]
**display** | **object** | Display information for the instrument. | [optional]
**payment_info_hash** | **string** | Hash identifying the on-chain payment authorization. |
**operator** | **string** | Operator address. |
**payer** | **string** | Payer address. |
**chain_id** | **int** | EVM chain id. |
**contract** | **string** | Escrow contract address. |
**receiver** | **string** | Receiver address for captures. |
**token** | [**\LocalProtocolSdk\Model\EvmToken**](EvmToken.md) |  |
**max_amount** | [**\LocalProtocolSdk\Model\EvmAuthCaptureEscrowInstrumentAllOfMaxAmount**](EvmAuthCaptureEscrowInstrumentAllOfMaxAmount.md) |  |
**preapproval_expires_at** | **\DateTime** | Pre-approval expiration (RFC 3339). |
**authorization_expires_at** | **\DateTime** | Authorization expiration (RFC 3339). |
**refund_expires_at** | **\DateTime** | Refund expiration (RFC 3339). |
**nonce** | **string** | Unique nonce for payment info hash computation. |
**amount** | [**\LocalProtocolSdk\Model\EvmAuthCaptureEscrowInstrumentAllOfAmount**](EvmAuthCaptureEscrowInstrumentAllOfAmount.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
