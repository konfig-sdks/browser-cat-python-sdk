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


class KeyPublic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "lastFour",
            "expiredAt",
            "role",
            "name",
            "keyId",
        }
        
        class properties:
            keyId = schemas.StrSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MEMBER(cls):
                    return cls("member")
                
                @schemas.classproperty
                def ADMIN(cls):
                    return cls("admin")
            
            
            class lastFour(
                schemas.StrSchema
            ):
                pass
            expiredAt = schemas.DateTimeSchema
            __annotations__ = {
                "keyId": keyId,
                "name": name,
                "role": role,
                "lastFour": lastFour,
                "expiredAt": expiredAt,
            }
    
    lastFour: MetaOapg.properties.lastFour
    expiredAt: MetaOapg.properties.expiredAt
    role: MetaOapg.properties.role
    name: MetaOapg.properties.name
    keyId: MetaOapg.properties.keyId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyId"]) -> MetaOapg.properties.keyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFour"]) -> MetaOapg.properties.lastFour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiredAt"]) -> MetaOapg.properties.expiredAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["keyId", "name", "role", "lastFour", "expiredAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyId"]) -> MetaOapg.properties.keyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFour"]) -> MetaOapg.properties.lastFour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiredAt"]) -> MetaOapg.properties.expiredAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["keyId", "name", "role", "lastFour", "expiredAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFour: typing.Union[MetaOapg.properties.lastFour, str, ],
        expiredAt: typing.Union[MetaOapg.properties.expiredAt, str, datetime, ],
        role: typing.Union[MetaOapg.properties.role, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        keyId: typing.Union[MetaOapg.properties.keyId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'KeyPublic':
        return super().__new__(
            cls,
            *args,
            lastFour=lastFour,
            expiredAt=expiredAt,
            role=role,
            name=name,
            keyId=keyId,
            _configuration=_configuration,
            **kwargs,
        )
