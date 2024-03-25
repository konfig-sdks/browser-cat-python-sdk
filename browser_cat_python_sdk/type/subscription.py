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


class RequiredSubscription(TypedDict):
    # Subscription ID
    subId: str

    tier: str

    status: str

    currency: str

    periodUnit: str

    periodCount: int

    periodStartsAt: datetime

    periodEndsAt: datetime

    anchoredAt: datetime

    canceledAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    resumedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    pausedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    stripeSubId: str

    stripeCusId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalSubscription(TypedDict, total=False):
    pass

class Subscription(RequiredSubscription, OptionalSubscription):
    pass
