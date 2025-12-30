# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IdentetyError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import app, orgs, roles, users, clients
    from .resources.app import AppResource, AsyncAppResource
    from .resources.orgs import OrgsResource, AsyncOrgsResource
    from .resources.roles import RolesResource, AsyncRolesResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.clients import ClientsResource, AsyncClientsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Identety",
    "AsyncIdentety",
    "Client",
    "AsyncClient",
]


class Identety(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Identety client instance.

        This automatically infers the `api_key` argument from the `X_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_API_KEY")
        if api_key is None:
            raise IdentetyError(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_API_KEY environment variable"
            )
        self.api_key = api_key

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def app(self) -> AppResource:
        from .resources.app import AppResource

        return AppResource(self)

    @cached_property
    def clients(self) -> ClientsResource:
        from .resources.clients import ClientsResource

        return ClientsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def orgs(self) -> OrgsResource:
        from .resources.orgs import OrgsResource

        return OrgsResource(self)

    @cached_property
    def roles(self) -> RolesResource:
        from .resources.roles import RolesResource

        return RolesResource(self)

    @cached_property
    def with_raw_response(self) -> IdentetyWithRawResponse:
        return IdentetyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentetyWithStreamedResponse:
        return IdentetyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncIdentety(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncIdentety client instance.

        This automatically infers the `api_key` argument from the `X_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_API_KEY")
        if api_key is None:
            raise IdentetyError(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_API_KEY environment variable"
            )
        self.api_key = api_key

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def app(self) -> AsyncAppResource:
        from .resources.app import AsyncAppResource

        return AsyncAppResource(self)

    @cached_property
    def clients(self) -> AsyncClientsResource:
        from .resources.clients import AsyncClientsResource

        return AsyncClientsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def orgs(self) -> AsyncOrgsResource:
        from .resources.orgs import AsyncOrgsResource

        return AsyncOrgsResource(self)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        from .resources.roles import AsyncRolesResource

        return AsyncRolesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncIdentetyWithRawResponse:
        return AsyncIdentetyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentetyWithStreamedResponse:
        return AsyncIdentetyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class IdentetyWithRawResponse:
    _client: Identety

    def __init__(self, client: Identety) -> None:
        self._client = client

    @cached_property
    def app(self) -> app.AppResourceWithRawResponse:
        from .resources.app import AppResourceWithRawResponse

        return AppResourceWithRawResponse(self._client.app)

    @cached_property
    def clients(self) -> clients.ClientsResourceWithRawResponse:
        from .resources.clients import ClientsResourceWithRawResponse

        return ClientsResourceWithRawResponse(self._client.clients)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithRawResponse:
        from .resources.orgs import OrgsResourceWithRawResponse

        return OrgsResourceWithRawResponse(self._client.orgs)

    @cached_property
    def roles(self) -> roles.RolesResourceWithRawResponse:
        from .resources.roles import RolesResourceWithRawResponse

        return RolesResourceWithRawResponse(self._client.roles)


class AsyncIdentetyWithRawResponse:
    _client: AsyncIdentety

    def __init__(self, client: AsyncIdentety) -> None:
        self._client = client

    @cached_property
    def app(self) -> app.AsyncAppResourceWithRawResponse:
        from .resources.app import AsyncAppResourceWithRawResponse

        return AsyncAppResourceWithRawResponse(self._client.app)

    @cached_property
    def clients(self) -> clients.AsyncClientsResourceWithRawResponse:
        from .resources.clients import AsyncClientsResourceWithRawResponse

        return AsyncClientsResourceWithRawResponse(self._client.clients)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithRawResponse:
        from .resources.orgs import AsyncOrgsResourceWithRawResponse

        return AsyncOrgsResourceWithRawResponse(self._client.orgs)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithRawResponse:
        from .resources.roles import AsyncRolesResourceWithRawResponse

        return AsyncRolesResourceWithRawResponse(self._client.roles)


class IdentetyWithStreamedResponse:
    _client: Identety

    def __init__(self, client: Identety) -> None:
        self._client = client

    @cached_property
    def app(self) -> app.AppResourceWithStreamingResponse:
        from .resources.app import AppResourceWithStreamingResponse

        return AppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def clients(self) -> clients.ClientsResourceWithStreamingResponse:
        from .resources.clients import ClientsResourceWithStreamingResponse

        return ClientsResourceWithStreamingResponse(self._client.clients)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithStreamingResponse:
        from .resources.orgs import OrgsResourceWithStreamingResponse

        return OrgsResourceWithStreamingResponse(self._client.orgs)

    @cached_property
    def roles(self) -> roles.RolesResourceWithStreamingResponse:
        from .resources.roles import RolesResourceWithStreamingResponse

        return RolesResourceWithStreamingResponse(self._client.roles)


class AsyncIdentetyWithStreamedResponse:
    _client: AsyncIdentety

    def __init__(self, client: AsyncIdentety) -> None:
        self._client = client

    @cached_property
    def app(self) -> app.AsyncAppResourceWithStreamingResponse:
        from .resources.app import AsyncAppResourceWithStreamingResponse

        return AsyncAppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def clients(self) -> clients.AsyncClientsResourceWithStreamingResponse:
        from .resources.clients import AsyncClientsResourceWithStreamingResponse

        return AsyncClientsResourceWithStreamingResponse(self._client.clients)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithStreamingResponse:
        from .resources.orgs import AsyncOrgsResourceWithStreamingResponse

        return AsyncOrgsResourceWithStreamingResponse(self._client.orgs)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithStreamingResponse:
        from .resources.roles import AsyncRolesResourceWithStreamingResponse

        return AsyncRolesResourceWithStreamingResponse(self._client.roles)


Client = Identety

AsyncClient = AsyncIdentety
