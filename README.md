<div align="center">

[![Visit Browsercat](./header.png)](https://browsercat.com)

# Browsercat<a id="browsercat"></a>

Providing purr-fect headless browser access via utility endpoints and direct websocket connections.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`browsercat.api_keys.create_api_key`](#browsercatapi_keyscreate_api_key)
  * [`browsercat.api_keys.get_key`](#browsercatapi_keysget_key)
  * [`browsercat.api_keys.list_all`](#browsercatapi_keyslist_all)
  * [`browsercat.api_keys.revoke_key`](#browsercatapi_keysrevoke_key)
  * [`browsercat.api_keys.update_api_key`](#browsercatapi_keysupdate_api_key)
  * [`browsercat.api_keys.update_key`](#browsercatapi_keysupdate_key)
  * [`browsercat.billing.get_active_subscription`](#browsercatbillingget_active_subscription)
  * [`browsercat.billing.get_invoice_pdf`](#browsercatbillingget_invoice_pdf)
  * [`browsercat.billing.get_specific_invoice`](#browsercatbillingget_specific_invoice)
  * [`browsercat.billing.get_specific_subscription`](#browsercatbillingget_specific_subscription)
  * [`browsercat.billing.list_invoices_range`](#browsercatbillinglist_invoices_range)
  * [`browsercat.billing.list_subscriptions_within_range`](#browsercatbillinglist_subscriptions_within_range)
  * [`browsercat.browsers.establish_connection`](#browsercatbrowsersestablish_connection)
  * [`browsercat.open_api.explore_functionality`](#browsercatopen_apiexplore_functionality)
  * [`browsercat.open_api.get_spec_json`](#browsercatopen_apiget_spec_json)
  * [`browsercat.open_api.get_yaml_spec`](#browsercatopen_apiget_yaml_spec)
  * [`browsercat.server.check_health_status`](#browsercatservercheck_health_status)
  * [`browsercat.server.show_metrics`](#browsercatservershow_metrics)
  * [`browsercat.usage.get_event_data`](#browsercatusageget_event_data)
  * [`browsercat.usage.get_request_data`](#browsercatusageget_request_data)
  * [`browsercat.usage.get_session_range`](#browsercatusageget_session_range)
  * [`browsercat.usage.list_aggregate_account_usage`](#browsercatusagelist_aggregate_account_usage)
  * [`browsercat.usage.list_request_events`](#browsercatusagelist_request_events)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=BrowserCat&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from browser_cat_python_sdk import BrowserCat, ApiException

browsercat = BrowserCat(
    jwt_cookie="YOUR_API_KEY",
    key_header="YOUR_API_KEY",
)

try:
    # Create an API key
    create_api_key_response = browsercat.api_keys.create_api_key(
        name="",
        role="member",
        expired_at="1970-01-01T00:00:00.00Z",
    )
    print(create_api_key_response)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_api_key: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
        pprint(e.body["invalid"])
        pprint(e.body["fields"])
    if e.status == 401:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from browser_cat_python_sdk import BrowserCat, ApiException

browsercat = BrowserCat(
    jwt_cookie="YOUR_API_KEY",
    key_header="YOUR_API_KEY",
)


async def main():
    try:
        # Create an API key
        create_api_key_response = await browsercat.api_keys.acreate_api_key(
            name="",
            role="member",
            expired_at="1970-01-01T00:00:00.00Z",
        )
        print(create_api_key_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi.create_api_key: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["status"])
            pprint(e.body["error"])
            pprint(e.body["message"])
            pprint(e.body["invalid"])
            pprint(e.body["fields"])
        if e.status == 401:
            pprint(e.body["status"])
            pprint(e.body["error"])
            pprint(e.body["message"])
        if e.status == 500:
            pprint(e.body["status"])
            pprint(e.body["error"])
            pprint(e.body["message"])
        if e.status == 403:
            pprint(e.body["status"])
            pprint(e.body["error"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from browser_cat_python_sdk import BrowserCat, ApiException

browsercat = BrowserCat(
    jwt_cookie="YOUR_API_KEY",
    key_header="YOUR_API_KEY",
)

try:
    # Create an API key
    create_api_key_response = browsercat.api_keys.raw.create_api_key(
        name="",
        role="member",
        expired_at="1970-01-01T00:00:00.00Z",
    )
    pprint(create_api_key_response.body)
    pprint(create_api_key_response.body["key_id"])
    pprint(create_api_key_response.body["name"])
    pprint(create_api_key_response.body["role"])
    pprint(create_api_key_response.body["last_four"])
    pprint(create_api_key_response.body["expired_at"])
    pprint(create_api_key_response.body["secret"])
    pprint(create_api_key_response.headers)
    pprint(create_api_key_response.status)
    pprint(create_api_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_api_key: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
        pprint(e.body["invalid"])
        pprint(e.body["fields"])
    if e.status == 401:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["status"])
        pprint(e.body["error"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `browsercat.api_keys.create_api_key`<a id="browsercatapi_keyscreate_api_key"></a>

Create a new API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_api_key_response = browsercat.api_keys.create_api_key(
    name="",
    role="member",
    expired_at="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### role: `str`<a id="role-str"></a>

##### expired_at: `datetime`<a id="expired_at-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KeyPost`](./browser_cat_python_sdk/type/key_post.py)
#### 🔄 Return<a id="🔄-return"></a>

[`KeySecret`](./browser_cat_python_sdk/pydantic/key_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.api_keys.get_key`<a id="browsercatapi_keysget_key"></a>

Retrieve an API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_key_response = browsercat.api_keys.get_key(
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`KeyPublic`](./browser_cat_python_sdk/pydantic/key_public.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys/{keyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.api_keys.list_all`<a id="browsercatapi_keyslist_all"></a>

List all API keys.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = browsercat.api_keys.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`KeyPublicList`](./browser_cat_python_sdk/pydantic/key_public_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.api_keys.revoke_key`<a id="browsercatapi_keysrevoke_key"></a>

Revoke an API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
revoke_key_response = browsercat.api_keys.revoke_key(
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`KeyPublic`](./browser_cat_python_sdk/pydantic/key_public.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys/{keyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.api_keys.update_api_key`<a id="browsercatapi_keysupdate_api_key"></a>

Update an API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_api_key_response = browsercat.api_keys.update_api_key(
    name="",
    role="member",
    expired_at="1970-01-01T00:00:00.00Z",
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### role: `str`<a id="role-str"></a>

##### expired_at: `datetime`<a id="expired_at-datetime"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KeyPut`](./browser_cat_python_sdk/type/key_put.py)
#### 🔄 Return<a id="🔄-return"></a>

[`KeyPublic`](./browser_cat_python_sdk/pydantic/key_public.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys/{keyId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.api_keys.update_key`<a id="browsercatapi_keysupdate_key"></a>

Patch an API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_key_response = browsercat.api_keys.update_key(
    key_id="keyId_example",
    name="",
    role="member",
    expired_at="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### role: `str`<a id="role-str"></a>

##### expired_at: `datetime`<a id="expired_at-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KeyPatch`](./browser_cat_python_sdk/type/key_patch.py)
#### 🔄 Return<a id="🔄-return"></a>

[`KeyPublic`](./browser_cat_python_sdk/pydantic/key_public.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/keys/{keyId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.get_active_subscription`<a id="browsercatbillingget_active_subscription"></a>

Get the primary, active subscription.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_active_subscription_response = browsercat.billing.get_active_subscription()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Subscription`](./browser_cat_python_sdk/pydantic/subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/subscriptions/current` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.get_invoice_pdf`<a id="browsercatbillingget_invoice_pdf"></a>

Get specific invoice PDF.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_invoice_pdf_response = browsercat.billing.get_invoice_pdf(
    inv_id="invId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inv_id: `str`<a id="inv_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/invoices/{invId}.pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.get_specific_invoice`<a id="browsercatbillingget_specific_invoice"></a>

Get specific invoice info.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_invoice_response = browsercat.billing.get_specific_invoice(
    inv_id="invId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inv_id: `str`<a id="inv_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Invoice`](./browser_cat_python_sdk/pydantic/invoice.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/invoices/{invId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.get_specific_subscription`<a id="browsercatbillingget_specific_subscription"></a>

Get specific subscription details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_subscription_response = browsercat.billing.get_specific_subscription(
    sub_id="subId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sub_id: `str`<a id="sub_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Subscription`](./browser_cat_python_sdk/pydantic/subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/subscriptions/{subId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.list_invoices_range`<a id="browsercatbillinglist_invoices_range"></a>

List all invoices (including failed and refunds) within a given time range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_invoices_range_response = browsercat.billing.list_invoices_range(
    limit=100,
    offset=None,
    after_date="1970-01-01T00:00:00.00Z",
    before_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./browser_cat_python_sdk/type/.py)<a id="offset-unionbool-date-datetime-dict-float-int-list-str-nonebrowser_cat_python_sdktypepy"></a>

##### after_date: `datetime`<a id="after_date-datetime"></a>

##### before_date: `datetime`<a id="before_date-datetime"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceList`](./browser_cat_python_sdk/pydantic/invoice_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.billing.list_subscriptions_within_range`<a id="browsercatbillinglist_subscriptions_within_range"></a>

List all current and previous subscriptions within a given time range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriptions_within_range_response = (
    browsercat.billing.list_subscriptions_within_range(
        limit=100,
        offset=None,
        after_date="1970-01-01T00:00:00.00Z",
        before_date="1970-01-01T00:00:00.00Z",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./browser_cat_python_sdk/type/.py)<a id="offset-unionbool-date-datetime-dict-float-int-list-str-nonebrowser_cat_python_sdktypepy"></a>

##### after_date: `datetime`<a id="after_date-datetime"></a>

##### before_date: `datetime`<a id="before_date-datetime"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SubscriptionList`](./browser_cat_python_sdk/pydantic/subscription_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing/subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.browsers.establish_connection`<a id="browsercatbrowsersestablish_connection"></a>

Create a websocket connection to a headless browser. Currently only supports Playwright.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
browsercat.browsers.establish_connection(
    region="ams",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### region: `str`<a id="region-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.open_api.explore_functionality`<a id="browsercatopen_apiexplore_functionality"></a>

Open OpenAPI docs explorer. Easily explore functionality, request formats, and response types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
explore_functionality_response = browsercat.open_api.explore_functionality()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/openapi` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.open_api.get_spec_json`<a id="browsercatopen_apiget_spec_json"></a>

Retrieve API spec in JSON format. Use this format to generate types, clients, and mocks in your language of choice.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_spec_json_response = browsercat.open_api.get_spec_json()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OpenApiGetSpecJsonResponse`](./browser_cat_python_sdk/pydantic/open_api_get_spec_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/openapi.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.open_api.get_yaml_spec`<a id="browsercatopen_apiget_yaml_spec"></a>

Retrieve API spec in YAML format. Use this format to generate types, clients, and mocks in your language of choice.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_yaml_spec_response = browsercat.open_api.get_yaml_spec()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OpenApiGetYamlSpecResponse`](./browser_cat_python_sdk/pydantic/open_api_get_yaml_spec_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/openapi.yaml` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.server.check_health_status`<a id="browsercatservercheck_health_status"></a>

Lightweight endpoint to check server health.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_health_status_response = browsercat.server.check_health_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ServerCheckHealthStatusResponse`](./browser_cat_python_sdk/pydantic/server_check_health_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.server.show_metrics`<a id="browsercatservershow_metrics"></a>

Returns server metrics in Prometheus format. Use this endpoint to monitor server health.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
browsercat.server.show_metrics()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.usage.get_event_data`<a id="browsercatusageget_event_data"></a>

Retrieve a particular event for a request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_data_response = browsercat.usage.get_event_data(
    session_id="sessionId_example",
    event_id="eventId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

##### event_id: `str`<a id="event_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageEvent`](./browser_cat_python_sdk/pydantic/usage_event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/usage/sessions/{sessionId}/events/{eventId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.usage.get_request_data`<a id="browsercatusageget_request_data"></a>

Retrieve data for a particular request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_request_data_response = browsercat.usage.get_request_data(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageSessionPublic`](./browser_cat_python_sdk/pydantic/usage_session_public.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/usage/sessions/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.usage.get_session_range`<a id="browsercatusageget_session_range"></a>

List all sessions within a time range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_session_range_response = browsercat.usage.get_session_range(
    limit=100,
    offset=None,
    after_date="1970-01-01T00:00:00.00Z",
    before_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./browser_cat_python_sdk/type/.py)<a id="offset-unionbool-date-datetime-dict-float-int-list-str-nonebrowser_cat_python_sdktypepy"></a>

##### after_date: `datetime`<a id="after_date-datetime"></a>

##### before_date: `datetime`<a id="before_date-datetime"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageSessionPublicList`](./browser_cat_python_sdk/pydantic/usage_session_public_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/usage/sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.usage.list_aggregate_account_usage`<a id="browsercatusagelist_aggregate_account_usage"></a>

List account usage within a time range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_aggregate_account_usage_response = browsercat.usage.list_aggregate_account_usage(
    limit=100,
    offset=None,
    after_date="1970-01-01T00:00:00.00Z",
    before_date="1970-01-01T00:00:00.00Z",
    unit="minute",
    user_id="",
    key_id="bf325375-e030-fccb-a009-17317c574773",
    method="api",
    endpoint="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./browser_cat_python_sdk/type/.py)<a id="offset-unionbool-date-datetime-dict-float-int-list-str-nonebrowser_cat_python_sdktypepy"></a>

##### after_date: `datetime`<a id="after_date-datetime"></a>

##### before_date: `datetime`<a id="before_date-datetime"></a>

##### unit: `str`<a id="unit-str"></a>

##### user_id: Union[`str`, `str`]<a id="user_id-unionstr-str"></a>


##### key_id: Union[`str`, `str`]<a id="key_id-unionstr-str"></a>


##### method: `str`<a id="method-str"></a>

##### endpoint: `str`<a id="endpoint-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageBucketList`](./browser_cat_python_sdk/pydantic/usage_bucket_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/usage/buckets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `browsercat.usage.list_request_events`<a id="browsercatusagelist_request_events"></a>

List all events within a particular request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_request_events_response = browsercat.usage.list_request_events(
    session_id="sessionId_example",
    limit=100,
    offset=None,
    after_date="1970-01-01T00:00:00.00Z",
    before_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./browser_cat_python_sdk/type/.py)<a id="offset-unionbool-date-datetime-dict-float-int-list-str-nonebrowser_cat_python_sdktypepy"></a>

##### after_date: `datetime`<a id="after_date-datetime"></a>

##### before_date: `datetime`<a id="before_date-datetime"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageEventList`](./browser_cat_python_sdk/pydantic/usage_event_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/usage/sessions/{sessionId}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
