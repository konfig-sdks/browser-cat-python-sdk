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


class RequiredUsageEvent(TypedDict):
    usageEventId: str

    usageSessionId: str

    type: str

    status: str

    sentAt: datetime

    createdAt: datetime

    # UsageSession ID
    sessionId: str

    # UsageEvent ID
    eventId: str

class OptionalUsageEvent(TypedDict, total=False):
    data: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class UsageEvent(RequiredUsageEvent, OptionalUsageEvent):
    pass
