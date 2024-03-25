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


class UsageEvent(BaseModel):
    usage_event_id: str = Field(alias='usageEventId')

    usage_session_id: str = Field(alias='usageSessionId')

    type: str = Field(alias='type')

    status: Literal["pending", "success", "failure"] = Field(alias='status')

    sent_at: datetime = Field(alias='sentAt')

    created_at: datetime = Field(alias='createdAt')

    # UsageSession ID
    session_id: str = Field(alias='sessionId')

    # UsageEvent ID
    event_id: str = Field(alias='eventId')

    data: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
