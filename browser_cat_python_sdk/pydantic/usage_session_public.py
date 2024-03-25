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


class UsageSessionPublic(BaseModel):
    usage_session_id: str = Field(alias='usageSessionId')

    clerk_org_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='clerkOrgId')

    clerk_user_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='clerkUserId')

    key_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='keyId')

    method: Literal["api", "ws"] = Field(alias='method')

    endpoint: str = Field(alias='endpoint')

    status: Literal["pending", "success", "failure"] = Field(alias='status')

    machine_id: str = Field(alias='machineId')

    machine_region: str = Field(alias='machineRegion')

    browser_type: Literal["chromium", "firefox", "webkit", "chrome", "chrome-beta", "msedge", "msedge-beta", "msedge-dev"] = Field(alias='browserType')

    browser_version: str = Field(alias='browserVersion')

    agent_type: Literal["playwright", "puppeteer", "selenium"] = Field(alias='agentType')

    agent_version: str = Field(alias='agentVersion')

    started_at: datetime = Field(alias='startedAt')

    ended_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='endedAt')

    # UsageSession ID
    session_id: str = Field(alias='sessionId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
