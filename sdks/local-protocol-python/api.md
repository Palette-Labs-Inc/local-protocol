# WellKnown

Types:

```python
from local_protocol.types import WellKnownRetrieveResponse
```

Methods:

- <code title="get /.well-known/local-protocol">client.well_known.<a href="./src/local_protocol/resources/well_known.py">retrieve</a>() -> <a href="./src/local_protocol/types/well_known_retrieve_response.py">WellKnownRetrieveResponse</a></code>

# Healthz

Types:

```python
from local_protocol.types import HealthzCheckResponse
```

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/local_protocol/resources/healthz.py">check</a>() -> <a href="./src/local_protocol/types/healthz_check_response.py">HealthzCheckResponse</a></code>

# Requests

Types:

```python
from local_protocol.types import (
    Coordinates,
    DeliveryRequest,
    Location,
    PostalAddress,
    RequestListResponse,
)
```

Methods:

- <code title="post /requests">client.requests.<a href="./src/local_protocol/resources/requests/requests.py">create</a>(\*\*<a href="src/local_protocol/types/request_create_params.py">params</a>) -> <a href="./src/local_protocol/types/delivery_request.py">DeliveryRequest</a></code>
- <code title="get /requests/{request_id}">client.requests.<a href="./src/local_protocol/resources/requests/requests.py">retrieve</a>(request_id) -> <a href="./src/local_protocol/types/delivery_request.py">DeliveryRequest</a></code>
- <code title="get /requests">client.requests.<a href="./src/local_protocol/resources/requests/requests.py">list</a>() -> <a href="./src/local_protocol/types/request_list_response.py">RequestListResponse</a></code>

## Quotes

Types:

```python
from local_protocol.types.requests import DeliveryQuote, QuoteListResponse
```

Methods:

- <code title="post /requests/{request_id}/quotes">client.requests.quotes.<a href="./src/local_protocol/resources/requests/quotes.py">create</a>(request_id, \*\*<a href="src/local_protocol/types/requests/quote_create_params.py">params</a>) -> <a href="./src/local_protocol/types/requests/delivery_quote.py">DeliveryQuote</a></code>
- <code title="get /requests/{request_id}/quotes/{quote_id}">client.requests.quotes.<a href="./src/local_protocol/resources/requests/quotes.py">retrieve</a>(quote_id, \*, request_id) -> <a href="./src/local_protocol/types/requests/delivery_quote.py">DeliveryQuote</a></code>
- <code title="get /requests/{request_id}/quotes">client.requests.quotes.<a href="./src/local_protocol/resources/requests/quotes.py">list</a>(request_id) -> <a href="./src/local_protocol/types/requests/quote_list_response.py">QuoteListResponse</a></code>

# Deliveries

Types:

```python
from local_protocol.types import Delivery, DeliveryListResponse
```

Methods:

- <code title="post /deliveries">client.deliveries.<a href="./src/local_protocol/resources/deliveries.py">create</a>(\*\*<a href="src/local_protocol/types/delivery_create_params.py">params</a>) -> <a href="./src/local_protocol/types/delivery.py">Delivery</a></code>
- <code title="get /deliveries/{delivery_id}">client.deliveries.<a href="./src/local_protocol/resources/deliveries.py">retrieve</a>(delivery_id) -> <a href="./src/local_protocol/types/delivery.py">Delivery</a></code>
- <code title="get /deliveries">client.deliveries.<a href="./src/local_protocol/resources/deliveries.py">list</a>() -> <a href="./src/local_protocol/types/delivery_list_response.py">DeliveryListResponse</a></code>
- <code title="patch /deliveries/{delivery_id}/event">client.deliveries.<a href="./src/local_protocol/resources/deliveries.py">update_event</a>(delivery_id, \*\*<a href="src/local_protocol/types/delivery_update_event_params.py">params</a>) -> <a href="./src/local_protocol/types/delivery.py">Delivery</a></code>

# Merchants

Types:

```python
from local_protocol.types import (
    Availability,
    CatalogCategory,
    ModifierGroup,
    ModifierOption,
    MerchantRetrieveResponse,
)
```

Methods:

- <code title="get /merchants/{merchant_id}">client.merchants.<a href="./src/local_protocol/resources/merchants.py">retrieve</a>(merchant_id) -> <a href="./src/local_protocol/types/merchant_retrieve_response.py">MerchantRetrieveResponse</a></code>

# Orders

Types:

```python
from local_protocol.types import Order
```

Methods:

- <code title="post /orders">client.orders.<a href="./src/local_protocol/resources/orders/orders.py">create</a>(\*\*<a href="src/local_protocol/types/order_create_params.py">params</a>) -> <a href="./src/local_protocol/types/order.py">Order</a></code>
- <code title="get /orders/{order_id}">client.orders.<a href="./src/local_protocol/resources/orders/orders.py">retrieve</a>(order_id) -> <a href="./src/local_protocol/types/order.py">Order</a></code>

## Requests

Types:

```python
from local_protocol.types.orders import RequestCreateResponse
```

Methods:

- <code title="post /orders/requests">client.orders.requests.<a href="./src/local_protocol/resources/orders/requests/requests.py">create</a>(\*\*<a href="src/local_protocol/types/orders/request_create_params.py">params</a>) -> <a href="./src/local_protocol/types/orders/request_create_response.py">RequestCreateResponse</a></code>

### Quotes

Types:

```python
from local_protocol.types.orders.requests import OrderQuote, QuoteListResponse
```

Methods:

- <code title="get /orders/requests/{order_request_id}/quotes/{order_quote_id}">client.orders.requests.quotes.<a href="./src/local_protocol/resources/orders/requests/quotes.py">retrieve</a>(order_quote_id, \*, order_request_id) -> <a href="./src/local_protocol/types/orders/requests/order_quote.py">OrderQuote</a></code>
- <code title="get /orders/requests/{order_request_id}/quotes">client.orders.requests.quotes.<a href="./src/local_protocol/resources/orders/requests/quotes.py">list</a>(order_request_id) -> <a href="./src/local_protocol/types/orders/requests/quote_list_response.py">QuoteListResponse</a></code>

# EventVocabularies

Types:

```python
from local_protocol.types import EventVocabularyRetrieveResponse
```

Methods:

- <code title="get /event-vocabularies/{name}">client.event_vocabularies.<a href="./src/local_protocol/resources/event_vocabularies.py">retrieve</a>(name) -> <a href="./src/local_protocol/types/event_vocabulary_retrieve_response.py">EventVocabularyRetrieveResponse</a></code>

# PaymentInstruments

Types:

```python
from local_protocol.types import (
    Amount,
    EvmAuthCaptureEscrowInstrument,
    EvmAuthCaptureEscrowInstrumentDetails,
    EvmCurrency,
    Payment,
    PaymentInstrument,
    SelectedPaymentInstrument,
    SelectedPaymentInstrumentSelectionState,
)
```

Methods:

- <code title="post /payment-instruments">client.payment_instruments.<a href="./src/local_protocol/resources/payment_instruments.py">register</a>(\*\*<a href="src/local_protocol/types/payment_instrument_register_params.py">params</a>) -> <a href="./src/local_protocol/types/evm_auth_capture_escrow_instrument.py">EvmAuthCaptureEscrowInstrument</a></code>
