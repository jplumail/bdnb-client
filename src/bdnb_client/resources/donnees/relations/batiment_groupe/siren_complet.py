# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, strip_not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncDefault, AsyncDefault
from ....._base_client import AsyncPaginator, make_request_options
from .....types.donnees.relations.batiment_groupe import siren_complet_list_params
from .....types.donnees.relations.batiment_groupe.rel_batiment_groupe_siren_complet import RelBatimentGroupeSirenComplet

__all__ = ["SirenCompletResource", "AsyncSirenCompletResource"]


class SirenCompletResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SirenCompletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return SirenCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SirenCompletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return SirenCompletResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cat_org: str | NotGiven = NOT_GIVEN,
        cat_org_simplifie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        dans_majic_pm_ou_etablissement: str | NotGiven = NOT_GIVEN,
        date_creation: Union[str, date] | NotGiven = NOT_GIVEN,
        date_dernier_traitement: Union[str, date] | NotGiven = NOT_GIVEN,
        denomination_personne_morale: str | NotGiven = NOT_GIVEN,
        etablissement: str | NotGiven = NOT_GIVEN,
        etat_administratif_actif: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        nb_siret_actifs: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        personne_type: str | NotGiven = NOT_GIVEN,
        proprietaire_open: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        siren_dans_sirene: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[RelBatimentGroupeSirenComplet]:
        """
        Table de relation entre les bâtiments de la BDNB et les siren.

        Args:
          batiment_groupe_id: Clé d'Intéropérabilité du bâtiment dans la BDNB.

          cat_org: Catégorie de l'organisation selon la base RPLS.

          cat_org_simplifie: Catégorie de l'organisation - simplifiée

          code_departement_insee: (bdnb) Code département INSEE dans lequel se trouve le bâtiment

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          dans_majic_pm_ou_etablissement: Identifié comme établissement ou dans majic_pm - permet de filtrer les éléments
              en open data

          date_creation: La date de création de l'unité légale - correspond à la date qui figure dans la
              déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.

          date_dernier_traitement: Date du dernier traitement de l'unité légale dans le répertoire Sirene.

          denomination_personne_morale: Dénomination de la personne morale.

          etablissement: Identifié comme établissement

          etat_administratif_actif: à‰tat administratif de l'unité légale (siren). Si l'unité légale est signalée
              comme active alors la variable est indiquée comme 'Vrai'.

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) Nombre de locaux déclarés dans majic_pm.

          nb_siret_actifs: Nombre de siret actifs.

          offset: Limiting and Pagination

          order: Ordering

          personne_type: Permet de différencier les personnes physiques des personnes morales.

          proprietaire_open: Permet de filtrer les propriétaires de type open

          select: Filtering Columns

          siren: Siren de la personne morale.

          siren_dans_sirene: Le Siren est présent dans la base sirene.

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
            "/donnees/rel_batiment_groupe_siren_complet",
            page=SyncDefault[RelBatimentGroupeSirenComplet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "cat_org": cat_org,
                        "cat_org_simplifie": cat_org_simplifie,
                        "code_departement_insee": code_departement_insee,
                        "dans_majic_pm": dans_majic_pm,
                        "dans_majic_pm_ou_etablissement": dans_majic_pm_ou_etablissement,
                        "date_creation": date_creation,
                        "date_dernier_traitement": date_dernier_traitement,
                        "denomination_personne_morale": denomination_personne_morale,
                        "etablissement": etablissement,
                        "etat_administratif_actif": etat_administratif_actif,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "nb_siret_actifs": nb_siret_actifs,
                        "offset": offset,
                        "order": order,
                        "personne_type": personne_type,
                        "proprietaire_open": proprietaire_open,
                        "select": select,
                        "siren": siren,
                        "siren_dans_sirene": siren_dans_sirene,
                    },
                    siren_complet_list_params.SirenCompletListParams,
                ),
            ),
            model=RelBatimentGroupeSirenComplet,
        )


class AsyncSirenCompletResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSirenCompletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncSirenCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSirenCompletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncSirenCompletResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cat_org: str | NotGiven = NOT_GIVEN,
        cat_org_simplifie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        dans_majic_pm_ou_etablissement: str | NotGiven = NOT_GIVEN,
        date_creation: Union[str, date] | NotGiven = NOT_GIVEN,
        date_dernier_traitement: Union[str, date] | NotGiven = NOT_GIVEN,
        denomination_personne_morale: str | NotGiven = NOT_GIVEN,
        etablissement: str | NotGiven = NOT_GIVEN,
        etat_administratif_actif: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        nb_siret_actifs: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        personne_type: str | NotGiven = NOT_GIVEN,
        proprietaire_open: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        siren_dans_sirene: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RelBatimentGroupeSirenComplet, AsyncDefault[RelBatimentGroupeSirenComplet]]:
        """
        Table de relation entre les bâtiments de la BDNB et les siren.

        Args:
          batiment_groupe_id: Clé d'Intéropérabilité du bâtiment dans la BDNB.

          cat_org: Catégorie de l'organisation selon la base RPLS.

          cat_org_simplifie: Catégorie de l'organisation - simplifiée

          code_departement_insee: (bdnb) Code département INSEE dans lequel se trouve le bâtiment

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          dans_majic_pm_ou_etablissement: Identifié comme établissement ou dans majic_pm - permet de filtrer les éléments
              en open data

          date_creation: La date de création de l'unité légale - correspond à la date qui figure dans la
              déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.

          date_dernier_traitement: Date du dernier traitement de l'unité légale dans le répertoire Sirene.

          denomination_personne_morale: Dénomination de la personne morale.

          etablissement: Identifié comme établissement

          etat_administratif_actif: à‰tat administratif de l'unité légale (siren). Si l'unité légale est signalée
              comme active alors la variable est indiquée comme 'Vrai'.

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) Nombre de locaux déclarés dans majic_pm.

          nb_siret_actifs: Nombre de siret actifs.

          offset: Limiting and Pagination

          order: Ordering

          personne_type: Permet de différencier les personnes physiques des personnes morales.

          proprietaire_open: Permet de filtrer les propriétaires de type open

          select: Filtering Columns

          siren: Siren de la personne morale.

          siren_dans_sirene: Le Siren est présent dans la base sirene.

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
            "/donnees/rel_batiment_groupe_siren_complet",
            page=AsyncDefault[RelBatimentGroupeSirenComplet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "cat_org": cat_org,
                        "cat_org_simplifie": cat_org_simplifie,
                        "code_departement_insee": code_departement_insee,
                        "dans_majic_pm": dans_majic_pm,
                        "dans_majic_pm_ou_etablissement": dans_majic_pm_ou_etablissement,
                        "date_creation": date_creation,
                        "date_dernier_traitement": date_dernier_traitement,
                        "denomination_personne_morale": denomination_personne_morale,
                        "etablissement": etablissement,
                        "etat_administratif_actif": etat_administratif_actif,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "nb_siret_actifs": nb_siret_actifs,
                        "offset": offset,
                        "order": order,
                        "personne_type": personne_type,
                        "proprietaire_open": proprietaire_open,
                        "select": select,
                        "siren": siren,
                        "siren_dans_sirene": siren_dans_sirene,
                    },
                    siren_complet_list_params.SirenCompletListParams,
                ),
            ),
            model=RelBatimentGroupeSirenComplet,
        )


class SirenCompletResourceWithRawResponse:
    def __init__(self, siren_complet: SirenCompletResource) -> None:
        self._siren_complet = siren_complet

        self.list = to_raw_response_wrapper(
            siren_complet.list,
        )


class AsyncSirenCompletResourceWithRawResponse:
    def __init__(self, siren_complet: AsyncSirenCompletResource) -> None:
        self._siren_complet = siren_complet

        self.list = async_to_raw_response_wrapper(
            siren_complet.list,
        )


class SirenCompletResourceWithStreamingResponse:
    def __init__(self, siren_complet: SirenCompletResource) -> None:
        self._siren_complet = siren_complet

        self.list = to_streamed_response_wrapper(
            siren_complet.list,
        )


class AsyncSirenCompletResourceWithStreamingResponse:
    def __init__(self, siren_complet: AsyncSirenCompletResource) -> None:
        self._siren_complet = siren_complet

        self.list = async_to_streamed_response_wrapper(
            siren_complet.list,
        )
