# # Merchant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Merchant identifier. |
**name** | **string** | Merchant name. |
**timezone** | **string** | IANA timezone for availability schedules. |
**last_updated** | **\DateTime** | RFC 3339 timestamp of the latest catalog update. | [optional]
**catalogs** | [**\LocalProtocolSdk\Model\Catalog[]**](Catalog.md) | Catalogs available for the merchant. |
**metadata** | **array<string,mixed>** | Business-defined custom data. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
