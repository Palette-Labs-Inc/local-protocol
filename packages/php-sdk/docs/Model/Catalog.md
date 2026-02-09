# # Catalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Catalog identifier. |
**name** | **string** | Catalog name. |
**description** | **string** | Catalog description. | [optional]
**categories** | [**\LocalProtocolSdk\Model\CatalogCategory[]**](CatalogCategory.md) | Ordered top-level categories. |
**items** | [**\LocalProtocolSdk\Model\CatalogItem[]**](CatalogItem.md) | Items not assigned to a category. | [optional]
**availability** | [**\LocalProtocolSdk\Model\Availability**](Availability.md) | Catalog-wide availability override. | [optional]
**metadata** | **array<string,mixed>** | Business-defined custom data. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
