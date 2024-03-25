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

from browser_cat_python_sdk.model.billing_get_specific_subscription500_response import BillingGetSpecificSubscription500Response as BillingGetSpecificSubscription500ResponseSchema
from browser_cat_python_sdk.model.billing_get_specific_subscription_response import BillingGetSpecificSubscriptionResponse as BillingGetSpecificSubscriptionResponseSchema
from browser_cat_python_sdk.model.billing_get_specific_subscription403_response import BillingGetSpecificSubscription403Response as BillingGetSpecificSubscription403ResponseSchema
from browser_cat_python_sdk.model.billing_get_specific_subscription401_response import BillingGetSpecificSubscription401Response as BillingGetSpecificSubscription401ResponseSchema
from browser_cat_python_sdk.model.billing_get_specific_subscription404_response import BillingGetSpecificSubscription404Response as BillingGetSpecificSubscription404ResponseSchema
from browser_cat_python_sdk.model.subscription import Subscription as SubscriptionSchema

from browser_cat_python_sdk.type.subscription import Subscription
from browser_cat_python_sdk.type.billing_get_specific_subscription_response import BillingGetSpecificSubscriptionResponse
from browser_cat_python_sdk.type.billing_get_specific_subscription401_response import BillingGetSpecificSubscription401Response
from browser_cat_python_sdk.type.billing_get_specific_subscription500_response import BillingGetSpecificSubscription500Response
from browser_cat_python_sdk.type.billing_get_specific_subscription404_response import BillingGetSpecificSubscription404Response
from browser_cat_python_sdk.type.billing_get_specific_subscription403_response import BillingGetSpecificSubscription403Response

from ...api_client import Dictionary
from browser_cat_python_sdk.pydantic.billing_get_specific_subscription401_response import BillingGetSpecificSubscription401Response as BillingGetSpecificSubscription401ResponsePydantic
from browser_cat_python_sdk.pydantic.billing_get_specific_subscription500_response import BillingGetSpecificSubscription500Response as BillingGetSpecificSubscription500ResponsePydantic
from browser_cat_python_sdk.pydantic.billing_get_specific_subscription403_response import BillingGetSpecificSubscription403Response as BillingGetSpecificSubscription403ResponsePydantic
from browser_cat_python_sdk.pydantic.billing_get_specific_subscription_response import BillingGetSpecificSubscriptionResponse as BillingGetSpecificSubscriptionResponsePydantic
from browser_cat_python_sdk.pydantic.subscription import Subscription as SubscriptionPydantic
from browser_cat_python_sdk.pydantic.billing_get_specific_subscription404_response import BillingGetSpecificSubscription404Response as BillingGetSpecificSubscription404ResponsePydantic

from . import path

# Path params
SubIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'subId': typing.Union[SubIdSchema, str, ],
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


request_path_sub_id = api_client.PathParameter(
    name="subId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SubIdSchema,
    required=True,
)
_auth = [
    'jwtCookie',
    'keyHeader',
]
SchemaFor200ResponseBodyApplicationJson = SubscriptionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Subscription


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Subscription


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = BillingGetSpecificSubscriptionResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BillingGetSpecificSubscriptionResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BillingGetSpecificSubscriptionResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = BillingGetSpecificSubscription401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: BillingGetSpecificSubscription401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: BillingGetSpecificSubscription401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = BillingGetSpecificSubscription403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: BillingGetSpecificSubscription403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: BillingGetSpecificSubscription403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = BillingGetSpecificSubscription404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: BillingGetSpecificSubscription404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: BillingGetSpecificSubscription404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = BillingGetSpecificSubscription500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: BillingGetSpecificSubscription500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: BillingGetSpecificSubscription500Response


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
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_specific_subscription_mapped_args(
        self,
        sub_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if sub_id is not None:
            _path_params["subId"] = sub_id
        args.path = _path_params
        return args

    async def _aget_specific_subscription_oapg(
        self,
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
        Get specific subscription
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_sub_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/billing/subscriptions/{subId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _get_specific_subscription_oapg(
        self,
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
        Get specific subscription
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_sub_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/billing/subscriptions/{subId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class GetSpecificSubscriptionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_specific_subscription(
        self,
        sub_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_specific_subscription_mapped_args(
            sub_id=sub_id,
        )
        return await self._aget_specific_subscription_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_specific_subscription(
        self,
        sub_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_specific_subscription_mapped_args(
            sub_id=sub_id,
        )
        return self._get_specific_subscription_oapg(
            path_params=args.path,
        )

class GetSpecificSubscription(BaseApi):

    async def aget_specific_subscription(
        self,
        sub_id: str,
        validate: bool = False,
        **kwargs,
    ) -> SubscriptionPydantic:
        raw_response = await self.raw.aget_specific_subscription(
            sub_id=sub_id,
            **kwargs,
        )
        if validate:
            return SubscriptionPydantic(**raw_response.body)
        return api_client.construct_model_instance(SubscriptionPydantic, raw_response.body)
    
    
    def get_specific_subscription(
        self,
        sub_id: str,
        validate: bool = False,
    ) -> SubscriptionPydantic:
        raw_response = self.raw.get_specific_subscription(
            sub_id=sub_id,
        )
        if validate:
            return SubscriptionPydantic(**raw_response.body)
        return api_client.construct_model_instance(SubscriptionPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        sub_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_specific_subscription_mapped_args(
            sub_id=sub_id,
        )
        return await self._aget_specific_subscription_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        sub_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_specific_subscription_mapped_args(
            sub_id=sub_id,
        )
        return self._get_specific_subscription_oapg(
            path_params=args.path,
        )

