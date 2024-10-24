# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["DepartementResource", "AsyncDepartementResource"]


class DepartementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DepartementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DepartementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepartementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DepartementResourceWithStreamingResponse(self)

    def list(
        self,
        y: str,
        *,
        zoom: str,
        x: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Tuiles vectorielles pour le référentiel administratif département.

        0->9

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zoom:
            raise ValueError(f"Expected a non-empty value for `zoom` but received {zoom!r}")
        if not x:
            raise ValueError(f"Expected a non-empty value for `x` but received {x!r}")
        if not y:
            raise ValueError(f"Expected a non-empty value for `y` but received {y!r}")
        extra_headers = {"Accept": "application/vnd.mapbox-vector-tile", **(extra_headers or {})}
        return self._get(
            f"/tuiles/departement/{zoom}/{x}/{y}.pbf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncDepartementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDepartementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDepartementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepartementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDepartementResourceWithStreamingResponse(self)

    async def list(
        self,
        y: str,
        *,
        zoom: str,
        x: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Tuiles vectorielles pour le référentiel administratif département.

        0->9

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zoom:
            raise ValueError(f"Expected a non-empty value for `zoom` but received {zoom!r}")
        if not x:
            raise ValueError(f"Expected a non-empty value for `x` but received {x!r}")
        if not y:
            raise ValueError(f"Expected a non-empty value for `y` but received {y!r}")
        extra_headers = {"Accept": "application/vnd.mapbox-vector-tile", **(extra_headers or {})}
        return await self._get(
            f"/tuiles/departement/{zoom}/{x}/{y}.pbf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class DepartementResourceWithRawResponse:
    def __init__(self, departement: DepartementResource) -> None:
        self._departement = departement

        self.list = to_custom_raw_response_wrapper(
            departement.list,
            BinaryAPIResponse,
        )


class AsyncDepartementResourceWithRawResponse:
    def __init__(self, departement: AsyncDepartementResource) -> None:
        self._departement = departement

        self.list = async_to_custom_raw_response_wrapper(
            departement.list,
            AsyncBinaryAPIResponse,
        )


class DepartementResourceWithStreamingResponse:
    def __init__(self, departement: DepartementResource) -> None:
        self._departement = departement

        self.list = to_custom_streamed_response_wrapper(
            departement.list,
            StreamedBinaryAPIResponse,
        )


class AsyncDepartementResourceWithStreamingResponse:
    def __init__(self, departement: AsyncDepartementResource) -> None:
        self._departement = departement

        self.list = async_to_custom_streamed_response_wrapper(
            departement.list,
            AsyncStreamedBinaryAPIResponse,
        )
