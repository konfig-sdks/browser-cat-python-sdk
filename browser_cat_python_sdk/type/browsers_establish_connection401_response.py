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


class RequiredBrowsersEstablishConnection401Response(TypedDict):
    status: typing.Union[int, float]

    error: str

    # Suggestions for debugging the issue
    message: str

class OptionalBrowsersEstablishConnection401Response(TypedDict, total=False):
    pass

class BrowsersEstablishConnection401Response(RequiredBrowsersEstablishConnection401Response, OptionalBrowsersEstablishConnection401Response):
    pass
