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
from ....types.donnees.batiment_groupe import dpe_statistique_logement_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_dpe_statistique_logement import (
    BatimentGroupeDpeStatistiqueLogement,
)

__all__ = ["DpeStatistiqueLogementResource", "AsyncDpeStatistiqueLogementResource"]


class DpeStatistiqueLogementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DpeStatistiqueLogementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DpeStatistiqueLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DpeStatistiqueLogementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DpeStatistiqueLogementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_a: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_b: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_c: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_d: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_e: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_f: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_g: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_a: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_b: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_c: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_d: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_e: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_f: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_g: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_nc: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeDpeStatistiqueLogement]:
        """
        Données statistiques du nombre de DPE par étiquette sur un bâtiment de logement.
        Pour les étiquettes DPE de l'ancien arràªté qui ne sont plus en vigueur les
        colonnes sont suffixées par "arrete_2012"

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nb_classe_bilan_dpe_a: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe A

          nb_classe_bilan_dpe_b: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe B

          nb_classe_bilan_dpe_c: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe C

          nb_classe_bilan_dpe_d: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe D

          nb_classe_bilan_dpe_e: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe E

          nb_classe_bilan_dpe_f: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe F

          nb_classe_bilan_dpe_g: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe G

          nb_classe_conso_energie_arrete_2012_a: (dpe) Nombre de DPE de la classe énergétique A. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_b: (dpe) Nombre de DPE de la classe énergétique B. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_c: (dpe) Nombre de DPE de la classe énergétique C. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_d: (dpe) Nombre de DPE de la classe énergétique D. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_e: (dpe) Nombre de DPE de la classe énergétique E. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_f: (dpe) Nombre de DPE de la classe énergétique F. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_g: (dpe) Nombre de DPE de la classe énergétique G. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_nc: (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
              (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

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
            "/donnees/batiment_groupe_dpe_statistique_logement",
            page=SyncDefault[BatimentGroupeDpeStatistiqueLogement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nb_classe_bilan_dpe_a": nb_classe_bilan_dpe_a,
                        "nb_classe_bilan_dpe_b": nb_classe_bilan_dpe_b,
                        "nb_classe_bilan_dpe_c": nb_classe_bilan_dpe_c,
                        "nb_classe_bilan_dpe_d": nb_classe_bilan_dpe_d,
                        "nb_classe_bilan_dpe_e": nb_classe_bilan_dpe_e,
                        "nb_classe_bilan_dpe_f": nb_classe_bilan_dpe_f,
                        "nb_classe_bilan_dpe_g": nb_classe_bilan_dpe_g,
                        "nb_classe_conso_energie_arrete_2012_a": nb_classe_conso_energie_arrete_2012_a,
                        "nb_classe_conso_energie_arrete_2012_b": nb_classe_conso_energie_arrete_2012_b,
                        "nb_classe_conso_energie_arrete_2012_c": nb_classe_conso_energie_arrete_2012_c,
                        "nb_classe_conso_energie_arrete_2012_d": nb_classe_conso_energie_arrete_2012_d,
                        "nb_classe_conso_energie_arrete_2012_e": nb_classe_conso_energie_arrete_2012_e,
                        "nb_classe_conso_energie_arrete_2012_f": nb_classe_conso_energie_arrete_2012_f,
                        "nb_classe_conso_energie_arrete_2012_g": nb_classe_conso_energie_arrete_2012_g,
                        "nb_classe_conso_energie_arrete_2012_nc": nb_classe_conso_energie_arrete_2012_nc,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    dpe_statistique_logement_list_params.DpeStatistiqueLogementListParams,
                ),
            ),
            model=BatimentGroupeDpeStatistiqueLogement,
        )


class AsyncDpeStatistiqueLogementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDpeStatistiqueLogementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDpeStatistiqueLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDpeStatistiqueLogementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDpeStatistiqueLogementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_a: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_b: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_c: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_d: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_e: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_f: str | NotGiven = NOT_GIVEN,
        nb_classe_bilan_dpe_g: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_a: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_b: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_c: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_d: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_e: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_f: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_g: str | NotGiven = NOT_GIVEN,
        nb_classe_conso_energie_arrete_2012_nc: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeDpeStatistiqueLogement, AsyncDefault[BatimentGroupeDpeStatistiqueLogement]]:
        """
        Données statistiques du nombre de DPE par étiquette sur un bâtiment de logement.
        Pour les étiquettes DPE de l'ancien arràªté qui ne sont plus en vigueur les
        colonnes sont suffixées par "arrete_2012"

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nb_classe_bilan_dpe_a: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe A

          nb_classe_bilan_dpe_b: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe B

          nb_classe_bilan_dpe_c: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe C

          nb_classe_bilan_dpe_d: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe D

          nb_classe_bilan_dpe_e: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe E

          nb_classe_bilan_dpe_f: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe F

          nb_classe_bilan_dpe_g: (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
              classe G

          nb_classe_conso_energie_arrete_2012_a: (dpe) Nombre de DPE de la classe énergétique A. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_b: (dpe) Nombre de DPE de la classe énergétique B. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_c: (dpe) Nombre de DPE de la classe énergétique C. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_d: (dpe) Nombre de DPE de la classe énergétique D. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_e: (dpe) Nombre de DPE de la classe énergétique E. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_f: (dpe) Nombre de DPE de la classe énergétique F. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_g: (dpe) Nombre de DPE de la classe énergétique G. valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 8 février 2012

          nb_classe_conso_energie_arrete_2012_nc: (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
              (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

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
            "/donnees/batiment_groupe_dpe_statistique_logement",
            page=AsyncDefault[BatimentGroupeDpeStatistiqueLogement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nb_classe_bilan_dpe_a": nb_classe_bilan_dpe_a,
                        "nb_classe_bilan_dpe_b": nb_classe_bilan_dpe_b,
                        "nb_classe_bilan_dpe_c": nb_classe_bilan_dpe_c,
                        "nb_classe_bilan_dpe_d": nb_classe_bilan_dpe_d,
                        "nb_classe_bilan_dpe_e": nb_classe_bilan_dpe_e,
                        "nb_classe_bilan_dpe_f": nb_classe_bilan_dpe_f,
                        "nb_classe_bilan_dpe_g": nb_classe_bilan_dpe_g,
                        "nb_classe_conso_energie_arrete_2012_a": nb_classe_conso_energie_arrete_2012_a,
                        "nb_classe_conso_energie_arrete_2012_b": nb_classe_conso_energie_arrete_2012_b,
                        "nb_classe_conso_energie_arrete_2012_c": nb_classe_conso_energie_arrete_2012_c,
                        "nb_classe_conso_energie_arrete_2012_d": nb_classe_conso_energie_arrete_2012_d,
                        "nb_classe_conso_energie_arrete_2012_e": nb_classe_conso_energie_arrete_2012_e,
                        "nb_classe_conso_energie_arrete_2012_f": nb_classe_conso_energie_arrete_2012_f,
                        "nb_classe_conso_energie_arrete_2012_g": nb_classe_conso_energie_arrete_2012_g,
                        "nb_classe_conso_energie_arrete_2012_nc": nb_classe_conso_energie_arrete_2012_nc,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    dpe_statistique_logement_list_params.DpeStatistiqueLogementListParams,
                ),
            ),
            model=BatimentGroupeDpeStatistiqueLogement,
        )


class DpeStatistiqueLogementResourceWithRawResponse:
    def __init__(self, dpe_statistique_logement: DpeStatistiqueLogementResource) -> None:
        self._dpe_statistique_logement = dpe_statistique_logement

        self.list = to_raw_response_wrapper(
            dpe_statistique_logement.list,
        )


class AsyncDpeStatistiqueLogementResourceWithRawResponse:
    def __init__(self, dpe_statistique_logement: AsyncDpeStatistiqueLogementResource) -> None:
        self._dpe_statistique_logement = dpe_statistique_logement

        self.list = async_to_raw_response_wrapper(
            dpe_statistique_logement.list,
        )


class DpeStatistiqueLogementResourceWithStreamingResponse:
    def __init__(self, dpe_statistique_logement: DpeStatistiqueLogementResource) -> None:
        self._dpe_statistique_logement = dpe_statistique_logement

        self.list = to_streamed_response_wrapper(
            dpe_statistique_logement.list,
        )


class AsyncDpeStatistiqueLogementResourceWithStreamingResponse:
    def __init__(self, dpe_statistique_logement: AsyncDpeStatistiqueLogementResource) -> None:
        self._dpe_statistique_logement = dpe_statistique_logement

        self.list = async_to_streamed_response_wrapper(
            dpe_statistique_logement.list,
        )
