# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.metadonnees import table_list_params
from ...types.metadonnees.table_list_response import TableListResponse

__all__ = ["TableResource", "AsyncTableResource"]


class TableResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TableResourceWithRawResponse:
        return TableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TableResourceWithStreamingResponse:
        return TableResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        external_pk: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quality_elements: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableListResponse:
        """
        Descriptions des tables de la BDNB

        Args:
          description: Commentaire de la table

          limit: Limiting and Pagination

          nom_table: Nom de la table

          offset: Limiting and Pagination

          order: Ordering

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
        return self._get(
            "/metadonnees/table",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "external_pk": external_pk,
                        "limit": limit,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "quality_elements": quality_elements,
                        "select": select,
                    },
                    table_list_params.TableListParams,
                ),
            ),
            cast_to=TableListResponse,
        )


class AsyncTableResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTableResourceWithRawResponse:
        return AsyncTableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTableResourceWithStreamingResponse:
        return AsyncTableResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        external_pk: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quality_elements: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableListResponse:
        """
        Descriptions des tables de la BDNB

        Args:
          description: Commentaire de la table

          limit: Limiting and Pagination

          nom_table: Nom de la table

          offset: Limiting and Pagination

          order: Ordering

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
        return await self._get(
            "/metadonnees/table",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "description": description,
                        "external_pk": external_pk,
                        "limit": limit,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "quality_elements": quality_elements,
                        "select": select,
                    },
                    table_list_params.TableListParams,
                ),
            ),
            cast_to=TableListResponse,
        )


class TableResourceWithRawResponse:
    def __init__(self, table: TableResource) -> None:
        self._table = table

        self.list = to_raw_response_wrapper(
            table.list,
        )


class AsyncTableResourceWithRawResponse:
    def __init__(self, table: AsyncTableResource) -> None:
        self._table = table

        self.list = async_to_raw_response_wrapper(
            table.list,
        )


class TableResourceWithStreamingResponse:
    def __init__(self, table: TableResource) -> None:
        self._table = table

        self.list = to_streamed_response_wrapper(
            table.list,
        )


class AsyncTableResourceWithStreamingResponse:
    def __init__(self, table: AsyncTableResource) -> None:
        self._table = table

        self.list = async_to_streamed_response_wrapper(
            table.list,
        )
