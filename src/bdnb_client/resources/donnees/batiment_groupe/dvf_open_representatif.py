# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

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
from ....types.donnees.batiment_groupe import dvf_open_representatif_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_dvf_open_representatif import BatimentGroupeDvfOpenRepresentatif

__all__ = ["DvfOpenRepresentatifResource", "AsyncDvfOpenRepresentatifResource"]


class DvfOpenRepresentatifResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DvfOpenRepresentatifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DvfOpenRepresentatifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DvfOpenRepresentatifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DvfOpenRepresentatifResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        date_mutation: Union[str, date] | NotGiven = NOT_GIVEN,
        id_opendata: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_maison_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_piece_principale: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_dependance: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_collective: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_individuelle: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_tertiaire: str | NotGiven = NOT_GIVEN,
        surface_terrain_mutee: str | NotGiven = NOT_GIVEN,
        valeur_fonciere: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeDvfOpenRepresentatif]:
        """
        Données des mutations issues des valeurs DVF open data pour une mutation
        représentative du batiment_groupe

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          date_mutation: (dv3f) date de la mutation

          id_opendata: Identifiant open data de la mutation.

          limit: Limiting and Pagination

          nb_appartement_mutee_mutation: Nombre d'appartements ayant mutés lors de la mutation représentative.

          nb_dependance_mutee_mutation: Nombre de dépendances ayant mutées lors de la mutation représentative.

          nb_locaux_mutee_mutation: Nombre de locaux ayant mutés lors de la mutation représentative.

          nb_locaux_tertiaire_mutee_mutation: Nombre de locaux tertiaires ayant mutés lors de la mutation représentative.

          nb_maison_mutee_mutation: Nombre de maisons ayant mutées lors de la mutation représentative.

          nb_piece_principale: Nombre de pièces principales de la résidence individuelle ou collective ayant
              muté. Cet indicateur est disponible lorsqu'une unique résidence individuelle ou
              collective a mutée.

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local: Prix au mÂ² de bâti en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (résidences
              individuelles + dépendances) ou (résidences collectives + dépendances) ont
              mutées [â‚¬]

          prix_m2_terrain: Prix au mÂ² du terrain en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (résidences
              individuelles + dépendances) ou (résidences collectives + dépendances) ont
              mutées [â‚¬]

          select: Filtering Columns

          surface_bati_mutee_dependance: Surface de bâti associée à des dépendances ayant mutées lors de la mutation
              représentative [mÂ²].

          surface_bati_mutee_residencielle_collective: Surface de bâti associée à des résidences collectives ayant mutées lors de la
              mutation représentative [mÂ²].

          surface_bati_mutee_residencielle_individuelle: Surface de bâti associée à des résidences individuelles ayant mutées lors de la
              mutation représentative [mÂ²].

          surface_bati_mutee_tertiaire: Surface de bâti associée à du tertiaire ayant mutées lors de la mutation
              représentative [mÂ²].

          surface_terrain_mutee: Surface de terrain ayant muté lors de la mutation représentative [mÂ²].

          valeur_fonciere: Valeur foncière en euros de la mutation représentative. [â‚¬]

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
            "/donnees/batiment_groupe_dvf_open_representatif",
            page=SyncDefault[BatimentGroupeDvfOpenRepresentatif],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "date_mutation": date_mutation,
                        "id_opendata": id_opendata,
                        "limit": limit,
                        "nb_appartement_mutee_mutation": nb_appartement_mutee_mutation,
                        "nb_dependance_mutee_mutation": nb_dependance_mutee_mutation,
                        "nb_locaux_mutee_mutation": nb_locaux_mutee_mutation,
                        "nb_locaux_tertiaire_mutee_mutation": nb_locaux_tertiaire_mutee_mutation,
                        "nb_maison_mutee_mutation": nb_maison_mutee_mutation,
                        "nb_piece_principale": nb_piece_principale,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local": prix_m2_local,
                        "prix_m2_terrain": prix_m2_terrain,
                        "select": select,
                        "surface_bati_mutee_dependance": surface_bati_mutee_dependance,
                        "surface_bati_mutee_residencielle_collective": surface_bati_mutee_residencielle_collective,
                        "surface_bati_mutee_residencielle_individuelle": surface_bati_mutee_residencielle_individuelle,
                        "surface_bati_mutee_tertiaire": surface_bati_mutee_tertiaire,
                        "surface_terrain_mutee": surface_terrain_mutee,
                        "valeur_fonciere": valeur_fonciere,
                    },
                    dvf_open_representatif_list_params.DvfOpenRepresentatifListParams,
                ),
            ),
            model=BatimentGroupeDvfOpenRepresentatif,
        )


class AsyncDvfOpenRepresentatifResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDvfOpenRepresentatifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDvfOpenRepresentatifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDvfOpenRepresentatifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDvfOpenRepresentatifResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        date_mutation: Union[str, date] | NotGiven = NOT_GIVEN,
        id_opendata: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_maison_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_piece_principale: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_dependance: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_collective: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_individuelle: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_tertiaire: str | NotGiven = NOT_GIVEN,
        surface_terrain_mutee: str | NotGiven = NOT_GIVEN,
        valeur_fonciere: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeDvfOpenRepresentatif, AsyncDefault[BatimentGroupeDvfOpenRepresentatif]]:
        """
        Données des mutations issues des valeurs DVF open data pour une mutation
        représentative du batiment_groupe

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          date_mutation: (dv3f) date de la mutation

          id_opendata: Identifiant open data de la mutation.

          limit: Limiting and Pagination

          nb_appartement_mutee_mutation: Nombre d'appartements ayant mutés lors de la mutation représentative.

          nb_dependance_mutee_mutation: Nombre de dépendances ayant mutées lors de la mutation représentative.

          nb_locaux_mutee_mutation: Nombre de locaux ayant mutés lors de la mutation représentative.

          nb_locaux_tertiaire_mutee_mutation: Nombre de locaux tertiaires ayant mutés lors de la mutation représentative.

          nb_maison_mutee_mutation: Nombre de maisons ayant mutées lors de la mutation représentative.

          nb_piece_principale: Nombre de pièces principales de la résidence individuelle ou collective ayant
              muté. Cet indicateur est disponible lorsqu'une unique résidence individuelle ou
              collective a mutée.

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local: Prix au mÂ² de bâti en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (résidences
              individuelles + dépendances) ou (résidences collectives + dépendances) ont
              mutées [â‚¬]

          prix_m2_terrain: Prix au mÂ² du terrain en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (résidences
              individuelles + dépendances) ou (résidences collectives + dépendances) ont
              mutées [â‚¬]

          select: Filtering Columns

          surface_bati_mutee_dependance: Surface de bâti associée à des dépendances ayant mutées lors de la mutation
              représentative [mÂ²].

          surface_bati_mutee_residencielle_collective: Surface de bâti associée à des résidences collectives ayant mutées lors de la
              mutation représentative [mÂ²].

          surface_bati_mutee_residencielle_individuelle: Surface de bâti associée à des résidences individuelles ayant mutées lors de la
              mutation représentative [mÂ²].

          surface_bati_mutee_tertiaire: Surface de bâti associée à du tertiaire ayant mutées lors de la mutation
              représentative [mÂ²].

          surface_terrain_mutee: Surface de terrain ayant muté lors de la mutation représentative [mÂ²].

          valeur_fonciere: Valeur foncière en euros de la mutation représentative. [â‚¬]

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
            "/donnees/batiment_groupe_dvf_open_representatif",
            page=AsyncDefault[BatimentGroupeDvfOpenRepresentatif],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "date_mutation": date_mutation,
                        "id_opendata": id_opendata,
                        "limit": limit,
                        "nb_appartement_mutee_mutation": nb_appartement_mutee_mutation,
                        "nb_dependance_mutee_mutation": nb_dependance_mutee_mutation,
                        "nb_locaux_mutee_mutation": nb_locaux_mutee_mutation,
                        "nb_locaux_tertiaire_mutee_mutation": nb_locaux_tertiaire_mutee_mutation,
                        "nb_maison_mutee_mutation": nb_maison_mutee_mutation,
                        "nb_piece_principale": nb_piece_principale,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local": prix_m2_local,
                        "prix_m2_terrain": prix_m2_terrain,
                        "select": select,
                        "surface_bati_mutee_dependance": surface_bati_mutee_dependance,
                        "surface_bati_mutee_residencielle_collective": surface_bati_mutee_residencielle_collective,
                        "surface_bati_mutee_residencielle_individuelle": surface_bati_mutee_residencielle_individuelle,
                        "surface_bati_mutee_tertiaire": surface_bati_mutee_tertiaire,
                        "surface_terrain_mutee": surface_terrain_mutee,
                        "valeur_fonciere": valeur_fonciere,
                    },
                    dvf_open_representatif_list_params.DvfOpenRepresentatifListParams,
                ),
            ),
            model=BatimentGroupeDvfOpenRepresentatif,
        )


class DvfOpenRepresentatifResourceWithRawResponse:
    def __init__(self, dvf_open_representatif: DvfOpenRepresentatifResource) -> None:
        self._dvf_open_representatif = dvf_open_representatif

        self.list = to_raw_response_wrapper(
            dvf_open_representatif.list,
        )


class AsyncDvfOpenRepresentatifResourceWithRawResponse:
    def __init__(self, dvf_open_representatif: AsyncDvfOpenRepresentatifResource) -> None:
        self._dvf_open_representatif = dvf_open_representatif

        self.list = async_to_raw_response_wrapper(
            dvf_open_representatif.list,
        )


class DvfOpenRepresentatifResourceWithStreamingResponse:
    def __init__(self, dvf_open_representatif: DvfOpenRepresentatifResource) -> None:
        self._dvf_open_representatif = dvf_open_representatif

        self.list = to_streamed_response_wrapper(
            dvf_open_representatif.list,
        )


class AsyncDvfOpenRepresentatifResourceWithStreamingResponse:
    def __init__(self, dvf_open_representatif: AsyncDvfOpenRepresentatifResource) -> None:
        self._dvf_open_representatif = dvf_open_representatif

        self.list = async_to_streamed_response_wrapper(
            dvf_open_representatif.list,
        )
