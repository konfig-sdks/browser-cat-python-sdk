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


class KeyPublic(BaseModel):
    # Key ID
    key_id: str = Field(alias='keyId')

    name: str = Field(alias='name')

    role: Literal["member", "admin"] = Field(alias='role')

    last_four: str = Field(alias='lastFour')

    expired_at: datetime = Field(alias='expiredAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
