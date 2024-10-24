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
from ....types.donnees.batiment_groupe import synthese_enveloppe_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_synthese_enveloppe import BatimentGroupeSyntheseEnveloppe

__all__ = ["SyntheseEnveloppeResource", "AsyncSyntheseEnveloppeResource"]


class SyntheseEnveloppeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyntheseEnveloppeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return SyntheseEnveloppeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyntheseEnveloppeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return SyntheseEnveloppeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        epaisseur_isolation_mur_exterieur_estim: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        epaisseur_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_mur: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_plancher_bas: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_plancher_haut: str | NotGiven = NOT_GIVEN,
        l_orientation_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_orientation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_mur: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur_simplifie: str | NotGiven = NOT_GIVEN,
        materiaux_toiture_simplifie: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        score_fiabilite: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        source_information_principale: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_batiment_dpe: str | NotGiven = NOT_GIVEN,
        type_fermeture: str | NotGiven = NOT_GIVEN,
        type_gaz_lame: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_porte: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_brut_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        u_porte: str | NotGiven = NOT_GIVEN,
        uw: str | NotGiven = NOT_GIVEN,
        vitrage_vir: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeSyntheseEnveloppe]:
        """Table de synthèse des informations sur l'enveloppe du bâtiment.

        Elle contient
        des informations sur les performances énergétiques des parois, leurs
        caractéristiques technique et les types de matériaux utilisés. Cette première
        version ne contient que des informations issues des DPE ou fichiers fonciers.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code département INSEE

          epaisseur_isolation_mur_exterieur_estim: epaisseur d'isolation moyenne des murs extérieurs estimée à partir de la
              différence entre le U de mur et le U de mur nu. Dans le cas d'une épaisseur
              déclarée c'est directement l'épaisseur déclarée qui est considérée, dans le cas
              contraire l'épaisseur est estimée aussi pour les U conventionels de la méthode
              3CL DPE.

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
              DPE.

          epaisseur_structure_mur_exterieur: epaisseur moyenne de la partie structure du mur (sans l'isolation rapportée ni
              les doublages)

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrée. coefficient entre 0
              et 1

          l_local_non_chauffe_mur: liste des locaux non chauffés en contact avec les murs (enum DPE 2021)

          l_local_non_chauffe_plancher_bas: liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)

          l_local_non_chauffe_plancher_haut: liste des locaux non chauffés en contact avec les planchers hauts (enum
              DPE 2021)

          l_orientation_baie_vitree: liste des orientations des baies vitrées (enum version BDNB)

          l_orientation_mur_exterieur: liste des orientations des murs donnant sur l'extérieur (enum version BDNB)

          limit: Limiting and Pagination

          local_non_chauffe_principal_mur: liste des locaux non chauffés en contact avec les murs (enum DPE 2021)

          local_non_chauffe_principal_plancher_bas: liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)

          local_non_chauffe_principal_plancher_haut: liste des locaux non chauffés en contact avec les planchers hauts (enum
              DPE 2021)

          materiaux_structure_mur_exterieur: matériaux ou principe constructif principal utilisé pour les murs extérieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utilié pour les murs extérieur simplifié. Cette information
              peut àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          materiaux_toiture_simplifie: materiaux principal utilié pour la toiture simplifié. Cette information peut
              àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le moment)

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          score_fiabilite: score de fiabilité attribué aux informations affichées. En fonction de la source
              principale et du recoupement des informations de plusieurs sources le score peut
              àªtre plus ou moins élevé. Le score maximal de confiance est de 10, le score
              minimal de 1. des informations recoupées par plusieurs sources ont un score de
              confiance plus élevé que des informations fournies par une unique source (voir
              méthodo)

          select: Filtering Columns

          source_information_principale: base de données source principale d'oà¹ est tirée directement les informations
              sur les systèmes énergétiques du bâtiment. (pour l'instant pas de combinaisons
              de sources voir méthodo)

          traversant: indicateur du cà´té traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_batiment_dpe: type de bâtiment au sens du DPE (maison, appartement ou immeuble). Cette colonne
              est renseignée uniquement si la source d'information est un DPE.

          type_fermeture: type de fermeture principale installée sur les baies vitrées du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injecté principalement dans la lame entre les vitrages des baies
              vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)

          type_isolation_mur_exterieur: type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
              version BDNB)

          type_isolation_plancher_bas: type d'isolation principal des planchers bas déperditifs pour le DPE (enum
              version BDNB)

          type_isolation_plancher_haut: type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
              version BDNB)

          type_materiaux_menuiserie: type de matériaux principal des menuiseries des baies vitrées du DPE (enum
              version BDNB)

          type_plancher_bas_deperditif: materiaux ou principe constructif principal des planchers bas (enum version
              BDNB)

          type_plancher_haut_deperditif: materiaux ou principe constructif principal des planchers hauts (enum version
              BDNB)

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_vitrage: type de vitrage principal des baies vitrées du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrées en incluant le
              calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)

          u_plancher_bas_brut_deperditif: Coefficient de transmission thermique moyen des planchers bas brut.

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
              méthode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          u_porte: Coefficient de transmission thermique moyen des portes (W/mÂ²/K)

          uw: Coefficient de transmission thermique moyen des baies vitrées sans prise en
              compte des fermeture (W/mÂ²/K)

          vitrage_vir: le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
              plus performant d'un point de vue thermique.

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
            "/donnees/batiment_groupe_synthese_enveloppe",
            page=SyncDefault[BatimentGroupeSyntheseEnveloppe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_inertie": classe_inertie,
                        "code_departement_insee": code_departement_insee,
                        "epaisseur_isolation_mur_exterieur_estim": epaisseur_isolation_mur_exterieur_estim,
                        "epaisseur_lame": epaisseur_lame,
                        "epaisseur_structure_mur_exterieur": epaisseur_structure_mur_exterieur,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "l_local_non_chauffe_mur": l_local_non_chauffe_mur,
                        "l_local_non_chauffe_plancher_bas": l_local_non_chauffe_plancher_bas,
                        "l_local_non_chauffe_plancher_haut": l_local_non_chauffe_plancher_haut,
                        "l_orientation_baie_vitree": l_orientation_baie_vitree,
                        "l_orientation_mur_exterieur": l_orientation_mur_exterieur,
                        "limit": limit,
                        "local_non_chauffe_principal_mur": local_non_chauffe_principal_mur,
                        "local_non_chauffe_principal_plancher_bas": local_non_chauffe_principal_plancher_bas,
                        "local_non_chauffe_principal_plancher_haut": local_non_chauffe_principal_plancher_haut,
                        "materiaux_structure_mur_exterieur": materiaux_structure_mur_exterieur,
                        "materiaux_structure_mur_exterieur_simplifie": materiaux_structure_mur_exterieur_simplifie,
                        "materiaux_toiture_simplifie": materiaux_toiture_simplifie,
                        "offset": offset,
                        "order": order,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "score_fiabilite": score_fiabilite,
                        "select": select,
                        "source_information_principale": source_information_principale,
                        "traversant": traversant,
                        "type_adjacence_principal_plancher_bas": type_adjacence_principal_plancher_bas,
                        "type_adjacence_principal_plancher_haut": type_adjacence_principal_plancher_haut,
                        "type_batiment_dpe": type_batiment_dpe,
                        "type_fermeture": type_fermeture,
                        "type_gaz_lame": type_gaz_lame,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_porte": type_porte,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_brut_deperditif": u_plancher_bas_brut_deperditif,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "u_porte": u_porte,
                        "uw": uw,
                        "vitrage_vir": vitrage_vir,
                    },
                    synthese_enveloppe_list_params.SyntheseEnveloppeListParams,
                ),
            ),
            model=BatimentGroupeSyntheseEnveloppe,
        )


class AsyncSyntheseEnveloppeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyntheseEnveloppeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncSyntheseEnveloppeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyntheseEnveloppeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncSyntheseEnveloppeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        epaisseur_isolation_mur_exterieur_estim: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        epaisseur_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_mur: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_plancher_bas: str | NotGiven = NOT_GIVEN,
        l_local_non_chauffe_plancher_haut: str | NotGiven = NOT_GIVEN,
        l_orientation_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_orientation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_mur: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        local_non_chauffe_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur_simplifie: str | NotGiven = NOT_GIVEN,
        materiaux_toiture_simplifie: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        score_fiabilite: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        source_information_principale: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_batiment_dpe: str | NotGiven = NOT_GIVEN,
        type_fermeture: str | NotGiven = NOT_GIVEN,
        type_gaz_lame: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_porte: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_brut_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        u_porte: str | NotGiven = NOT_GIVEN,
        uw: str | NotGiven = NOT_GIVEN,
        vitrage_vir: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeSyntheseEnveloppe, AsyncDefault[BatimentGroupeSyntheseEnveloppe]]:
        """Table de synthèse des informations sur l'enveloppe du bâtiment.

        Elle contient
        des informations sur les performances énergétiques des parois, leurs
        caractéristiques technique et les types de matériaux utilisés. Cette première
        version ne contient que des informations issues des DPE ou fichiers fonciers.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code département INSEE

          epaisseur_isolation_mur_exterieur_estim: epaisseur d'isolation moyenne des murs extérieurs estimée à partir de la
              différence entre le U de mur et le U de mur nu. Dans le cas d'une épaisseur
              déclarée c'est directement l'épaisseur déclarée qui est considérée, dans le cas
              contraire l'épaisseur est estimée aussi pour les U conventionels de la méthode
              3CL DPE.

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
              DPE.

          epaisseur_structure_mur_exterieur: epaisseur moyenne de la partie structure du mur (sans l'isolation rapportée ni
              les doublages)

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrée. coefficient entre 0
              et 1

          l_local_non_chauffe_mur: liste des locaux non chauffés en contact avec les murs (enum DPE 2021)

          l_local_non_chauffe_plancher_bas: liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)

          l_local_non_chauffe_plancher_haut: liste des locaux non chauffés en contact avec les planchers hauts (enum
              DPE 2021)

          l_orientation_baie_vitree: liste des orientations des baies vitrées (enum version BDNB)

          l_orientation_mur_exterieur: liste des orientations des murs donnant sur l'extérieur (enum version BDNB)

          limit: Limiting and Pagination

          local_non_chauffe_principal_mur: liste des locaux non chauffés en contact avec les murs (enum DPE 2021)

          local_non_chauffe_principal_plancher_bas: liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)

          local_non_chauffe_principal_plancher_haut: liste des locaux non chauffés en contact avec les planchers hauts (enum
              DPE 2021)

          materiaux_structure_mur_exterieur: matériaux ou principe constructif principal utilisé pour les murs extérieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utilié pour les murs extérieur simplifié. Cette information
              peut àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          materiaux_toiture_simplifie: materiaux principal utilié pour la toiture simplifié. Cette information peut
              àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le moment)

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          score_fiabilite: score de fiabilité attribué aux informations affichées. En fonction de la source
              principale et du recoupement des informations de plusieurs sources le score peut
              àªtre plus ou moins élevé. Le score maximal de confiance est de 10, le score
              minimal de 1. des informations recoupées par plusieurs sources ont un score de
              confiance plus élevé que des informations fournies par une unique source (voir
              méthodo)

          select: Filtering Columns

          source_information_principale: base de données source principale d'oà¹ est tirée directement les informations
              sur les systèmes énergétiques du bâtiment. (pour l'instant pas de combinaisons
              de sources voir méthodo)

          traversant: indicateur du cà´té traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_batiment_dpe: type de bâtiment au sens du DPE (maison, appartement ou immeuble). Cette colonne
              est renseignée uniquement si la source d'information est un DPE.

          type_fermeture: type de fermeture principale installée sur les baies vitrées du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injecté principalement dans la lame entre les vitrages des baies
              vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)

          type_isolation_mur_exterieur: type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
              version BDNB)

          type_isolation_plancher_bas: type d'isolation principal des planchers bas déperditifs pour le DPE (enum
              version BDNB)

          type_isolation_plancher_haut: type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
              version BDNB)

          type_materiaux_menuiserie: type de matériaux principal des menuiseries des baies vitrées du DPE (enum
              version BDNB)

          type_plancher_bas_deperditif: materiaux ou principe constructif principal des planchers bas (enum version
              BDNB)

          type_plancher_haut_deperditif: materiaux ou principe constructif principal des planchers hauts (enum version
              BDNB)

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_vitrage: type de vitrage principal des baies vitrées du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrées en incluant le
              calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)

          u_plancher_bas_brut_deperditif: Coefficient de transmission thermique moyen des planchers bas brut.

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
              méthode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          u_porte: Coefficient de transmission thermique moyen des portes (W/mÂ²/K)

          uw: Coefficient de transmission thermique moyen des baies vitrées sans prise en
              compte des fermeture (W/mÂ²/K)

          vitrage_vir: le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
              plus performant d'un point de vue thermique.

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
            "/donnees/batiment_groupe_synthese_enveloppe",
            page=AsyncDefault[BatimentGroupeSyntheseEnveloppe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_inertie": classe_inertie,
                        "code_departement_insee": code_departement_insee,
                        "epaisseur_isolation_mur_exterieur_estim": epaisseur_isolation_mur_exterieur_estim,
                        "epaisseur_lame": epaisseur_lame,
                        "epaisseur_structure_mur_exterieur": epaisseur_structure_mur_exterieur,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "l_local_non_chauffe_mur": l_local_non_chauffe_mur,
                        "l_local_non_chauffe_plancher_bas": l_local_non_chauffe_plancher_bas,
                        "l_local_non_chauffe_plancher_haut": l_local_non_chauffe_plancher_haut,
                        "l_orientation_baie_vitree": l_orientation_baie_vitree,
                        "l_orientation_mur_exterieur": l_orientation_mur_exterieur,
                        "limit": limit,
                        "local_non_chauffe_principal_mur": local_non_chauffe_principal_mur,
                        "local_non_chauffe_principal_plancher_bas": local_non_chauffe_principal_plancher_bas,
                        "local_non_chauffe_principal_plancher_haut": local_non_chauffe_principal_plancher_haut,
                        "materiaux_structure_mur_exterieur": materiaux_structure_mur_exterieur,
                        "materiaux_structure_mur_exterieur_simplifie": materiaux_structure_mur_exterieur_simplifie,
                        "materiaux_toiture_simplifie": materiaux_toiture_simplifie,
                        "offset": offset,
                        "order": order,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "score_fiabilite": score_fiabilite,
                        "select": select,
                        "source_information_principale": source_information_principale,
                        "traversant": traversant,
                        "type_adjacence_principal_plancher_bas": type_adjacence_principal_plancher_bas,
                        "type_adjacence_principal_plancher_haut": type_adjacence_principal_plancher_haut,
                        "type_batiment_dpe": type_batiment_dpe,
                        "type_fermeture": type_fermeture,
                        "type_gaz_lame": type_gaz_lame,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_porte": type_porte,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_brut_deperditif": u_plancher_bas_brut_deperditif,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "u_porte": u_porte,
                        "uw": uw,
                        "vitrage_vir": vitrage_vir,
                    },
                    synthese_enveloppe_list_params.SyntheseEnveloppeListParams,
                ),
            ),
            model=BatimentGroupeSyntheseEnveloppe,
        )


class SyntheseEnveloppeResourceWithRawResponse:
    def __init__(self, synthese_enveloppe: SyntheseEnveloppeResource) -> None:
        self._synthese_enveloppe = synthese_enveloppe

        self.list = to_raw_response_wrapper(
            synthese_enveloppe.list,
        )


class AsyncSyntheseEnveloppeResourceWithRawResponse:
    def __init__(self, synthese_enveloppe: AsyncSyntheseEnveloppeResource) -> None:
        self._synthese_enveloppe = synthese_enveloppe

        self.list = async_to_raw_response_wrapper(
            synthese_enveloppe.list,
        )


class SyntheseEnveloppeResourceWithStreamingResponse:
    def __init__(self, synthese_enveloppe: SyntheseEnveloppeResource) -> None:
        self._synthese_enveloppe = synthese_enveloppe

        self.list = to_streamed_response_wrapper(
            synthese_enveloppe.list,
        )


class AsyncSyntheseEnveloppeResourceWithStreamingResponse:
    def __init__(self, synthese_enveloppe: AsyncSyntheseEnveloppeResource) -> None:
        self._synthese_enveloppe = synthese_enveloppe

        self.list = async_to_streamed_response_wrapper(
            synthese_enveloppe.list,
        )
