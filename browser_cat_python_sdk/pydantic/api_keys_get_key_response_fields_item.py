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

from browser_cat_python_sdk.pydantic.api_keys_get_key_response_fields_item_path import ApiKeysGetKeyResponseFieldsItemPath

class ApiKeysGetKeyResponseFieldsItem(BaseModel):
    code: str = Field(alias='code')

    path: ApiKeysGetKeyResponseFieldsItemPath = Field(alias='path')

    expected: typing.Optional[str] = Field(None, alias='expected')

    received: typing.Optional[str] = Field(None, alias='received')

    validation: typing.Optional[str] = Field(None, alias='validation')

    message: typing.Optional[str] = Field(None, alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
