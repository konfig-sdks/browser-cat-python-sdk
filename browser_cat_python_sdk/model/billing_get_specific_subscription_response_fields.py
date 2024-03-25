# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from browser_cat_python_sdk import schemas  # noqa: F401


class BillingGetSpecificSubscriptionResponseFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Validation errors, when available
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BillingGetSpecificSubscriptionResponseFieldsItem']:
            return BillingGetSpecificSubscriptionResponseFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['BillingGetSpecificSubscriptionResponseFieldsItem'], typing.List['BillingGetSpecificSubscriptionResponseFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BillingGetSpecificSubscriptionResponseFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BillingGetSpecificSubscriptionResponseFieldsItem':
        return super().__getitem__(i)

from browser_cat_python_sdk.model.billing_get_specific_subscription_response_fields_item import BillingGetSpecificSubscriptionResponseFieldsItem
