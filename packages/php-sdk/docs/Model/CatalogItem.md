# # CatalogItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Item identifier. |
**name** | **string** | Item name. |
**description** | **string** | Item description. |
**price** | [**\LocalProtocolSdk\Model\Amount**](Amount.md) | Base price for the item. |
**media** | [**\LocalProtocolSdk\Model\Media[]**](Media.md) | Item media (images, videos, 3D models). | [optional]
**modifier_groups** | [**\LocalProtocolSdk\Model\ModifierGroup[]**](ModifierGroup.md) | Modifier groups available for this item. | [optional]
**availability** | [**\LocalProtocolSdk\Model\Availability**](Availability.md) | Item availability. | [optional]
**metadata** | **array<string,mixed>** | Business-defined custom data. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
