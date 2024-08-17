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
from ...types.donnees import batiment_groupe_dle_elec_multimillesime_list_params
from ...types.donnees.batiment_groupe_dle_elec_multimillesime_list_response import (
    BatimentGroupeDleElecMultimillesimeListResponse,
)

__all__ = ["BatimentGroupeDleElecMultimillesimeResource", "AsyncBatimentGroupeDleElecMultimillesimeResource"]


class BatimentGroupeDleElecMultimillesimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_pro: str | NotGiven = NOT_GIVEN,
        conso_pro_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_res: str | NotGiven = NOT_GIVEN,
        conso_res_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_tot: str | NotGiven = NOT_GIVEN,
        conso_tot_par_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeDleElecMultimillesimeListResponse:
        """
        Données de consommations des données locales de l'énergie du SDES pour le
        vecteur éléctrique agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          limit: Limiting and Pagination

          millesime: Millésime des données

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

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
            "/donnees/batiment_groupe_dle_elec_multimillesime",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "conso_pro": conso_pro,
                        "conso_pro_par_pdl": conso_pro_par_pdl,
                        "conso_res": conso_res,
                        "conso_res_par_pdl": conso_res_par_pdl,
                        "conso_tot": conso_tot,
                        "conso_tot_par_pdl": conso_tot_par_pdl,
                        "limit": limit,
                        "millesime": millesime,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_dle_elec_multimillesime_list_params.BatimentGroupeDleElecMultimillesimeListParams,
                ),
            ),
            cast_to=BatimentGroupeDleElecMultimillesimeListResponse,
        )


class AsyncBatimentGroupeDleElecMultimillesimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_pro: str | NotGiven = NOT_GIVEN,
        conso_pro_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_res: str | NotGiven = NOT_GIVEN,
        conso_res_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_tot: str | NotGiven = NOT_GIVEN,
        conso_tot_par_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeDleElecMultimillesimeListResponse:
        """
        Données de consommations des données locales de l'énergie du SDES pour le
        vecteur éléctrique agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          limit: Limiting and Pagination

          millesime: Millésime des données

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

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
            "/donnees/batiment_groupe_dle_elec_multimillesime",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "conso_pro": conso_pro,
                        "conso_pro_par_pdl": conso_pro_par_pdl,
                        "conso_res": conso_res,
                        "conso_res_par_pdl": conso_res_par_pdl,
                        "conso_tot": conso_tot,
                        "conso_tot_par_pdl": conso_tot_par_pdl,
                        "limit": limit,
                        "millesime": millesime,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_dle_elec_multimillesime_list_params.BatimentGroupeDleElecMultimillesimeListParams,
                ),
            ),
            cast_to=BatimentGroupeDleElecMultimillesimeListResponse,
        )


class BatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
    def __init__(self, batiment_groupe_dle_elec_multimillesime: BatimentGroupeDleElecMultimillesimeResource) -> None:
        self._batiment_groupe_dle_elec_multimillesime = batiment_groupe_dle_elec_multimillesime

        self.list = to_raw_response_wrapper(
            batiment_groupe_dle_elec_multimillesime.list,
        )


class AsyncBatimentGroupeDleElecMultimillesimeResourceWithRawResponse:
    def __init__(
        self, batiment_groupe_dle_elec_multimillesime: AsyncBatimentGroupeDleElecMultimillesimeResource
    ) -> None:
        self._batiment_groupe_dle_elec_multimillesime = batiment_groupe_dle_elec_multimillesime

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_dle_elec_multimillesime.list,
        )


class BatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_dle_elec_multimillesime: BatimentGroupeDleElecMultimillesimeResource) -> None:
        self._batiment_groupe_dle_elec_multimillesime = batiment_groupe_dle_elec_multimillesime

        self.list = to_streamed_response_wrapper(
            batiment_groupe_dle_elec_multimillesime.list,
        )


class AsyncBatimentGroupeDleElecMultimillesimeResourceWithStreamingResponse:
    def __init__(
        self, batiment_groupe_dle_elec_multimillesime: AsyncBatimentGroupeDleElecMultimillesimeResource
    ) -> None:
        self._batiment_groupe_dle_elec_multimillesime = batiment_groupe_dle_elec_multimillesime

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_dle_elec_multimillesime.list,
        )
