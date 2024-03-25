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


class RequiredKeySecret(TypedDict):
    # Key ID
    keyId: str

    name: str

    role: str

    lastFour: str

    expiredAt: datetime

    secret: str

class OptionalKeySecret(TypedDict, total=False):
    pass

class KeySecret(RequiredKeySecret, OptionalKeySecret):
    pass
