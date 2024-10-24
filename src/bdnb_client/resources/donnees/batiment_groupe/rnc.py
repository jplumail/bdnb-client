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
from ....types.donnees.batiment_groupe import rnc_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_rnc import BatimentGroupeRnc

__all__ = ["RncResource", "AsyncRncResource"]


class RncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return RncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return RncResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        copro_dans_pvd: str | NotGiven = NOT_GIVEN,
        l_annee_construction: str | NotGiven = NOT_GIVEN,
        l_nom_copro: str | NotGiven = NOT_GIVEN,
        l_siret: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_lot_garpark: str | NotGiven = NOT_GIVEN,
        nb_lot_tertiaire: str | NotGiven = NOT_GIVEN,
        nb_lot_tot: str | NotGiven = NOT_GIVEN,
        numero_immat_principal: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        periode_construction_max: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeRnc]:
        """
        Informations issues de la base RNC agrégées à l'échelle du bâtiment (si
        certaines données sont restreintes aux ayants_droit RNC, la majorité des
        informations sont accessibles en open-data)

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          copro_dans_pvd: (rnc) au moins une des coproprietés est dans le programme petites villes de
              demain

          l_annee_construction: Liste des années de construction

          l_nom_copro: (rnc) liste des noms des copropriétés

          l_siret: liste de siret

          limit: Limiting and Pagination

          nb_log: (rnc) Nombre de logements

          nb_lot_garpark: Nombre de lots de stationnement

          nb_lot_tertiaire: Nombre de lots de type bureau et commerce

          nb_lot_tot: Nombre total de lots

          numero_immat_principal: numéro d'immatriculation principal associé au bâtiment groupe. (numéro
              d'immatriculation copropriété qui comporte le plus de lots)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_max: (rnc) Période de construction du local le plus récent

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
            "/donnees/batiment_groupe_rnc",
            page=SyncDefault[BatimentGroupeRnc],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "copro_dans_pvd": copro_dans_pvd,
                        "l_annee_construction": l_annee_construction,
                        "l_nom_copro": l_nom_copro,
                        "l_siret": l_siret,
                        "limit": limit,
                        "nb_log": nb_log,
                        "nb_lot_garpark": nb_lot_garpark,
                        "nb_lot_tertiaire": nb_lot_tertiaire,
                        "nb_lot_tot": nb_lot_tot,
                        "numero_immat_principal": numero_immat_principal,
                        "offset": offset,
                        "order": order,
                        "periode_construction_max": periode_construction_max,
                        "select": select,
                    },
                    rnc_list_params.RncListParams,
                ),
            ),
            model=BatimentGroupeRnc,
        )


class AsyncRncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncRncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncRncResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        copro_dans_pvd: str | NotGiven = NOT_GIVEN,
        l_annee_construction: str | NotGiven = NOT_GIVEN,
        l_nom_copro: str | NotGiven = NOT_GIVEN,
        l_siret: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_lot_garpark: str | NotGiven = NOT_GIVEN,
        nb_lot_tertiaire: str | NotGiven = NOT_GIVEN,
        nb_lot_tot: str | NotGiven = NOT_GIVEN,
        numero_immat_principal: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        periode_construction_max: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeRnc, AsyncDefault[BatimentGroupeRnc]]:
        """
        Informations issues de la base RNC agrégées à l'échelle du bâtiment (si
        certaines données sont restreintes aux ayants_droit RNC, la majorité des
        informations sont accessibles en open-data)

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          copro_dans_pvd: (rnc) au moins une des coproprietés est dans le programme petites villes de
              demain

          l_annee_construction: Liste des années de construction

          l_nom_copro: (rnc) liste des noms des copropriétés

          l_siret: liste de siret

          limit: Limiting and Pagination

          nb_log: (rnc) Nombre de logements

          nb_lot_garpark: Nombre de lots de stationnement

          nb_lot_tertiaire: Nombre de lots de type bureau et commerce

          nb_lot_tot: Nombre total de lots

          numero_immat_principal: numéro d'immatriculation principal associé au bâtiment groupe. (numéro
              d'immatriculation copropriété qui comporte le plus de lots)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_max: (rnc) Période de construction du local le plus récent

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
            "/donnees/batiment_groupe_rnc",
            page=AsyncDefault[BatimentGroupeRnc],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "copro_dans_pvd": copro_dans_pvd,
                        "l_annee_construction": l_annee_construction,
                        "l_nom_copro": l_nom_copro,
                        "l_siret": l_siret,
                        "limit": limit,
                        "nb_log": nb_log,
                        "nb_lot_garpark": nb_lot_garpark,
                        "nb_lot_tertiaire": nb_lot_tertiaire,
                        "nb_lot_tot": nb_lot_tot,
                        "numero_immat_principal": numero_immat_principal,
                        "offset": offset,
                        "order": order,
                        "periode_construction_max": periode_construction_max,
                        "select": select,
                    },
                    rnc_list_params.RncListParams,
                ),
            ),
            model=BatimentGroupeRnc,
        )


class RncResourceWithRawResponse:
    def __init__(self, rnc: RncResource) -> None:
        self._rnc = rnc

        self.list = to_raw_response_wrapper(
            rnc.list,
        )


class AsyncRncResourceWithRawResponse:
    def __init__(self, rnc: AsyncRncResource) -> None:
        self._rnc = rnc

        self.list = async_to_raw_response_wrapper(
            rnc.list,
        )


class RncResourceWithStreamingResponse:
    def __init__(self, rnc: RncResource) -> None:
        self._rnc = rnc

        self.list = to_streamed_response_wrapper(
            rnc.list,
        )


class AsyncRncResourceWithStreamingResponse:
    def __init__(self, rnc: AsyncRncResource) -> None:
        self._rnc = rnc

        self.list = async_to_streamed_response_wrapper(
            rnc.list,
        )
