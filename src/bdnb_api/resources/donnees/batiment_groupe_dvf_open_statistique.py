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
from ...types.donnees import batiment_groupe_dvf_open_statistique_list_params
from ...types.donnees.batiment_groupe_dvf_open_statistique_list_response import (
    BatimentGroupeDvfOpenStatistiqueListResponse,
)

__all__ = ["BatimentGroupeDvfOpenStatistiqueResource", "AsyncBatimentGroupeDvfOpenStatistiqueResource"]


class BatimentGroupeDvfOpenStatistiqueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
        return BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
        return BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee: str | NotGiven = NOT_GIVEN,
        nb_maisons_mutee: str | NotGiven = NOT_GIVEN,
        nb_mutation: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local_max: str | NotGiven = NOT_GIVEN,
        prix_m2_local_median: str | NotGiven = NOT_GIVEN,
        prix_m2_local_min: str | NotGiven = NOT_GIVEN,
        prix_m2_local_moyen: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_max: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_median: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_min: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_moyen: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_max: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_median: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_min: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_moyenne: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeDvfOpenStatistiqueListResponse:
        """
        Données statistiques des mutations issues des valeurs DVF open data à l'échelle
        du bâtiment groupe.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nb_appartement_mutee: Nombre d'appartements qui ont mutés sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_dependance_mutee: Nombre de dépendances qui ont mutées sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_locaux_mutee: Nombre de locaux qui ont mutés sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_locaux_tertiaire_mutee: Nombre de locaux tertiaires qui ont mutés sur le batiment_groupe (sur la période
              de référence des DVF).

          nb_maisons_mutee: Nombre de maisons qui ont mutées sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_mutation: Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la période de
              référence des DVF).

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local_max: Prix maximale au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_median: Prix médian au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_min: Prix minimale au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_moyen: Prix moyen au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_max: Prix maximale au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_median: Prix médian au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_min: Prix minimale au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_moyen: Prix moyen au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          select: Filtering Columns

          valeur_fonciere_max: (dv3f) valeur foncière maximale parmi les locaux du bâtiment rapporté au mÂ²
              habitable (SHAB)[â‚¬/mÂ²]

          valeur_fonciere_median: Valeur foncière médiane en euros calculée sur l'ensemble des mutations qui ont
              eu lieu sur le batiment_groupe.

          valeur_fonciere_min: (dv3f) valeur foncière minimale parmi les locaux du bâtiment rapporté au mÂ²
              habitable (SHAB) [â‚¬/mÂ²]

          valeur_fonciere_moyenne: Valeur foncière moyenne en euros calculée sur l'ensemble des mutations qui ont
              eu lieu sur le batiment_groupe.

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
            "/donnees/batiment_groupe_dvf_open_statistique",
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
                        "nb_appartement_mutee": nb_appartement_mutee,
                        "nb_dependance_mutee": nb_dependance_mutee,
                        "nb_locaux_mutee": nb_locaux_mutee,
                        "nb_locaux_tertiaire_mutee": nb_locaux_tertiaire_mutee,
                        "nb_maisons_mutee": nb_maisons_mutee,
                        "nb_mutation": nb_mutation,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local_max": prix_m2_local_max,
                        "prix_m2_local_median": prix_m2_local_median,
                        "prix_m2_local_min": prix_m2_local_min,
                        "prix_m2_local_moyen": prix_m2_local_moyen,
                        "prix_m2_terrain_max": prix_m2_terrain_max,
                        "prix_m2_terrain_median": prix_m2_terrain_median,
                        "prix_m2_terrain_min": prix_m2_terrain_min,
                        "prix_m2_terrain_moyen": prix_m2_terrain_moyen,
                        "select": select,
                        "valeur_fonciere_max": valeur_fonciere_max,
                        "valeur_fonciere_median": valeur_fonciere_median,
                        "valeur_fonciere_min": valeur_fonciere_min,
                        "valeur_fonciere_moyenne": valeur_fonciere_moyenne,
                    },
                    batiment_groupe_dvf_open_statistique_list_params.BatimentGroupeDvfOpenStatistiqueListParams,
                ),
            ),
            cast_to=BatimentGroupeDvfOpenStatistiqueListResponse,
        )


class AsyncBatimentGroupeDvfOpenStatistiqueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
        return AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
        return AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee: str | NotGiven = NOT_GIVEN,
        nb_maisons_mutee: str | NotGiven = NOT_GIVEN,
        nb_mutation: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local_max: str | NotGiven = NOT_GIVEN,
        prix_m2_local_median: str | NotGiven = NOT_GIVEN,
        prix_m2_local_min: str | NotGiven = NOT_GIVEN,
        prix_m2_local_moyen: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_max: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_median: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_min: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain_moyen: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_max: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_median: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_min: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_moyenne: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeDvfOpenStatistiqueListResponse:
        """
        Données statistiques des mutations issues des valeurs DVF open data à l'échelle
        du bâtiment groupe.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nb_appartement_mutee: Nombre d'appartements qui ont mutés sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_dependance_mutee: Nombre de dépendances qui ont mutées sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_locaux_mutee: Nombre de locaux qui ont mutés sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_locaux_tertiaire_mutee: Nombre de locaux tertiaires qui ont mutés sur le batiment_groupe (sur la période
              de référence des DVF).

          nb_maisons_mutee: Nombre de maisons qui ont mutées sur le batiment_groupe (sur la période de
              référence des DVF).

          nb_mutation: Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la période de
              référence des DVF).

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local_max: Prix maximale au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_median: Prix médian au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_min: Prix minimale au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_local_moyen: Prix moyen au m2 de bâti en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_max: Prix maximale au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_median: Prix médian au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_min: Prix minimale au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          prix_m2_terrain_moyen: Prix moyen au m2 de terrain en euros calculé à partir des transactions dont
              uniquement des locaux (résidences individuelles + dépendances) ou (résidences
              collectives + dépendances) ont mutées

          select: Filtering Columns

          valeur_fonciere_max: (dv3f) valeur foncière maximale parmi les locaux du bâtiment rapporté au mÂ²
              habitable (SHAB)[â‚¬/mÂ²]

          valeur_fonciere_median: Valeur foncière médiane en euros calculée sur l'ensemble des mutations qui ont
              eu lieu sur le batiment_groupe.

          valeur_fonciere_min: (dv3f) valeur foncière minimale parmi les locaux du bâtiment rapporté au mÂ²
              habitable (SHAB) [â‚¬/mÂ²]

          valeur_fonciere_moyenne: Valeur foncière moyenne en euros calculée sur l'ensemble des mutations qui ont
              eu lieu sur le batiment_groupe.

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
            "/donnees/batiment_groupe_dvf_open_statistique",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nb_appartement_mutee": nb_appartement_mutee,
                        "nb_dependance_mutee": nb_dependance_mutee,
                        "nb_locaux_mutee": nb_locaux_mutee,
                        "nb_locaux_tertiaire_mutee": nb_locaux_tertiaire_mutee,
                        "nb_maisons_mutee": nb_maisons_mutee,
                        "nb_mutation": nb_mutation,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local_max": prix_m2_local_max,
                        "prix_m2_local_median": prix_m2_local_median,
                        "prix_m2_local_min": prix_m2_local_min,
                        "prix_m2_local_moyen": prix_m2_local_moyen,
                        "prix_m2_terrain_max": prix_m2_terrain_max,
                        "prix_m2_terrain_median": prix_m2_terrain_median,
                        "prix_m2_terrain_min": prix_m2_terrain_min,
                        "prix_m2_terrain_moyen": prix_m2_terrain_moyen,
                        "select": select,
                        "valeur_fonciere_max": valeur_fonciere_max,
                        "valeur_fonciere_median": valeur_fonciere_median,
                        "valeur_fonciere_min": valeur_fonciere_min,
                        "valeur_fonciere_moyenne": valeur_fonciere_moyenne,
                    },
                    batiment_groupe_dvf_open_statistique_list_params.BatimentGroupeDvfOpenStatistiqueListParams,
                ),
            ),
            cast_to=BatimentGroupeDvfOpenStatistiqueListResponse,
        )


class BatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
    def __init__(self, batiment_groupe_dvf_open_statistique: BatimentGroupeDvfOpenStatistiqueResource) -> None:
        self._batiment_groupe_dvf_open_statistique = batiment_groupe_dvf_open_statistique

        self.list = to_raw_response_wrapper(
            batiment_groupe_dvf_open_statistique.list,
        )


class AsyncBatimentGroupeDvfOpenStatistiqueResourceWithRawResponse:
    def __init__(self, batiment_groupe_dvf_open_statistique: AsyncBatimentGroupeDvfOpenStatistiqueResource) -> None:
        self._batiment_groupe_dvf_open_statistique = batiment_groupe_dvf_open_statistique

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_dvf_open_statistique.list,
        )


class BatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_dvf_open_statistique: BatimentGroupeDvfOpenStatistiqueResource) -> None:
        self._batiment_groupe_dvf_open_statistique = batiment_groupe_dvf_open_statistique

        self.list = to_streamed_response_wrapper(
            batiment_groupe_dvf_open_statistique.list,
        )


class AsyncBatimentGroupeDvfOpenStatistiqueResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_dvf_open_statistique: AsyncBatimentGroupeDvfOpenStatistiqueResource) -> None:
        self._batiment_groupe_dvf_open_statistique = batiment_groupe_dvf_open_statistique

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_dvf_open_statistique.list,
        )