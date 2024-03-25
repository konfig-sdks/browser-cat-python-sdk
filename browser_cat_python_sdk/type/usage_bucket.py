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


class RequiredUsageBucket(TypedDict):
    usageBucketId: str

    keyId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    clerkOrgId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    clerkUserId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    bucket: datetime

    method: str

    endpoint: str

    credits: int

    countSuccess: int

    countFailure: int

    durationSuccess: int

    durationFailure: int

    durationMin: int

    durationMax: int

    durationMean: int

    durationStd: int

class OptionalUsageBucket(TypedDict, total=False):
    pass

class UsageBucket(RequiredUsageBucket, OptionalUsageBucket):
    pass
