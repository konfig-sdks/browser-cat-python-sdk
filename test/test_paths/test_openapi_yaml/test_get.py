# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

import unittest
from unittest.mock import patch

import urllib3

import browser_cat_python_sdk
from browser_cat_python_sdk.paths.openapi_yaml import get
from browser_cat_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOpenapiYaml(ApiTestMixin, unittest.TestCase):
    """
    OpenapiYaml unit test stubs
        Retrieve API spec as YAML
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
