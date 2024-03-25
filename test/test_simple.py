# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

import unittest

import os
from pprint import pprint
from browser_cat_python_sdk import BrowserCat

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        browsercat = BrowserCat(
        
                        jwt_cookie = 'YOUR_API_KEY',
        
            access_token = 'YOUR_BEARER_TOKEN',
        
                        key_header = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(browsercat)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
