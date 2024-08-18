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
from ...types.donnees import batiment_groupe_list_params
from ...types.donnees.batiment_groupe import BatimentGroupe

__all__ = ["BatimentGroupeResource", "AsyncBatimentGroupeResource"]


class BatimentGroupeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe_pos_wgs84: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupe]:
        """
        Complexes de bâtiments au sens de la BDNB

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          contient_fictive_geom_groupe: Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
              et ne représente pas la géométrie du groupe de bâtiment.

          geom_groupe: Géométrie multipolygonale du groupe de bâtiment (Lambert-93)

          geom_groupe_pos_wgs84: Point sur la surface du groupe de bâtiment en WSG84

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

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
            "/donnees/batiment_groupe",
            page=SyncDefault[BatimentGroupe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "geom_groupe": geom_groupe,
                        "geom_groupe_pos_wgs84": geom_groupe_pos_wgs84,
                        "libelle_commune_insee": libelle_commune_insee,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            model=BatimentGroupe,
        )


class AsyncBatimentGroupeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        geom_groupe_pos_wgs84: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupe, AsyncDefault[BatimentGroupe]]:
        """
        Complexes de bâtiments au sens de la BDNB

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          contient_fictive_geom_groupe: Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
              et ne représente pas la géométrie du groupe de bâtiment.

          geom_groupe: Géométrie multipolygonale du groupe de bâtiment (Lambert-93)

          geom_groupe_pos_wgs84: Point sur la surface du groupe de bâtiment en WSG84

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          limit: Limiting and Pagination

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

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
            "/donnees/batiment_groupe",
            page=AsyncDefault[BatimentGroupe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "geom_groupe": geom_groupe,
                        "geom_groupe_pos_wgs84": geom_groupe_pos_wgs84,
                        "libelle_commune_insee": libelle_commune_insee,
                        "limit": limit,
                        "nom_qp": nom_qp,
                        "offset": offset,
                        "order": order,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            model=BatimentGroupe,
        )


class BatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_raw_response_wrapper(
            batiment_groupe.list,
        )


class AsyncBatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_raw_response_wrapper(
            batiment_groupe.list,
        )


class BatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_streamed_response_wrapper(
            batiment_groupe.list,
        )


class AsyncBatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe.list,
        )
