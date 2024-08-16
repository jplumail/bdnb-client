# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .adresses import (
    AdressesResource,
    AsyncAdressesResource,
    AdressesResourceWithRawResponse,
    AsyncAdressesResourceWithRawResponse,
    AdressesResourceWithStreamingResponse,
    AsyncAdressesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .parcelles import (
    ParcellesResource,
    AsyncParcellesResource,
    ParcellesResourceWithRawResponse,
    AsyncParcellesResourceWithRawResponse,
    ParcellesResourceWithStreamingResponse,
    AsyncParcellesResourceWithStreamingResponse,
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
from ....types.donnees import batiments_groupes_complet_list_params
from ....types.donnees.batiments_groupes_complet_list_response import BatimentsGroupesCompletListResponse

__all__ = ["BatimentsGroupesCompletsResource", "AsyncBatimentsGroupesCompletsResource"]


class BatimentsGroupesCompletsResource(SyncAPIResource):
    @cached_property
    def parcelles(self) -> ParcellesResource:
        return ParcellesResource(self._client)

    @cached_property
    def adresses(self) -> AdressesResource:
        return AdressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatimentsGroupesCompletsResourceWithRawResponse:
        return BatimentsGroupesCompletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentsGroupesCompletsResourceWithStreamingResponse:
        return BatimentsGroupesCompletsResourceWithStreamingResponse(self)

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
        indicateur_distance_au_reseau: str | NotGiven = NOT_GIVEN,
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
        potentiel_raccordement_reseau_chaleur: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentsGroupesCompletListResponse:
        """
        jointure batiment_groupe avec l'ensemble des tables mÃ©tiers

        Args:
          alea_argiles: (argiles) AlÃ©a du risque argiles

          alea_radon: (radon) alea du risque radon

          altitude_sol_mean: (ign) Altitude au sol moyenne [m]

          annee_construction: AnnÃ©e de construction du bÃ¢timent

          arrete_2021: prÃ©cise si le DPE est un DPE qui est issu de la nouvelle rÃ©forme du DPE
              (arrÃªtÃ© du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification
              antÃ©rieure de 2012.

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          chauffage_solaire: prÃ©sence de chauffage solaire

          classe_bilan_dpe: Classe du DPE issu de la synthÃ¨se du double seuil sur les consommations
              Ã©nergie primaire et les Ã©missions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          classe_conso_energie_arrete_2012: classe d'Ã©mission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          cle_interop_adr_principale_ban: ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code rÃ©gion INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
              ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
              (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
              pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          conso_pro_dle_elec_2020: Consommation professionnelle Ã©lectrique [kWh/an]

          conso_pro_dle_gaz_2020: Consommation professionnelle gaz [kWh/an]

          conso_res_dle_elec_2020: Consommation rÃ©sidentielle Ã©lectrique [kWh/an]

          conso_res_dle_gaz_2020: Consommation rÃ©sidentielle gaz [kWh/an]

          contient_fictive_geom_groupe: Vaut "vrai", si la gÃ©omÃ©trie du groupe de bÃ¢timent est gÃ©nÃ©rÃ©e
              automatiquement et ne reprÃ©sente pas la gÃ©omÃ©trie du groupe de bÃ¢timent.

          croisement_geospx_reussi: le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
              considÃ©rÃ©e comme rÃ©ussi

          date_reception_dpe: date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          distance_batiment_historique_plus_proche: (mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]

          ecs_solaire: prÃ©sence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
              autoconsommÃ©e)
              (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
              vigueur actuellement)

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
              DPE.

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
              rÃ©novation [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rÃ©novation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rÃ©novation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
              un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
              de rÃ©novation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
              probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
              Ã 5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
              bÃ¢timent. Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est
              l'Ã©tiquette la plus probable , G la seconde Ã©tiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
              classÃ© F ou G.

          etiquette_dpe_renove_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
              aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_synthese_particulier_simple: Etiquette DPE selon l'arrÃªtÃ© 2021. Si un DPE existe, l'Ã©tiquette provient
              d'un DPE de l'AEDME, sinon, il s'agit d'une simulation.

          etiquette_dpe_synthese_particulier_source: TODO

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrÃ©e. coefficient entre 0
              et 1

          fiabilite_cr_adr_niv_1: FiabilitÃ© des donnÃ©es croisÃ©es Ã l'adresse ('donnÃ©es croisÃ©es Ã l'adresse
              fiables', 'donnÃ©es croisÃ©es Ã l'adresse fiables Ã l'echelle de la parcelle
              unifiee', 'donnÃ©es croisÃ©es Ã l'adresse moyennement fiables', 'problÃ¨me de
              gÃ©ocodage')

          fiabilite_cr_adr_niv_2: FiabilitÃ© dÃ©taillÃ©e des donnÃ©es croisÃ©es Ã l'adresse

          fiabilite_emprise_sol: FiabilitÃ© de l'emprise au sol du bÃ¢timent

          fiabilite_hauteur: FiabilitÃ© de la hauteur du bÃ¢timent

          geom_groupe: GÃ©omÃ©trie multipolygonale du groupe de bÃ¢timent (Lambert-93)

          gisement_gain_conso_finale_total: (cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)

          gisement_gain_energetique_mean: Estimation du gain Ã©nergÃ©tique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
              serre

          hauteur_mean: (ign) Hauteur moyenne des bÃ¢timents [m]

          identifiant_dpe: identifiant de la table des DPE ademe

          indicateur_distance_au_reseau: Indication sur la distance entre le bÃ¢timent et le point au rÃ©seau de chaleur
              le plus proche en vue d'un potentiel raccordement au rÃ©seau.

          l_cle_interop_adr: Liste de clÃ©s d'interopÃ©rabilitÃ© de l'adresse postale

          l_denomination_proprietaire: Liste de dÃ©nominations de propriÃ©taires

          l_libelle_adr: Liste de libellÃ© complet de l'adresse

          l_orientation_baie_vitree: liste des orientations des baies vitrÃ©es (enum version BDNB)

          l_parcelle_id: Liste d'identifiants de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          l_siren: Liste d'identifiants siren

          l_type_generateur_chauffage: type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)
              concatÃ©nÃ© en liste pour tous les DPE

          l_type_generateur_ecs: type de gÃ©nÃ©rateur d'ECS principal (enum version simplifiÃ©e BDNB) concatÃ©nÃ©
              en liste pour tous les DPE

          libelle_adr_principale_ban: LibellÃ© complet de l'adresse principale (issue de la BAN)

          libelle_commune_insee: (insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent

          limit: Limiting and Pagination

          mat_mur_txt: (ffo) MatÃ©riaux principal des murs extÃ©rieurs

          mat_toit_txt: (ffo) MatÃ©riau principal des toitures

          materiaux_structure_mur_exterieur: matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©. Cette
              information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers
              ou DPE pour le moment)

          materiaux_toiture_simplifie: materiaux principal utiliÃ© pour la toiture simplifiÃ©. Cette information peut
              Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          nb_adresse_valid_ban: Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
              groupe de bÃ¢timent

          nb_classe_bilan_dpe_a: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe A

          nb_classe_bilan_dpe_b: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe B

          nb_classe_bilan_dpe_c: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe C

          nb_classe_bilan_dpe_d: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe D

          nb_classe_bilan_dpe_e: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe E

          nb_classe_bilan_dpe_f: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe F

          nb_classe_bilan_dpe_g: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe G

          nb_classe_conso_energie_arrete_2012_a: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique A. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_b: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique B. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_c: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique C. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_d: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique D. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_e: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique E. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_f: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique F. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_g: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique G. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_nc: (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
              (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_log: (rnc) Nombre de logements

          nb_log_rnc: (rnc) Nombre de logements

          nb_lot_garpark_rnc: Nombre de lots de stationnement

          nb_lot_tertiaire_rnc: Nombre de lots de type bureau et commerce

          nb_niveau: (ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)

          nb_pdl_pro_dle_elec_2020: Nombre de points de livraison Ã©lectrique professionnels [kWh/an]

          nb_pdl_pro_dle_gaz_2020: Nombre de points de livraison gaz professionnels [kWh/an]

          nb_pdl_res_dle_elec_2020: Nombre de points de livraison Ã©lectrique rÃ©sidentiels [kWh/an]

          nb_pdl_res_dle_gaz_2020: Nombre de points de livraison gaz rÃ©sidentiels [kWh/an]

          nom_batiment_historique_plus_proche: (mer:tico) nom du bÃ¢timent historique le plus proche

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

          nom_quartier_qpv: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

          numero_immat_principal: numÃ©ro d'immatriculation principal associÃ© au bÃ¢timent groupe. (numÃ©ro
              d'immatriculation copropriÃ©tÃ© qui comporte le plus de lots)

          offset: Limiting and Pagination

          order: Ordering

          potentiel_raccordement_reseau_chaleur: Indicateur de potentiel de raccordement au rÃ©seau de chaleur. L'indicateur
              dÃ©pend de la distance entre le bÃ¢timent et le rÃ©seau et du type de circuit de
              chauffage existant du bÃ¢timent. Enfin, si le bÃ¢timent est dÃ©jÃ raccordÃ©
              alors il est indiquÃ© comme tel.

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          quartier_prioritaire: Est situÃ© dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)

          select: Filtering Columns

          surface_emprise_sol: Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)

          surface_facade_ext: Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_dpe: type de DPE. Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021),
              son objet (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul
              utilisÃ© (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
              simplifiÃ©e BDNB)

          type_energie_chauffage_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
              simplifiÃ©e BDNB)

          type_fermeture: type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
              vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
              BDNB)

          type_generateur_chauffage: type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)

          type_generateur_chauffage_anciennete: anciennetÃ© du gÃ©nÃ©rateur de chauffage principal

          type_generateur_chauffage_anciennete_appoint: anciennetÃ© du gÃ©nÃ©rateur de chauffage d'appoint

          type_generateur_chauffage_appoint: type de gÃ©nÃ©rateur de chauffage d'appoint (enum version simplifiÃ©e BDNB)

          type_generateur_climatisation: type de gÃ©nÃ©rateur de climatisation principal (enum version simplifiÃ©e BDNB)

          type_generateur_climatisation_anciennete: anciennetÃ© du gÃ©nÃ©rateur de climatisation principal

          type_generateur_ecs: type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal (enum version
              simplifiÃ©e BDNB)

          type_generateur_ecs_anciennete: anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal

          type_installation_chauffage: type d'installation de chauffage (collectif ou individuel) (enum version
              simplifiÃ©e BDNB)

          type_installation_ecs: type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
              version simplifiÃ©e BDNB)

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

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

          type_vitrage: type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
              calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
              mÃ©thode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          usage_niveau_1_txt: indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          vitrage_vir: le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
              rend plus performant d'un point de vue thermique.

          volume_brut: Volume brut du bÃ¢timent [m3]

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
            "/donnees/batiment_groupe_complet",
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
                        "indicateur_distance_au_reseau": indicateur_distance_au_reseau,
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
                        "potentiel_raccordement_reseau_chaleur": potentiel_raccordement_reseau_chaleur,
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
                    batiments_groupes_complet_list_params.BatimentsGroupesCompletListParams,
                ),
            ),
            cast_to=BatimentsGroupesCompletListResponse,
        )


class AsyncBatimentsGroupesCompletsResource(AsyncAPIResource):
    @cached_property
    def parcelles(self) -> AsyncParcellesResource:
        return AsyncParcellesResource(self._client)

    @cached_property
    def adresses(self) -> AsyncAdressesResource:
        return AsyncAdressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatimentsGroupesCompletsResourceWithRawResponse:
        return AsyncBatimentsGroupesCompletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentsGroupesCompletsResourceWithStreamingResponse:
        return AsyncBatimentsGroupesCompletsResourceWithStreamingResponse(self)

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
        indicateur_distance_au_reseau: str | NotGiven = NOT_GIVEN,
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
        potentiel_raccordement_reseau_chaleur: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentsGroupesCompletListResponse:
        """
        jointure batiment_groupe avec l'ensemble des tables mÃ©tiers

        Args:
          alea_argiles: (argiles) AlÃ©a du risque argiles

          alea_radon: (radon) alea du risque radon

          altitude_sol_mean: (ign) Altitude au sol moyenne [m]

          annee_construction: AnnÃ©e de construction du bÃ¢timent

          arrete_2021: prÃ©cise si le DPE est un DPE qui est issu de la nouvelle rÃ©forme du DPE
              (arrÃªtÃ© du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification
              antÃ©rieure de 2012.

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          chauffage_solaire: prÃ©sence de chauffage solaire

          classe_bilan_dpe: Classe du DPE issu de la synthÃ¨se du double seuil sur les consommations
              Ã©nergie primaire et les Ã©missions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          classe_conso_energie_arrete_2012: classe d'Ã©mission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          cle_interop_adr_principale_ban: ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_epci_insee: Code de l'EPCI

          code_iris: Code iris INSEE

          code_qp: identifiant de la table qpv

          code_region_insee: Code rÃ©gion INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
              ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
              (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
              pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          conso_pro_dle_elec_2020: Consommation professionnelle Ã©lectrique [kWh/an]

          conso_pro_dle_gaz_2020: Consommation professionnelle gaz [kWh/an]

          conso_res_dle_elec_2020: Consommation rÃ©sidentielle Ã©lectrique [kWh/an]

          conso_res_dle_gaz_2020: Consommation rÃ©sidentielle gaz [kWh/an]

          contient_fictive_geom_groupe: Vaut "vrai", si la gÃ©omÃ©trie du groupe de bÃ¢timent est gÃ©nÃ©rÃ©e
              automatiquement et ne reprÃ©sente pas la gÃ©omÃ©trie du groupe de bÃ¢timent.

          croisement_geospx_reussi: le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
              considÃ©rÃ©e comme rÃ©ussi

          date_reception_dpe: date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          distance_batiment_historique_plus_proche: (mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]

          ecs_solaire: prÃ©sence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
              autoconsommÃ©e)
              (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
              vigueur actuellement)

          epaisseur_lame: epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
              DPE.

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
              rÃ©novation [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rÃ©novation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rÃ©novation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
              un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
              de rÃ©novation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
              probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
              Ã 5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
              bÃ¢timent. Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est
              l'Ã©tiquette la plus probable , G la seconde Ã©tiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
              classÃ© F ou G.

          etiquette_dpe_renove_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
              aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_synthese_particulier_simple: Etiquette DPE selon l'arrÃªtÃ© 2021. Si un DPE existe, l'Ã©tiquette provient
              d'un DPE de l'AEDME, sinon, il s'agit d'une simulation.

          etiquette_dpe_synthese_particulier_source: TODO

          facteur_solaire_baie_vitree: facteur de transmission du flux solaire par la baie vitrÃ©e. coefficient entre 0
              et 1

          fiabilite_cr_adr_niv_1: FiabilitÃ© des donnÃ©es croisÃ©es Ã l'adresse ('donnÃ©es croisÃ©es Ã l'adresse
              fiables', 'donnÃ©es croisÃ©es Ã l'adresse fiables Ã l'echelle de la parcelle
              unifiee', 'donnÃ©es croisÃ©es Ã l'adresse moyennement fiables', 'problÃ¨me de
              gÃ©ocodage')

          fiabilite_cr_adr_niv_2: FiabilitÃ© dÃ©taillÃ©e des donnÃ©es croisÃ©es Ã l'adresse

          fiabilite_emprise_sol: FiabilitÃ© de l'emprise au sol du bÃ¢timent

          fiabilite_hauteur: FiabilitÃ© de la hauteur du bÃ¢timent

          geom_groupe: GÃ©omÃ©trie multipolygonale du groupe de bÃ¢timent (Lambert-93)

          gisement_gain_conso_finale_total: (cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)

          gisement_gain_energetique_mean: Estimation du gain Ã©nergÃ©tique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
              serre

          hauteur_mean: (ign) Hauteur moyenne des bÃ¢timents [m]

          identifiant_dpe: identifiant de la table des DPE ademe

          indicateur_distance_au_reseau: Indication sur la distance entre le bÃ¢timent et le point au rÃ©seau de chaleur
              le plus proche en vue d'un potentiel raccordement au rÃ©seau.

          l_cle_interop_adr: Liste de clÃ©s d'interopÃ©rabilitÃ© de l'adresse postale

          l_denomination_proprietaire: Liste de dÃ©nominations de propriÃ©taires

          l_libelle_adr: Liste de libellÃ© complet de l'adresse

          l_orientation_baie_vitree: liste des orientations des baies vitrÃ©es (enum version BDNB)

          l_parcelle_id: Liste d'identifiants de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          l_siren: Liste d'identifiants siren

          l_type_generateur_chauffage: type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)
              concatÃ©nÃ© en liste pour tous les DPE

          l_type_generateur_ecs: type de gÃ©nÃ©rateur d'ECS principal (enum version simplifiÃ©e BDNB) concatÃ©nÃ©
              en liste pour tous les DPE

          libelle_adr_principale_ban: LibellÃ© complet de l'adresse principale (issue de la BAN)

          libelle_commune_insee: (insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent

          limit: Limiting and Pagination

          mat_mur_txt: (ffo) MatÃ©riaux principal des murs extÃ©rieurs

          mat_toit_txt: (ffo) MatÃ©riau principal des toitures

          materiaux_structure_mur_exterieur: matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
              (enum version BDNB)

          materiaux_structure_mur_exterieur_simplifie: materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©. Cette
              information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers
              ou DPE pour le moment)

          materiaux_toiture_simplifie: materiaux principal utiliÃ© pour la toiture simplifiÃ©. Cette information peut
              Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers Fonciers ou DPE pour le
              moment)

          nb_adresse_valid_ban: Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
              groupe de bÃ¢timent

          nb_classe_bilan_dpe_a: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe A

          nb_classe_bilan_dpe_b: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe B

          nb_classe_bilan_dpe_c: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe C

          nb_classe_bilan_dpe_d: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe D

          nb_classe_bilan_dpe_e: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe E

          nb_classe_bilan_dpe_f: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe F

          nb_classe_bilan_dpe_g: (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
              classe G

          nb_classe_conso_energie_arrete_2012_a: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique A. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_b: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique B. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_c: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique C. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_d: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique D. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_e: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique E. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_f: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique F. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_g: (dpe) Nombre de DPE de la classe Ã©nergÃ©tique G. valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_classe_conso_energie_arrete_2012_nc: (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
              (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          nb_log: (rnc) Nombre de logements

          nb_log_rnc: (rnc) Nombre de logements

          nb_lot_garpark_rnc: Nombre de lots de stationnement

          nb_lot_tertiaire_rnc: Nombre de lots de type bureau et commerce

          nb_niveau: (ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)

          nb_pdl_pro_dle_elec_2020: Nombre de points de livraison Ã©lectrique professionnels [kWh/an]

          nb_pdl_pro_dle_gaz_2020: Nombre de points de livraison gaz professionnels [kWh/an]

          nb_pdl_res_dle_elec_2020: Nombre de points de livraison Ã©lectrique rÃ©sidentiels [kWh/an]

          nb_pdl_res_dle_gaz_2020: Nombre de points de livraison gaz rÃ©sidentiels [kWh/an]

          nom_batiment_historique_plus_proche: (mer:tico) nom du bÃ¢timent historique le plus proche

          nom_qp: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

          nom_quartier_qpv: Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent

          numero_immat_principal: numÃ©ro d'immatriculation principal associÃ© au bÃ¢timent groupe. (numÃ©ro
              d'immatriculation copropriÃ©tÃ© qui comporte le plus de lots)

          offset: Limiting and Pagination

          order: Ordering

          potentiel_raccordement_reseau_chaleur: Indicateur de potentiel de raccordement au rÃ©seau de chaleur. L'indicateur
              dÃ©pend de la distance entre le bÃ¢timent et le rÃ©seau et du type de circuit de
              chauffage existant du bÃ¢timent. Enfin, si le bÃ¢timent est dÃ©jÃ raccordÃ©
              alors il est indiquÃ© comme tel.

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          quartier_prioritaire: Est situÃ© dans un quartier prioritaire

          s_geom_groupe: Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)

          select: Filtering Columns

          surface_emprise_sol: Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)

          surface_facade_ext: Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_dpe: type de DPE. Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021),
              son objet (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul
              utilisÃ© (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
              simplifiÃ©e BDNB)

          type_energie_chauffage_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
              simplifiÃ©e BDNB)

          type_fermeture: type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
              vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
              BDNB)

          type_generateur_chauffage: type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)

          type_generateur_chauffage_anciennete: anciennetÃ© du gÃ©nÃ©rateur de chauffage principal

          type_generateur_chauffage_anciennete_appoint: anciennetÃ© du gÃ©nÃ©rateur de chauffage d'appoint

          type_generateur_chauffage_appoint: type de gÃ©nÃ©rateur de chauffage d'appoint (enum version simplifiÃ©e BDNB)

          type_generateur_climatisation: type de gÃ©nÃ©rateur de climatisation principal (enum version simplifiÃ©e BDNB)

          type_generateur_climatisation_anciennete: anciennetÃ© du gÃ©nÃ©rateur de climatisation principal

          type_generateur_ecs: type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal (enum version
              simplifiÃ©e BDNB)

          type_generateur_ecs_anciennete: anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal

          type_installation_chauffage: type d'installation de chauffage (collectif ou individuel) (enum version
              simplifiÃ©e BDNB)

          type_installation_ecs: type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
              version simplifiÃ©e BDNB)

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

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

          type_vitrage: type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)

          u_baie_vitree: Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
              calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)

          u_mur_exterieur: Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)

          u_plancher_bas_final_deperditif: Coefficient de transmission thermique moyen des planchers bas en prenant en
              compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
              mÃ©thode 3CL(W/mÂ²/K)

          u_plancher_haut_deperditif: Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)

          usage_niveau_1_txt: indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          vitrage_vir: le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
              rend plus performant d'un point de vue thermique.

          volume_brut: Volume brut du bÃ¢timent [m3]

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
            "/donnees/batiment_groupe_complet",
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
                        "indicateur_distance_au_reseau": indicateur_distance_au_reseau,
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
                        "potentiel_raccordement_reseau_chaleur": potentiel_raccordement_reseau_chaleur,
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
                    batiments_groupes_complet_list_params.BatimentsGroupesCompletListParams,
                ),
            ),
            cast_to=BatimentsGroupesCompletListResponse,
        )


class BatimentsGroupesCompletsResourceWithRawResponse:
    def __init__(self, batiments_groupes_complets: BatimentsGroupesCompletsResource) -> None:
        self._batiments_groupes_complets = batiments_groupes_complets

        self.list = to_raw_response_wrapper(
            batiments_groupes_complets.list,
        )

    @cached_property
    def parcelles(self) -> ParcellesResourceWithRawResponse:
        return ParcellesResourceWithRawResponse(self._batiments_groupes_complets.parcelles)

    @cached_property
    def adresses(self) -> AdressesResourceWithRawResponse:
        return AdressesResourceWithRawResponse(self._batiments_groupes_complets.adresses)


class AsyncBatimentsGroupesCompletsResourceWithRawResponse:
    def __init__(self, batiments_groupes_complets: AsyncBatimentsGroupesCompletsResource) -> None:
        self._batiments_groupes_complets = batiments_groupes_complets

        self.list = async_to_raw_response_wrapper(
            batiments_groupes_complets.list,
        )

    @cached_property
    def parcelles(self) -> AsyncParcellesResourceWithRawResponse:
        return AsyncParcellesResourceWithRawResponse(self._batiments_groupes_complets.parcelles)

    @cached_property
    def adresses(self) -> AsyncAdressesResourceWithRawResponse:
        return AsyncAdressesResourceWithRawResponse(self._batiments_groupes_complets.adresses)


class BatimentsGroupesCompletsResourceWithStreamingResponse:
    def __init__(self, batiments_groupes_complets: BatimentsGroupesCompletsResource) -> None:
        self._batiments_groupes_complets = batiments_groupes_complets

        self.list = to_streamed_response_wrapper(
            batiments_groupes_complets.list,
        )

    @cached_property
    def parcelles(self) -> ParcellesResourceWithStreamingResponse:
        return ParcellesResourceWithStreamingResponse(self._batiments_groupes_complets.parcelles)

    @cached_property
    def adresses(self) -> AdressesResourceWithStreamingResponse:
        return AdressesResourceWithStreamingResponse(self._batiments_groupes_complets.adresses)


class AsyncBatimentsGroupesCompletsResourceWithStreamingResponse:
    def __init__(self, batiments_groupes_complets: AsyncBatimentsGroupesCompletsResource) -> None:
        self._batiments_groupes_complets = batiments_groupes_complets

        self.list = async_to_streamed_response_wrapper(
            batiments_groupes_complets.list,
        )

    @cached_property
    def parcelles(self) -> AsyncParcellesResourceWithStreamingResponse:
        return AsyncParcellesResourceWithStreamingResponse(self._batiments_groupes_complets.parcelles)

    @cached_property
    def adresses(self) -> AsyncAdressesResourceWithStreamingResponse:
        return AsyncAdressesResourceWithStreamingResponse(self._batiments_groupes_complets.adresses)
