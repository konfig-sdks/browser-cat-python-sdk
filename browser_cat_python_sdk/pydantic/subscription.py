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


class Subscription(BaseModel):
    # Subscription ID
    sub_id: str = Field(alias='subId')

    tier: Literal["hobby", "business", "enterprise"] = Field(alias='tier')

    status: Literal["incomplete", "incomplete_expired", "active", "trialing", "past_due", "unpaid", "canceled", "paused"] = Field(alias='status')

    currency: str = Field(alias='currency')

    period_unit: Literal["day", "week", "month", "year"] = Field(alias='periodUnit')

    period_count: int = Field(alias='periodCount')

    period_starts_at: datetime = Field(alias='periodStartsAt')

    period_ends_at: datetime = Field(alias='periodEndsAt')

    anchored_at: datetime = Field(alias='anchoredAt')

    canceled_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='canceledAt')

    resumed_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='resumedAt')

    paused_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='pausedAt')

    stripe_sub_id: str = Field(alias='stripeSubId')

    stripe_cus_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='stripeCusId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
