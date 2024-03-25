# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from browser_cat_python_sdk import schemas  # noqa: F401


class BillingGetActiveSubscriptionResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "error",
            "message",
            "status",
        }
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.NumberSchema
            ):
                
                @schemas.classproperty
                def POSITIVE_400(cls):
                    return cls(400)
            
            
            class error(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BAD_REQUEST(cls):
                    return cls("Bad Request")
            message = schemas.StrSchema
            
            
            class invalid(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BODY(cls):
                    return cls("body")
                
                @schemas.classproperty
                def PATH(cls):
                    return cls("path")
                
                @schemas.classproperty
                def QUERY(cls):
                    return cls("query")
        
            @staticmethod
            def fields() -> typing.Type['BillingGetActiveSubscriptionResponseFields']:
                return BillingGetActiveSubscriptionResponseFields
            __annotations__ = {
                "status": status,
                "error": error,
                "message": message,
                "invalid": invalid,
                "fields": fields,
            }
    
    error: MetaOapg.properties.error
    message: MetaOapg.properties.message
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invalid"]) -> MetaOapg.properties.invalid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'BillingGetActiveSubscriptionResponseFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "error", "message", "invalid", "fields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invalid"]) -> typing.Union[MetaOapg.properties.invalid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['BillingGetActiveSubscriptionResponseFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "error", "message", "invalid", "fields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, float, ],
        invalid: typing.Union[MetaOapg.properties.invalid, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['BillingGetActiveSubscriptionResponseFields', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BillingGetActiveSubscriptionResponse':
        return super().__new__(
            cls,
            *args,
            error=error,
            message=message,
            status=status,
            invalid=invalid,
            fields=fields,
            _configuration=_configuration,
            **kwargs,
        )

from browser_cat_python_sdk.model.billing_get_active_subscription_response_fields import BillingGetActiveSubscriptionResponseFields
