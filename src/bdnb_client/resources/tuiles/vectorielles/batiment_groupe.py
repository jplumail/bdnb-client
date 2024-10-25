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

__all__ = ["BatimentGroupeResource", "AsyncBatimentGroupeResource"]


class BatimentGroupeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentGroupeResourceWithStreamingResponse(self)

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
        """
        Tuiles vectorielles des groupes de bâtiments BDNB (Souscription Api Expert).
        Zoom = 14

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
            f"/tuiles/batiment_groupe/{zoom}/{x}/{y}.pbf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBatimentGroupeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentGroupeResourceWithStreamingResponse(self)

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
        """
        Tuiles vectorielles des groupes de bâtiments BDNB (Souscription Api Expert).
        Zoom = 14

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
            f"/tuiles/batiment_groupe/{zoom}/{x}/{y}.pbf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_custom_raw_response_wrapper(
            batiment_groupe.list,
            BinaryAPIResponse,
        )


class AsyncBatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_custom_raw_response_wrapper(
            batiment_groupe.list,
            AsyncBinaryAPIResponse,
        )


class BatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_custom_streamed_response_wrapper(
            batiment_groupe.list,
            StreamedBinaryAPIResponse,
        )


class AsyncBatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_custom_streamed_response_wrapper(
            batiment_groupe.list,
            AsyncStreamedBinaryAPIResponse,
        )
