# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Bdnb",
    "AsyncBdnb",
    "Client",
    "AsyncClient",
]


class Bdnb(SyncAPIClient):
    autocompletion: resources.AutocompletionResource
    stats: resources.StatsResource
    donnees: resources.DonneesResource
    metadonnees: resources.MetadonneesResource
    tuiles: resources.TuilesResource
    with_raw_response: BdnbWithRawResponse
    with_streaming_response: BdnbWithStreamedResponse

    # client options
    prefer_option: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        prefer_option: str | None = "count=exact",
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous BDNB client instance.

        This automatically infers the `api_key` argument from the `BDNB_API_KEY` environment variable if it is not provided.
        """
        if prefer_option is None:
            prefer_option = "count=exact"
        self.prefer_option = prefer_option

        if api_key is None:
            api_key = os.environ.get("BDNB_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BDNB_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bdnb.io/v1/bdnb/"

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

        self.autocompletion = resources.AutocompletionResource(self)
        self.stats = resources.StatsResource(self)
        self.donnees = resources.DonneesResource(self)
        self.metadonnees = resources.MetadonneesResource(self)
        self.tuiles = resources.TuilesResource(self)
        self.with_raw_response = BdnbWithRawResponse(self)
        self.with_streaming_response = BdnbWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Gravitee-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Prefer": self.prefer_option if self.prefer_option is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        prefer_option: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            prefer_option=prefer_option or self.prefer_option,
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


class AsyncBdnb(AsyncAPIClient):
    autocompletion: resources.AsyncAutocompletionResource
    stats: resources.AsyncStatsResource
    donnees: resources.AsyncDonneesResource
    metadonnees: resources.AsyncMetadonneesResource
    tuiles: resources.AsyncTuilesResource
    with_raw_response: AsyncBdnbWithRawResponse
    with_streaming_response: AsyncBdnbWithStreamedResponse

    # client options
    prefer_option: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        prefer_option: str | None = "count=exact",
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async BDNB client instance.

        This automatically infers the `api_key` argument from the `BDNB_API_KEY` environment variable if it is not provided.
        """
        if prefer_option is None:
            prefer_option = "count=exact"
        self.prefer_option = prefer_option

        if api_key is None:
            api_key = os.environ.get("BDNB_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BDNB_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bdnb.io/v1/bdnb/"

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

        self.autocompletion = resources.AsyncAutocompletionResource(self)
        self.stats = resources.AsyncStatsResource(self)
        self.donnees = resources.AsyncDonneesResource(self)
        self.metadonnees = resources.AsyncMetadonneesResource(self)
        self.tuiles = resources.AsyncTuilesResource(self)
        self.with_raw_response = AsyncBdnbWithRawResponse(self)
        self.with_streaming_response = AsyncBdnbWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Gravitee-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Prefer": self.prefer_option if self.prefer_option is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        prefer_option: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            prefer_option=prefer_option or self.prefer_option,
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


class BdnbWithRawResponse:
    def __init__(self, client: Bdnb) -> None:
        self.autocompletion = resources.AutocompletionResourceWithRawResponse(client.autocompletion)
        self.stats = resources.StatsResourceWithRawResponse(client.stats)
        self.donnees = resources.DonneesResourceWithRawResponse(client.donnees)
        self.metadonnees = resources.MetadonneesResourceWithRawResponse(client.metadonnees)
        self.tuiles = resources.TuilesResourceWithRawResponse(client.tuiles)


class AsyncBdnbWithRawResponse:
    def __init__(self, client: AsyncBdnb) -> None:
        self.autocompletion = resources.AsyncAutocompletionResourceWithRawResponse(client.autocompletion)
        self.stats = resources.AsyncStatsResourceWithRawResponse(client.stats)
        self.donnees = resources.AsyncDonneesResourceWithRawResponse(client.donnees)
        self.metadonnees = resources.AsyncMetadonneesResourceWithRawResponse(client.metadonnees)
        self.tuiles = resources.AsyncTuilesResourceWithRawResponse(client.tuiles)


class BdnbWithStreamedResponse:
    def __init__(self, client: Bdnb) -> None:
        self.autocompletion = resources.AutocompletionResourceWithStreamingResponse(client.autocompletion)
        self.stats = resources.StatsResourceWithStreamingResponse(client.stats)
        self.donnees = resources.DonneesResourceWithStreamingResponse(client.donnees)
        self.metadonnees = resources.MetadonneesResourceWithStreamingResponse(client.metadonnees)
        self.tuiles = resources.TuilesResourceWithStreamingResponse(client.tuiles)


class AsyncBdnbWithStreamedResponse:
    def __init__(self, client: AsyncBdnb) -> None:
        self.autocompletion = resources.AsyncAutocompletionResourceWithStreamingResponse(client.autocompletion)
        self.stats = resources.AsyncStatsResourceWithStreamingResponse(client.stats)
        self.donnees = resources.AsyncDonneesResourceWithStreamingResponse(client.donnees)
        self.metadonnees = resources.AsyncMetadonneesResourceWithStreamingResponse(client.metadonnees)
        self.tuiles = resources.AsyncTuilesResourceWithStreamingResponse(client.tuiles)


Client = Bdnb

AsyncClient = AsyncBdnb
