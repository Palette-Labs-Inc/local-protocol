# # DeliveryEventVocabulary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** | Standard identifier in reverse-domain notation. |
**version** | **string** | Version in YYYY-MM-DD format. |
**extends** | **string[]** | Parent standard this extends (optional, max one). | [optional]
**title** | **string** | Human-readable title. |
**description** | **string** | Human-readable description. | [optional]
**spec** | **string** | URL to specification document. | [optional]
**events** | [**array<string,\LocalProtocolSdk\Model\DeliveryEvent>**](DeliveryEvent.md) | Map of event IDs to event definitions. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
