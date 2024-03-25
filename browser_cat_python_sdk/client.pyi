# coding: utf-8
"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

import typing
import inspect
from datetime import date, datetime
from browser_cat_python_sdk.client_custom import ClientCustom
from browser_cat_python_sdk.configuration import Configuration
from browser_cat_python_sdk.api_client import ApiClient
from browser_cat_python_sdk.type_util import copy_signature
from browser_cat_python_sdk.apis.tags.api_keys_api import APIKeysApi
from browser_cat_python_sdk.apis.tags.billing_api import BillingApi
from browser_cat_python_sdk.apis.tags.browsers_api import BrowsersApi
from browser_cat_python_sdk.apis.tags.open_api_api import OpenAPIApi
from browser_cat_python_sdk.apis.tags.server_api import ServerApi
from browser_cat_python_sdk.apis.tags.usage_api import UsageApi



class BrowserCat(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.api_keys: APIKeysApi = APIKeysApi(api_client)
        self.billing: BillingApi = BillingApi(api_client)
        self.browsers: BrowsersApi = BrowsersApi(api_client)
        self.open_api: OpenAPIApi = OpenAPIApi(api_client)
        self.server: ServerApi = ServerApi(api_client)
        self.usage: UsageApi = UsageApi(api_client)
