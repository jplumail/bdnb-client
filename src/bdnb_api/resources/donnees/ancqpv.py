# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
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
from ...types.donnees import ancqpv_list_params
from ...types.donnees.ancqpv_list_response import AncqpvListResponse

__all__ = ["AncqpvResource", "AsyncAncqpvResource"]


class AncqpvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AncqpvResourceWithRawResponse:
        return AncqpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AncqpvResourceWithStreamingResponse:
        return AncqpvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_qp: str | NotGiven = NOT_GIVEN,
        commune_qp: str | NotGiven = NOT_GIVEN,
        geom: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AncqpvListResponse:
        """
        Base des Quartiers Prioritaires de la Ville (QPV)

        Args:
          code_qp: identifiant de la table qpv

          commune_qp: TODO

          geom: GÃ©ometrie de l'entitÃ©

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/ancqpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_qp": code_qp,
                        "commune_qp": commune_qp,
                        "geom": geom,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    ancqpv_list_params.AncqpvListParams,
                ),
            ),
            cast_to=AncqpvListResponse,
        )


class AsyncAncqpvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAncqpvResourceWithRawResponse:
        return AsyncAncqpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAncqpvResourceWithStreamingResponse:
        return AsyncAncqpvResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        code_qp: str | NotGiven = NOT_GIVEN,
        commune_qp: str | NotGiven = NOT_GIVEN,
        geom: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AncqpvListResponse:
        """
        Base des Quartiers Prioritaires de la Ville (QPV)

        Args:
          code_qp: identifiant de la table qpv

          commune_qp: TODO

          geom: GÃ©ometrie de l'entitÃ©

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/ancqpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code_qp": code_qp,
                        "commune_qp": commune_qp,
                        "geom": geom,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    ancqpv_list_params.AncqpvListParams,
                ),
            ),
            cast_to=AncqpvListResponse,
        )


class AncqpvResourceWithRawResponse:
    def __init__(self, ancqpv: AncqpvResource) -> None:
        self._ancqpv = ancqpv

        self.list = to_raw_response_wrapper(
            ancqpv.list,
        )


class AsyncAncqpvResourceWithRawResponse:
    def __init__(self, ancqpv: AsyncAncqpvResource) -> None:
        self._ancqpv = ancqpv

        self.list = async_to_raw_response_wrapper(
            ancqpv.list,
        )


class AncqpvResourceWithStreamingResponse:
    def __init__(self, ancqpv: AncqpvResource) -> None:
        self._ancqpv = ancqpv

        self.list = to_streamed_response_wrapper(
            ancqpv.list,
        )


class AsyncAncqpvResourceWithStreamingResponse:
    def __init__(self, ancqpv: AsyncAncqpvResource) -> None:
        self._ancqpv = ancqpv

        self.list = async_to_streamed_response_wrapper(
            ancqpv.list,
        )
