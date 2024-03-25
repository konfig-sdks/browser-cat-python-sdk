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


class RequiredInvoice(TypedDict):
    # Invoice ID
    invId: str

    subId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    status: str

    error: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    currency: str

    amountDue: int

    amountPaid: int

    total: int

    totalDiscount: int

    totalTax: int

    billedAt: datetime

    stripeInvId: str

    stripeSubId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    stripeCusId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalInvoice(TypedDict, total=False):
    pass

class Invoice(RequiredInvoice, OptionalInvoice):
    pass
