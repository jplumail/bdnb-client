# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

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
from ...types.donnees import rel_batiment_groupe_siren_complet_list_params
from ...types.donnees.rel_batiment_groupe_siren_complet_list_response import RelBatimentGroupeSirenCompletListResponse

__all__ = ["RelBatimentGroupeSirenCompletResource", "AsyncRelBatimentGroupeSirenCompletResource"]


class RelBatimentGroupeSirenCompletResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeSirenCompletResourceWithRawResponse:
        return RelBatimentGroupeSirenCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return RelBatimentGroupeSirenCompletResourceWithStreamingResponse(self)

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
    ) -> RelBatimentGroupeSirenCompletListResponse:
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
        return self._get(
            "/donnees/rel_batiment_groupe_siren_complet",
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
                    rel_batiment_groupe_siren_complet_list_params.RelBatimentGroupeSirenCompletListParams,
                ),
            ),
            cast_to=RelBatimentGroupeSirenCompletListResponse,
        )


class AsyncRelBatimentGroupeSirenCompletResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse(self)

    async def list(
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
    ) -> RelBatimentGroupeSirenCompletListResponse:
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
        return await self._get(
            "/donnees/rel_batiment_groupe_siren_complet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
                    rel_batiment_groupe_siren_complet_list_params.RelBatimentGroupeSirenCompletListParams,
                ),
            ),
            cast_to=RelBatimentGroupeSirenCompletListResponse,
        )


class RelBatimentGroupeSirenCompletResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_siren_complet: RelBatimentGroupeSirenCompletResource) -> None:
        self._rel_batiment_groupe_siren_complet = rel_batiment_groupe_siren_complet

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_siren_complet.list,
        )


class AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_siren_complet: AsyncRelBatimentGroupeSirenCompletResource) -> None:
        self._rel_batiment_groupe_siren_complet = rel_batiment_groupe_siren_complet

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_siren_complet.list,
        )


class RelBatimentGroupeSirenCompletResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_siren_complet: RelBatimentGroupeSirenCompletResource) -> None:
        self._rel_batiment_groupe_siren_complet = rel_batiment_groupe_siren_complet

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_siren_complet.list,
        )


class AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_siren_complet: AsyncRelBatimentGroupeSirenCompletResource) -> None:
        self._rel_batiment_groupe_siren_complet = rel_batiment_groupe_siren_complet

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_siren_complet.list,
        )
