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
from ...types.tables_bdnb import batiment_groupe_bdtopo_bat_list_params
from ...types.tables_bdnb.batiment_groupe_bdtopo_bat_list_response import BatimentGroupeBdtopoBatListResponse

__all__ = ["BatimentGroupeBdtopoBatResource", "AsyncBatimentGroupeBdtopoBatResource"]


class BatimentGroupeBdtopoBatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeBdtopoBatResourceWithRawResponse:
        return BatimentGroupeBdtopoBatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return BatimentGroupeBdtopoBatResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        altitude_sol_mean: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        hauteur_mean: str | NotGiven = NOT_GIVEN,
        l_etat: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_usage_1: str | NotGiven = NOT_GIVEN,
        l_usage_2: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        max_hauteur: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeBdtopoBatListResponse:
        """
        Informations de la BDTopo, couche bâti, agrégées à l'échelle du bâtiment

        Args:
          altitude_sol_mean: (ign) Altitude au sol moyenne [m]

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          hauteur_mean: (ign) Hauteur moyenne des bâtiments [m]

          l_etat: (ign) Etat des bâtiments

          l_nature: (ign) Catégorie de nature du bâtiment

          l_usage_1: (ign) Usage principal du bâtiment

          l_usage_2: (ign) Usage secondaire du bâtiment

          limit: Limiting and Pagination

          max_hauteur: (ign) Hauteur maximale des bâtiments [m]

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
            "/donnees/batiment_groupe_bdtopo_bat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "altitude_sol_mean": altitude_sol_mean,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "hauteur_mean": hauteur_mean,
                        "l_etat": l_etat,
                        "l_nature": l_nature,
                        "l_usage_1": l_usage_1,
                        "l_usage_2": l_usage_2,
                        "limit": limit,
                        "max_hauteur": max_hauteur,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_bdtopo_bat_list_params.BatimentGroupeBdtopoBatListParams,
                ),
            ),
            cast_to=BatimentGroupeBdtopoBatListResponse,
        )


class AsyncBatimentGroupeBdtopoBatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeBdtopoBatResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        altitude_sol_mean: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        hauteur_mean: str | NotGiven = NOT_GIVEN,
        l_etat: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_usage_1: str | NotGiven = NOT_GIVEN,
        l_usage_2: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        max_hauteur: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeBdtopoBatListResponse:
        """
        Informations de la BDTopo, couche bâti, agrégées à l'échelle du bâtiment

        Args:
          altitude_sol_mean: (ign) Altitude au sol moyenne [m]

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          hauteur_mean: (ign) Hauteur moyenne des bâtiments [m]

          l_etat: (ign) Etat des bâtiments

          l_nature: (ign) Catégorie de nature du bâtiment

          l_usage_1: (ign) Usage principal du bâtiment

          l_usage_2: (ign) Usage secondaire du bâtiment

          limit: Limiting and Pagination

          max_hauteur: (ign) Hauteur maximale des bâtiments [m]

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
            "/donnees/batiment_groupe_bdtopo_bat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "altitude_sol_mean": altitude_sol_mean,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "hauteur_mean": hauteur_mean,
                        "l_etat": l_etat,
                        "l_nature": l_nature,
                        "l_usage_1": l_usage_1,
                        "l_usage_2": l_usage_2,
                        "limit": limit,
                        "max_hauteur": max_hauteur,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_bdtopo_bat_list_params.BatimentGroupeBdtopoBatListParams,
                ),
            ),
            cast_to=BatimentGroupeBdtopoBatListResponse,
        )


class BatimentGroupeBdtopoBatResourceWithRawResponse:
    def __init__(self, batiment_groupe_bdtopo_bat: BatimentGroupeBdtopoBatResource) -> None:
        self._batiment_groupe_bdtopo_bat = batiment_groupe_bdtopo_bat

        self.list = to_raw_response_wrapper(
            batiment_groupe_bdtopo_bat.list,
        )


class AsyncBatimentGroupeBdtopoBatResourceWithRawResponse:
    def __init__(self, batiment_groupe_bdtopo_bat: AsyncBatimentGroupeBdtopoBatResource) -> None:
        self._batiment_groupe_bdtopo_bat = batiment_groupe_bdtopo_bat

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_bdtopo_bat.list,
        )


class BatimentGroupeBdtopoBatResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bdtopo_bat: BatimentGroupeBdtopoBatResource) -> None:
        self._batiment_groupe_bdtopo_bat = batiment_groupe_bdtopo_bat

        self.list = to_streamed_response_wrapper(
            batiment_groupe_bdtopo_bat.list,
        )


class AsyncBatimentGroupeBdtopoBatResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bdtopo_bat: AsyncBatimentGroupeBdtopoBatResource) -> None:
        self._batiment_groupe_bdtopo_bat = batiment_groupe_bdtopo_bat

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_bdtopo_bat.list,
        )
