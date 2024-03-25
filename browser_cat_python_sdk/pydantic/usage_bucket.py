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


class UsageBucket(BaseModel):
    usage_bucket_id: str = Field(alias='usageBucketId')

    key_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='keyId')

    clerk_org_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='clerkOrgId')

    clerk_user_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='clerkUserId')

    bucket: datetime = Field(alias='bucket')

    method: Literal["api", "ws"] = Field(alias='method')

    endpoint: str = Field(alias='endpoint')

    credits: int = Field(alias='credits')

    count_success: int = Field(alias='countSuccess')

    count_failure: int = Field(alias='countFailure')

    duration_success: int = Field(alias='durationSuccess')

    duration_failure: int = Field(alias='durationFailure')

    duration_min: int = Field(alias='durationMin')

    duration_max: int = Field(alias='durationMax')

    duration_mean: int = Field(alias='durationMean')

    duration_std: int = Field(alias='durationStd')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
