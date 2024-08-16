# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.donnees import (
    tables_bdnb_retrieve_batiment_groupe_qpv_params,
    tables_bdnb_retrieve_batiment_groupe_geospx_params,
    tables_bdnb_retrieve_rel_batiment_groupe_qpv_params,
    tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_params,
    tables_bdnb_retrieve_rel_batiment_groupe_adresse_params,
    tables_bdnb_retrieve_referentiel_administratif_iris_params,
    tables_bdnb_retrieve_rel_batiment_construction_adresse_params,
    tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_params,
    tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_params,
    tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_params,
)
from ....types.donnees.tables_bdnb_retrieve_batiment_groupe_qpv_response import (
    TablesBdnbRetrieveBatimentGroupeQpvResponse,
)
from ....types.donnees.tables_bdnb_retrieve_batiment_groupe_geospx_response import (
    TablesBdnbRetrieveBatimentGroupeGeospxResponse,
)
from ....types.donnees.tables_bdnb_retrieve_rel_batiment_groupe_qpv_response import (
    TablesBdnbRetrieveRelBatimentGroupeQpvResponse,
)
from ....types.donnees.tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_response import (
    TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse,
)
from ....types.donnees.tables_bdnb_retrieve_rel_batiment_groupe_adresse_response import (
    TablesBdnbRetrieveRelBatimentGroupeAdresseResponse,
)
from ....types.donnees.tables_bdnb_retrieve_referentiel_administratif_iris_response import (
    TablesBdnbRetrieveReferentielAdministratifIrisResponse,
)
from ....types.donnees.tables_bdnb_retrieve_rel_batiment_construction_adresse_response import (
    TablesBdnbRetrieveRelBatimentConstructionAdresseResponse,
)
from ....types.donnees.tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_response import (
    TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse,
)
from ....types.donnees.tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_response import (
    TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse,
)
from ....types.donnees.tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_response import (
    TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse,
)

__all__ = ["TablesBdnbResource", "AsyncTablesBdnbResource"]


class TablesBdnbResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesBdnbResourceWithRawResponse:
        return TablesBdnbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesBdnbResourceWithStreamingResponse:
        return TablesBdnbResourceWithStreamingResponse(self)

    def retrieve_batiment_groupe_bdtopo_zoac(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_nature_detaillee: str | NotGiven = NOT_GIVEN,
        l_toponyme: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse:
        """
        Informations de la BDTopo, couche zone d'activitÃ©, agrÃ©gÃ©es Ã l'Ã©chelle du
        bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          l_nature: (ign) CatÃ©gorie de nature du bÃ¢timent

          l_nature_detaillee: (ign) CatÃ©gorie dÃ©taillÃ©e de nature de l'Ã©quipement

          l_toponyme: (ign) Toponymie de l'Ã©quipement

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_bdtopo_zoac",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nature": l_nature,
                        "l_nature_detaillee": l_nature_detaillee,
                        "l_toponyme": l_toponyme,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_params.TablesBdnbRetrieveBatimentGroupeBdtopoZoacParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse,
        )

    def retrieve_batiment_groupe_dvf_open_statistique(
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
    ) -> TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse:
        """
        DonnÃ©es statistiques des mutations issues des valeurs DVF open data Ã
        l'Ã©chelle du bÃ¢timent groupe.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          nb_appartement_mutee: Nombre d'appartements qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_dependance_mutee: Nombre de dÃ©pendances qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode
              de rÃ©fÃ©rence des DVF).

          nb_locaux_mutee: Nombre de locaux qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_locaux_tertiaire_mutee: Nombre de locaux tertiaires qui ont mutÃ©s sur le batiment_groupe (sur la
              pÃ©riode de rÃ©fÃ©rence des DVF).

          nb_maisons_mutee: Nombre de maisons qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_mutation: Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local_max: Prix maximale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_median: Prix mÃ©dian au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_min: Prix minimale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_moyen: Prix moyen au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_max: Prix maximale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_median: Prix mÃ©dian au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_min: Prix minimale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_moyen: Prix moyen au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          select: Filtering Columns

          valeur_fonciere_max: (dv3f) valeur fonciÃ¨re maximale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
              habitable (SHAB)[â‚¬/mÂ²]

          valeur_fonciere_median: Valeur fonciÃ¨re mÃ©diane en euros calculÃ©e sur l'ensemble des mutations qui
              ont eu lieu sur le batiment_groupe.

          valeur_fonciere_min: (dv3f) valeur fonciÃ¨re minimale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
              habitable (SHAB) [â‚¬/mÂ²]

          valeur_fonciere_moyenne: Valeur fonciÃ¨re moyenne en euros calculÃ©e sur l'ensemble des mutations qui ont
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
                    tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_params.TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse,
        )

    def retrieve_batiment_groupe_geospx(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        fiabilite_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeGeospxResponse:
        """
        MÃ©triques du bÃ¢timent par rapport Ã son environnement gÃ©ospatial.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          croisement_geospx_reussi: le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
              considÃ©rÃ©e comme rÃ©ussi

          fiabilite_adresse: FiabilitÃ© des adresses du bÃ¢timent : "vrai" si les Fichiers Fonciers et BDTOpo
              partagent au moins une mÃªme adresse BAN

          fiabilite_emprise_sol: FiabilitÃ© de l'emprise au sol du bÃ¢timent

          fiabilite_hauteur: FiabilitÃ© de la hauteur du bÃ¢timent

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_geospx",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "fiabilite_adresse": fiabilite_adresse,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_geospx_params.TablesBdnbRetrieveBatimentGroupeGeospxParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeGeospxResponse,
        )

    def retrieve_batiment_groupe_qpv(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_quartier: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeQpvResponse:
        """
        Informations sur les Quartiers Prioritaires de la Ville agrÃ©gÃ©es Ã l'Ã©chelle
        du bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          nom_quartier: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_qpv",
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
                        "nom_quartier": nom_quartier,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_qpv_params.TablesBdnbRetrieveBatimentGroupeQpvParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeQpvResponse,
        )

    def retrieve_batiment_groupe_synthese_enveloppe(
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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse:
        """Table de synthÃ¨se des informations sur l'enveloppe du bÃ¢timent.

        Elle contient
        des informations sur les performances Ã©nergÃ©tiques des parois, leurs
        caractÃ©ristiques technique et les types de matÃ©riaux utilisÃ©s. Cette
        premiÃ¨re version ne contient que des informations issues des DPE ou fichiers
        fonciers.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code dÃ©partement INSEE

          epaisseur_isolation_mur_exterieur_estim: epaisseur d'isolation moyenne des murs extÃ©rieurs estimÃ©e Ã partir de la
              diffÃ©rence entre le U de mur et le U de mur nu. Dans le cas d'une Ã©paisseur
              dÃ©clarÃ©e c'est directement l'Ã©paisseur dÃ©clarÃ©e qui est considÃ©rÃ©e, dans
              le cas contraire l'Ã©paisseur est estimÃ©e aussi pour les U conventionels de la
              mÃ©thode 3CL DPE.

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
              DPE.

          epaisseur_structure_mur_exterieur: epaisseur moyenne de la partie structure du mur (sans l'isolation rapportÃ©e ni
              les doublages)

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrÃ©e. coefficient entre 0
              et 1

          l_local_non_chauffe_mur: liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)

          l_local_non_chauffe_plancher_bas: liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)

          l_local_non_chauffe_plancher_haut: liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
              DPE 2021)

          l_orientation_baie_vitree: liste des orientations des baies vitrÃ©es (enum version BDNB)

          l_orientation_mur_exterieur: liste des orientations des murs donnant sur l'extÃ©rieur (enum version BDNB)

          limit: Limiting and Pagination

          local_non_chauffe_principal_mur: liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)

          local_non_chauffe_principal_plancher_bas: liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)

          local_non_chauffe_principal_plancher_haut: liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
              DPE 2021)

          materiaux_structure_mur_exterieur: matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©. Cette
              information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers
              ou DPE pour le moment)

          materiaux_toiture_simplifie: materiaux principal utiliÃ© pour la toiture simplifiÃ©. Cette information peut
              Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          score_fiabilite: score de fiabilitÃ© attribuÃ© aux informations affichÃ©es. En fonction de la
              source principale et du recoupement des informations de plusieurs sources le
              score peut Ãªtre plus ou moins Ã©levÃ©. Le score maximal de confiance est de 10,
              le score minimal de 1. des informations recoupÃ©es par plusieurs sources ont un
              score de confiance plus Ã©levÃ© que des informations fournies par une unique
              source (voir mÃ©thodo)

          select: Filtering Columns

          source_information_principale: base de donnÃ©es source principale d'oÃ¹ est tirÃ©e directement les informations
              sur les systÃ¨mes Ã©nergÃ©tiques du bÃ¢timent. (pour l'instant pas de
              combinaisons de sources voir mÃ©thodo)

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_batiment_dpe: type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble). Cette
              colonne est renseignÃ©e uniquement si la source d'information est un DPE.

          type_fermeture: type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
              vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
              BDNB)

          type_isolation_mur_exterieur: type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
              version BDNB)

          type_isolation_plancher_bas: type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
              version BDNB)

          type_isolation_plancher_haut: type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
              version BDNB)

          type_materiaux_menuiserie: type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
              version BDNB)

          type_plancher_bas_deperditif: materiaux ou principe constructif principal des planchers bas (enum version
              BDNB)

          type_plancher_haut_deperditif: materiaux ou principe constructif principal des planchers hauts (enum version
              BDNB)

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_vitrage: type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
              calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)

          u_plancher_bas_brut_deperditif: Coefficient de transmission thermique moyen des planchers bas brut.

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
              mÃ©thode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          u_porte: Coefficient de transmission thermique moyen des portes (W/mÂ²/K)

          uw: Coefficient de transmission thermique moyen des baies vitrÃ©es sans prise en
              compte des fermeture (W/mÂ²/K)

          vitrage_vir: le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
              rend plus performant d'un point de vue thermique.

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
            "/donnees/batiment_groupe_synthese_enveloppe",
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
                    tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_params.TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse,
        )

    def retrieve_referentiel_administratif_iris(
        self,
        *,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        libelle_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_iris: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveReferentielAdministratifIrisResponse:
        """
        DonnÃ©es sur les IRIS Grande Echelle fournies par l'IGN pour le compte de
        l'INSEE

        Args:
          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_iris: Code iris INSEE

          geom_iris: GÃ©omÃ©trie de l'IRIS

          libelle_iris: LibellÃ© de l'iris

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_iris: Type de l'IRIS

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
            "/donnees/referentiel_administratif_iris",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "geom_iris": geom_iris,
                        "libelle_iris": libelle_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_iris": type_iris,
                    },
                    tables_bdnb_retrieve_referentiel_administratif_iris_params.TablesBdnbRetrieveReferentielAdministratifIrisParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveReferentielAdministratifIrisResponse,
        )

    def retrieve_rel_batiment_construction_adresse(
        self,
        *,
        adresse_principale: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_construction_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentConstructionAdresseResponse:
        """
        Table de relation entre les adresses postales BAN/Arcep et les entrÃ©es de la
        table [batiment_construction]. Pour plus d'informations voir la mÃ©thodologie
        dÃ©taillÃ©e d'association des adresses aux bÃ¢timents, publiÃ©e sur le site de
        la BDNB.

        Args:
          adresse_principale: BoolÃ©en prÃ©cisant si l'adresse courante est l'une des adresses principales de
              la construction ou non. Une relation est taguÃ©e comme `principale` si l'adresse
              qui la compose obtient le score de fiabilitÃ© le plus important parmi toutes les
              adresses desservant une mÃªme construction. Il se peut, par consÃ©quent, qu'une
              construction ait plusieurs adresses principales : toutes celles ayant le score
              de fiabilitÃ© le plus haut pour cette construction.

          batiment_construction_id: Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          distance_batiment_construction_adresse: Distance entre le gÃ©olocalisant adresse et la gÃ©omÃ©trie de bÃ¢timent

          fiabilite: Niveau de fiabilitÃ©

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/rel_batiment_construction_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adresse_principale": adresse_principale,
                        "batiment_construction_id": batiment_construction_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_construction_adresse": distance_batiment_construction_adresse,
                        "fiabilite": fiabilite,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_construction_adresse_params.TablesBdnbRetrieveRelBatimentConstructionAdresseParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentConstructionAdresseResponse,
        )

    def retrieve_rel_batiment_groupe_adresse(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        geom_bat_adresse: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeAdresseResponse:
        """
        Table de relation entre les adresses et les groupes de bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe: Classe de mÃ©thodologie de croisement Ã l'adresse (Fichiers_fonciers, Cadastre)

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          geom_bat_adresse: GÃ©olocalisant du trait reliant le point adresse Ã la gÃ©omÃ©trie du bÃ¢timent
              groupe (Lambert-93, SRID=2154)

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considÃ©rÃ© comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associÃ© Ã
              des fichiers fonciers

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          origine: Origine de l'entrÃ©e bÃ¢timent. Elle provient soit des donnÃ©es fonciÃ¨res
              (Fichiers Fonciers), soit d'un croisement gÃ©ospatial entre le Cadastre, la
              BDTopo et des bases de donnÃ©es mÃ©tiers (ex: BPE ou MÃ©rimÃ©e)

          select: Filtering Columns

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
            "/donnees/rel_batiment_groupe_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe": classe,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "geom_bat_adresse": geom_bat_adresse,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "origine": origine,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_adresse_params.TablesBdnbRetrieveRelBatimentGroupeAdresseParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeAdresseResponse,
        )

    def retrieve_rel_batiment_groupe_proprietaire_siren(
        self,
        *,
        bat_prop_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        is_bailleur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse:
        """
        Table de relation entre les propriÃ©taires et les groupes de bÃ¢timent (la
        version open filtre sur la colonne `dans_majic_pm)

        Args:
          bat_prop_denomination_proprietaire: TODO

          dans_majic_pm: (majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm

          is_bailleur: Vrai si le propriÃ©taire est un bailleur social

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          siren: NumÃ©ro de SIREN de la personne morale (FF)

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
            "/donnees/rel_batiment_groupe_proprietaire_siren",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bat_prop_denomination_proprietaire": bat_prop_denomination_proprietaire,
                        "dans_majic_pm": dans_majic_pm,
                        "is_bailleur": is_bailleur,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "siren": siren,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_params.TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse,
        )

    def retrieve_rel_batiment_groupe_qpv(
        self,
        *,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        qpv_code_qp: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeQpvResponse:
        """
        Table de relation entre les bÃ¢timents de la BDNB et les Ã©lÃ©ments de la table
        QPV

        Args:
          batiment_construction_id: Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          qpv_code_qp: identifiant de la table qpv

          select: Filtering Columns

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
            "/donnees/rel_batiment_groupe_qpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "qpv_code_qp": qpv_code_qp,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_qpv_params.TablesBdnbRetrieveRelBatimentGroupeQpvParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeQpvResponse,
        )


class AsyncTablesBdnbResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesBdnbResourceWithRawResponse:
        return AsyncTablesBdnbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesBdnbResourceWithStreamingResponse:
        return AsyncTablesBdnbResourceWithStreamingResponse(self)

    async def retrieve_batiment_groupe_bdtopo_zoac(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_nature_detaillee: str | NotGiven = NOT_GIVEN,
        l_toponyme: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse:
        """
        Informations de la BDTopo, couche zone d'activitÃ©, agrÃ©gÃ©es Ã l'Ã©chelle du
        bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          l_nature: (ign) CatÃ©gorie de nature du bÃ¢timent

          l_nature_detaillee: (ign) CatÃ©gorie dÃ©taillÃ©e de nature de l'Ã©quipement

          l_toponyme: (ign) Toponymie de l'Ã©quipement

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_bdtopo_zoac",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nature": l_nature,
                        "l_nature_detaillee": l_nature_detaillee,
                        "l_toponyme": l_toponyme,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_bdtopo_zoac_params.TablesBdnbRetrieveBatimentGroupeBdtopoZoacParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse,
        )

    async def retrieve_batiment_groupe_dvf_open_statistique(
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
    ) -> TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse:
        """
        DonnÃ©es statistiques des mutations issues des valeurs DVF open data Ã
        l'Ã©chelle du bÃ¢timent groupe.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          nb_appartement_mutee: Nombre d'appartements qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_dependance_mutee: Nombre de dÃ©pendances qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode
              de rÃ©fÃ©rence des DVF).

          nb_locaux_mutee: Nombre de locaux qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_locaux_tertiaire_mutee: Nombre de locaux tertiaires qui ont mutÃ©s sur le batiment_groupe (sur la
              pÃ©riode de rÃ©fÃ©rence des DVF).

          nb_maisons_mutee: Nombre de maisons qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          nb_mutation: Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la pÃ©riode de
              rÃ©fÃ©rence des DVF).

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local_max: Prix maximale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_median: Prix mÃ©dian au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_min: Prix minimale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_local_moyen: Prix moyen au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_max: Prix maximale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_median: Prix mÃ©dian au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_min: Prix minimale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          prix_m2_terrain_moyen: Prix moyen au m2 de terrain en euros calculÃ© Ã partir des transactions dont
              uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
              collectives + dÃ©pendances) ont mutÃ©es

          select: Filtering Columns

          valeur_fonciere_max: (dv3f) valeur fonciÃ¨re maximale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
              habitable (SHAB)[â‚¬/mÂ²]

          valeur_fonciere_median: Valeur fonciÃ¨re mÃ©diane en euros calculÃ©e sur l'ensemble des mutations qui
              ont eu lieu sur le batiment_groupe.

          valeur_fonciere_min: (dv3f) valeur fonciÃ¨re minimale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
              habitable (SHAB) [â‚¬/mÂ²]

          valeur_fonciere_moyenne: Valeur fonciÃ¨re moyenne en euros calculÃ©e sur l'ensemble des mutations qui ont
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
                    tables_bdnb_retrieve_batiment_groupe_dvf_open_statistique_params.TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse,
        )

    async def retrieve_batiment_groupe_geospx(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        fiabilite_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeGeospxResponse:
        """
        MÃ©triques du bÃ¢timent par rapport Ã son environnement gÃ©ospatial.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          croisement_geospx_reussi: le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
              considÃ©rÃ©e comme rÃ©ussi

          fiabilite_adresse: FiabilitÃ© des adresses du bÃ¢timent : "vrai" si les Fichiers Fonciers et BDTOpo
              partagent au moins une mÃªme adresse BAN

          fiabilite_emprise_sol: FiabilitÃ© de l'emprise au sol du bÃ¢timent

          fiabilite_hauteur: FiabilitÃ© de la hauteur du bÃ¢timent

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_geospx",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "fiabilite_adresse": fiabilite_adresse,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_geospx_params.TablesBdnbRetrieveBatimentGroupeGeospxParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeGeospxResponse,
        )

    async def retrieve_batiment_groupe_qpv(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_quartier: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeQpvResponse:
        """
        Informations sur les Quartiers Prioritaires de la Ville agrÃ©gÃ©es Ã l'Ã©chelle
        du bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          nom_quartier: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_qpv",
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
                        "nom_quartier": nom_quartier,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_batiment_groupe_qpv_params.TablesBdnbRetrieveBatimentGroupeQpvParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeQpvResponse,
        )

    async def retrieve_batiment_groupe_synthese_enveloppe(
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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse:
        """Table de synthÃ¨se des informations sur l'enveloppe du bÃ¢timent.

        Elle contient
        des informations sur les performances Ã©nergÃ©tiques des parois, leurs
        caractÃ©ristiques technique et les types de matÃ©riaux utilisÃ©s. Cette
        premiÃ¨re version ne contient que des informations issues des DPE ou fichiers
        fonciers.

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code dÃ©partement INSEE

          epaisseur_isolation_mur_exterieur_estim: epaisseur d'isolation moyenne des murs extÃ©rieurs estimÃ©e Ã partir de la
              diffÃ©rence entre le U de mur et le U de mur nu. Dans le cas d'une Ã©paisseur
              dÃ©clarÃ©e c'est directement l'Ã©paisseur dÃ©clarÃ©e qui est considÃ©rÃ©e, dans
              le cas contraire l'Ã©paisseur est estimÃ©e aussi pour les U conventionels de la
              mÃ©thode 3CL DPE.

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
              DPE.

          epaisseur_structure_mur_exterieur: epaisseur moyenne de la partie structure du mur (sans l'isolation rapportÃ©e ni
              les doublages)

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrÃ©e. coefficient entre 0
              et 1

          l_local_non_chauffe_mur: liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)

          l_local_non_chauffe_plancher_bas: liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)

          l_local_non_chauffe_plancher_haut: liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
              DPE 2021)

          l_orientation_baie_vitree: liste des orientations des baies vitrÃ©es (enum version BDNB)

          l_orientation_mur_exterieur: liste des orientations des murs donnant sur l'extÃ©rieur (enum version BDNB)

          limit: Limiting and Pagination

          local_non_chauffe_principal_mur: liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)

          local_non_chauffe_principal_plancher_bas: liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)

          local_non_chauffe_principal_plancher_haut: liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
              DPE 2021)

          materiaux_structure_mur_exterieur: matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©. Cette
              information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers
              ou DPE pour le moment)

          materiaux_toiture_simplifie: materiaux principal utiliÃ© pour la toiture simplifiÃ©. Cette information peut
              Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          score_fiabilite: score de fiabilitÃ© attribuÃ© aux informations affichÃ©es. En fonction de la
              source principale et du recoupement des informations de plusieurs sources le
              score peut Ãªtre plus ou moins Ã©levÃ©. Le score maximal de confiance est de 10,
              le score minimal de 1. des informations recoupÃ©es par plusieurs sources ont un
              score de confiance plus Ã©levÃ© que des informations fournies par une unique
              source (voir mÃ©thodo)

          select: Filtering Columns

          source_information_principale: base de donnÃ©es source principale d'oÃ¹ est tirÃ©e directement les informations
              sur les systÃ¨mes Ã©nergÃ©tiques du bÃ¢timent. (pour l'instant pas de
              combinaisons de sources voir mÃ©thodo)

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_batiment_dpe: type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble). Cette
              colonne est renseignÃ©e uniquement si la source d'information est un DPE.

          type_fermeture: type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
              vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
              BDNB)

          type_isolation_mur_exterieur: type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
              version BDNB)

          type_isolation_plancher_bas: type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
              version BDNB)

          type_isolation_plancher_haut: type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
              version BDNB)

          type_materiaux_menuiserie: type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
              version BDNB)

          type_plancher_bas_deperditif: materiaux ou principe constructif principal des planchers bas (enum version
              BDNB)

          type_plancher_haut_deperditif: materiaux ou principe constructif principal des planchers hauts (enum version
              BDNB)

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_vitrage: type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
              calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)

          u_plancher_bas_brut_deperditif: Coefficient de transmission thermique moyen des planchers bas brut.

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
              mÃ©thode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          u_porte: Coefficient de transmission thermique moyen des portes (W/mÂ²/K)

          uw: Coefficient de transmission thermique moyen des baies vitrÃ©es sans prise en
              compte des fermeture (W/mÂ²/K)

          vitrage_vir: le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
              rend plus performant d'un point de vue thermique.

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
            "/donnees/batiment_groupe_synthese_enveloppe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
                    tables_bdnb_retrieve_batiment_groupe_synthese_enveloppe_params.TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse,
        )

    async def retrieve_referentiel_administratif_iris(
        self,
        *,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        libelle_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_iris: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveReferentielAdministratifIrisResponse:
        """
        DonnÃ©es sur les IRIS Grande Echelle fournies par l'IGN pour le compte de
        l'INSEE

        Args:
          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_iris: Code iris INSEE

          geom_iris: GÃ©omÃ©trie de l'IRIS

          libelle_iris: LibellÃ© de l'iris

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_iris: Type de l'IRIS

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
            "/donnees/referentiel_administratif_iris",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "geom_iris": geom_iris,
                        "libelle_iris": libelle_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_iris": type_iris,
                    },
                    tables_bdnb_retrieve_referentiel_administratif_iris_params.TablesBdnbRetrieveReferentielAdministratifIrisParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveReferentielAdministratifIrisResponse,
        )

    async def retrieve_rel_batiment_construction_adresse(
        self,
        *,
        adresse_principale: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_construction_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentConstructionAdresseResponse:
        """
        Table de relation entre les adresses postales BAN/Arcep et les entrÃ©es de la
        table [batiment_construction]. Pour plus d'informations voir la mÃ©thodologie
        dÃ©taillÃ©e d'association des adresses aux bÃ¢timents, publiÃ©e sur le site de
        la BDNB.

        Args:
          adresse_principale: BoolÃ©en prÃ©cisant si l'adresse courante est l'une des adresses principales de
              la construction ou non. Une relation est taguÃ©e comme `principale` si l'adresse
              qui la compose obtient le score de fiabilitÃ© le plus important parmi toutes les
              adresses desservant une mÃªme construction. Il se peut, par consÃ©quent, qu'une
              construction ait plusieurs adresses principales : toutes celles ayant le score
              de fiabilitÃ© le plus haut pour cette construction.

          batiment_construction_id: Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          distance_batiment_construction_adresse: Distance entre le gÃ©olocalisant adresse et la gÃ©omÃ©trie de bÃ¢timent

          fiabilite: Niveau de fiabilitÃ©

          limit: Limiting and Pagination

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/rel_batiment_construction_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "adresse_principale": adresse_principale,
                        "batiment_construction_id": batiment_construction_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_construction_adresse": distance_batiment_construction_adresse,
                        "fiabilite": fiabilite,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_construction_adresse_params.TablesBdnbRetrieveRelBatimentConstructionAdresseParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentConstructionAdresseResponse,
        )

    async def retrieve_rel_batiment_groupe_adresse(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        geom_bat_adresse: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeAdresseResponse:
        """
        Table de relation entre les adresses et les groupes de bÃ¢timent

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe: Classe de mÃ©thodologie de croisement Ã l'adresse (Fichiers_fonciers, Cadastre)

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          geom_bat_adresse: GÃ©olocalisant du trait reliant le point adresse Ã la gÃ©omÃ©trie du bÃ¢timent
              groupe (Lambert-93, SRID=2154)

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considÃ©rÃ© comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associÃ© Ã
              des fichiers fonciers

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          origine: Origine de l'entrÃ©e bÃ¢timent. Elle provient soit des donnÃ©es fonciÃ¨res
              (Fichiers Fonciers), soit d'un croisement gÃ©ospatial entre le Cadastre, la
              BDTopo et des bases de donnÃ©es mÃ©tiers (ex: BPE ou MÃ©rimÃ©e)

          select: Filtering Columns

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
            "/donnees/rel_batiment_groupe_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe": classe,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "geom_bat_adresse": geom_bat_adresse,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "origine": origine,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_adresse_params.TablesBdnbRetrieveRelBatimentGroupeAdresseParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeAdresseResponse,
        )

    async def retrieve_rel_batiment_groupe_proprietaire_siren(
        self,
        *,
        bat_prop_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        is_bailleur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse:
        """
        Table de relation entre les propriÃ©taires et les groupes de bÃ¢timent (la
        version open filtre sur la colonne `dans_majic_pm)

        Args:
          bat_prop_denomination_proprietaire: TODO

          dans_majic_pm: (majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm

          is_bailleur: Vrai si le propriÃ©taire est un bailleur social

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          siren: NumÃ©ro de SIREN de la personne morale (FF)

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
            "/donnees/rel_batiment_groupe_proprietaire_siren",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bat_prop_denomination_proprietaire": bat_prop_denomination_proprietaire,
                        "dans_majic_pm": dans_majic_pm,
                        "is_bailleur": is_bailleur,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "siren": siren,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_proprietaire_siren_params.TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse,
        )

    async def retrieve_rel_batiment_groupe_qpv(
        self,
        *,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        qpv_code_qp: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TablesBdnbRetrieveRelBatimentGroupeQpvResponse:
        """
        Table de relation entre les bÃ¢timents de la BDNB et les Ã©lÃ©ments de la table
        QPV

        Args:
          batiment_construction_id: Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          qpv_code_qp: identifiant de la table qpv

          select: Filtering Columns

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
            "/donnees/rel_batiment_groupe_qpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "qpv_code_qp": qpv_code_qp,
                        "select": select,
                    },
                    tables_bdnb_retrieve_rel_batiment_groupe_qpv_params.TablesBdnbRetrieveRelBatimentGroupeQpvParams,
                ),
            ),
            cast_to=TablesBdnbRetrieveRelBatimentGroupeQpvResponse,
        )


class TablesBdnbResourceWithRawResponse:
    def __init__(self, tables_bdnb: TablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

        self.retrieve_batiment_groupe_bdtopo_zoac = to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac,
        )
        self.retrieve_batiment_groupe_dvf_open_statistique = to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique,
        )
        self.retrieve_batiment_groupe_geospx = to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_geospx,
        )
        self.retrieve_batiment_groupe_qpv = to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_qpv,
        )
        self.retrieve_batiment_groupe_synthese_enveloppe = to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe,
        )
        self.retrieve_referentiel_administratif_iris = to_raw_response_wrapper(
            tables_bdnb.retrieve_referentiel_administratif_iris,
        )
        self.retrieve_rel_batiment_construction_adresse = to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_construction_adresse,
        )
        self.retrieve_rel_batiment_groupe_adresse = to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_adresse,
        )
        self.retrieve_rel_batiment_groupe_proprietaire_siren = to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren,
        )
        self.retrieve_rel_batiment_groupe_qpv = to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_qpv,
        )


class AsyncTablesBdnbResourceWithRawResponse:
    def __init__(self, tables_bdnb: AsyncTablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

        self.retrieve_batiment_groupe_bdtopo_zoac = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac,
        )
        self.retrieve_batiment_groupe_dvf_open_statistique = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique,
        )
        self.retrieve_batiment_groupe_geospx = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_geospx,
        )
        self.retrieve_batiment_groupe_qpv = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_qpv,
        )
        self.retrieve_batiment_groupe_synthese_enveloppe = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe,
        )
        self.retrieve_referentiel_administratif_iris = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_referentiel_administratif_iris,
        )
        self.retrieve_rel_batiment_construction_adresse = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_construction_adresse,
        )
        self.retrieve_rel_batiment_groupe_adresse = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_adresse,
        )
        self.retrieve_rel_batiment_groupe_proprietaire_siren = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren,
        )
        self.retrieve_rel_batiment_groupe_qpv = async_to_raw_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_qpv,
        )


class TablesBdnbResourceWithStreamingResponse:
    def __init__(self, tables_bdnb: TablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

        self.retrieve_batiment_groupe_bdtopo_zoac = to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac,
        )
        self.retrieve_batiment_groupe_dvf_open_statistique = to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique,
        )
        self.retrieve_batiment_groupe_geospx = to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_geospx,
        )
        self.retrieve_batiment_groupe_qpv = to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_qpv,
        )
        self.retrieve_batiment_groupe_synthese_enveloppe = to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe,
        )
        self.retrieve_referentiel_administratif_iris = to_streamed_response_wrapper(
            tables_bdnb.retrieve_referentiel_administratif_iris,
        )
        self.retrieve_rel_batiment_construction_adresse = to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_construction_adresse,
        )
        self.retrieve_rel_batiment_groupe_adresse = to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_adresse,
        )
        self.retrieve_rel_batiment_groupe_proprietaire_siren = to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren,
        )
        self.retrieve_rel_batiment_groupe_qpv = to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_qpv,
        )


class AsyncTablesBdnbResourceWithStreamingResponse:
    def __init__(self, tables_bdnb: AsyncTablesBdnbResource) -> None:
        self._tables_bdnb = tables_bdnb

        self.retrieve_batiment_groupe_bdtopo_zoac = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac,
        )
        self.retrieve_batiment_groupe_dvf_open_statistique = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique,
        )
        self.retrieve_batiment_groupe_geospx = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_geospx,
        )
        self.retrieve_batiment_groupe_qpv = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_qpv,
        )
        self.retrieve_batiment_groupe_synthese_enveloppe = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe,
        )
        self.retrieve_referentiel_administratif_iris = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_referentiel_administratif_iris,
        )
        self.retrieve_rel_batiment_construction_adresse = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_construction_adresse,
        )
        self.retrieve_rel_batiment_groupe_adresse = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_adresse,
        )
        self.retrieve_rel_batiment_groupe_proprietaire_siren = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren,
        )
        self.retrieve_rel_batiment_groupe_qpv = async_to_streamed_response_wrapper(
            tables_bdnb.retrieve_rel_batiment_groupe_qpv,
        )
