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
from ...types.metadonnees import contrainte_acce_retrieve_params
from ...types.metadonnees.contrainte_acce_retrieve_response import ContrainteAcceRetrieveResponse

__all__ = ["ContrainteAccesResource", "AsyncContrainteAccesResource"]


class ContrainteAccesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContrainteAccesResourceWithRawResponse:
        return ContrainteAccesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContrainteAccesResourceWithStreamingResponse:
        return ContrainteAccesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
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
    ) -> ContrainteAcceRetrieveResponse:
        """
        Ensemble des contraintes d'accès valides de la BDNB

        Args:
          contrainte_acces: Dénomination de la contrainte d'accès

          description: Description de la série de données

          limit: Limiting and Pagination

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
            "/metadonnees/contrainte_acces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    contrainte_acce_retrieve_params.ContrainteAcceRetrieveParams,
                ),
            ),
            cast_to=ContrainteAcceRetrieveResponse,
        )


class AsyncContrainteAccesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContrainteAccesResourceWithRawResponse:
        return AsyncContrainteAccesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContrainteAccesResourceWithStreamingResponse:
        return AsyncContrainteAccesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
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
    ) -> ContrainteAcceRetrieveResponse:
        """
        Ensemble des contraintes d'accès valides de la BDNB

        Args:
          contrainte_acces: Dénomination de la contrainte d'accès

          description: Description de la série de données

          limit: Limiting and Pagination

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
            "/metadonnees/contrainte_acces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    contrainte_acce_retrieve_params.ContrainteAcceRetrieveParams,
                ),
            ),
            cast_to=ContrainteAcceRetrieveResponse,
        )


class ContrainteAccesResourceWithRawResponse:
    def __init__(self, contrainte_acces: ContrainteAccesResource) -> None:
        self._contrainte_acces = contrainte_acces

        self.retrieve = to_raw_response_wrapper(
            contrainte_acces.retrieve,
        )


class AsyncContrainteAccesResourceWithRawResponse:
    def __init__(self, contrainte_acces: AsyncContrainteAccesResource) -> None:
        self._contrainte_acces = contrainte_acces

        self.retrieve = async_to_raw_response_wrapper(
            contrainte_acces.retrieve,
        )


class ContrainteAccesResourceWithStreamingResponse:
    def __init__(self, contrainte_acces: ContrainteAccesResource) -> None:
        self._contrainte_acces = contrainte_acces

        self.retrieve = to_streamed_response_wrapper(
            contrainte_acces.retrieve,
        )


class AsyncContrainteAccesResourceWithStreamingResponse:
    def __init__(self, contrainte_acces: AsyncContrainteAccesResource) -> None:
        self._contrainte_acces = contrainte_acces

        self.retrieve = async_to_streamed_response_wrapper(
            contrainte_acces.retrieve,
        )
