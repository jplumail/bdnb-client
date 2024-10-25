# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.donnees.batiment_groupe.complet import bbox_list_params
from .....types.donnees.batiment_groupe.complet.bbox_list_response import BboxListResponse

__all__ = ["BboxResource", "AsyncBboxResource"]


class BboxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BboxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        xmax: float,
        xmin: float,
        ymax: float,
        ymin: float,
        srid: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BboxListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/donnees/batiment_groupe_complet/bbox",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "xmax": xmax,
                        "xmin": xmin,
                        "ymax": ymax,
                        "ymin": ymin,
                        "srid": srid,
                    },
                    bbox_list_params.BboxListParams,
                ),
            ),
            cast_to=BboxListResponse,
        )


class AsyncBboxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBboxResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        xmax: float,
        xmin: float,
        ymax: float,
        ymin: float,
        srid: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BboxListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/donnees/batiment_groupe_complet/bbox",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "xmax": xmax,
                        "xmin": xmin,
                        "ymax": ymax,
                        "ymin": ymin,
                        "srid": srid,
                    },
                    bbox_list_params.BboxListParams,
                ),
            ),
            cast_to=BboxListResponse,
        )


class BboxResourceWithRawResponse:
    def __init__(self, bbox: BboxResource) -> None:
        self._bbox = bbox

        self.list = to_raw_response_wrapper(
            bbox.list,
        )


class AsyncBboxResourceWithRawResponse:
    def __init__(self, bbox: AsyncBboxResource) -> None:
        self._bbox = bbox

        self.list = async_to_raw_response_wrapper(
            bbox.list,
        )


class BboxResourceWithStreamingResponse:
    def __init__(self, bbox: BboxResource) -> None:
        self._bbox = bbox

        self.list = to_streamed_response_wrapper(
            bbox.list,
        )


class AsyncBboxResourceWithStreamingResponse:
    def __init__(self, bbox: AsyncBboxResource) -> None:
        self._bbox = bbox

        self.list = async_to_streamed_response_wrapper(
            bbox.list,
        )
