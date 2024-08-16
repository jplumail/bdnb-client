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
from ...types.donnees import batiment_groupe_merimee_list_params
from ...types.donnees.batiment_groupe_merimee_list_response import BatimentGroupeMerimeeListResponse

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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeMerimeeListResponse:
        """
        Informations MÃ©rimÃ©e (bÃ¢timents classÃ©s aux Monuments Historiques)
        agrÃ©gÃ©es Ã l'Ã©chelle du bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          distance_batiment_historique_plus_proche: (mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]

          limit: Limiting and Pagination

          nom_batiment_historique_plus_proche: (mer:tico) nom du bÃ¢timent historique le plus proche

          offset: Limiting and Pagination

          order: Ordering

          perimetre_bat_historique: Vrai si l'entitÃ© est dans le pÃ©rimÃ¨tre d'un bÃ¢timent historique

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
            "/donnees/batiment_groupe_merimee",
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
            cast_to=BatimentGroupeMerimeeListResponse,
        )


class AsyncBatimentGroupeMerimeeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeMerimeeResourceWithRawResponse:
        return AsyncBatimentGroupeMerimeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeMerimeeResourceWithStreamingResponse:
        return AsyncBatimentGroupeMerimeeResourceWithStreamingResponse(self)

    async def list(
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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeMerimeeListResponse:
        """
        Informations MÃ©rimÃ©e (bÃ¢timents classÃ©s aux Monuments Historiques)
        agrÃ©gÃ©es Ã l'Ã©chelle du bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          distance_batiment_historique_plus_proche: (mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]

          limit: Limiting and Pagination

          nom_batiment_historique_plus_proche: (mer:tico) nom du bÃ¢timent historique le plus proche

          offset: Limiting and Pagination

          order: Ordering

          perimetre_bat_historique: Vrai si l'entitÃ© est dans le pÃ©rimÃ¨tre d'un bÃ¢timent historique

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
            "/donnees/batiment_groupe_merimee",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
            cast_to=BatimentGroupeMerimeeListResponse,
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
