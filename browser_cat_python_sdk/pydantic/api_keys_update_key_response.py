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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from browser_cat_python_sdk.pydantic.api_keys_update_key_response_fields import ApiKeysUpdateKeyResponseFields

class ApiKeysUpdateKeyResponse(BaseModel):
    status: Literal[400] = Field(alias='status')

    error: Literal["Bad Request"] = Field(alias='error')

    # Suggestions for debugging the issue
    message: str = Field(alias='message')

    # Where the validation error occurred
    invalid: typing.Optional[Literal["body", "path", "query"]] = Field(None, alias='invalid')

    fields: typing.Optional[ApiKeysUpdateKeyResponseFields] = Field(None, alias='fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
