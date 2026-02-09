# # CatalogCategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Category identifier. |
**name** | **string** | Category display name. |
**description** | **string** | Optional category description. | [optional]
**categories** | [**\LocalProtocolSdk\Model\CatalogCategory[]**](CatalogCategory.md) | Ordered child categories for nested category trees. | [optional]
**items** | [**\LocalProtocolSdk\Model\CatalogItem[]**](CatalogItem.md) | Ordered items in this category. |
**availability** | [**\LocalProtocolSdk\Model\Availability**](Availability.md) | Category availability. | [optional]
**metadata** | **array<string,mixed>** | Business-defined custom data. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
