# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.donnees.batiment_groupe.complet import polygon_list_params
from .....types.donnees.batiment_groupe.complet.polygon_list_response import PolygonListResponse

__all__ = ["PolygonResource", "AsyncPolygonResource"]


class PolygonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolygonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return PolygonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolygonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return PolygonResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        coordinates: Iterable[Iterable[Iterable[float]]] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolygonListResponse:
        """
        récupérer les bâtiments qui sont à l'intérieur d'un polygone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/donnees/batiment_groupe_complet/polygon",
            body=maybe_transform(
                {
                    "coordinates": coordinates,
                    "type": type,
                },
                polygon_list_params.PolygonListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, polygon_list_params.PolygonListParams),
            ),
            cast_to=PolygonListResponse,
        )


class AsyncPolygonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolygonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncPolygonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolygonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncPolygonResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        coordinates: Iterable[Iterable[Iterable[float]]] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolygonListResponse:
        """
        récupérer les bâtiments qui sont à l'intérieur d'un polygone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/donnees/batiment_groupe_complet/polygon",
            body=await async_maybe_transform(
                {
                    "coordinates": coordinates,
                    "type": type,
                },
                polygon_list_params.PolygonListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, polygon_list_params.PolygonListParams),
            ),
            cast_to=PolygonListResponse,
        )


class PolygonResourceWithRawResponse:
    def __init__(self, polygon: PolygonResource) -> None:
        self._polygon = polygon

        self.list = to_raw_response_wrapper(
            polygon.list,
        )


class AsyncPolygonResourceWithRawResponse:
    def __init__(self, polygon: AsyncPolygonResource) -> None:
        self._polygon = polygon

        self.list = async_to_raw_response_wrapper(
            polygon.list,
        )


class PolygonResourceWithStreamingResponse:
    def __init__(self, polygon: PolygonResource) -> None:
        self._polygon = polygon

        self.list = to_streamed_response_wrapper(
            polygon.list,
        )


class AsyncPolygonResourceWithStreamingResponse:
    def __init__(self, polygon: AsyncPolygonResource) -> None:
        self._polygon = polygon

        self.list = async_to_streamed_response_wrapper(
            polygon.list,
        )
