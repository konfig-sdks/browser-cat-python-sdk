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


class UsageListAggregateAccountUsageResponseFieldsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "path",
            "code",
        }
        
        class properties:
            code = schemas.StrSchema
        
            @staticmethod
            def path() -> typing.Type['UsageListAggregateAccountUsageResponseFieldsItemPath']:
                return UsageListAggregateAccountUsageResponseFieldsItemPath
            expected = schemas.StrSchema
            received = schemas.StrSchema
            validation = schemas.StrSchema
            message = schemas.StrSchema
            __annotations__ = {
                "code": code,
                "path": path,
                "expected": expected,
                "received": received,
                "validation": validation,
                "message": message,
            }
    
    path: 'UsageListAggregateAccountUsageResponseFieldsItemPath'
    code: MetaOapg.properties.code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> 'UsageListAggregateAccountUsageResponseFieldsItemPath': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expected"]) -> MetaOapg.properties.expected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["received"]) -> MetaOapg.properties.received: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation"]) -> MetaOapg.properties.validation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "path", "expected", "received", "validation", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> 'UsageListAggregateAccountUsageResponseFieldsItemPath': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expected"]) -> typing.Union[MetaOapg.properties.expected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["received"]) -> typing.Union[MetaOapg.properties.received, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union[MetaOapg.properties.validation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "path", "expected", "received", "validation", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        path: 'UsageListAggregateAccountUsageResponseFieldsItemPath',
        code: typing.Union[MetaOapg.properties.code, str, ],
        expected: typing.Union[MetaOapg.properties.expected, str, schemas.Unset] = schemas.unset,
        received: typing.Union[MetaOapg.properties.received, str, schemas.Unset] = schemas.unset,
        validation: typing.Union[MetaOapg.properties.validation, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsageListAggregateAccountUsageResponseFieldsItem':
        return super().__new__(
            cls,
            *args,
            path=path,
            code=code,
            expected=expected,
            received=received,
            validation=validation,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from browser_cat_python_sdk.model.usage_list_aggregate_account_usage_response_fields_item_path import UsageListAggregateAccountUsageResponseFieldsItemPath
