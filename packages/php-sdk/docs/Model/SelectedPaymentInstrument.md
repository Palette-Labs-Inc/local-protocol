# # SelectedPaymentInstrument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique instrument identifier. |
**handler_id** | **string** | Handler instance identifier. |
**type** | **string** | Instrument category (e.g., &#39;card&#39;, &#39;tokenized_card&#39;). |
**billing_address** | [**\LocalProtocolSdk\Model\PostalAddress**](PostalAddress.md) | Billing address. | [optional]
**credential** | [**\LocalProtocolSdk\Model\PaymentCredential**](PaymentCredential.md) |  | [optional]
**display** | **object** | Display information for the instrument. | [optional]
**selected** | **bool** | Whether this instrument is selected by the user. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
