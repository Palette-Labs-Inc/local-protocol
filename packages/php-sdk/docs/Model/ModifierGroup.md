# # ModifierGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Modifier group identifier. |
**name** | **string** | Display name for the modifier group. |
**description** | **string** | Optional modifier group description. | [optional]
**minimum_selections** | **int** | Minimum selections required. | [optional]
**maximum_selections** | **int** | Maximum selections allowed. | [optional]
**allow_quantities** | **bool** | Whether options can be selected with quantities &gt; 1. | [optional]
**max_per_modifier** | **int** | Maximum quantity per modifier option. | [optional] [default to 1]
**modifier_options** | [**\LocalProtocolSdk\Model\ModifierOption[]**](ModifierOption.md) | Ordered modifier options within this group. |
**type** | **string** | Modifier group type classification. | [optional]
**metadata** | **array<string,mixed>** | Business-defined custom data. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
