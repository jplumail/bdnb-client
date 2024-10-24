# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefault, AsyncDefault
from ...._base_client import AsyncPaginator, make_request_options
from ....types.donnees.batiment_groupe import dle_reseaux_multimillesime_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_dle_reseaux_multimillesime import (
    BatimentGroupeDleReseauxMultimillesime,
)

__all__ = ["DleReseauxMultimillesimeResource", "AsyncDleReseauxMultimillesimeResource"]


class DleReseauxMultimillesimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DleReseauxMultimillesimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DleReseauxMultimillesimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DleReseauxMultimillesimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DleReseauxMultimillesimeResourceWithStreamingResponse(self)

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
        identifiant_reseau: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_reseau: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeDleReseauxMultimillesime]:
        """
        Données de consommations des données locales de l'énergie du SDES pour le
        vecteur réseau de chaleur agrégées à l'échelle du bâtiment. Attention les
        données sur les réseaux de chaleurs sont aujourd'hui bien moins fiable que les
        vecteurs gaz ou éléctricité.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          identifiant_reseau: Identifiant du reseau de chaleur

          limit: Limiting and Pagination

          millesime: Millésime des données

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_reseau: type du réseau de chaleur

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
            "/donnees/batiment_groupe_dle_reseaux_multimillesime",
            page=SyncDefault[BatimentGroupeDleReseauxMultimillesime],
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
                        "identifiant_reseau": identifiant_reseau,
                        "limit": limit,
                        "millesime": millesime,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_reseau": type_reseau,
                    },
                    dle_reseaux_multimillesime_list_params.DleReseauxMultimillesimeListParams,
                ),
            ),
            model=BatimentGroupeDleReseauxMultimillesime,
        )


class AsyncDleReseauxMultimillesimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDleReseauxMultimillesimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDleReseauxMultimillesimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDleReseauxMultimillesimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDleReseauxMultimillesimeResourceWithStreamingResponse(self)

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
        identifiant_reseau: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_reseau: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeDleReseauxMultimillesime, AsyncDefault[BatimentGroupeDleReseauxMultimillesime]]:
        """
        Données de consommations des données locales de l'énergie du SDES pour le
        vecteur réseau de chaleur agrégées à l'échelle du bâtiment. Attention les
        données sur les réseaux de chaleurs sont aujourd'hui bien moins fiable que les
        vecteurs gaz ou éléctricité.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          identifiant_reseau: Identifiant du reseau de chaleur

          limit: Limiting and Pagination

          millesime: Millésime des données

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_reseau: type du réseau de chaleur

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
            "/donnees/batiment_groupe_dle_reseaux_multimillesime",
            page=AsyncDefault[BatimentGroupeDleReseauxMultimillesime],
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
                        "identifiant_reseau": identifiant_reseau,
                        "limit": limit,
                        "millesime": millesime,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_reseau": type_reseau,
                    },
                    dle_reseaux_multimillesime_list_params.DleReseauxMultimillesimeListParams,
                ),
            ),
            model=BatimentGroupeDleReseauxMultimillesime,
        )


class DleReseauxMultimillesimeResourceWithRawResponse:
    def __init__(self, dle_reseaux_multimillesime: DleReseauxMultimillesimeResource) -> None:
        self._dle_reseaux_multimillesime = dle_reseaux_multimillesime

        self.list = to_raw_response_wrapper(
            dle_reseaux_multimillesime.list,
        )


class AsyncDleReseauxMultimillesimeResourceWithRawResponse:
    def __init__(self, dle_reseaux_multimillesime: AsyncDleReseauxMultimillesimeResource) -> None:
        self._dle_reseaux_multimillesime = dle_reseaux_multimillesime

        self.list = async_to_raw_response_wrapper(
            dle_reseaux_multimillesime.list,
        )


class DleReseauxMultimillesimeResourceWithStreamingResponse:
    def __init__(self, dle_reseaux_multimillesime: DleReseauxMultimillesimeResource) -> None:
        self._dle_reseaux_multimillesime = dle_reseaux_multimillesime

        self.list = to_streamed_response_wrapper(
            dle_reseaux_multimillesime.list,
        )


class AsyncDleReseauxMultimillesimeResourceWithStreamingResponse:
    def __init__(self, dle_reseaux_multimillesime: AsyncDleReseauxMultimillesimeResource) -> None:
        self._dle_reseaux_multimillesime = dle_reseaux_multimillesime

        self.list = async_to_streamed_response_wrapper(
            dle_reseaux_multimillesime.list,
        )
