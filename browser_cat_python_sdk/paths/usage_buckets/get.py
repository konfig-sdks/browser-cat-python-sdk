# coding: utf-8

"""
    BrowserCat API

    Providing purr-fect headless browser access via utility endpoints and direct websocket connections.

    The version of the OpenAPI document: 1.0.0
    Contact: support@browsercat.com
    Created by: https://www.browsercat.com/contact
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from browser_cat_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from browser_cat_python_sdk.api_response import AsyncGeneratorResponse
from browser_cat_python_sdk import api_client, exceptions
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

from browser_cat_python_sdk.model.usage_bucket_list import UsageBucketList as UsageBucketListSchema
from browser_cat_python_sdk.model.usage_list_aggregate_account_usage401_response import UsageListAggregateAccountUsage401Response as UsageListAggregateAccountUsage401ResponseSchema
from browser_cat_python_sdk.model.usage_list_aggregate_account_usage403_response import UsageListAggregateAccountUsage403Response as UsageListAggregateAccountUsage403ResponseSchema
from browser_cat_python_sdk.model.usage_list_aggregate_account_usage500_response import UsageListAggregateAccountUsage500Response as UsageListAggregateAccountUsage500ResponseSchema
from browser_cat_python_sdk.model.usage_list_aggregate_account_usage_response import UsageListAggregateAccountUsageResponse as UsageListAggregateAccountUsageResponseSchema

from browser_cat_python_sdk.type.usage_bucket_list import UsageBucketList
from browser_cat_python_sdk.type.usage_list_aggregate_account_usage403_response import UsageListAggregateAccountUsage403Response
from browser_cat_python_sdk.type.usage_list_aggregate_account_usage_response import UsageListAggregateAccountUsageResponse
from browser_cat_python_sdk.type.usage_list_aggregate_account_usage401_response import UsageListAggregateAccountUsage401Response
from browser_cat_python_sdk.type.usage_list_aggregate_account_usage500_response import UsageListAggregateAccountUsage500Response

from ...api_client import Dictionary
from browser_cat_python_sdk.pydantic.usage_bucket_list import UsageBucketList as UsageBucketListPydantic
from browser_cat_python_sdk.pydantic.usage_list_aggregate_account_usage403_response import UsageListAggregateAccountUsage403Response as UsageListAggregateAccountUsage403ResponsePydantic
from browser_cat_python_sdk.pydantic.usage_list_aggregate_account_usage401_response import UsageListAggregateAccountUsage401Response as UsageListAggregateAccountUsage401ResponsePydantic
from browser_cat_python_sdk.pydantic.usage_list_aggregate_account_usage500_response import UsageListAggregateAccountUsage500Response as UsageListAggregateAccountUsage500ResponsePydantic
from browser_cat_python_sdk.pydantic.usage_list_aggregate_account_usage_response import UsageListAggregateAccountUsageResponse as UsageListAggregateAccountUsageResponsePydantic

from . import path

# Query params


class LimitSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 1000
        inclusive_minimum = 1


class OffsetSchema(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        inclusive_minimum = 0


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OffsetSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
AfterDateSchema = schemas.DateTimeSchema
BeforeDateSchema = schemas.DateTimeSchema


class UnitSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "minute": "MINUTE",
            "hour": "HOUR",
            "day": "DAY",
            "week": "WEEK",
        }
    
    @schemas.classproperty
    def MINUTE(cls):
        return cls("minute")
    
    @schemas.classproperty
    def HOUR(cls):
        return cls("hour")
    
    @schemas.classproperty
    def DAY(cls):
        return cls("day")
    
    @schemas.classproperty
    def WEEK(cls):
        return cls("week")


class UserIdSchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class any_of_0(
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                max_length = 128
                min_length = 0
        
        
        class any_of_1(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "null": "NONE",
                }
            
            @schemas.classproperty
            def NONE(cls):
                return cls("null")
        
        @classmethod
        @functools.lru_cache()
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class KeyIdSchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class any_of_0(
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                regex=[{
                    'pattern': r'^[\da-f]{8}(?:-[\da-f]{4}){3}-[\da-f]{12}$',
                }]
        
        
        class any_of_1(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "null": "NONE",
                }
            
            @schemas.classproperty
            def NONE(cls):
                return cls("null")
        
        @classmethod
        @functools.lru_cache()
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'KeyIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class MethodSchema(
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
EndpointSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'afterDate': typing.Union[AfterDateSchema, str, datetime, ],
        'beforeDate': typing.Union[BeforeDateSchema, str, datetime, ],
        'unit': typing.Union[UnitSchema, str, ],
        'userId': typing.Union[UserIdSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'keyId': typing.Union[KeyIdSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'method': typing.Union[MethodSchema, str, ],
        'endpoint': typing.Union[EndpointSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_after_date = api_client.QueryParameter(
    name="afterDate",
    style=api_client.ParameterStyle.FORM,
    schema=AfterDateSchema,
    explode=True,
)
request_query_before_date = api_client.QueryParameter(
    name="beforeDate",
    style=api_client.ParameterStyle.FORM,
    schema=BeforeDateSchema,
    explode=True,
)
request_query_unit = api_client.QueryParameter(
    name="unit",
    style=api_client.ParameterStyle.FORM,
    schema=UnitSchema,
    explode=True,
)
request_query_user_id = api_client.QueryParameter(
    name="userId",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
request_query_key_id = api_client.QueryParameter(
    name="keyId",
    style=api_client.ParameterStyle.FORM,
    schema=KeyIdSchema,
    explode=True,
)
request_query_method = api_client.QueryParameter(
    name="method",
    style=api_client.ParameterStyle.FORM,
    schema=MethodSchema,
    explode=True,
)
request_query_endpoint = api_client.QueryParameter(
    name="endpoint",
    style=api_client.ParameterStyle.FORM,
    schema=EndpointSchema,
    explode=True,
)
_auth = [
    'jwtCookie',
    'keyHeader',
]
SchemaFor200ResponseBodyApplicationJson = UsageBucketListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsageBucketList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsageBucketList


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = UsageListAggregateAccountUsageResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: UsageListAggregateAccountUsageResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: UsageListAggregateAccountUsageResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UsageListAggregateAccountUsage401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UsageListAggregateAccountUsage401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UsageListAggregateAccountUsage401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = UsageListAggregateAccountUsage403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: UsageListAggregateAccountUsage403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: UsageListAggregateAccountUsage403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = UsageListAggregateAccountUsage500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: UsageListAggregateAccountUsage500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: UsageListAggregateAccountUsage500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_aggregate_account_usage_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if after_date is not None:
            _query_params["afterDate"] = after_date
        if before_date is not None:
            _query_params["beforeDate"] = before_date
        if unit is not None:
            _query_params["unit"] = unit
        if user_id is not None:
            _query_params["userId"] = user_id
        if key_id is not None:
            _query_params["keyId"] = key_id
        if method is not None:
            _query_params["method"] = method
        if endpoint is not None:
            _query_params["endpoint"] = endpoint
        args.query = _query_params
        return args

    async def _alist_aggregate_account_usage_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List aggregate account usage
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_after_date,
            request_query_before_date,
            request_query_unit,
            request_query_user_id,
            request_query_key_id,
            request_query_method,
            request_query_endpoint,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/usage/buckets',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_aggregate_account_usage_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List aggregate account usage
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_after_date,
            request_query_before_date,
            request_query_unit,
            request_query_user_id,
            request_query_key_id,
            request_query_method,
            request_query_endpoint,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/usage/buckets',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAggregateAccountUsageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_aggregate_account_usage(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_aggregate_account_usage_mapped_args(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
        )
        return await self._alist_aggregate_account_usage_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_aggregate_account_usage(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_aggregate_account_usage_mapped_args(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
        )
        return self._list_aggregate_account_usage_oapg(
            query_params=args.query,
        )

class ListAggregateAccountUsage(BaseApi):

    async def alist_aggregate_account_usage(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsageBucketListPydantic:
        raw_response = await self.raw.alist_aggregate_account_usage(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
            **kwargs,
        )
        if validate:
            return RootModel[UsageBucketListPydantic](raw_response.body).root
        return api_client.construct_model_instance(UsageBucketListPydantic, raw_response.body)
    
    
    def list_aggregate_account_usage(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsageBucketListPydantic:
        raw_response = self.raw.list_aggregate_account_usage(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
        )
        if validate:
            return RootModel[UsageBucketListPydantic](raw_response.body).root
        return api_client.construct_model_instance(UsageBucketListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_aggregate_account_usage_mapped_args(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
        )
        return await self._alist_aggregate_account_usage_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        unit: typing.Optional[str] = None,
        user_id: typing.Optional[typing.Union[str, str]] = None,
        key_id: typing.Optional[typing.Union[str, str]] = None,
        method: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_aggregate_account_usage_mapped_args(
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            unit=unit,
            user_id=user_id,
            key_id=key_id,
            method=method,
            endpoint=endpoint,
        )
        return self._list_aggregate_account_usage_oapg(
            query_params=args.query,
        )

