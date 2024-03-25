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


class RequiredUsageSessionPublic(TypedDict):
    usageSessionId: str

    clerkOrgId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    clerkUserId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    keyId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    method: str

    endpoint: str

    status: str

    machineId: str

    machineRegion: str

    browserType: str

    browserVersion: str

    agentType: str

    agentVersion: str

    startedAt: datetime

    endedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # UsageSession ID
    sessionId: str

class OptionalUsageSessionPublic(TypedDict, total=False):
    pass

class UsageSessionPublic(RequiredUsageSessionPublic, OptionalUsageSessionPublic):
    pass
