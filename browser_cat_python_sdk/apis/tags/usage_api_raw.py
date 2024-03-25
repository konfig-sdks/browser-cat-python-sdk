# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from browser_cat_python_sdk.paths.usage_sessions_session_id_events_event_id.get import GetEventDataRaw
from browser_cat_python_sdk.paths.usage_sessions_session_id.get import GetRequestDataRaw
from browser_cat_python_sdk.paths.usage_sessions.get import GetSessionRangeRaw
from browser_cat_python_sdk.paths.usage_buckets.get import ListAggregateAccountUsageRaw
from browser_cat_python_sdk.paths.usage_sessions_session_id_events.get import ListRequestEventsRaw


class UsageApiRaw(
    GetEventDataRaw,
    GetRequestDataRaw,
    GetSessionRangeRaw,
    ListAggregateAccountUsageRaw,
    ListRequestEventsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
