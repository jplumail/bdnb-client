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
from ...types.meta_donnees import fournisseur_retrieve_params
from ...types.meta_donnees.fournisseur_retrieve_response import FournisseurRetrieveResponse

__all__ = ["FournisseurResource", "AsyncFournisseurResource"]


class FournisseurResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FournisseurResourceWithRawResponse:
        return FournisseurResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FournisseurResourceWithStreamingResponse:
        return FournisseurResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        acronyme: str | NotGiven = NOT_GIVEN,
        denomination_fournisseur: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
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
    ) -> FournisseurRetrieveResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          acronyme: Acronyme du fournisseur de données

          denomination_fournisseur: Dénomination du fournisseur de données

          description: Description du fournisseur de données

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/metadonnees/fournisseur",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "acronyme": acronyme,
                        "denomination_fournisseur": denomination_fournisseur,
                        "description": description,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    fournisseur_retrieve_params.FournisseurRetrieveParams,
                ),
            ),
            cast_to=FournisseurRetrieveResponse,
        )


class AsyncFournisseurResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFournisseurResourceWithRawResponse:
        return AsyncFournisseurResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFournisseurResourceWithStreamingResponse:
        return AsyncFournisseurResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        acronyme: str | NotGiven = NOT_GIVEN,
        denomination_fournisseur: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
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
    ) -> FournisseurRetrieveResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          acronyme: Acronyme du fournisseur de données

          denomination_fournisseur: Dénomination du fournisseur de données

          description: Description du fournisseur de données

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/metadonnees/fournisseur",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "acronyme": acronyme,
                        "denomination_fournisseur": denomination_fournisseur,
                        "description": description,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    fournisseur_retrieve_params.FournisseurRetrieveParams,
                ),
            ),
            cast_to=FournisseurRetrieveResponse,
        )


class FournisseurResourceWithRawResponse:
    def __init__(self, fournisseur: FournisseurResource) -> None:
        self._fournisseur = fournisseur

        self.retrieve = to_raw_response_wrapper(
            fournisseur.retrieve,
        )


class AsyncFournisseurResourceWithRawResponse:
    def __init__(self, fournisseur: AsyncFournisseurResource) -> None:
        self._fournisseur = fournisseur

        self.retrieve = async_to_raw_response_wrapper(
            fournisseur.retrieve,
        )


class FournisseurResourceWithStreamingResponse:
    def __init__(self, fournisseur: FournisseurResource) -> None:
        self._fournisseur = fournisseur

        self.retrieve = to_streamed_response_wrapper(
            fournisseur.retrieve,
        )


class AsyncFournisseurResourceWithStreamingResponse:
    def __init__(self, fournisseur: AsyncFournisseurResource) -> None:
        self._fournisseur = fournisseur

        self.retrieve = async_to_streamed_response_wrapper(
            fournisseur.retrieve,
        )
