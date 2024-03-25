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

from browser_cat_python_sdk.model.browsers_establish_connection401_response import BrowsersEstablishConnection401Response as BrowsersEstablishConnection401ResponseSchema
from browser_cat_python_sdk.model.browsers_establish_connection500_response import BrowsersEstablishConnection500Response as BrowsersEstablishConnection500ResponseSchema
from browser_cat_python_sdk.model.browsers_establish_connection403_response import BrowsersEstablishConnection403Response as BrowsersEstablishConnection403ResponseSchema
from browser_cat_python_sdk.model.browsers_establish_connection_response import BrowsersEstablishConnectionResponse as BrowsersEstablishConnectionResponseSchema

from browser_cat_python_sdk.type.browsers_establish_connection500_response import BrowsersEstablishConnection500Response
from browser_cat_python_sdk.type.browsers_establish_connection_response import BrowsersEstablishConnectionResponse
from browser_cat_python_sdk.type.browsers_establish_connection403_response import BrowsersEstablishConnection403Response
from browser_cat_python_sdk.type.browsers_establish_connection401_response import BrowsersEstablishConnection401Response

from ...api_client import Dictionary
from browser_cat_python_sdk.pydantic.browsers_establish_connection401_response import BrowsersEstablishConnection401Response as BrowsersEstablishConnection401ResponsePydantic
from browser_cat_python_sdk.pydantic.browsers_establish_connection_response import BrowsersEstablishConnectionResponse as BrowsersEstablishConnectionResponsePydantic
from browser_cat_python_sdk.pydantic.browsers_establish_connection403_response import BrowsersEstablishConnection403Response as BrowsersEstablishConnection403ResponsePydantic
from browser_cat_python_sdk.pydantic.browsers_establish_connection500_response import BrowsersEstablishConnection500Response as BrowsersEstablishConnection500ResponsePydantic

# Query params


class RegionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def AMS(cls):
        return cls("ams")
    
    @schemas.classproperty
    def IAD(cls):
        return cls("iad")
    
    @schemas.classproperty
    def ATL(cls):
        return cls("atl")
    
    @schemas.classproperty
    def BOG(cls):
        return cls("bog")
    
    @schemas.classproperty
    def BOS(cls):
        return cls("bos")
    
    @schemas.classproperty
    def OTP(cls):
        return cls("otp")
    
    @schemas.classproperty
    def MAA(cls):
        return cls("maa")
    
    @schemas.classproperty
    def ORD(cls):
        return cls("ord")
    
    @schemas.classproperty
    def DFW(cls):
        return cls("dfw")
    
    @schemas.classproperty
    def DEN(cls):
        return cls("den")
    
    @schemas.classproperty
    def EZE(cls):
        return cls("eze")
    
    @schemas.classproperty
    def FRA(cls):
        return cls("fra")
    
    @schemas.classproperty
    def GDL(cls):
        return cls("gdl")
    
    @schemas.classproperty
    def HKG(cls):
        return cls("hkg")
    
    @schemas.classproperty
    def JNB(cls):
        return cls("jnb")
    
    @schemas.classproperty
    def LHR(cls):
        return cls("lhr")
    
    @schemas.classproperty
    def LAX(cls):
        return cls("lax")
    
    @schemas.classproperty
    def MAD(cls):
        return cls("mad")
    
    @schemas.classproperty
    def MIA(cls):
        return cls("mia")
    
    @schemas.classproperty
    def YUL(cls):
        return cls("yul")
    
    @schemas.classproperty
    def BOM(cls):
        return cls("bom")
    
    @schemas.classproperty
    def CDG(cls):
        return cls("cdg")
    
    @schemas.classproperty
    def PHX(cls):
        return cls("phx")
    
    @schemas.classproperty
    def QRO(cls):
        return cls("qro")
    
    @schemas.classproperty
    def GIG(cls):
        return cls("gig")
    
    @schemas.classproperty
    def SJC(cls):
        return cls("sjc")
    
    @schemas.classproperty
    def SCL(cls):
        return cls("scl")
    
    @schemas.classproperty
    def GRU(cls):
        return cls("gru")
    
    @schemas.classproperty
    def SEA(cls):
        return cls("sea")
    
    @schemas.classproperty
    def EWR(cls):
        return cls("ewr")
    
    @schemas.classproperty
    def SIN(cls):
        return cls("sin")
    
    @schemas.classproperty
    def ARN(cls):
        return cls("arn")
    
    @schemas.classproperty
    def SYD(cls):
        return cls("syd")
    
    @schemas.classproperty
    def NRT(cls):
        return cls("nrt")
    
    @schemas.classproperty
    def YYZ(cls):
        return cls("yyz")
    
    @schemas.classproperty
    def WAW(cls):
        return cls("waw")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'region': typing.Union[RegionSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_region = api_client.QueryParameter(
    name="region",
    style=api_client.ParameterStyle.FORM,
    schema=RegionSchema,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: 


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)
SchemaFor400ResponseBodyApplicationJson = BrowsersEstablishConnectionResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BrowsersEstablishConnectionResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BrowsersEstablishConnectionResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = BrowsersEstablishConnection401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: BrowsersEstablishConnection401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: BrowsersEstablishConnection401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = BrowsersEstablishConnection403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: BrowsersEstablishConnection403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: BrowsersEstablishConnection403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = BrowsersEstablishConnection500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: BrowsersEstablishConnection500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: BrowsersEstablishConnection500Response


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

    def _establish_connection_mapped_args(
        self,
        region: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if region is not None:
            _query_params["region"] = region
        args.query = _query_params
        return args

    async def _aestablish_connection_oapg(
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
        Connect to a browser
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_region,
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
            path_template='/connect',
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


    def _establish_connection_oapg(
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
        Connect to a browser
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_region,
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
            path_template='/connect',
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


class EstablishConnectionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aestablish_connection(
        self,
        region: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._establish_connection_mapped_args(
            region=region,
        )
        return await self._aestablish_connection_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def establish_connection(
        self,
        region: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._establish_connection_mapped_args(
            region=region,
        )
        return self._establish_connection_oapg(
            query_params=args.query,
        )

class EstablishConnection(BaseApi):

    async def aestablish_connection(
        self,
        region: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aestablish_connection(
            region=region,
            **kwargs,
        )
    
    
    def establish_connection(
        self,
        region: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.establish_connection(
            region=region,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        region: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._establish_connection_mapped_args(
            region=region,
        )
        return await self._aestablish_connection_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        region: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._establish_connection_mapped_args(
            region=region,
        )
        return self._establish_connection_oapg(
            query_params=args.query,
        )

