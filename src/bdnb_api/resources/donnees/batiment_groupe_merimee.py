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
from ...types.donnees import batiment_groupe_merimee_list_params
from ...types.batiment_groupe_merimee_api_expert import BatimentGroupeMerimeeAPIExpert

__all__ = ["BatimentGroupeMerimeeResource", "AsyncBatimentGroupeMerimeeResource"]


class BatimentGroupeMerimeeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeMerimeeResourceWithRawResponse:
        return BatimentGroupeMerimeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeMerimeeResourceWithStreamingResponse:
        return BatimentGroupeMerimeeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        perimetre_bat_historique: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeMerimeeAPIExpert]:
        """
        Informations Mérimée (bâtiments classés aux Monuments Historiques) agrégées à
        l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          distance_batiment_historique_plus_proche: (mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]

          limit: Limiting and Pagination

          nom_batiment_historique_plus_proche: (mer:tico) nom du bâtiment historique le plus proche

          offset: Limiting and Pagination

          order: Ordering

          perimetre_bat_historique: Vrai si l'entité est dans le périmètre d'un bâtiment historique

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
            "/donnees/batiment_groupe_merimee",
            page=SyncDefault[BatimentGroupeMerimeeAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_historique_plus_proche": distance_batiment_historique_plus_proche,
                        "limit": limit,
                        "nom_batiment_historique_plus_proche": nom_batiment_historique_plus_proche,
                        "offset": offset,
                        "order": order,
                        "perimetre_bat_historique": perimetre_bat_historique,
                        "select": select,
                    },
                    batiment_groupe_merimee_list_params.BatimentGroupeMerimeeListParams,
                ),
            ),
            model=BatimentGroupeMerimeeAPIExpert,
        )


class AsyncBatimentGroupeMerimeeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeMerimeeResourceWithRawResponse:
        return AsyncBatimentGroupeMerimeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeMerimeeResourceWithStreamingResponse:
        return AsyncBatimentGroupeMerimeeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        perimetre_bat_historique: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeMerimeeAPIExpert, AsyncDefault[BatimentGroupeMerimeeAPIExpert]]:
        """
        Informations Mérimée (bâtiments classés aux Monuments Historiques) agrégées à
        l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          distance_batiment_historique_plus_proche: (mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]

          limit: Limiting and Pagination

          nom_batiment_historique_plus_proche: (mer:tico) nom du bâtiment historique le plus proche

          offset: Limiting and Pagination

          order: Ordering

          perimetre_bat_historique: Vrai si l'entité est dans le périmètre d'un bâtiment historique

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
            "/donnees/batiment_groupe_merimee",
            page=AsyncDefault[BatimentGroupeMerimeeAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_historique_plus_proche": distance_batiment_historique_plus_proche,
                        "limit": limit,
                        "nom_batiment_historique_plus_proche": nom_batiment_historique_plus_proche,
                        "offset": offset,
                        "order": order,
                        "perimetre_bat_historique": perimetre_bat_historique,
                        "select": select,
                    },
                    batiment_groupe_merimee_list_params.BatimentGroupeMerimeeListParams,
                ),
            ),
            model=BatimentGroupeMerimeeAPIExpert,
        )


class BatimentGroupeMerimeeResourceWithRawResponse:
    def __init__(self, batiment_groupe_merimee: BatimentGroupeMerimeeResource) -> None:
        self._batiment_groupe_merimee = batiment_groupe_merimee

        self.list = to_raw_response_wrapper(
            batiment_groupe_merimee.list,
        )


class AsyncBatimentGroupeMerimeeResourceWithRawResponse:
    def __init__(self, batiment_groupe_merimee: AsyncBatimentGroupeMerimeeResource) -> None:
        self._batiment_groupe_merimee = batiment_groupe_merimee

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_merimee.list,
        )


class BatimentGroupeMerimeeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_merimee: BatimentGroupeMerimeeResource) -> None:
        self._batiment_groupe_merimee = batiment_groupe_merimee

        self.list = to_streamed_response_wrapper(
            batiment_groupe_merimee.list,
        )


class AsyncBatimentGroupeMerimeeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_merimee: AsyncBatimentGroupeMerimeeResource) -> None:
        self._batiment_groupe_merimee = batiment_groupe_merimee

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_merimee.list,
        )
