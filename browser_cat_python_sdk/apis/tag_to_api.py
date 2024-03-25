import typing_extensions

from browser_cat_python_sdk.apis.tags import TagValues
from browser_cat_python_sdk.apis.tags.api_keys_api import APIKeysApi
from browser_cat_python_sdk.apis.tags.billing_api import BillingApi
from browser_cat_python_sdk.apis.tags.usage_api import UsageApi
from browser_cat_python_sdk.apis.tags.open_api_api import OpenAPIApi
from browser_cat_python_sdk.apis.tags.server_api import ServerApi
from browser_cat_python_sdk.apis.tags.browsers_api import BrowsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.API_KEYS: APIKeysApi,
        TagValues.BILLING: BillingApi,
        TagValues.USAGE: UsageApi,
        TagValues.OPEN_API: OpenAPIApi,
        TagValues.SERVER: ServerApi,
        TagValues.BROWSERS: BrowsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.API_KEYS: APIKeysApi,
        TagValues.BILLING: BillingApi,
        TagValues.USAGE: UsageApi,
        TagValues.OPEN_API: OpenAPIApi,
        TagValues.SERVER: ServerApi,
        TagValues.BROWSERS: BrowsersApi,
    }
)
