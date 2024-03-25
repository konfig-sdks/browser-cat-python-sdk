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

from browser_cat_python_sdk.model.usage_list_request_events401_response import UsageListRequestEvents401Response as UsageListRequestEvents401ResponseSchema
from browser_cat_python_sdk.model.usage_list_request_events403_response import UsageListRequestEvents403Response as UsageListRequestEvents403ResponseSchema
from browser_cat_python_sdk.model.usage_event_list import UsageEventList as UsageEventListSchema
from browser_cat_python_sdk.model.usage_list_request_events_response import UsageListRequestEventsResponse as UsageListRequestEventsResponseSchema
from browser_cat_python_sdk.model.usage_list_request_events500_response import UsageListRequestEvents500Response as UsageListRequestEvents500ResponseSchema

from browser_cat_python_sdk.type.usage_list_request_events_response import UsageListRequestEventsResponse
from browser_cat_python_sdk.type.usage_list_request_events403_response import UsageListRequestEvents403Response
from browser_cat_python_sdk.type.usage_event_list import UsageEventList
from browser_cat_python_sdk.type.usage_list_request_events401_response import UsageListRequestEvents401Response
from browser_cat_python_sdk.type.usage_list_request_events500_response import UsageListRequestEvents500Response

from ...api_client import Dictionary
from browser_cat_python_sdk.pydantic.usage_list_request_events500_response import UsageListRequestEvents500Response as UsageListRequestEvents500ResponsePydantic
from browser_cat_python_sdk.pydantic.usage_list_request_events_response import UsageListRequestEventsResponse as UsageListRequestEventsResponsePydantic
from browser_cat_python_sdk.pydantic.usage_list_request_events403_response import UsageListRequestEvents403Response as UsageListRequestEvents403ResponsePydantic
from browser_cat_python_sdk.pydantic.usage_event_list import UsageEventList as UsageEventListPydantic
from browser_cat_python_sdk.pydantic.usage_list_request_events401_response import UsageListRequestEvents401Response as UsageListRequestEvents401ResponsePydantic

# Query params


class LimitSchema(
    schemas.IntSchema
):
    pass


class OffsetSchema(
    schemas.AnyTypeSchema,
):


    class MetaOapg:


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
# Path params
SessionIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'sessionId': typing.Union[SessionIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_session_id = api_client.PathParameter(
    name="sessionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SessionIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = UsageEventListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsageEventList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsageEventList


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = UsageListRequestEventsResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: UsageListRequestEventsResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: UsageListRequestEventsResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UsageListRequestEvents401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UsageListRequestEvents401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UsageListRequestEvents401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = UsageListRequestEvents403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: UsageListRequestEvents403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: UsageListRequestEvents403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = UsageListRequestEvents500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: UsageListRequestEvents500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: UsageListRequestEvents500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_request_events_mapped_args(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if after_date is not None:
            _query_params["afterDate"] = after_date
        if before_date is not None:
            _query_params["beforeDate"] = before_date
        if session_id is not None:
            _path_params["sessionId"] = session_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_request_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        List events for a request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_session_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_after_date,
            request_query_before_date,
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
            path_template='/usage/sessions/{sessionId}/events',
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


    def _list_request_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List events for a request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_session_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_after_date,
            request_query_before_date,
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
            path_template='/usage/sessions/{sessionId}/events',
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


class ListRequestEventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_request_events(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_request_events_mapped_args(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
        )
        return await self._alist_request_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_request_events(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_request_events_mapped_args(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
        )
        return self._list_request_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListRequestEvents(BaseApi):

    async def alist_request_events(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsageEventListPydantic:
        raw_response = await self.raw.alist_request_events(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
            **kwargs,
        )
        if validate:
            return RootModel[UsageEventListPydantic](raw_response.body).root
        return api_client.construct_model_instance(UsageEventListPydantic, raw_response.body)
    
    
    def list_request_events(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> UsageEventListPydantic:
        raw_response = self.raw.list_request_events(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
        )
        if validate:
            return RootModel[UsageEventListPydantic](raw_response.body).root
        return api_client.construct_model_instance(UsageEventListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_request_events_mapped_args(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
        )
        return await self._alist_request_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        session_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        after_date: typing.Optional[datetime] = None,
        before_date: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_request_events_mapped_args(
            session_id=session_id,
            limit=limit,
            offset=offset,
            after_date=after_date,
            before_date=before_date,
        )
        return self._list_request_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

