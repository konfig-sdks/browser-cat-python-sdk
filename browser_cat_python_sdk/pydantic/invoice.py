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


class Invoice(BaseModel):
    # Invoice ID
    inv_id: str = Field(alias='invId')

    sub_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='subId')

    status: Literal["draft", "open", "void", "paid", "uncollectible"] = Field(alias='status')

    error: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='error')

    currency: str = Field(alias='currency')

    amount_due: int = Field(alias='amountDue')

    amount_paid: int = Field(alias='amountPaid')

    total: int = Field(alias='total')

    total_discount: int = Field(alias='totalDiscount')

    total_tax: int = Field(alias='totalTax')

    billed_at: datetime = Field(alias='billedAt')

    stripe_inv_id: str = Field(alias='stripeInvId')

    stripe_sub_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='stripeSubId')

    stripe_cus_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='stripeCusId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
