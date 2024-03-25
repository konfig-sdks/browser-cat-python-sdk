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

from browser_cat_python_sdk.type.api_keys_get_key_response_fields import ApiKeysGetKeyResponseFields

class RequiredApiKeysGetKeyResponse(TypedDict):
    status: typing.Union[int, float]

    error: str

    # Suggestions for debugging the issue
    message: str

class OptionalApiKeysGetKeyResponse(TypedDict, total=False):
    # Where the validation error occurred
    invalid: str

    fields: ApiKeysGetKeyResponseFields

class ApiKeysGetKeyResponse(RequiredApiKeysGetKeyResponse, OptionalApiKeysGetKeyResponse):
    pass
