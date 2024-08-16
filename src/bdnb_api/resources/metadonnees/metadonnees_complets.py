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
from ...types.metadonnees import metadonnees_complet_list_params
from ...types.metadonnees.metadonnees_complet_list_response import MetadonneesCompletListResponse

__all__ = ["MetadonneesCompletsResource", "AsyncMetadonneesCompletsResource"]


class MetadonneesCompletsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadonneesCompletsResourceWithRawResponse:
        return MetadonneesCompletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadonneesCompletsResourceWithStreamingResponse:
        return MetadonneesCompletsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        api_expert: str | NotGiven = NOT_GIVEN,
        api_open: str | NotGiven = NOT_GIVEN,
        colonne_gorenove_legacy: str | NotGiven = NOT_GIVEN,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        contrainte_acces_table: str | NotGiven = NOT_GIVEN,
        couverture_spatiale: str | NotGiven = NOT_GIVEN,
        couverture_temporelle: str | NotGiven = NOT_GIVEN,
        date_publication: str | NotGiven = NOT_GIVEN,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        libelle_metier: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        row_number: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadonneesCompletListResponse:
        """
        jointure de toutes les metadata Ã l'Ã©chelle colonne

        Args:
          api_expert: Disponible pour les abonnÃ©s de l'API Expert

          api_open: Disponible sans souscription

          colonne_gorenove_legacy: Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings

          contrainte_acces: Contrainte d'accÃ¨s de la colonne

          contrainte_acces_table: Contrainte d'accÃ¨s de la table

          couverture_spatiale: Couverture spatiale du jeu de donnÃ©es

          couverture_temporelle: Couverture temporelle du jeu de donnÃ©es

          date_publication: Date de publication du jeu de donnÃ©es

          denomination_serie: DÃ©nomination du jeu de donnÃ©es

          description: Description de la table

          description_jeu_de_donnees: Description du jeu de donnÃ©es

          index: la colonne est indexÃ©e dans la table

          libelle_metier: libelle Ã utiliser dans les applications web

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: MillÃ©sime du jeu de donnÃ©es

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachÃ©e

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type: Type de la colonne

          unite: UnitÃ© de la colonne

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
            "/metadonnees/metadonnees_complet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_expert": api_expert,
                        "api_open": api_open,
                        "colonne_gorenove_legacy": colonne_gorenove_legacy,
                        "contrainte_acces": contrainte_acces,
                        "contrainte_acces_table": contrainte_acces_table,
                        "couverture_spatiale": couverture_spatiale,
                        "couverture_temporelle": couverture_temporelle,
                        "date_publication": date_publication,
                        "denomination_serie": denomination_serie,
                        "description": description,
                        "description_jeu_de_donnees": description_jeu_de_donnees,
                        "description_table": description_table,
                        "index": index,
                        "libelle_metier": libelle_metier,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "row_number": row_number,
                        "select": select,
                        "type": type,
                        "unite": unite,
                    },
                    metadonnees_complet_list_params.MetadonneesCompletListParams,
                ),
            ),
            cast_to=MetadonneesCompletListResponse,
        )


class AsyncMetadonneesCompletsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadonneesCompletsResourceWithRawResponse:
        return AsyncMetadonneesCompletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadonneesCompletsResourceWithStreamingResponse:
        return AsyncMetadonneesCompletsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        api_expert: str | NotGiven = NOT_GIVEN,
        api_open: str | NotGiven = NOT_GIVEN,
        colonne_gorenove_legacy: str | NotGiven = NOT_GIVEN,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        contrainte_acces_table: str | NotGiven = NOT_GIVEN,
        couverture_spatiale: str | NotGiven = NOT_GIVEN,
        couverture_temporelle: str | NotGiven = NOT_GIVEN,
        date_publication: str | NotGiven = NOT_GIVEN,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        libelle_metier: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        row_number: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadonneesCompletListResponse:
        """
        jointure de toutes les metadata Ã l'Ã©chelle colonne

        Args:
          api_expert: Disponible pour les abonnÃ©s de l'API Expert

          api_open: Disponible sans souscription

          colonne_gorenove_legacy: Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings

          contrainte_acces: Contrainte d'accÃ¨s de la colonne

          contrainte_acces_table: Contrainte d'accÃ¨s de la table

          couverture_spatiale: Couverture spatiale du jeu de donnÃ©es

          couverture_temporelle: Couverture temporelle du jeu de donnÃ©es

          date_publication: Date de publication du jeu de donnÃ©es

          denomination_serie: DÃ©nomination du jeu de donnÃ©es

          description: Description de la table

          description_jeu_de_donnees: Description du jeu de donnÃ©es

          index: la colonne est indexÃ©e dans la table

          libelle_metier: libelle Ã utiliser dans les applications web

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: MillÃ©sime du jeu de donnÃ©es

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachÃ©e

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type: Type de la colonne

          unite: UnitÃ© de la colonne

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
            "/metadonnees/metadonnees_complet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "api_expert": api_expert,
                        "api_open": api_open,
                        "colonne_gorenove_legacy": colonne_gorenove_legacy,
                        "contrainte_acces": contrainte_acces,
                        "contrainte_acces_table": contrainte_acces_table,
                        "couverture_spatiale": couverture_spatiale,
                        "couverture_temporelle": couverture_temporelle,
                        "date_publication": date_publication,
                        "denomination_serie": denomination_serie,
                        "description": description,
                        "description_jeu_de_donnees": description_jeu_de_donnees,
                        "description_table": description_table,
                        "index": index,
                        "libelle_metier": libelle_metier,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "row_number": row_number,
                        "select": select,
                        "type": type,
                        "unite": unite,
                    },
                    metadonnees_complet_list_params.MetadonneesCompletListParams,
                ),
            ),
            cast_to=MetadonneesCompletListResponse,
        )


class MetadonneesCompletsResourceWithRawResponse:
    def __init__(self, metadonnees_complets: MetadonneesCompletsResource) -> None:
        self._metadonnees_complets = metadonnees_complets

        self.list = to_raw_response_wrapper(
            metadonnees_complets.list,
        )


class AsyncMetadonneesCompletsResourceWithRawResponse:
    def __init__(self, metadonnees_complets: AsyncMetadonneesCompletsResource) -> None:
        self._metadonnees_complets = metadonnees_complets

        self.list = async_to_raw_response_wrapper(
            metadonnees_complets.list,
        )


class MetadonneesCompletsResourceWithStreamingResponse:
    def __init__(self, metadonnees_complets: MetadonneesCompletsResource) -> None:
        self._metadonnees_complets = metadonnees_complets

        self.list = to_streamed_response_wrapper(
            metadonnees_complets.list,
        )


class AsyncMetadonneesCompletsResourceWithStreamingResponse:
    def __init__(self, metadonnees_complets: AsyncMetadonneesCompletsResource) -> None:
        self._metadonnees_complets = metadonnees_complets

        self.list = async_to_streamed_response_wrapper(
            metadonnees_complets.list,
        )
