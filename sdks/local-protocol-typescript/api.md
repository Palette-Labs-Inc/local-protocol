# WellKnown

Types:

- <code><a href="./src/resources/well-known.ts">WellKnownRetrieveResponse</a></code>

Methods:

- <code title="get /.well-known/local-protocol">client.wellKnown.<a href="./src/resources/well-known.ts">retrieve</a>() -> WellKnownRetrieveResponse</code>

# Healthz

Types:

- <code><a href="./src/resources/healthz.ts">HealthzCheckResponse</a></code>

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/resources/healthz.ts">check</a>() -> HealthzCheckResponse</code>

# Requests

Types:

- <code><a href="./src/resources/requests/requests.ts">DeliveryRequest</a></code>
- <code><a href="./src/resources/requests/requests.ts">Location</a></code>
- <code><a href="./src/resources/requests/requests.ts">PostalAddress</a></code>
- <code><a href="./src/resources/requests/requests.ts">RequestListResponse</a></code>

Methods:

- <code title="post /requests">client.requests.<a href="./src/resources/requests/requests.ts">create</a>({ ...params }) -> DeliveryRequest</code>
- <code title="get /requests/{request_id}">client.requests.<a href="./src/resources/requests/requests.ts">retrieve</a>(requestID) -> DeliveryRequest</code>
- <code title="get /requests">client.requests.<a href="./src/resources/requests/requests.ts">list</a>() -> RequestListResponse</code>

## Quotes

Types:

- <code><a href="./src/resources/requests/quotes.ts">DeliveryQuote</a></code>
- <code><a href="./src/resources/requests/quotes.ts">QuoteListResponse</a></code>

Methods:

- <code title="post /requests/{request_id}/quotes">client.requests.quotes.<a href="./src/resources/requests/quotes.ts">create</a>(requestID, { ...params }) -> DeliveryQuote</code>
- <code title="get /requests/{request_id}/quotes/{quote_id}">client.requests.quotes.<a href="./src/resources/requests/quotes.ts">retrieve</a>(quoteID, { ...params }) -> DeliveryQuote</code>
- <code title="get /requests/{request_id}/quotes">client.requests.quotes.<a href="./src/resources/requests/quotes.ts">list</a>(requestID) -> QuoteListResponse</code>

# Deliveries

Types:

- <code><a href="./src/resources/deliveries.ts">Delivery</a></code>
- <code><a href="./src/resources/deliveries.ts">DeliveryListResponse</a></code>

Methods:

- <code title="post /deliveries">client.deliveries.<a href="./src/resources/deliveries.ts">create</a>({ ...params }) -> Delivery</code>
- <code title="get /deliveries/{delivery_id}">client.deliveries.<a href="./src/resources/deliveries.ts">retrieve</a>(deliveryID) -> Delivery</code>
- <code title="get /deliveries">client.deliveries.<a href="./src/resources/deliveries.ts">list</a>() -> DeliveryListResponse</code>
- <code title="patch /deliveries/{delivery_id}/event">client.deliveries.<a href="./src/resources/deliveries.ts">updateEvent</a>(deliveryID, { ...params }) -> Delivery</code>

# Merchants

Types:

- <code><a href="./src/resources/merchants.ts">Availability</a></code>
- <code><a href="./src/resources/merchants.ts">CatalogCategory</a></code>
- <code><a href="./src/resources/merchants.ts">ModifierGroup</a></code>
- <code><a href="./src/resources/merchants.ts">ModifierOption</a></code>
- <code><a href="./src/resources/merchants.ts">MerchantRetrieveResponse</a></code>

Methods:

- <code title="get /merchants/{merchant_id}">client.merchants.<a href="./src/resources/merchants.ts">retrieve</a>(merchantID) -> MerchantRetrieveResponse</code>

# Orders

Types:

- <code><a href="./src/resources/orders/orders.ts">Order</a></code>

Methods:

- <code title="post /orders">client.orders.<a href="./src/resources/orders/orders.ts">create</a>({ ...params }) -> Order</code>
- <code title="get /orders/{order_id}">client.orders.<a href="./src/resources/orders/orders.ts">retrieve</a>(orderID) -> Order</code>

## Requests

Types:

- <code><a href="./src/resources/orders/requests/requests.ts">RequestCreateResponse</a></code>

Methods:

- <code title="post /orders/requests">client.orders.requests.<a href="./src/resources/orders/requests/requests.ts">create</a>({ ...params }) -> RequestCreateResponse</code>

### Quotes

Types:

- <code><a href="./src/resources/orders/requests/quotes.ts">OrderQuote</a></code>
- <code><a href="./src/resources/orders/requests/quotes.ts">QuoteListResponse</a></code>

Methods:

- <code title="get /orders/requests/{order_request_id}/quotes/{order_quote_id}">client.orders.requests.quotes.<a href="./src/resources/orders/requests/quotes.ts">retrieve</a>(orderQuoteID, { ...params }) -> OrderQuote</code>
- <code title="get /orders/requests/{order_request_id}/quotes">client.orders.requests.quotes.<a href="./src/resources/orders/requests/quotes.ts">list</a>(orderRequestID) -> QuoteListResponse</code>

# EventVocabularies

Types:

- <code><a href="./src/resources/event-vocabularies.ts">EventVocabularyRetrieveResponse</a></code>

Methods:

- <code title="get /event-vocabularies/{name}">client.eventVocabularies.<a href="./src/resources/event-vocabularies.ts">retrieve</a>(name) -> EventVocabularyRetrieveResponse</code>

# PaymentInstruments

Types:

- <code><a href="./src/resources/payment-instruments.ts">Amount</a></code>
- <code><a href="./src/resources/payment-instruments.ts">EvmAuthCaptureEscrowInstrument</a></code>
- <code><a href="./src/resources/payment-instruments.ts">EvmCurrency</a></code>
- <code><a href="./src/resources/payment-instruments.ts">PaymentInstrument</a></code>

Methods:

- <code title="post /payment-instruments">client.paymentInstruments.<a href="./src/resources/payment-instruments.ts">register</a>({ ...params }) -> EvmAuthCaptureEscrowInstrument</code>
