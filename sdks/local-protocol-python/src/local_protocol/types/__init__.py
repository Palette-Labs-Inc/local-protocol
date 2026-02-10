# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import modifier_group, modifier_option, catalog_category, merchant_retrieve_response
from .. import _compat
from .order import Order as Order
from .amount import Amount as Amount
from .delivery import Delivery as Delivery
from .location import Location as Location
from .amount_param import AmountParam as AmountParam
from .availability import Availability as Availability
from .evm_currency import EvmCurrency as EvmCurrency
from .location_param import LocationParam as LocationParam
from .modifier_group import ModifierGroup as ModifierGroup
from .postal_address import PostalAddress as PostalAddress
from .modifier_option import ModifierOption as ModifierOption
from .catalog_category import CatalogCategory as CatalogCategory
from .delivery_request import DeliveryRequest as DeliveryRequest
from .evm_currency_param import EvmCurrencyParam as EvmCurrencyParam
from .payment_instrument import PaymentInstrument as PaymentInstrument
from .order_create_params import OrderCreateParams as OrderCreateParams
from .postal_address_param import PostalAddressParam as PostalAddressParam
from .request_create_params import RequestCreateParams as RequestCreateParams
from .request_list_response import RequestListResponse as RequestListResponse
from .delivery_create_params import DeliveryCreateParams as DeliveryCreateParams
from .delivery_list_response import DeliveryListResponse as DeliveryListResponse
from .healthz_check_response import HealthzCheckResponse as HealthzCheckResponse
from .payment_instrument_param import PaymentInstrumentParam as PaymentInstrumentParam
from .merchant_retrieve_response import MerchantRetrieveResponse as MerchantRetrieveResponse
from .delivery_update_event_params import DeliveryUpdateEventParams as DeliveryUpdateEventParams
from .well_known_retrieve_response import WellKnownRetrieveResponse as WellKnownRetrieveResponse
from .event_vocabulary_retrieve_response import EventVocabularyRetrieveResponse as EventVocabularyRetrieveResponse
from .evm_auth_capture_escrow_instrument import EvmAuthCaptureEscrowInstrument as EvmAuthCaptureEscrowInstrument
from .payment_instrument_register_params import PaymentInstrumentRegisterParams as PaymentInstrumentRegisterParams

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    catalog_category.CatalogCategory.update_forward_refs()  # type: ignore
    modifier_group.ModifierGroup.update_forward_refs()  # type: ignore
    modifier_option.ModifierOption.update_forward_refs()  # type: ignore
    merchant_retrieve_response.MerchantRetrieveResponse.update_forward_refs()  # type: ignore
else:
    catalog_category.CatalogCategory.model_rebuild(_parent_namespace_depth=0)
    modifier_group.ModifierGroup.model_rebuild(_parent_namespace_depth=0)
    modifier_option.ModifierOption.model_rebuild(_parent_namespace_depth=0)
    merchant_retrieve_response.MerchantRetrieveResponse.model_rebuild(_parent_namespace_depth=0)
