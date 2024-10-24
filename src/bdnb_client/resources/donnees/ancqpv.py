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
from ...types.donnees import ancqpv_list_params
from ...types.donnees.ancqpv import Ancqpv

__all__ = ["AncqpvResource", "AsyncAncqpvResource"]


class AncqpvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AncqpvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AncqpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AncqpvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[Ancqpv]:
        """
        Base des Quartiers Prioritaires de la Ville (QPV)

        Args:
          code_qp: identifiant de la table qpv

          commune_qp: TODO

          geom: Géometrie de l'entité

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

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
        return self._get_api_list(
            "/donnees/ancqpv",
            page=SyncDefault[Ancqpv],
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
            model=Ancqpv,
        )


class AsyncAncqpvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAncqpvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAncqpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAncqpvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncAncqpvResourceWithStreamingResponse(self)

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Ancqpv, AsyncDefault[Ancqpv]]:
        """
        Base des Quartiers Prioritaires de la Ville (QPV)

        Args:
          code_qp: identifiant de la table qpv

          commune_qp: TODO

          geom: Géometrie de l'entité

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

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
        return self._get_api_list(
            "/donnees/ancqpv",
            page=AsyncDefault[Ancqpv],
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
            model=Ancqpv,
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
