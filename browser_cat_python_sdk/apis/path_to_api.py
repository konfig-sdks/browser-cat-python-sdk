import typing_extensions

from browser_cat_python_sdk.paths import PathValues
from browser_cat_python_sdk.apis.paths.health import Health
from browser_cat_python_sdk.apis.paths.metrics import Metrics
from browser_cat_python_sdk.apis.paths.openapi import Openapi
from browser_cat_python_sdk.apis.paths.openapi_json import OpenapiJson
from browser_cat_python_sdk.apis.paths.openapi_yaml import OpenapiYaml
from browser_cat_python_sdk.apis.paths.connect import Connect
from browser_cat_python_sdk.apis.paths.auth_keys import AuthKeys
from browser_cat_python_sdk.apis.paths.auth_keys_key_id import AuthKeysKeyId
from browser_cat_python_sdk.apis.paths.usage_buckets import UsageBuckets
from browser_cat_python_sdk.apis.paths.usage_sessions import UsageSessions
from browser_cat_python_sdk.apis.paths.usage_sessions_session_id import UsageSessionsSessionId
from browser_cat_python_sdk.apis.paths.usage_sessions_session_id_events import UsageSessionsSessionIdEvents
from browser_cat_python_sdk.apis.paths.usage_sessions_session_id_events_event_id import UsageSessionsSessionIdEventsEventId
from browser_cat_python_sdk.apis.paths.billing_subscriptions import BillingSubscriptions
from browser_cat_python_sdk.apis.paths.billing_subscriptions_current import BillingSubscriptionsCurrent
from browser_cat_python_sdk.apis.paths.billing_subscriptions_sub_id import BillingSubscriptionsSubId
from browser_cat_python_sdk.apis.paths.billing_invoices import BillingInvoices
from browser_cat_python_sdk.apis.paths.billing_invoices_inv_id import BillingInvoicesInvId
from browser_cat_python_sdk.apis.paths.billing_invoices_inv_id_pdf import BillingInvoicesInvIdPdf

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HEALTH: Health,
        PathValues.METRICS: Metrics,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.CONNECT: Connect,
        PathValues.AUTH_KEYS: AuthKeys,
        PathValues.AUTH_KEYS_KEY_ID: AuthKeysKeyId,
        PathValues.USAGE_BUCKETS: UsageBuckets,
        PathValues.USAGE_SESSIONS: UsageSessions,
        PathValues.USAGE_SESSIONS_SESSION_ID: UsageSessionsSessionId,
        PathValues.USAGE_SESSIONS_SESSION_ID_EVENTS: UsageSessionsSessionIdEvents,
        PathValues.USAGE_SESSIONS_SESSION_ID_EVENTS_EVENT_ID: UsageSessionsSessionIdEventsEventId,
        PathValues.BILLING_SUBSCRIPTIONS: BillingSubscriptions,
        PathValues.BILLING_SUBSCRIPTIONS_CURRENT: BillingSubscriptionsCurrent,
        PathValues.BILLING_SUBSCRIPTIONS_SUB_ID: BillingSubscriptionsSubId,
        PathValues.BILLING_INVOICES: BillingInvoices,
        PathValues.BILLING_INVOICES_INV_ID: BillingInvoicesInvId,
        PathValues.BILLING_INVOICES_INV_ID_PDF: BillingInvoicesInvIdPdf,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HEALTH: Health,
        PathValues.METRICS: Metrics,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.CONNECT: Connect,
        PathValues.AUTH_KEYS: AuthKeys,
        PathValues.AUTH_KEYS_KEY_ID: AuthKeysKeyId,
        PathValues.USAGE_BUCKETS: UsageBuckets,
        PathValues.USAGE_SESSIONS: UsageSessions,
        PathValues.USAGE_SESSIONS_SESSION_ID: UsageSessionsSessionId,
        PathValues.USAGE_SESSIONS_SESSION_ID_EVENTS: UsageSessionsSessionIdEvents,
        PathValues.USAGE_SESSIONS_SESSION_ID_EVENTS_EVENT_ID: UsageSessionsSessionIdEventsEventId,
        PathValues.BILLING_SUBSCRIPTIONS: BillingSubscriptions,
        PathValues.BILLING_SUBSCRIPTIONS_CURRENT: BillingSubscriptionsCurrent,
        PathValues.BILLING_SUBSCRIPTIONS_SUB_ID: BillingSubscriptionsSubId,
        PathValues.BILLING_INVOICES: BillingInvoices,
        PathValues.BILLING_INVOICES_INV_ID: BillingInvoicesInvId,
        PathValues.BILLING_INVOICES_INV_ID_PDF: BillingInvoicesInvIdPdf,
    }
)
