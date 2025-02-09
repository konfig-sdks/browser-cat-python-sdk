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


class UsageSessionPublic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "usageSessionId",
            "agentType",
            "method",
            "clerkUserId",
            "keyId",
            "startedAt",
            "sessionId",
            "clerkOrgId",
            "machineRegion",
            "browserType",
            "endpoint",
            "machineId",
            "endedAt",
            "browserVersion",
            "agentVersion",
            "status",
        }
        
        class properties:
            
            
            class usageSessionId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\da-f]{8}(?:-[\da-f]{4}){3}-[\da-f]{12}$',
                    }]
            
            
            class clerkOrgId(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 128
                    min_length = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'clerkOrgId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class clerkUserId(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    max_length = 128
                    min_length = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'clerkUserId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class keyId(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\da-f]{8}(?:-[\da-f]{4}){3}-[\da-f]{12}$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'keyId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "api": "API",
                        "ws": "WS",
                    }
                
                @schemas.classproperty
                def API(cls):
                    return cls("api")
                
                @schemas.classproperty
                def WS(cls):
                    return cls("ws")
            endpoint = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "success": "SUCCESS",
                        "failure": "FAILURE",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("success")
                
                @schemas.classproperty
                def FAILURE(cls):
                    return cls("failure")
            
            
            class machineId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class machineRegion(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class browserType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "chromium": "CHROMIUM",
                        "firefox": "FIREFOX",
                        "webkit": "WEBKIT",
                        "chrome": "CHROME",
                        "chrome-beta": "CHROMEBETA",
                        "msedge": "MSEDGE",
                        "msedge-beta": "MSEDGEBETA",
                        "msedge-dev": "MSEDGEDEV",
                    }
                
                @schemas.classproperty
                def CHROMIUM(cls):
                    return cls("chromium")
                
                @schemas.classproperty
                def FIREFOX(cls):
                    return cls("firefox")
                
                @schemas.classproperty
                def WEBKIT(cls):
                    return cls("webkit")
                
                @schemas.classproperty
                def CHROME(cls):
                    return cls("chrome")
                
                @schemas.classproperty
                def CHROMEBETA(cls):
                    return cls("chrome-beta")
                
                @schemas.classproperty
                def MSEDGE(cls):
                    return cls("msedge")
                
                @schemas.classproperty
                def MSEDGEBETA(cls):
                    return cls("msedge-beta")
                
                @schemas.classproperty
                def MSEDGEDEV(cls):
                    return cls("msedge-dev")
            
            
            class browserVersion(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class agentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "playwright": "PLAYWRIGHT",
                        "puppeteer": "PUPPETEER",
                        "selenium": "SELENIUM",
                    }
                
                @schemas.classproperty
                def PLAYWRIGHT(cls):
                    return cls("playwright")
                
                @schemas.classproperty
                def PUPPETEER(cls):
                    return cls("puppeteer")
                
                @schemas.classproperty
                def SELENIUM(cls):
                    return cls("selenium")
            
            
            class agentVersion(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            startedAt = schemas.DateTimeSchema
            
            
            class endedAt(
                schemas.DateTimeBase,
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'endedAt':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            sessionId = schemas.StrSchema
            __annotations__ = {
                "usageSessionId": usageSessionId,
                "clerkOrgId": clerkOrgId,
                "clerkUserId": clerkUserId,
                "keyId": keyId,
                "method": method,
                "endpoint": endpoint,
                "status": status,
                "machineId": machineId,
                "machineRegion": machineRegion,
                "browserType": browserType,
                "browserVersion": browserVersion,
                "agentType": agentType,
                "agentVersion": agentVersion,
                "startedAt": startedAt,
                "endedAt": endedAt,
                "sessionId": sessionId,
            }
    
    usageSessionId: MetaOapg.properties.usageSessionId
    agentType: MetaOapg.properties.agentType
    method: MetaOapg.properties.method
    clerkUserId: MetaOapg.properties.clerkUserId
    keyId: MetaOapg.properties.keyId
    startedAt: MetaOapg.properties.startedAt
    sessionId: MetaOapg.properties.sessionId
    clerkOrgId: MetaOapg.properties.clerkOrgId
    machineRegion: MetaOapg.properties.machineRegion
    browserType: MetaOapg.properties.browserType
    endpoint: MetaOapg.properties.endpoint
    machineId: MetaOapg.properties.machineId
    endedAt: MetaOapg.properties.endedAt
    browserVersion: MetaOapg.properties.browserVersion
    agentVersion: MetaOapg.properties.agentVersion
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usageSessionId"]) -> MetaOapg.properties.usageSessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clerkOrgId"]) -> MetaOapg.properties.clerkOrgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clerkUserId"]) -> MetaOapg.properties.clerkUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyId"]) -> MetaOapg.properties.keyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machineId"]) -> MetaOapg.properties.machineId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machineRegion"]) -> MetaOapg.properties.machineRegion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browserType"]) -> MetaOapg.properties.browserType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browserVersion"]) -> MetaOapg.properties.browserVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentType"]) -> MetaOapg.properties.agentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentVersion"]) -> MetaOapg.properties.agentVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endedAt"]) -> MetaOapg.properties.endedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["usageSessionId", "clerkOrgId", "clerkUserId", "keyId", "method", "endpoint", "status", "machineId", "machineRegion", "browserType", "browserVersion", "agentType", "agentVersion", "startedAt", "endedAt", "sessionId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usageSessionId"]) -> MetaOapg.properties.usageSessionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clerkOrgId"]) -> MetaOapg.properties.clerkOrgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clerkUserId"]) -> MetaOapg.properties.clerkUserId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyId"]) -> MetaOapg.properties.keyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machineId"]) -> MetaOapg.properties.machineId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machineRegion"]) -> MetaOapg.properties.machineRegion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browserType"]) -> MetaOapg.properties.browserType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browserVersion"]) -> MetaOapg.properties.browserVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentType"]) -> MetaOapg.properties.agentType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentVersion"]) -> MetaOapg.properties.agentVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endedAt"]) -> MetaOapg.properties.endedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["usageSessionId", "clerkOrgId", "clerkUserId", "keyId", "method", "endpoint", "status", "machineId", "machineRegion", "browserType", "browserVersion", "agentType", "agentVersion", "startedAt", "endedAt", "sessionId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        usageSessionId: typing.Union[MetaOapg.properties.usageSessionId, str, ],
        agentType: typing.Union[MetaOapg.properties.agentType, str, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        clerkUserId: typing.Union[MetaOapg.properties.clerkUserId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        keyId: typing.Union[MetaOapg.properties.keyId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        startedAt: typing.Union[MetaOapg.properties.startedAt, str, datetime, ],
        sessionId: typing.Union[MetaOapg.properties.sessionId, str, ],
        clerkOrgId: typing.Union[MetaOapg.properties.clerkOrgId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        machineRegion: typing.Union[MetaOapg.properties.machineRegion, str, ],
        browserType: typing.Union[MetaOapg.properties.browserType, str, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, ],
        machineId: typing.Union[MetaOapg.properties.machineId, str, ],
        endedAt: typing.Union[MetaOapg.properties.endedAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        browserVersion: typing.Union[MetaOapg.properties.browserVersion, str, ],
        agentVersion: typing.Union[MetaOapg.properties.agentVersion, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsageSessionPublic':
        return super().__new__(
            cls,
            *args,
            usageSessionId=usageSessionId,
            agentType=agentType,
            method=method,
            clerkUserId=clerkUserId,
            keyId=keyId,
            startedAt=startedAt,
            sessionId=sessionId,
            clerkOrgId=clerkOrgId,
            machineRegion=machineRegion,
            browserType=browserType,
            endpoint=endpoint,
            machineId=machineId,
            endedAt=endedAt,
            browserVersion=browserVersion,
            agentVersion=agentVersion,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
