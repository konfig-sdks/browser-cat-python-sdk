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

from browser_cat_python_sdk.model.key_post import KeyPost as KeyPostSchema
from browser_cat_python_sdk.model.api_keys_create_api_key403_response import ApiKeysCreateApiKey403Response as ApiKeysCreateApiKey403ResponseSchema
from browser_cat_python_sdk.model.api_keys_create_api_key401_response import ApiKeysCreateApiKey401Response as ApiKeysCreateApiKey401ResponseSchema
from browser_cat_python_sdk.model.api_keys_create_api_key_response import ApiKeysCreateApiKeyResponse as ApiKeysCreateApiKeyResponseSchema
from browser_cat_python_sdk.model.key_secret import KeySecret as KeySecretSchema
from browser_cat_python_sdk.model.api_keys_create_api_key500_response import ApiKeysCreateApiKey500Response as ApiKeysCreateApiKey500ResponseSchema

from browser_cat_python_sdk.type.api_keys_create_api_key401_response import ApiKeysCreateApiKey401Response
from browser_cat_python_sdk.type.api_keys_create_api_key500_response import ApiKeysCreateApiKey500Response
from browser_cat_python_sdk.type.key_post import KeyPost
from browser_cat_python_sdk.type.api_keys_create_api_key403_response import ApiKeysCreateApiKey403Response
from browser_cat_python_sdk.type.key_secret import KeySecret
from browser_cat_python_sdk.type.api_keys_create_api_key_response import ApiKeysCreateApiKeyResponse

from ...api_client import Dictionary
from browser_cat_python_sdk.pydantic.key_post import KeyPost as KeyPostPydantic
from browser_cat_python_sdk.pydantic.api_keys_create_api_key500_response import ApiKeysCreateApiKey500Response as ApiKeysCreateApiKey500ResponsePydantic
from browser_cat_python_sdk.pydantic.api_keys_create_api_key_response import ApiKeysCreateApiKeyResponse as ApiKeysCreateApiKeyResponsePydantic
from browser_cat_python_sdk.pydantic.api_keys_create_api_key403_response import ApiKeysCreateApiKey403Response as ApiKeysCreateApiKey403ResponsePydantic
from browser_cat_python_sdk.pydantic.api_keys_create_api_key401_response import ApiKeysCreateApiKey401Response as ApiKeysCreateApiKey401ResponsePydantic
from browser_cat_python_sdk.pydantic.key_secret import KeySecret as KeySecretPydantic

# body param
SchemaForRequestBodyApplicationJson = KeyPostSchema


request_body_key_post = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = KeySecretSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: KeySecret


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: KeySecret


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ApiKeysCreateApiKeyResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ApiKeysCreateApiKeyResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ApiKeysCreateApiKeyResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ApiKeysCreateApiKey401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ApiKeysCreateApiKey401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ApiKeysCreateApiKey401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ApiKeysCreateApiKey403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ApiKeysCreateApiKey403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ApiKeysCreateApiKey403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ApiKeysCreateApiKey500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ApiKeysCreateApiKey500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ApiKeysCreateApiKey500Response


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

    def _create_api_key_mapped_args(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if role is not None:
            _body["role"] = role
        if expired_at is not None:
            _body["expiredAt"] = expired_at
        args.body = _body
        return args

    async def _acreate_api_key_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create an API key
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/auth/keys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_key_post.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _create_api_key_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create an API key
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/auth/keys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_key_post.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class CreateApiKeyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_api_key(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_api_key_mapped_args(
            name=name,
            role=role,
            expired_at=expired_at,
        )
        return await self._acreate_api_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_api_key(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_api_key_mapped_args(
            name=name,
            role=role,
            expired_at=expired_at,
        )
        return self._create_api_key_oapg(
            body=args.body,
        )

class CreateApiKey(BaseApi):

    async def acreate_api_key(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> KeySecretPydantic:
        raw_response = await self.raw.acreate_api_key(
            name=name,
            role=role,
            expired_at=expired_at,
            **kwargs,
        )
        if validate:
            return KeySecretPydantic(**raw_response.body)
        return api_client.construct_model_instance(KeySecretPydantic, raw_response.body)
    
    
    def create_api_key(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> KeySecretPydantic:
        raw_response = self.raw.create_api_key(
            name=name,
            role=role,
            expired_at=expired_at,
        )
        if validate:
            return KeySecretPydantic(**raw_response.body)
        return api_client.construct_model_instance(KeySecretPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_api_key_mapped_args(
            name=name,
            role=role,
            expired_at=expired_at,
        )
        return await self._acreate_api_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        role: typing.Optional[str] = None,
        expired_at: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_api_key_mapped_args(
            name=name,
            role=role,
            expired_at=expired_at,
        )
        return self._create_api_key_oapg(
            body=args.body,
        )

