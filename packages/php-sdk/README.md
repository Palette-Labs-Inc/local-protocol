# LocalProtocolSdk

Local Protocol delivery API. Covers service discovery, delivery requests, quotes, and deliveries.


## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/LocalProtocolSdk/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');




$apiInstance = new LocalProtocolSdk\Api\DeliveriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$create_delivery_request = new \LocalProtocolSdk\Model\CreateDeliveryRequest(); // \LocalProtocolSdk\Model\CreateDeliveryRequest

try {
    $result = $apiInstance->createDelivery($create_delivery_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DeliveriesApi->createDelivery: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *http://localhost:8000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeliveriesApi* | [**createDelivery**](docs/Api/DeliveriesApi.md#createdelivery) | **POST** /deliveries | Create delivery
*DeliveriesApi* | [**getDelivery**](docs/Api/DeliveriesApi.md#getdelivery) | **GET** /deliveries/{delivery_id} | Get delivery
*DeliveriesApi* | [**listDeliveries**](docs/Api/DeliveriesApi.md#listdeliveries) | **GET** /deliveries | List deliveries
*DeliveriesApi* | [**updateDeliveryEvent**](docs/Api/DeliveriesApi.md#updatedeliveryevent) | **PATCH** /deliveries/{delivery_id}/event | Update delivery event
*DiscoveryApi* | [**getDiscovery**](docs/Api/DiscoveryApi.md#getdiscovery) | **GET** /.well-known/local-protocol | Service discovery
*DiscoveryApi* | [**getHealth**](docs/Api/DiscoveryApi.md#gethealth) | **GET** /healthz | Health check
*QuotesApi* | [**createQuote**](docs/Api/QuotesApi.md#createquote) | **POST** /requests/{request_id}/quotes | Create quote
*QuotesApi* | [**getQuote**](docs/Api/QuotesApi.md#getquote) | **GET** /requests/{request_id}/quotes/{quote_id} | Get quote
*QuotesApi* | [**listQuotes**](docs/Api/QuotesApi.md#listquotes) | **GET** /requests/{request_id}/quotes | List quotes for request
*RequestsApi* | [**createRequest**](docs/Api/RequestsApi.md#createrequest) | **POST** /requests | Create delivery request
*RequestsApi* | [**getRequest**](docs/Api/RequestsApi.md#getrequest) | **GET** /requests/{request_id} | Get delivery request
*RequestsApi* | [**listRequests**](docs/Api/RequestsApi.md#listrequests) | **GET** /requests | List delivery requests

## Models

- [Amount](docs/Model/Amount.md)
- [AmountCurrency](docs/Model/AmountCurrency.md)
- [Availability](docs/Model/Availability.md)
- [Cart](docs/Model/Cart.md)
- [CartItem](docs/Model/CartItem.md)
- [Catalog](docs/Model/Catalog.md)
- [CatalogCategory](docs/Model/CatalogCategory.md)
- [CatalogItem](docs/Model/CatalogItem.md)
- [Coordinates](docs/Model/Coordinates.md)
- [CreateDeliveryRequest](docs/Model/CreateDeliveryRequest.md)
- [Delivery](docs/Model/Delivery.md)
- [DeliveryEvent](docs/Model/DeliveryEvent.md)
- [DeliveryEventVocabulary](docs/Model/DeliveryEventVocabulary.md)
- [DeliveryQuote](docs/Model/DeliveryQuote.md)
- [DeliveryQuoteCreate](docs/Model/DeliveryQuoteCreate.md)
- [DeliveryRequest](docs/Model/DeliveryRequest.md)
- [DeliveryRequestCreate](docs/Model/DeliveryRequestCreate.md)
- [DiscoveryResponse](docs/Model/DiscoveryResponse.md)
- [ErrorResponse](docs/Model/ErrorResponse.md)
- [EvmAuthCaptureEscrowConfig](docs/Model/EvmAuthCaptureEscrowConfig.md)
- [EvmAuthCaptureEscrowInstrument](docs/Model/EvmAuthCaptureEscrowInstrument.md)
- [EvmAuthCaptureEscrowInstrumentAllOfAmount](docs/Model/EvmAuthCaptureEscrowInstrumentAllOfAmount.md)
- [EvmAuthCaptureEscrowInstrumentAllOfMaxAmount](docs/Model/EvmAuthCaptureEscrowInstrumentAllOfMaxAmount.md)
- [EvmCurrency](docs/Model/EvmCurrency.md)
- [EvmToken](docs/Model/EvmToken.md)
- [FiatCurrency](docs/Model/FiatCurrency.md)
- [HealthResponse](docs/Model/HealthResponse.md)
- [Interval](docs/Model/Interval.md)
- [Location](docs/Model/Location.md)
- [Media](docs/Model/Media.md)
- [Merchant](docs/Model/Merchant.md)
- [ModifierGroup](docs/Model/ModifierGroup.md)
- [ModifierItem](docs/Model/ModifierItem.md)
- [ModifierOption](docs/Model/ModifierOption.md)
- [Order](docs/Model/Order.md)
- [OrderQuote](docs/Model/OrderQuote.md)
- [OrderRequest](docs/Model/OrderRequest.md)
- [Payment](docs/Model/Payment.md)
- [PaymentCredential](docs/Model/PaymentCredential.md)
- [PaymentInstrument](docs/Model/PaymentInstrument.md)
- [PostalAddress](docs/Model/PostalAddress.md)
- [SelectedPaymentInstrument](docs/Model/SelectedPaymentInstrument.md)
- [UpdateEventRequest](docs/Model/UpdateEventRequest.md)
- [ValidationErrorResponse](docs/Model/ValidationErrorResponse.md)
- [ValidationErrorResponseDetail](docs/Model/ValidationErrorResponseDetail.md)

## Authorization
Endpoints do not require authorization.

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `0.1.0`
    - Package version: `0.1.0`
    - Generator version: `7.19.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
