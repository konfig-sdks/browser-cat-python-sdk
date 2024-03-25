# coding: utf-8

# flake8: noqa

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

__version__ = "1.0.0"

# import ApiClient
from browser_cat_python_sdk.api_client import ApiClient

# import Configuration
from browser_cat_python_sdk.configuration import Configuration

# import exceptions
from browser_cat_python_sdk.exceptions import OpenApiException
from browser_cat_python_sdk.exceptions import ApiAttributeError
from browser_cat_python_sdk.exceptions import ApiTypeError
from browser_cat_python_sdk.exceptions import ApiValueError
from browser_cat_python_sdk.exceptions import ApiKeyError
from browser_cat_python_sdk.exceptions import ApiException

from browser_cat_python_sdk.client import BrowserCat
