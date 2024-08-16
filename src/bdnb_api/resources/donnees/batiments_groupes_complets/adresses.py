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
from ....types.donnees.batiments_groupes_complets import adress_list_params
from ....types.donnees.batiments_groupes_complets.adress_list_response import AdressListResponse

__all__ = ["AdressesResource", "AsyncAdressesResource"]


class AdressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdressesResourceWithRawResponse:
        return AdressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdressesResourceWithStreamingResponse:
        return AdressesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        alea_argiles: str | NotGiven = NOT_GIVEN,
        alea_radon: str | NotGiven = NOT_GIVEN,
        altitude_sol_mean: str | NotGiven = NOT_GIVEN,
        annee_construction: str | NotGiven = NOT_GIVEN,
        arrete_2021: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        chauffage_solaire: str | NotGiven = NOT_GIVEN,
        classe_bilan_dpe: str | NotGiven = NOT_GIVEN,
        classe_conso_energie_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        cle_interop_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        conso_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ep_m2: str | NotGiven = NOT_GIVEN,
        conso_pro_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        conso_pro_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        conso_res_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        conso_res_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        date_reception_dpe: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        ecs_solaire: str | NotGiven = NOT_GIVEN,
        emission_ges_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        emission_ges_5_usages_m2: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_synthese_particulier_simple: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_synthese_particulier_source: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_1: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_2: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        gisement_gain_conso_finale_total: str | NotGiven = NOT_GIVEN,
        gisement_gain_energetique_mean: str | NotGiven = NOT_GIVEN,
        gisement_gain_ges_mean: str | NotGiven = NOT_GIVEN,
        hauteur_mean: str | NotGiven = NOT_GIVEN,
        identifiant_dpe: str | NotGiven = NOT_GIVEN,
        l_cle_interop_adr: str | NotGiven = NOT_GIVEN,
        l_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        l_libelle_adr: str | NotGiven = NOT_GIVEN,
        l_orientation_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_parcelle_id: str | NotGiven = NOT_GIVEN,
        l_siren: str | NotGiven = NOT_GIVEN,
        l_type_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        l_type_generateur_ecs: str | NotGiven = NOT_GIVEN,
        libelle_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        mat_mur_txt: str | NotGiven = NOT_GIVEN,
        mat_toit_txt: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur_simplifie: str | NotGiven = NOT_GIVEN,
        materiaux_toiture_simplifie: str | NotGiven = NOT_GIVEN,
        nb_adresse_valid_ban: str | NotGiven = NOT_GIVEN,
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
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_log_rnc: str | NotGiven = NOT_GIVEN,
        nb_lot_garpark_rnc: str | NotGiven = NOT_GIVEN,
        nb_lot_tertiaire_rnc: str | NotGiven = NOT_GIVEN,
        nb_niveau: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_res_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_res_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        nom_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        nom_quartier_qpv: str | NotGiven = NOT_GIVEN,
        numero_immat_principal: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_emprise_sol: str | NotGiven = NOT_GIVEN,
        surface_facade_ext: str | NotGiven = NOT_GIVEN,
        surface_facade_mitoyenne: str | NotGiven = NOT_GIVEN,
        surface_facade_totale: str | NotGiven = NOT_GIVEN,
        surface_facade_vitree: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_dpe: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_fermeture: str | NotGiven = NOT_GIVEN,
        type_gaz_lame: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_anciennete: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_anciennete_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_climatisation: str | NotGiven = NOT_GIVEN,
        type_generateur_climatisation_anciennete: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs_anciennete: str | NotGiven = NOT_GIVEN,
        type_installation_chauffage: str | NotGiven = NOT_GIVEN,
        type_installation_ecs: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_production_energie_renouvelable: str | NotGiven = NOT_GIVEN,
        type_ventilation: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        vitrage_vir: str | NotGiven = NOT_GIVEN,
        volume_brut: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdressListResponse:
        """
        Jointure des tables métiers avec la table batiment_groupe

        Args:
          arrete_2021: précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
              du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
              de 2012.

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_bilan_dpe: Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
              primaire et les émissions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_conso_energie_arrete_2012: classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          cle_interop_adr_principale_ban: Clé d'interopérabilité de l'adresse principale (issue de la BAN)

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
              de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          conso_pro_dle_elec_2020: Consommation professionnelle électrique [kWh/an]

          conso_pro_dle_gaz_2020: Consommation professionnelle gaz [kWh/an]

          conso_res_dle_elec_2020: Consommation résidentielle électrique [kWh/an]

          conso_res_dle_gaz_2020: Consommation résidentielle gaz [kWh/an]

          date_reception_dpe: date de réception du DPE dans la base de données de l'ADEME

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
              Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
              autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
              valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
              2021 (en vigueur actuellement)

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
              DPE.

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rénovation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rénovation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rénovation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations énergétiques finales après un
              scénario de rénovation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule après rénovation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule après rénovation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
              probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
              5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment

          etiquette_dpe_initial_map_2nd: 2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment. Si
              le champs vaut F-G alors F la première étiquette est l'étiquette la plus
              probable , G la seconde étiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité pour l'état actuel du bâtiment. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
              ou G.

          etiquette_dpe_renove_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
              un scénario de rénovation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de système énergétique de chauffage) [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          etiquette_dpe_synthese_particulier_simple: Etiquette DPE selon l'arràªté 2021. Si un DPE existe, l'étiquette provient d'un
              DPE de l'AEDME, sinon, il s'agit d'une simulation.

          etiquette_dpe_synthese_particulier_source: TODO

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrée. coefficient entre 0
              et 1

          gisement_gain_conso_finale_total: (cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)

          gisement_gain_energetique_mean: (cstb) Estilation du gain énergétique moyen (kWh/m2/an)

          gisement_gain_ges_mean: (cstb) Estimation du gain de ges moyen (kgCO2/m2/an)

          identifiant_dpe: identifiant de la table des DPE ademe

          l_cle_interop_adr: Liste de clés d'interopérabilité de l'adresse postale

          l_denomination_proprietaire: Liste de dénominations de propriétaires

          l_libelle_adr: Liste de libellé complet de l'adresse

          l_orientation_baie_vitree: liste des orientations des baies vitrées (enum version BDNB)

          l_parcelle_id: Liste d'identifiants de parcelle (Concaténation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          l_siren: Liste d'identifiants siren

          libelle_adr_principale_ban: Libellé complet de l'adresse principale (issue de la BAN)

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
              des fichiers fonciers

          limit: Limiting and Pagination

          materiaux_structure_mur_exterieur: matériaux ou principe constructif principal utilisé pour les murs extérieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utilié pour les murs extérieur simplifié. Cette information
              peut àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          nb_adresse_valid_ban: Nombre d'adresses valides différentes provenant de la BAN qui desservent le
              groupe de bâtiment

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

          nb_log: (rnc) Nombre de logements

          nb_niveau: (ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)

          nb_pdl_pro_dle_elec_2020: Nombre de points de livraison électrique professionnels [kWh/an]

          nb_pdl_pro_dle_gaz_2020: Nombre de points de livraison gaz professionnels [kWh/an]

          nb_pdl_res_dle_elec_2020: Nombre de points de livraison électrique résidentiels [kWh/an]

          nb_pdl_res_dle_gaz_2020: Nombre de points de livraison gaz résidentiels [kWh/an]

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          select: Filtering Columns

          surface_emprise_sol: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          surface_facade_ext: Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faà§ade vitrée [mÂ²]

          traversant: indicateur du cà´té traversant du logement.

          type_dpe: type de DPE. Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son
              objet (logement, immeuble de logement, tertiaire) et la méthode de calcul
              utilisé (3CL conventionel,facture ou RT2012/RE2020)

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

          type_vitrage: type de vitrage principal des baies vitrées du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrées en incluant le
              calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
              méthode 3CL(W/mÂ²/K)

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          vitrage_vir: le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
              plus performant d'un point de vue thermique.

          volume_brut: Volume brut du bâtiment [m3]

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
            "/donnees/batiment_groupe_complet/adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "alea_argiles": alea_argiles,
                        "alea_radon": alea_radon,
                        "altitude_sol_mean": altitude_sol_mean,
                        "annee_construction": annee_construction,
                        "arrete_2021": arrete_2021,
                        "batiment_groupe_id": batiment_groupe_id,
                        "chauffage_solaire": chauffage_solaire,
                        "classe_bilan_dpe": classe_bilan_dpe,
                        "classe_conso_energie_arrete_2012": classe_conso_energie_arrete_2012,
                        "classe_inertie": classe_inertie,
                        "cle_interop_adr": cle_interop_adr,
                        "cle_interop_adr_principale_ban": cle_interop_adr_principale_ban,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "conso_3_usages_ep_m2_arrete_2012": conso_3_usages_ep_m2_arrete_2012,
                        "conso_5_usages_ep_m2": conso_5_usages_ep_m2,
                        "conso_pro_dle_elec_2020": conso_pro_dle_elec_2020,
                        "conso_pro_dle_gaz_2020": conso_pro_dle_gaz_2020,
                        "conso_res_dle_elec_2020": conso_res_dle_elec_2020,
                        "conso_res_dle_gaz_2020": conso_res_dle_gaz_2020,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "date_reception_dpe": date_reception_dpe,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "distance_batiment_historique_plus_proche": distance_batiment_historique_plus_proche,
                        "ecs_solaire": ecs_solaire,
                        "emission_ges_3_usages_ep_m2_arrete_2012": emission_ges_3_usages_ep_m2_arrete_2012,
                        "emission_ges_5_usages_m2": emission_ges_5_usages_m2,
                        "epaisseur_lame": epaisseur_lame,
                        "etat_initial_consommation_energie_estim_inc": etat_initial_consommation_energie_estim_inc,
                        "etat_initial_consommation_energie_estim_lower": etat_initial_consommation_energie_estim_lower,
                        "etat_initial_consommation_energie_estim_mean": etat_initial_consommation_energie_estim_mean,
                        "etat_initial_consommation_energie_estim_upper": etat_initial_consommation_energie_estim_upper,
                        "etat_initial_consommation_energie_primaire_estim_lower": etat_initial_consommation_energie_primaire_estim_lower,
                        "etat_initial_consommation_energie_primaire_estim_mean": etat_initial_consommation_energie_primaire_estim_mean,
                        "etat_initial_consommation_energie_primaire_estim_upper": etat_initial_consommation_energie_primaire_estim_upper,
                        "etat_initial_consommation_ges_estim_inc": etat_initial_consommation_ges_estim_inc,
                        "etat_initial_ges_estim_lower": etat_initial_ges_estim_lower,
                        "etat_initial_ges_estim_mean": etat_initial_ges_estim_mean,
                        "etat_initial_ges_estim_upper": etat_initial_ges_estim_upper,
                        "etat_initial_risque_canicule": etat_initial_risque_canicule,
                        "etat_initial_risque_canicule_inc": etat_initial_risque_canicule_inc,
                        "etat_renove_consommation_energie_estim_inc": etat_renove_consommation_energie_estim_inc,
                        "etat_renove_consommation_energie_estim_lower": etat_renove_consommation_energie_estim_lower,
                        "etat_renove_consommation_energie_estim_mean": etat_renove_consommation_energie_estim_mean,
                        "etat_renove_consommation_energie_estim_upper": etat_renove_consommation_energie_estim_upper,
                        "etat_renove_consommation_energie_primaire_estim_lower": etat_renove_consommation_energie_primaire_estim_lower,
                        "etat_renove_consommation_energie_primaire_estim_mean": etat_renove_consommation_energie_primaire_estim_mean,
                        "etat_renove_consommation_energie_primaire_estim_upper": etat_renove_consommation_energie_primaire_estim_upper,
                        "etat_renove_consommation_ges_estim_inc": etat_renove_consommation_ges_estim_inc,
                        "etat_renove_ges_estim_lower": etat_renove_ges_estim_lower,
                        "etat_renove_ges_estim_mean": etat_renove_ges_estim_mean,
                        "etat_renove_ges_estim_upper": etat_renove_ges_estim_upper,
                        "etat_renove_risque_canicule": etat_renove_risque_canicule,
                        "etat_renove_risque_canicule_inc": etat_renove_risque_canicule_inc,
                        "etiquette_dpe_initial_a": etiquette_dpe_initial_a,
                        "etiquette_dpe_initial_b": etiquette_dpe_initial_b,
                        "etiquette_dpe_initial_c": etiquette_dpe_initial_c,
                        "etiquette_dpe_initial_d": etiquette_dpe_initial_d,
                        "etiquette_dpe_initial_e": etiquette_dpe_initial_e,
                        "etiquette_dpe_initial_f": etiquette_dpe_initial_f,
                        "etiquette_dpe_initial_g": etiquette_dpe_initial_g,
                        "etiquette_dpe_initial_inc": etiquette_dpe_initial_inc,
                        "etiquette_dpe_initial_map": etiquette_dpe_initial_map,
                        "etiquette_dpe_initial_map_2nd": etiquette_dpe_initial_map_2nd,
                        "etiquette_dpe_initial_map_2nd_prob": etiquette_dpe_initial_map_2nd_prob,
                        "etiquette_dpe_renove_a": etiquette_dpe_renove_a,
                        "etiquette_dpe_renove_b": etiquette_dpe_renove_b,
                        "etiquette_dpe_renove_c": etiquette_dpe_renove_c,
                        "etiquette_dpe_renove_d": etiquette_dpe_renove_d,
                        "etiquette_dpe_renove_e": etiquette_dpe_renove_e,
                        "etiquette_dpe_renove_f": etiquette_dpe_renove_f,
                        "etiquette_dpe_renove_g": etiquette_dpe_renove_g,
                        "etiquette_dpe_renove_inc": etiquette_dpe_renove_inc,
                        "etiquette_dpe_renove_map": etiquette_dpe_renove_map,
                        "etiquette_dpe_renove_map_2nd": etiquette_dpe_renove_map_2nd,
                        "etiquette_dpe_renove_map_2nd_prob": etiquette_dpe_renove_map_2nd_prob,
                        "etiquette_dpe_synthese_particulier_simple": etiquette_dpe_synthese_particulier_simple,
                        "etiquette_dpe_synthese_particulier_source": etiquette_dpe_synthese_particulier_source,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "fiabilite_cr_adr_niv_1": fiabilite_cr_adr_niv_1,
                        "fiabilite_cr_adr_niv_2": fiabilite_cr_adr_niv_2,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "geom_groupe": geom_groupe,
                        "gisement_gain_conso_finale_total": gisement_gain_conso_finale_total,
                        "gisement_gain_energetique_mean": gisement_gain_energetique_mean,
                        "gisement_gain_ges_mean": gisement_gain_ges_mean,
                        "hauteur_mean": hauteur_mean,
                        "identifiant_dpe": identifiant_dpe,
                        "l_cle_interop_adr": l_cle_interop_adr,
                        "l_denomination_proprietaire": l_denomination_proprietaire,
                        "l_libelle_adr": l_libelle_adr,
                        "l_orientation_baie_vitree": l_orientation_baie_vitree,
                        "l_parcelle_id": l_parcelle_id,
                        "l_siren": l_siren,
                        "l_type_generateur_chauffage": l_type_generateur_chauffage,
                        "l_type_generateur_ecs": l_type_generateur_ecs,
                        "libelle_adr_principale_ban": libelle_adr_principale_ban,
                        "libelle_commune_insee": libelle_commune_insee,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "mat_mur_txt": mat_mur_txt,
                        "mat_toit_txt": mat_toit_txt,
                        "materiaux_structure_mur_exterieur": materiaux_structure_mur_exterieur,
                        "materiaux_structure_mur_exterieur_simplifie": materiaux_structure_mur_exterieur_simplifie,
                        "materiaux_toiture_simplifie": materiaux_toiture_simplifie,
                        "nb_adresse_valid_ban": nb_adresse_valid_ban,
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
                        "nb_log": nb_log,
                        "nb_log_rnc": nb_log_rnc,
                        "nb_lot_garpark_rnc": nb_lot_garpark_rnc,
                        "nb_lot_tertiaire_rnc": nb_lot_tertiaire_rnc,
                        "nb_niveau": nb_niveau,
                        "nb_pdl_pro_dle_elec_2020": nb_pdl_pro_dle_elec_2020,
                        "nb_pdl_pro_dle_gaz_2020": nb_pdl_pro_dle_gaz_2020,
                        "nb_pdl_res_dle_elec_2020": nb_pdl_res_dle_elec_2020,
                        "nb_pdl_res_dle_gaz_2020": nb_pdl_res_dle_gaz_2020,
                        "nom_batiment_historique_plus_proche": nom_batiment_historique_plus_proche,
                        "nom_qp": nom_qp,
                        "nom_quartier_qpv": nom_quartier_qpv,
                        "numero_immat_principal": numero_immat_principal,
                        "offset": offset,
                        "order": order,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                        "surface_emprise_sol": surface_emprise_sol,
                        "surface_facade_ext": surface_facade_ext,
                        "surface_facade_mitoyenne": surface_facade_mitoyenne,
                        "surface_facade_totale": surface_facade_totale,
                        "surface_facade_vitree": surface_facade_vitree,
                        "traversant": traversant,
                        "type_dpe": type_dpe,
                        "type_energie_chauffage": type_energie_chauffage,
                        "type_energie_chauffage_appoint": type_energie_chauffage_appoint,
                        "type_fermeture": type_fermeture,
                        "type_gaz_lame": type_gaz_lame,
                        "type_generateur_chauffage": type_generateur_chauffage,
                        "type_generateur_chauffage_anciennete": type_generateur_chauffage_anciennete,
                        "type_generateur_chauffage_anciennete_appoint": type_generateur_chauffage_anciennete_appoint,
                        "type_generateur_chauffage_appoint": type_generateur_chauffage_appoint,
                        "type_generateur_climatisation": type_generateur_climatisation,
                        "type_generateur_climatisation_anciennete": type_generateur_climatisation_anciennete,
                        "type_generateur_ecs": type_generateur_ecs,
                        "type_generateur_ecs_anciennete": type_generateur_ecs_anciennete,
                        "type_installation_chauffage": type_installation_chauffage,
                        "type_installation_ecs": type_installation_ecs,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_production_energie_renouvelable": type_production_energie_renouvelable,
                        "type_ventilation": type_ventilation,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "vitrage_vir": vitrage_vir,
                        "volume_brut": volume_brut,
                    },
                    adress_list_params.AdressListParams,
                ),
            ),
            cast_to=AdressListResponse,
        )


class AsyncAdressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdressesResourceWithRawResponse:
        return AsyncAdressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdressesResourceWithStreamingResponse:
        return AsyncAdressesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        alea_argiles: str | NotGiven = NOT_GIVEN,
        alea_radon: str | NotGiven = NOT_GIVEN,
        altitude_sol_mean: str | NotGiven = NOT_GIVEN,
        annee_construction: str | NotGiven = NOT_GIVEN,
        arrete_2021: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        chauffage_solaire: str | NotGiven = NOT_GIVEN,
        classe_bilan_dpe: str | NotGiven = NOT_GIVEN,
        classe_conso_energie_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        cle_interop_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        code_qp: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        conso_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ep_m2: str | NotGiven = NOT_GIVEN,
        conso_pro_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        conso_pro_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        conso_res_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        conso_res_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        contient_fictive_geom_groupe: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        date_reception_dpe: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        ecs_solaire: str | NotGiven = NOT_GIVEN,
        emission_ges_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        emission_ges_5_usages_m2: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_synthese_particulier_simple: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_synthese_particulier_source: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_1: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_2: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        geom_groupe: str | NotGiven = NOT_GIVEN,
        gisement_gain_conso_finale_total: str | NotGiven = NOT_GIVEN,
        gisement_gain_energetique_mean: str | NotGiven = NOT_GIVEN,
        gisement_gain_ges_mean: str | NotGiven = NOT_GIVEN,
        hauteur_mean: str | NotGiven = NOT_GIVEN,
        identifiant_dpe: str | NotGiven = NOT_GIVEN,
        l_cle_interop_adr: str | NotGiven = NOT_GIVEN,
        l_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        l_libelle_adr: str | NotGiven = NOT_GIVEN,
        l_orientation_baie_vitree: str | NotGiven = NOT_GIVEN,
        l_parcelle_id: str | NotGiven = NOT_GIVEN,
        l_siren: str | NotGiven = NOT_GIVEN,
        l_type_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        l_type_generateur_ecs: str | NotGiven = NOT_GIVEN,
        libelle_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        libelle_commune_insee: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        mat_mur_txt: str | NotGiven = NOT_GIVEN,
        mat_toit_txt: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        materiaux_structure_mur_exterieur_simplifie: str | NotGiven = NOT_GIVEN,
        materiaux_toiture_simplifie: str | NotGiven = NOT_GIVEN,
        nb_adresse_valid_ban: str | NotGiven = NOT_GIVEN,
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
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_log_rnc: str | NotGiven = NOT_GIVEN,
        nb_lot_garpark_rnc: str | NotGiven = NOT_GIVEN,
        nb_lot_tertiaire_rnc: str | NotGiven = NOT_GIVEN,
        nb_niveau: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_res_dle_elec_2020: str | NotGiven = NOT_GIVEN,
        nb_pdl_res_dle_gaz_2020: str | NotGiven = NOT_GIVEN,
        nom_batiment_historique_plus_proche: str | NotGiven = NOT_GIVEN,
        nom_qp: str | NotGiven = NOT_GIVEN,
        nom_quartier_qpv: str | NotGiven = NOT_GIVEN,
        numero_immat_principal: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        quartier_prioritaire: str | NotGiven = NOT_GIVEN,
        s_geom_groupe: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_emprise_sol: str | NotGiven = NOT_GIVEN,
        surface_facade_ext: str | NotGiven = NOT_GIVEN,
        surface_facade_mitoyenne: str | NotGiven = NOT_GIVEN,
        surface_facade_totale: str | NotGiven = NOT_GIVEN,
        surface_facade_vitree: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_dpe: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_fermeture: str | NotGiven = NOT_GIVEN,
        type_gaz_lame: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_anciennete: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_anciennete_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_climatisation: str | NotGiven = NOT_GIVEN,
        type_generateur_climatisation_anciennete: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs_anciennete: str | NotGiven = NOT_GIVEN,
        type_installation_chauffage: str | NotGiven = NOT_GIVEN,
        type_installation_ecs: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_production_energie_renouvelable: str | NotGiven = NOT_GIVEN,
        type_ventilation: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        vitrage_vir: str | NotGiven = NOT_GIVEN,
        volume_brut: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdressListResponse:
        """
        Jointure des tables métiers avec la table batiment_groupe

        Args:
          arrete_2021: précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
              du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
              de 2012.

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_bilan_dpe: Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
              primaire et les émissions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_conso_energie_arrete_2012: classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          cle_interop_adr_principale_ban: Clé d'interopérabilité de l'adresse principale (issue de la BAN)

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code région INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
              de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          conso_pro_dle_elec_2020: Consommation professionnelle électrique [kWh/an]

          conso_pro_dle_gaz_2020: Consommation professionnelle gaz [kWh/an]

          conso_res_dle_elec_2020: Consommation résidentielle électrique [kWh/an]

          conso_res_dle_gaz_2020: Consommation résidentielle gaz [kWh/an]

          date_reception_dpe: date de réception du DPE dans la base de données de l'ADEME

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
              Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
              autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
              valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
              2021 (en vigueur actuellement)

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
              DPE.

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rénovation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rénovation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rénovation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations énergétiques finales après un
              scénario de rénovation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule après rénovation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule après rénovation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
              probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
              5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment

          etiquette_dpe_initial_map_2nd: 2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment. Si
              le champs vaut F-G alors F la première étiquette est l'étiquette la plus
              probable , G la seconde étiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité pour l'état actuel du bâtiment. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
              ou G.

          etiquette_dpe_renove_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
              un scénario de rénovation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de système énergétique de chauffage) [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          etiquette_dpe_synthese_particulier_simple: Etiquette DPE selon l'arràªté 2021. Si un DPE existe, l'étiquette provient d'un
              DPE de l'AEDME, sinon, il s'agit d'une simulation.

          etiquette_dpe_synthese_particulier_source: TODO

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrée. coefficient entre 0
              et 1

          gisement_gain_conso_finale_total: (cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)

          gisement_gain_energetique_mean: (cstb) Estilation du gain énergétique moyen (kWh/m2/an)

          gisement_gain_ges_mean: (cstb) Estimation du gain de ges moyen (kgCO2/m2/an)

          identifiant_dpe: identifiant de la table des DPE ademe

          l_cle_interop_adr: Liste de clés d'interopérabilité de l'adresse postale

          l_denomination_proprietaire: Liste de dénominations de propriétaires

          l_libelle_adr: Liste de libellé complet de l'adresse

          l_orientation_baie_vitree: liste des orientations des baies vitrées (enum version BDNB)

          l_parcelle_id: Liste d'identifiants de parcelle (Concaténation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          l_siren: Liste d'identifiants siren

          libelle_adr_principale_ban: Libellé complet de l'adresse principale (issue de la BAN)

          libelle_commune_insee: (insee) Libellé de la commune accueillant le groupe de bâtiment

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
              des fichiers fonciers

          limit: Limiting and Pagination

          materiaux_structure_mur_exterieur: matériaux ou principe constructif principal utilisé pour les murs extérieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utilié pour les murs extérieur simplifié. Cette information
              peut àªtre récupérée de différentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          nb_adresse_valid_ban: Nombre d'adresses valides différentes provenant de la BAN qui desservent le
              groupe de bâtiment

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

          nb_log: (rnc) Nombre de logements

          nb_niveau: (ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)

          nb_pdl_pro_dle_elec_2020: Nombre de points de livraison électrique professionnels [kWh/an]

          nb_pdl_pro_dle_gaz_2020: Nombre de points de livraison gaz professionnels [kWh/an]

          nb_pdl_res_dle_elec_2020: Nombre de points de livraison électrique résidentiels [kWh/an]

          nb_pdl_res_dle_gaz_2020: Nombre de points de livraison gaz résidentiels [kWh/an]

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bâtiment

          offset: Limiting and Pagination

          order: Ordering

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          quartier_prioritaire: Est situé dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          select: Filtering Columns

          surface_emprise_sol: Surface au sol de la géométrie du bâtiment groupe (geom_groupe)

          surface_facade_ext: Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faà§ade vitrée [mÂ²]

          traversant: indicateur du cà´té traversant du logement.

          type_dpe: type de DPE. Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son
              objet (logement, immeuble de logement, tertiaire) et la méthode de calcul
              utilisé (3CL conventionel,facture ou RT2012/RE2020)

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

          type_vitrage: type de vitrage principal des baies vitrées du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrées en incluant le
              calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
              méthode 3CL(W/mÂ²/K)

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          vitrage_vir: le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
              plus performant d'un point de vue thermique.

          volume_brut: Volume brut du bâtiment [m3]

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
            "/donnees/batiment_groupe_complet/adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "alea_argiles": alea_argiles,
                        "alea_radon": alea_radon,
                        "altitude_sol_mean": altitude_sol_mean,
                        "annee_construction": annee_construction,
                        "arrete_2021": arrete_2021,
                        "batiment_groupe_id": batiment_groupe_id,
                        "chauffage_solaire": chauffage_solaire,
                        "classe_bilan_dpe": classe_bilan_dpe,
                        "classe_conso_energie_arrete_2012": classe_conso_energie_arrete_2012,
                        "classe_inertie": classe_inertie,
                        "cle_interop_adr": cle_interop_adr,
                        "cle_interop_adr_principale_ban": cle_interop_adr_principale_ban,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_epci_insee": code_epci_insee,
                        "code_iris": code_iris,
                        "code_qp": code_qp,
                        "code_region_insee": code_region_insee,
                        "conso_3_usages_ep_m2_arrete_2012": conso_3_usages_ep_m2_arrete_2012,
                        "conso_5_usages_ep_m2": conso_5_usages_ep_m2,
                        "conso_pro_dle_elec_2020": conso_pro_dle_elec_2020,
                        "conso_pro_dle_gaz_2020": conso_pro_dle_gaz_2020,
                        "conso_res_dle_elec_2020": conso_res_dle_elec_2020,
                        "conso_res_dle_gaz_2020": conso_res_dle_gaz_2020,
                        "contient_fictive_geom_groupe": contient_fictive_geom_groupe,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "date_reception_dpe": date_reception_dpe,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "distance_batiment_historique_plus_proche": distance_batiment_historique_plus_proche,
                        "ecs_solaire": ecs_solaire,
                        "emission_ges_3_usages_ep_m2_arrete_2012": emission_ges_3_usages_ep_m2_arrete_2012,
                        "emission_ges_5_usages_m2": emission_ges_5_usages_m2,
                        "epaisseur_lame": epaisseur_lame,
                        "etat_initial_consommation_energie_estim_inc": etat_initial_consommation_energie_estim_inc,
                        "etat_initial_consommation_energie_estim_lower": etat_initial_consommation_energie_estim_lower,
                        "etat_initial_consommation_energie_estim_mean": etat_initial_consommation_energie_estim_mean,
                        "etat_initial_consommation_energie_estim_upper": etat_initial_consommation_energie_estim_upper,
                        "etat_initial_consommation_energie_primaire_estim_lower": etat_initial_consommation_energie_primaire_estim_lower,
                        "etat_initial_consommation_energie_primaire_estim_mean": etat_initial_consommation_energie_primaire_estim_mean,
                        "etat_initial_consommation_energie_primaire_estim_upper": etat_initial_consommation_energie_primaire_estim_upper,
                        "etat_initial_consommation_ges_estim_inc": etat_initial_consommation_ges_estim_inc,
                        "etat_initial_ges_estim_lower": etat_initial_ges_estim_lower,
                        "etat_initial_ges_estim_mean": etat_initial_ges_estim_mean,
                        "etat_initial_ges_estim_upper": etat_initial_ges_estim_upper,
                        "etat_initial_risque_canicule": etat_initial_risque_canicule,
                        "etat_initial_risque_canicule_inc": etat_initial_risque_canicule_inc,
                        "etat_renove_consommation_energie_estim_inc": etat_renove_consommation_energie_estim_inc,
                        "etat_renove_consommation_energie_estim_lower": etat_renove_consommation_energie_estim_lower,
                        "etat_renove_consommation_energie_estim_mean": etat_renove_consommation_energie_estim_mean,
                        "etat_renove_consommation_energie_estim_upper": etat_renove_consommation_energie_estim_upper,
                        "etat_renove_consommation_energie_primaire_estim_lower": etat_renove_consommation_energie_primaire_estim_lower,
                        "etat_renove_consommation_energie_primaire_estim_mean": etat_renove_consommation_energie_primaire_estim_mean,
                        "etat_renove_consommation_energie_primaire_estim_upper": etat_renove_consommation_energie_primaire_estim_upper,
                        "etat_renove_consommation_ges_estim_inc": etat_renove_consommation_ges_estim_inc,
                        "etat_renove_ges_estim_lower": etat_renove_ges_estim_lower,
                        "etat_renove_ges_estim_mean": etat_renove_ges_estim_mean,
                        "etat_renove_ges_estim_upper": etat_renove_ges_estim_upper,
                        "etat_renove_risque_canicule": etat_renove_risque_canicule,
                        "etat_renove_risque_canicule_inc": etat_renove_risque_canicule_inc,
                        "etiquette_dpe_initial_a": etiquette_dpe_initial_a,
                        "etiquette_dpe_initial_b": etiquette_dpe_initial_b,
                        "etiquette_dpe_initial_c": etiquette_dpe_initial_c,
                        "etiquette_dpe_initial_d": etiquette_dpe_initial_d,
                        "etiquette_dpe_initial_e": etiquette_dpe_initial_e,
                        "etiquette_dpe_initial_f": etiquette_dpe_initial_f,
                        "etiquette_dpe_initial_g": etiquette_dpe_initial_g,
                        "etiquette_dpe_initial_inc": etiquette_dpe_initial_inc,
                        "etiquette_dpe_initial_map": etiquette_dpe_initial_map,
                        "etiquette_dpe_initial_map_2nd": etiquette_dpe_initial_map_2nd,
                        "etiquette_dpe_initial_map_2nd_prob": etiquette_dpe_initial_map_2nd_prob,
                        "etiquette_dpe_renove_a": etiquette_dpe_renove_a,
                        "etiquette_dpe_renove_b": etiquette_dpe_renove_b,
                        "etiquette_dpe_renove_c": etiquette_dpe_renove_c,
                        "etiquette_dpe_renove_d": etiquette_dpe_renove_d,
                        "etiquette_dpe_renove_e": etiquette_dpe_renove_e,
                        "etiquette_dpe_renove_f": etiquette_dpe_renove_f,
                        "etiquette_dpe_renove_g": etiquette_dpe_renove_g,
                        "etiquette_dpe_renove_inc": etiquette_dpe_renove_inc,
                        "etiquette_dpe_renove_map": etiquette_dpe_renove_map,
                        "etiquette_dpe_renove_map_2nd": etiquette_dpe_renove_map_2nd,
                        "etiquette_dpe_renove_map_2nd_prob": etiquette_dpe_renove_map_2nd_prob,
                        "etiquette_dpe_synthese_particulier_simple": etiquette_dpe_synthese_particulier_simple,
                        "etiquette_dpe_synthese_particulier_source": etiquette_dpe_synthese_particulier_source,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "fiabilite_cr_adr_niv_1": fiabilite_cr_adr_niv_1,
                        "fiabilite_cr_adr_niv_2": fiabilite_cr_adr_niv_2,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "geom_groupe": geom_groupe,
                        "gisement_gain_conso_finale_total": gisement_gain_conso_finale_total,
                        "gisement_gain_energetique_mean": gisement_gain_energetique_mean,
                        "gisement_gain_ges_mean": gisement_gain_ges_mean,
                        "hauteur_mean": hauteur_mean,
                        "identifiant_dpe": identifiant_dpe,
                        "l_cle_interop_adr": l_cle_interop_adr,
                        "l_denomination_proprietaire": l_denomination_proprietaire,
                        "l_libelle_adr": l_libelle_adr,
                        "l_orientation_baie_vitree": l_orientation_baie_vitree,
                        "l_parcelle_id": l_parcelle_id,
                        "l_siren": l_siren,
                        "l_type_generateur_chauffage": l_type_generateur_chauffage,
                        "l_type_generateur_ecs": l_type_generateur_ecs,
                        "libelle_adr_principale_ban": libelle_adr_principale_ban,
                        "libelle_commune_insee": libelle_commune_insee,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "mat_mur_txt": mat_mur_txt,
                        "mat_toit_txt": mat_toit_txt,
                        "materiaux_structure_mur_exterieur": materiaux_structure_mur_exterieur,
                        "materiaux_structure_mur_exterieur_simplifie": materiaux_structure_mur_exterieur_simplifie,
                        "materiaux_toiture_simplifie": materiaux_toiture_simplifie,
                        "nb_adresse_valid_ban": nb_adresse_valid_ban,
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
                        "nb_log": nb_log,
                        "nb_log_rnc": nb_log_rnc,
                        "nb_lot_garpark_rnc": nb_lot_garpark_rnc,
                        "nb_lot_tertiaire_rnc": nb_lot_tertiaire_rnc,
                        "nb_niveau": nb_niveau,
                        "nb_pdl_pro_dle_elec_2020": nb_pdl_pro_dle_elec_2020,
                        "nb_pdl_pro_dle_gaz_2020": nb_pdl_pro_dle_gaz_2020,
                        "nb_pdl_res_dle_elec_2020": nb_pdl_res_dle_elec_2020,
                        "nb_pdl_res_dle_gaz_2020": nb_pdl_res_dle_gaz_2020,
                        "nom_batiment_historique_plus_proche": nom_batiment_historique_plus_proche,
                        "nom_qp": nom_qp,
                        "nom_quartier_qpv": nom_quartier_qpv,
                        "numero_immat_principal": numero_immat_principal,
                        "offset": offset,
                        "order": order,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "quartier_prioritaire": quartier_prioritaire,
                        "s_geom_groupe": s_geom_groupe,
                        "select": select,
                        "surface_emprise_sol": surface_emprise_sol,
                        "surface_facade_ext": surface_facade_ext,
                        "surface_facade_mitoyenne": surface_facade_mitoyenne,
                        "surface_facade_totale": surface_facade_totale,
                        "surface_facade_vitree": surface_facade_vitree,
                        "traversant": traversant,
                        "type_dpe": type_dpe,
                        "type_energie_chauffage": type_energie_chauffage,
                        "type_energie_chauffage_appoint": type_energie_chauffage_appoint,
                        "type_fermeture": type_fermeture,
                        "type_gaz_lame": type_gaz_lame,
                        "type_generateur_chauffage": type_generateur_chauffage,
                        "type_generateur_chauffage_anciennete": type_generateur_chauffage_anciennete,
                        "type_generateur_chauffage_anciennete_appoint": type_generateur_chauffage_anciennete_appoint,
                        "type_generateur_chauffage_appoint": type_generateur_chauffage_appoint,
                        "type_generateur_climatisation": type_generateur_climatisation,
                        "type_generateur_climatisation_anciennete": type_generateur_climatisation_anciennete,
                        "type_generateur_ecs": type_generateur_ecs,
                        "type_generateur_ecs_anciennete": type_generateur_ecs_anciennete,
                        "type_installation_chauffage": type_installation_chauffage,
                        "type_installation_ecs": type_installation_ecs,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_production_energie_renouvelable": type_production_energie_renouvelable,
                        "type_ventilation": type_ventilation,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "vitrage_vir": vitrage_vir,
                        "volume_brut": volume_brut,
                    },
                    adress_list_params.AdressListParams,
                ),
            ),
            cast_to=AdressListResponse,
        )


class AdressesResourceWithRawResponse:
    def __init__(self, adresses: AdressesResource) -> None:
        self._adresses = adresses

        self.list = to_raw_response_wrapper(
            adresses.list,
        )


class AsyncAdressesResourceWithRawResponse:
    def __init__(self, adresses: AsyncAdressesResource) -> None:
        self._adresses = adresses

        self.list = async_to_raw_response_wrapper(
            adresses.list,
        )


class AdressesResourceWithStreamingResponse:
    def __init__(self, adresses: AdressesResource) -> None:
        self._adresses = adresses

        self.list = to_streamed_response_wrapper(
            adresses.list,
        )


class AsyncAdressesResourceWithStreamingResponse:
    def __init__(self, adresses: AsyncAdressesResource) -> None:
        self._adresses = adresses

        self.list = async_to_streamed_response_wrapper(
            adresses.list,
        )
