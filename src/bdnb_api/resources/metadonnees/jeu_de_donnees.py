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
from ...types.metadonnees import jeu_de_donnee_list_params
from ...types.metadonnees.jeu_de_donnee_list_response import JeuDeDonneeListResponse

__all__ = ["JeuDeDonneesResource", "AsyncJeuDeDonneesResource"]


class JeuDeDonneesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JeuDeDonneesResourceWithRawResponse:
        return JeuDeDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JeuDeDonneesResourceWithStreamingResponse:
        return JeuDeDonneesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        couverture_spatiale: str | NotGiven = NOT_GIVEN,
        couverture_temporelle: str | NotGiven = NOT_GIVEN,
        date_publication: str | NotGiven = NOT_GIVEN,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
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
    ) -> JeuDeDonneeListResponse:
        """
        Les jeux de donnÃ©es utilisÃ©es dans la BDNB

        Args:
          contrainte_acces: DÃ©nomination de la contrainte d'accÃ¨s associÃ©e

          couverture_spatiale: Couverture spatiale du jeu de donnÃ©es

          couverture_temporelle: Couverture temporelle du jeu de donnÃ©es

          date_publication: Date de publication du jeu de donnÃ©es

          denomination_serie: DÃ©nomination du jeu de donnÃ©es

          description: Description du jeu de donnÃ©es

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: MillÃ©sime du jeu de donnÃ©es

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
            "/metadonnees/jeu_de_donnees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "couverture_spatiale": couverture_spatiale,
                        "couverture_temporelle": couverture_temporelle,
                        "date_publication": date_publication,
                        "denomination_serie": denomination_serie,
                        "description": description,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    jeu_de_donnee_list_params.JeuDeDonneeListParams,
                ),
            ),
            cast_to=JeuDeDonneeListResponse,
        )


class AsyncJeuDeDonneesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJeuDeDonneesResourceWithRawResponse:
        return AsyncJeuDeDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJeuDeDonneesResourceWithStreamingResponse:
        return AsyncJeuDeDonneesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        couverture_spatiale: str | NotGiven = NOT_GIVEN,
        couverture_temporelle: str | NotGiven = NOT_GIVEN,
        date_publication: str | NotGiven = NOT_GIVEN,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
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
    ) -> JeuDeDonneeListResponse:
        """
        Les jeux de donnÃ©es utilisÃ©es dans la BDNB

        Args:
          contrainte_acces: DÃ©nomination de la contrainte d'accÃ¨s associÃ©e

          couverture_spatiale: Couverture spatiale du jeu de donnÃ©es

          couverture_temporelle: Couverture temporelle du jeu de donnÃ©es

          date_publication: Date de publication du jeu de donnÃ©es

          denomination_serie: DÃ©nomination du jeu de donnÃ©es

          description: Description du jeu de donnÃ©es

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: MillÃ©sime du jeu de donnÃ©es

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
            "/metadonnees/jeu_de_donnees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "couverture_spatiale": couverture_spatiale,
                        "couverture_temporelle": couverture_temporelle,
                        "date_publication": date_publication,
                        "denomination_serie": denomination_serie,
                        "description": description,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    jeu_de_donnee_list_params.JeuDeDonneeListParams,
                ),
            ),
            cast_to=JeuDeDonneeListResponse,
        )


class JeuDeDonneesResourceWithRawResponse:
    def __init__(self, jeu_de_donnees: JeuDeDonneesResource) -> None:
        self._jeu_de_donnees = jeu_de_donnees

        self.list = to_raw_response_wrapper(
            jeu_de_donnees.list,
        )


class AsyncJeuDeDonneesResourceWithRawResponse:
    def __init__(self, jeu_de_donnees: AsyncJeuDeDonneesResource) -> None:
        self._jeu_de_donnees = jeu_de_donnees

        self.list = async_to_raw_response_wrapper(
            jeu_de_donnees.list,
        )


class JeuDeDonneesResourceWithStreamingResponse:
    def __init__(self, jeu_de_donnees: JeuDeDonneesResource) -> None:
        self._jeu_de_donnees = jeu_de_donnees

        self.list = to_streamed_response_wrapper(
            jeu_de_donnees.list,
        )


class AsyncJeuDeDonneesResourceWithStreamingResponse:
    def __init__(self, jeu_de_donnees: AsyncJeuDeDonneesResource) -> None:
        self._jeu_de_donnees = jeu_de_donnees

        self.list = async_to_streamed_response_wrapper(
            jeu_de_donnees.list,
        )
