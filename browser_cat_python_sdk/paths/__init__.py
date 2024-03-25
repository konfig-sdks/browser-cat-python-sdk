# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from browser_cat_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HEALTH = "/health"
    METRICS = "/metrics"
    OPENAPI = "/openapi"
    OPENAPI_JSON = "/openapi.json"
    OPENAPI_YAML = "/openapi.yaml"
    CONNECT = "/connect"
    AUTH_KEYS = "/auth/keys"
    AUTH_KEYS_KEY_ID = "/auth/keys/{keyId}"
    USAGE_BUCKETS = "/usage/buckets"
    USAGE_SESSIONS = "/usage/sessions"
    USAGE_SESSIONS_SESSION_ID = "/usage/sessions/{sessionId}"
    USAGE_SESSIONS_SESSION_ID_EVENTS = "/usage/sessions/{sessionId}/events"
    USAGE_SESSIONS_SESSION_ID_EVENTS_EVENT_ID = "/usage/sessions/{sessionId}/events/{eventId}"
    BILLING_SUBSCRIPTIONS = "/billing/subscriptions"
    BILLING_SUBSCRIPTIONS_CURRENT = "/billing/subscriptions/current"
    BILLING_SUBSCRIPTIONS_SUB_ID = "/billing/subscriptions/{subId}"
    BILLING_INVOICES = "/billing/invoices"
    BILLING_INVOICES_INV_ID = "/billing/invoices/{invId}"
    BILLING_INVOICES_INV_ID_PDF = "/billing/invoices/{invId}.pdf"
