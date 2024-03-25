# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from browser_cat_python_sdk.type.billing_get_specific_subscription_response_fields_item_path import BillingGetSpecificSubscriptionResponseFieldsItemPath

class RequiredBillingGetSpecificSubscriptionResponseFieldsItem(TypedDict):
    code: str

    path: BillingGetSpecificSubscriptionResponseFieldsItemPath

class OptionalBillingGetSpecificSubscriptionResponseFieldsItem(TypedDict, total=False):
    expected: str

    received: str

    validation: str

    message: str

class BillingGetSpecificSubscriptionResponseFieldsItem(RequiredBillingGetSpecificSubscriptionResponseFieldsItem, OptionalBillingGetSpecificSubscriptionResponseFieldsItem):
    pass
