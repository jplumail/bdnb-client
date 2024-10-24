# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefault, AsyncDefault
from ..._base_client import AsyncPaginator, make_request_options
from ...types.metadonnees import info_list_params
from ...types.metadonnees.info import Info

__all__ = ["InfoResource", "AsyncInfoResource"]


class InfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return InfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return InfoResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        modifiee: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        publication_schema: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[Info]:
        """
        Information sur le millésime servi par l'API

        Args:
          limit: Limiting and Pagination

          modifiee: date de modification

          offset: Limiting and Pagination

          order: Ordering

          publication_schema: schema de publication

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/metadonnees/info",
            page=SyncDefault[Info],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "modifiee": modifiee,
                        "offset": offset,
                        "order": order,
                        "publication_schema": publication_schema,
                        "select": select,
                    },
                    info_list_params.InfoListParams,
                ),
            ),
            model=Info,
        )


class AsyncInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncInfoResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        modifiee: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        publication_schema: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Info, AsyncDefault[Info]]:
        """
        Information sur le millésime servi par l'API

        Args:
          limit: Limiting and Pagination

          modifiee: date de modification

          offset: Limiting and Pagination

          order: Ordering

          publication_schema: schema de publication

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/metadonnees/info",
            page=AsyncDefault[Info],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "modifiee": modifiee,
                        "offset": offset,
                        "order": order,
                        "publication_schema": publication_schema,
                        "select": select,
                    },
                    info_list_params.InfoListParams,
                ),
            ),
            model=Info,
        )


class InfoResourceWithRawResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.list = to_raw_response_wrapper(
            info.list,
        )


class AsyncInfoResourceWithRawResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.list = async_to_raw_response_wrapper(
            info.list,
        )


class InfoResourceWithStreamingResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.list = to_streamed_response_wrapper(
            info.list,
        )


class AsyncInfoResourceWithStreamingResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.list = async_to_streamed_response_wrapper(
            info.list,
        )
