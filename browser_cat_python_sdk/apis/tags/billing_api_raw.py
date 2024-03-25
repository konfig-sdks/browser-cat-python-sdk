# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from browser_cat_python_sdk.paths.billing_subscriptions_current.get import GetActiveSubscriptionRaw
from browser_cat_python_sdk.paths.billing_invoices_inv_id_pdf.get import GetInvoicePdfRaw
from browser_cat_python_sdk.paths.billing_invoices_inv_id.get import GetSpecificInvoiceRaw
from browser_cat_python_sdk.paths.billing_subscriptions_sub_id.get import GetSpecificSubscriptionRaw
from browser_cat_python_sdk.paths.billing_invoices.get import ListInvoicesRangeRaw
from browser_cat_python_sdk.paths.billing_subscriptions.get import ListSubscriptionsWithinRangeRaw


class BillingApiRaw(
    GetActiveSubscriptionRaw,
    GetInvoicePdfRaw,
    GetSpecificInvoiceRaw,
    GetSpecificSubscriptionRaw,
    ListInvoicesRangeRaw,
    ListSubscriptionsWithinRangeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
