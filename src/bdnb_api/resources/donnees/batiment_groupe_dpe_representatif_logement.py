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
from ...types.donnees import batiment_groupe_dpe_representatif_logement_list_params
from ...types.donnees.batiment_groupe_dpe_representatif_logement_list_response import (
    BatimentGroupeDpeRepresentatifLogementListResponse,
)

__all__ = ["BatimentGroupeDpeRepresentatifLogementResource", "AsyncBatimentGroupeDpeRepresentatifLogementResource"]


class BatimentGroupeDpeRepresentatifLogementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
        return BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
        return BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        annee_construction_dpe: str | NotGiven = NOT_GIVEN,
        arrete_2021: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        chauffage_solaire: str | NotGiven = NOT_GIVEN,
        classe_bilan_dpe: str | NotGiven = NOT_GIVEN,
        classe_conso_energie_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_emission_ges: str | NotGiven = NOT_GIVEN,
        classe_emission_ges_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ef_m2: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ep_m2: str | NotGiven = NOT_GIVEN,
        date_etablissement_dpe: str | NotGiven = NOT_GIVEN,
        date_reception_dpe: str | NotGiven = NOT_GIVEN,
        deperdition_baie_vitree: str | NotGiven = NOT_GIVEN,
        deperdition_mur: str | NotGiven = NOT_GIVEN,
        deperdition_plancher_bas: str | NotGiven = NOT_GIVEN,
        deperdition_plancher_haut: str | NotGiven = NOT_GIVEN,
        deperdition_pont_thermique: str | NotGiven = NOT_GIVEN,
        deperdition_porte: str | NotGiven = NOT_GIVEN,
        ecs_solaire: str | NotGiven = NOT_GIVEN,
        emission_ges_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        emission_ges_5_usages_m2: str | NotGiven = NOT_GIVEN,
        epaisseur_isolation_mur_exterieur_estim: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        epaisseur_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        identifiant_dpe: str | NotGiven = NOT_GIVEN,
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
        nb_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        nb_generateur_ecs: str | NotGiven = NOT_GIVEN,
        nb_installation_chauffage: str | NotGiven = NOT_GIVEN,
        nb_installation_ecs: str | NotGiven = NOT_GIVEN,
        nombre_niveau_immeuble: str | NotGiven = NOT_GIVEN,
        nombre_niveau_logement: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        periode_construction_dpe: str | NotGiven = NOT_GIVEN,
        plusieurs_facade_exposee: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_habitable_immeuble: str | NotGiven = NOT_GIVEN,
        surface_habitable_logement: str | NotGiven = NOT_GIVEN,
        surface_mur_deperditif: str | NotGiven = NOT_GIVEN,
        surface_mur_exterieur: str | NotGiven = NOT_GIVEN,
        surface_mur_totale: str | NotGiven = NOT_GIVEN,
        surface_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        surface_plancher_bas_totale: str | NotGiven = NOT_GIVEN,
        surface_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        surface_plancher_haut_totale: str | NotGiven = NOT_GIVEN,
        surface_porte: str | NotGiven = NOT_GIVEN,
        surface_vitree_est: str | NotGiven = NOT_GIVEN,
        surface_vitree_horizontal: str | NotGiven = NOT_GIVEN,
        surface_vitree_nord: str | NotGiven = NOT_GIVEN,
        surface_vitree_ouest: str | NotGiven = NOT_GIVEN,
        surface_vitree_sud: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_batiment_dpe: str | NotGiven = NOT_GIVEN,
        type_dpe: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_energie_climatisation: str | NotGiven = NOT_GIVEN,
        type_energie_ecs: str | NotGiven = NOT_GIVEN,
        type_energie_ecs_appoint: str | NotGiven = NOT_GIVEN,
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
        type_generateur_ecs_anciennete_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs_appoint: str | NotGiven = NOT_GIVEN,
        type_installation_chauffage: str | NotGiven = NOT_GIVEN,
        type_installation_ecs: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_porte: str | NotGiven = NOT_GIVEN,
        type_production_energie_renouvelable: str | NotGiven = NOT_GIVEN,
        type_ventilation: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_brut_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        u_porte: str | NotGiven = NOT_GIVEN,
        uw: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeDpeRepresentatifLogementListResponse:
        """Table qui contient les DPE reprÃ©sentatifs de chaque bÃ¢timent de logement.

        Le
        DPE reprÃ©sentatif est soit un DPE issu de l'ancien arrÃªtÃ© qui n'est plus en
        vigueur (arrÃªtÃ© 2012) ou d'un nouveau DPE (arrÃªtÃ© 2021). Pour filtrer ancien
        et nouveau DPE utiliser le boolÃ©en `arrete_2021`

        Args:
          annee_construction_dpe: (dpe representatif) annÃ©e de construction du logement (dpe)

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

          classe_emission_ges: classe d'Ã©mission GES du DPE 5 usages (chauffage, ECS, climatisation,
              Ã©clairage et auxiliaires). valable uniquement pour les DPE appliquant la
              mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur actuellement)

          classe_emission_ges_arrete_2012: classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code dÃ©partement INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
              ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          conso_5_usages_ef_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires)en Ã©nergie finale (dÃ©duit
              de la production pv autoconsommÃ©e) (kWhef/mÂ²/an). valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
              (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
              pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          date_etablissement_dpe: date de l'Ã©tablissement du dpe

          date_reception_dpe: date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME

          deperdition_baie_vitree: somme des dÃ©perditions par les baies vitrÃ©es du DPE (W/K)

          deperdition_mur: somme des dÃ©perditions par les murs du DPE (W/K)

          deperdition_plancher_bas: somme des deperditions par les planchers bas du logement (W/K)

          deperdition_plancher_haut: somme des deperditions par les planchers hauts du logement (W/K)

          deperdition_pont_thermique: somme des deperditions par les portes du DPE (W/K)

          deperdition_porte: somme des deperditions par les portes du DPE (W/K)

          ecs_solaire: prÃ©sence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
              autoconsommÃ©e)
              (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
              vigueur actuellement)

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

          identifiant_dpe: identifiant de la table des DPE ademe

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

          nb_generateur_chauffage: nombre de gÃ©nÃ©rateurs de chauffage

          nb_generateur_ecs: nombre de gÃ©nÃ©rateurs d'ecs

          nb_installation_chauffage: nombre d'installation de chauffage

          nb_installation_ecs: nombre d'installation d'ecs

          nombre_niveau_immeuble: nombre de niveaux total de l'immeuble

          nombre_niveau_logement: nombre de niveaux du logement (maison ou appartement)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_dpe: pÃ©riode de construction selon la segmentation par grandes pÃ©riodes
              "Ã©nergÃ©tiques" du DPE.

          plusieurs_facade_exposee: y a plusieurs facades exposÃ©es au vent

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          select: Filtering Columns

          surface_habitable_immeuble: surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
              usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)

          surface_habitable_logement: surface habitable du logement renseignÃ©e sauf dans le cas du dpe Ã l'immeuble.
              (surface habitable au sens du DPE)

          surface_mur_deperditif: somme de la surface de murs donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_mur_exterieur: somme de la surface surface de murs donnant sur l'extÃ©rieur

          surface_mur_totale: somme de la surface de murs totale

          surface_plancher_bas_deperditif: somme de la surface de plancher bas donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_plancher_bas_totale: somme de la surface de plancher bas totale

          surface_plancher_haut_deperditif: somme de la surface de plancher haut donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_plancher_haut_totale: somme de la surface de plancher haut totale

          surface_porte: somme de la surface de portes du DPE

          surface_vitree_est: somme de la surface de baies vitrÃ©es orientÃ©es est du DPE

          surface_vitree_horizontal: somme de la surface de baies vitrÃ©es horizontales du DPE (velux la plupart du
              temps)

          surface_vitree_nord: somme de la surface de baies vitrÃ©es orientÃ©es nord du DPE

          surface_vitree_ouest: somme de la surface de baies vitrÃ©es orientÃ©es ouest du DPE

          surface_vitree_sud: somme de la surface de baies vitrÃ©es orientÃ©es sud du DPE

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_batiment_dpe: type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble). Cette
              colonne est renseignÃ©e uniquement si la source d'information est un DPE.

          type_dpe: type de DPE. Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021),
              son objet (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul
              utilisÃ© (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
              simplifiÃ©e BDNB)

          type_energie_chauffage_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
              simplifiÃ©e BDNB)

          type_energie_climatisation: type d'Ã©nergie pour le gÃ©nÃ©rateur de climatisation principal (enum version
              simplifiÃ©e BDNB)

          type_energie_ecs: type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal
              (enum version simplifiÃ©e BDNB)

          type_energie_ecs_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint
              (enum version simplifiÃ©e BDNB)

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

          type_generateur_ecs_anciennete_appoint: anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint

          type_generateur_ecs_appoint: type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint (enum version
              simplifiÃ©e BDNB)

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

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

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

          version: version du DPE (arrÃªtÃ© 2021). CenumÃ©ro de version permet de tracer les
              Ã©volutions de modÃ¨le de donnÃ©es, decontexte rÃ©glementaire et de contrÃ´le
              mis en place sur les DPE. Chaque nouvelle version induit un certain nombre de
              changements substantiels. Certaines donnÃ©es ne sont disponible ou obligatoires
              qu'Ã partir d'une certaine version

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
            "/donnees/batiment_groupe_dpe_representatif_logement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annee_construction_dpe": annee_construction_dpe,
                        "arrete_2021": arrete_2021,
                        "batiment_groupe_id": batiment_groupe_id,
                        "chauffage_solaire": chauffage_solaire,
                        "classe_bilan_dpe": classe_bilan_dpe,
                        "classe_conso_energie_arrete_2012": classe_conso_energie_arrete_2012,
                        "classe_emission_ges": classe_emission_ges,
                        "classe_emission_ges_arrete_2012": classe_emission_ges_arrete_2012,
                        "classe_inertie": classe_inertie,
                        "code_departement_insee": code_departement_insee,
                        "conso_3_usages_ep_m2_arrete_2012": conso_3_usages_ep_m2_arrete_2012,
                        "conso_5_usages_ef_m2": conso_5_usages_ef_m2,
                        "conso_5_usages_ep_m2": conso_5_usages_ep_m2,
                        "date_etablissement_dpe": date_etablissement_dpe,
                        "date_reception_dpe": date_reception_dpe,
                        "deperdition_baie_vitree": deperdition_baie_vitree,
                        "deperdition_mur": deperdition_mur,
                        "deperdition_plancher_bas": deperdition_plancher_bas,
                        "deperdition_plancher_haut": deperdition_plancher_haut,
                        "deperdition_pont_thermique": deperdition_pont_thermique,
                        "deperdition_porte": deperdition_porte,
                        "ecs_solaire": ecs_solaire,
                        "emission_ges_3_usages_ep_m2_arrete_2012": emission_ges_3_usages_ep_m2_arrete_2012,
                        "emission_ges_5_usages_m2": emission_ges_5_usages_m2,
                        "epaisseur_isolation_mur_exterieur_estim": epaisseur_isolation_mur_exterieur_estim,
                        "epaisseur_lame": epaisseur_lame,
                        "epaisseur_structure_mur_exterieur": epaisseur_structure_mur_exterieur,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "identifiant_dpe": identifiant_dpe,
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
                        "nb_generateur_chauffage": nb_generateur_chauffage,
                        "nb_generateur_ecs": nb_generateur_ecs,
                        "nb_installation_chauffage": nb_installation_chauffage,
                        "nb_installation_ecs": nb_installation_ecs,
                        "nombre_niveau_immeuble": nombre_niveau_immeuble,
                        "nombre_niveau_logement": nombre_niveau_logement,
                        "offset": offset,
                        "order": order,
                        "periode_construction_dpe": periode_construction_dpe,
                        "plusieurs_facade_exposee": plusieurs_facade_exposee,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "select": select,
                        "surface_habitable_immeuble": surface_habitable_immeuble,
                        "surface_habitable_logement": surface_habitable_logement,
                        "surface_mur_deperditif": surface_mur_deperditif,
                        "surface_mur_exterieur": surface_mur_exterieur,
                        "surface_mur_totale": surface_mur_totale,
                        "surface_plancher_bas_deperditif": surface_plancher_bas_deperditif,
                        "surface_plancher_bas_totale": surface_plancher_bas_totale,
                        "surface_plancher_haut_deperditif": surface_plancher_haut_deperditif,
                        "surface_plancher_haut_totale": surface_plancher_haut_totale,
                        "surface_porte": surface_porte,
                        "surface_vitree_est": surface_vitree_est,
                        "surface_vitree_horizontal": surface_vitree_horizontal,
                        "surface_vitree_nord": surface_vitree_nord,
                        "surface_vitree_ouest": surface_vitree_ouest,
                        "surface_vitree_sud": surface_vitree_sud,
                        "traversant": traversant,
                        "type_adjacence_principal_plancher_bas": type_adjacence_principal_plancher_bas,
                        "type_adjacence_principal_plancher_haut": type_adjacence_principal_plancher_haut,
                        "type_batiment_dpe": type_batiment_dpe,
                        "type_dpe": type_dpe,
                        "type_energie_chauffage": type_energie_chauffage,
                        "type_energie_chauffage_appoint": type_energie_chauffage_appoint,
                        "type_energie_climatisation": type_energie_climatisation,
                        "type_energie_ecs": type_energie_ecs,
                        "type_energie_ecs_appoint": type_energie_ecs_appoint,
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
                        "type_generateur_ecs_anciennete_appoint": type_generateur_ecs_anciennete_appoint,
                        "type_generateur_ecs_appoint": type_generateur_ecs_appoint,
                        "type_installation_chauffage": type_installation_chauffage,
                        "type_installation_ecs": type_installation_ecs,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_porte": type_porte,
                        "type_production_energie_renouvelable": type_production_energie_renouvelable,
                        "type_ventilation": type_ventilation,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_brut_deperditif": u_plancher_bas_brut_deperditif,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "u_porte": u_porte,
                        "uw": uw,
                        "version": version,
                        "vitrage_vir": vitrage_vir,
                    },
                    batiment_groupe_dpe_representatif_logement_list_params.BatimentGroupeDpeRepresentatifLogementListParams,
                ),
            ),
            cast_to=BatimentGroupeDpeRepresentatifLogementListResponse,
        )


class AsyncBatimentGroupeDpeRepresentatifLogementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
        return AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
        return AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        annee_construction_dpe: str | NotGiven = NOT_GIVEN,
        arrete_2021: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        chauffage_solaire: str | NotGiven = NOT_GIVEN,
        classe_bilan_dpe: str | NotGiven = NOT_GIVEN,
        classe_conso_energie_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_emission_ges: str | NotGiven = NOT_GIVEN,
        classe_emission_ges_arrete_2012: str | NotGiven = NOT_GIVEN,
        classe_inertie: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ef_m2: str | NotGiven = NOT_GIVEN,
        conso_5_usages_ep_m2: str | NotGiven = NOT_GIVEN,
        date_etablissement_dpe: str | NotGiven = NOT_GIVEN,
        date_reception_dpe: str | NotGiven = NOT_GIVEN,
        deperdition_baie_vitree: str | NotGiven = NOT_GIVEN,
        deperdition_mur: str | NotGiven = NOT_GIVEN,
        deperdition_plancher_bas: str | NotGiven = NOT_GIVEN,
        deperdition_plancher_haut: str | NotGiven = NOT_GIVEN,
        deperdition_pont_thermique: str | NotGiven = NOT_GIVEN,
        deperdition_porte: str | NotGiven = NOT_GIVEN,
        ecs_solaire: str | NotGiven = NOT_GIVEN,
        emission_ges_3_usages_ep_m2_arrete_2012: str | NotGiven = NOT_GIVEN,
        emission_ges_5_usages_m2: str | NotGiven = NOT_GIVEN,
        epaisseur_isolation_mur_exterieur_estim: str | NotGiven = NOT_GIVEN,
        epaisseur_lame: str | NotGiven = NOT_GIVEN,
        epaisseur_structure_mur_exterieur: str | NotGiven = NOT_GIVEN,
        facteur_solaire_baie_vitree: str | NotGiven = NOT_GIVEN,
        identifiant_dpe: str | NotGiven = NOT_GIVEN,
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
        nb_generateur_chauffage: str | NotGiven = NOT_GIVEN,
        nb_generateur_ecs: str | NotGiven = NOT_GIVEN,
        nb_installation_chauffage: str | NotGiven = NOT_GIVEN,
        nb_installation_ecs: str | NotGiven = NOT_GIVEN,
        nombre_niveau_immeuble: str | NotGiven = NOT_GIVEN,
        nombre_niveau_logement: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        periode_construction_dpe: str | NotGiven = NOT_GIVEN,
        plusieurs_facade_exposee: str | NotGiven = NOT_GIVEN,
        pourcentage_surface_baie_vitree_exterieur: str | NotGiven = NOT_GIVEN,
        presence_balcon: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_habitable_immeuble: str | NotGiven = NOT_GIVEN,
        surface_habitable_logement: str | NotGiven = NOT_GIVEN,
        surface_mur_deperditif: str | NotGiven = NOT_GIVEN,
        surface_mur_exterieur: str | NotGiven = NOT_GIVEN,
        surface_mur_totale: str | NotGiven = NOT_GIVEN,
        surface_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        surface_plancher_bas_totale: str | NotGiven = NOT_GIVEN,
        surface_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        surface_plancher_haut_totale: str | NotGiven = NOT_GIVEN,
        surface_porte: str | NotGiven = NOT_GIVEN,
        surface_vitree_est: str | NotGiven = NOT_GIVEN,
        surface_vitree_horizontal: str | NotGiven = NOT_GIVEN,
        surface_vitree_nord: str | NotGiven = NOT_GIVEN,
        surface_vitree_ouest: str | NotGiven = NOT_GIVEN,
        surface_vitree_sud: str | NotGiven = NOT_GIVEN,
        traversant: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_adjacence_principal_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_batiment_dpe: str | NotGiven = NOT_GIVEN,
        type_dpe: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage: str | NotGiven = NOT_GIVEN,
        type_energie_chauffage_appoint: str | NotGiven = NOT_GIVEN,
        type_energie_climatisation: str | NotGiven = NOT_GIVEN,
        type_energie_ecs: str | NotGiven = NOT_GIVEN,
        type_energie_ecs_appoint: str | NotGiven = NOT_GIVEN,
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
        type_generateur_ecs_anciennete_appoint: str | NotGiven = NOT_GIVEN,
        type_generateur_ecs_appoint: str | NotGiven = NOT_GIVEN,
        type_installation_chauffage: str | NotGiven = NOT_GIVEN,
        type_installation_ecs: str | NotGiven = NOT_GIVEN,
        type_isolation_mur_exterieur: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_bas: str | NotGiven = NOT_GIVEN,
        type_isolation_plancher_haut: str | NotGiven = NOT_GIVEN,
        type_materiaux_menuiserie: str | NotGiven = NOT_GIVEN,
        type_plancher_bas_deperditif: str | NotGiven = NOT_GIVEN,
        type_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        type_porte: str | NotGiven = NOT_GIVEN,
        type_production_energie_renouvelable: str | NotGiven = NOT_GIVEN,
        type_ventilation: str | NotGiven = NOT_GIVEN,
        type_vitrage: str | NotGiven = NOT_GIVEN,
        u_baie_vitree: str | NotGiven = NOT_GIVEN,
        u_mur_exterieur: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_brut_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_bas_final_deperditif: str | NotGiven = NOT_GIVEN,
        u_plancher_haut_deperditif: str | NotGiven = NOT_GIVEN,
        u_porte: str | NotGiven = NOT_GIVEN,
        uw: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeDpeRepresentatifLogementListResponse:
        """Table qui contient les DPE reprÃ©sentatifs de chaque bÃ¢timent de logement.

        Le
        DPE reprÃ©sentatif est soit un DPE issu de l'ancien arrÃªtÃ© qui n'est plus en
        vigueur (arrÃªtÃ© 2012) ou d'un nouveau DPE (arrÃªtÃ© 2021). Pour filtrer ancien
        et nouveau DPE utiliser le boolÃ©en `arrete_2021`

        Args:
          annee_construction_dpe: (dpe representatif) annÃ©e de construction du logement (dpe)

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

          classe_emission_ges: classe d'Ã©mission GES du DPE 5 usages (chauffage, ECS, climatisation,
              Ã©clairage et auxiliaires). valable uniquement pour les DPE appliquant la
              mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur actuellement)

          classe_emission_ges_arrete_2012: classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8 fÃ©vrier 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code dÃ©partement INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
              ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012

          conso_5_usages_ef_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires)en Ã©nergie finale (dÃ©duit
              de la production pv autoconsommÃ©e) (kWhef/mÂ²/an). valable uniquement pour les
              DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
              (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
              pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
              actuellement)

          date_etablissement_dpe: date de l'Ã©tablissement du dpe

          date_reception_dpe: date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME

          deperdition_baie_vitree: somme des dÃ©perditions par les baies vitrÃ©es du DPE (W/K)

          deperdition_mur: somme des dÃ©perditions par les murs du DPE (W/K)

          deperdition_plancher_bas: somme des deperditions par les planchers bas du logement (W/K)

          deperdition_plancher_haut: somme des deperditions par les planchers hauts du logement (W/K)

          deperdition_pont_thermique: somme des deperditions par les portes du DPE (W/K)

          deperdition_porte: somme des deperditions par les portes du DPE (W/K)

          ecs_solaire: prÃ©sence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
              l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
              autoconsommÃ©e)
              (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
              uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
              vigueur actuellement)

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

          identifiant_dpe: identifiant de la table des DPE ademe

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

          nb_generateur_chauffage: nombre de gÃ©nÃ©rateurs de chauffage

          nb_generateur_ecs: nombre de gÃ©nÃ©rateurs d'ecs

          nb_installation_chauffage: nombre d'installation de chauffage

          nb_installation_ecs: nombre d'installation d'ecs

          nombre_niveau_immeuble: nombre de niveaux total de l'immeuble

          nombre_niveau_logement: nombre de niveaux du logement (maison ou appartement)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_dpe: pÃ©riode de construction selon la segmentation par grandes pÃ©riodes
              "Ã©nergÃ©tiques" du DPE.

          plusieurs_facade_exposee: y a plusieurs facades exposÃ©es au vent

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs

          presence_balcon: prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
              solaires du DPE.

          select: Filtering Columns

          surface_habitable_immeuble: surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
              usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)

          surface_habitable_logement: surface habitable du logement renseignÃ©e sauf dans le cas du dpe Ã l'immeuble.
              (surface habitable au sens du DPE)

          surface_mur_deperditif: somme de la surface de murs donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_mur_exterieur: somme de la surface surface de murs donnant sur l'extÃ©rieur

          surface_mur_totale: somme de la surface de murs totale

          surface_plancher_bas_deperditif: somme de la surface de plancher bas donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_plancher_bas_totale: somme de la surface de plancher bas totale

          surface_plancher_haut_deperditif: somme de la surface de plancher haut donnant sur des locaux non chauffÃ©s et sur
              l'extÃ©rieur (surfaces dÃ©perditives)

          surface_plancher_haut_totale: somme de la surface de plancher haut totale

          surface_porte: somme de la surface de portes du DPE

          surface_vitree_est: somme de la surface de baies vitrÃ©es orientÃ©es est du DPE

          surface_vitree_horizontal: somme de la surface de baies vitrÃ©es horizontales du DPE (velux la plupart du
              temps)

          surface_vitree_nord: somme de la surface de baies vitrÃ©es orientÃ©es nord du DPE

          surface_vitree_ouest: somme de la surface de baies vitrÃ©es orientÃ©es ouest du DPE

          surface_vitree_sud: somme de la surface de baies vitrÃ©es orientÃ©es sud du DPE

          traversant: indicateur du cÃ´tÃ© traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)

          type_batiment_dpe: type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble). Cette
              colonne est renseignÃ©e uniquement si la source d'information est un DPE.

          type_dpe: type de DPE. Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021),
              son objet (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul
              utilisÃ© (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
              simplifiÃ©e BDNB)

          type_energie_chauffage_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
              simplifiÃ©e BDNB)

          type_energie_climatisation: type d'Ã©nergie pour le gÃ©nÃ©rateur de climatisation principal (enum version
              simplifiÃ©e BDNB)

          type_energie_ecs: type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal
              (enum version simplifiÃ©e BDNB)

          type_energie_ecs_appoint: type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint
              (enum version simplifiÃ©e BDNB)

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

          type_generateur_ecs_anciennete_appoint: anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint

          type_generateur_ecs_appoint: type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint (enum version
              simplifiÃ©e BDNB)

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

          type_porte: type de porte du DPE (enum version DPE 2021)

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

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

          version: version du DPE (arrÃªtÃ© 2021). CenumÃ©ro de version permet de tracer les
              Ã©volutions de modÃ¨le de donnÃ©es, decontexte rÃ©glementaire et de contrÃ´le
              mis en place sur les DPE. Chaque nouvelle version induit un certain nombre de
              changements substantiels. Certaines donnÃ©es ne sont disponible ou obligatoires
              qu'Ã partir d'une certaine version

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
            "/donnees/batiment_groupe_dpe_representatif_logement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annee_construction_dpe": annee_construction_dpe,
                        "arrete_2021": arrete_2021,
                        "batiment_groupe_id": batiment_groupe_id,
                        "chauffage_solaire": chauffage_solaire,
                        "classe_bilan_dpe": classe_bilan_dpe,
                        "classe_conso_energie_arrete_2012": classe_conso_energie_arrete_2012,
                        "classe_emission_ges": classe_emission_ges,
                        "classe_emission_ges_arrete_2012": classe_emission_ges_arrete_2012,
                        "classe_inertie": classe_inertie,
                        "code_departement_insee": code_departement_insee,
                        "conso_3_usages_ep_m2_arrete_2012": conso_3_usages_ep_m2_arrete_2012,
                        "conso_5_usages_ef_m2": conso_5_usages_ef_m2,
                        "conso_5_usages_ep_m2": conso_5_usages_ep_m2,
                        "date_etablissement_dpe": date_etablissement_dpe,
                        "date_reception_dpe": date_reception_dpe,
                        "deperdition_baie_vitree": deperdition_baie_vitree,
                        "deperdition_mur": deperdition_mur,
                        "deperdition_plancher_bas": deperdition_plancher_bas,
                        "deperdition_plancher_haut": deperdition_plancher_haut,
                        "deperdition_pont_thermique": deperdition_pont_thermique,
                        "deperdition_porte": deperdition_porte,
                        "ecs_solaire": ecs_solaire,
                        "emission_ges_3_usages_ep_m2_arrete_2012": emission_ges_3_usages_ep_m2_arrete_2012,
                        "emission_ges_5_usages_m2": emission_ges_5_usages_m2,
                        "epaisseur_isolation_mur_exterieur_estim": epaisseur_isolation_mur_exterieur_estim,
                        "epaisseur_lame": epaisseur_lame,
                        "epaisseur_structure_mur_exterieur": epaisseur_structure_mur_exterieur,
                        "facteur_solaire_baie_vitree": facteur_solaire_baie_vitree,
                        "identifiant_dpe": identifiant_dpe,
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
                        "nb_generateur_chauffage": nb_generateur_chauffage,
                        "nb_generateur_ecs": nb_generateur_ecs,
                        "nb_installation_chauffage": nb_installation_chauffage,
                        "nb_installation_ecs": nb_installation_ecs,
                        "nombre_niveau_immeuble": nombre_niveau_immeuble,
                        "nombre_niveau_logement": nombre_niveau_logement,
                        "offset": offset,
                        "order": order,
                        "periode_construction_dpe": periode_construction_dpe,
                        "plusieurs_facade_exposee": plusieurs_facade_exposee,
                        "pourcentage_surface_baie_vitree_exterieur": pourcentage_surface_baie_vitree_exterieur,
                        "presence_balcon": presence_balcon,
                        "select": select,
                        "surface_habitable_immeuble": surface_habitable_immeuble,
                        "surface_habitable_logement": surface_habitable_logement,
                        "surface_mur_deperditif": surface_mur_deperditif,
                        "surface_mur_exterieur": surface_mur_exterieur,
                        "surface_mur_totale": surface_mur_totale,
                        "surface_plancher_bas_deperditif": surface_plancher_bas_deperditif,
                        "surface_plancher_bas_totale": surface_plancher_bas_totale,
                        "surface_plancher_haut_deperditif": surface_plancher_haut_deperditif,
                        "surface_plancher_haut_totale": surface_plancher_haut_totale,
                        "surface_porte": surface_porte,
                        "surface_vitree_est": surface_vitree_est,
                        "surface_vitree_horizontal": surface_vitree_horizontal,
                        "surface_vitree_nord": surface_vitree_nord,
                        "surface_vitree_ouest": surface_vitree_ouest,
                        "surface_vitree_sud": surface_vitree_sud,
                        "traversant": traversant,
                        "type_adjacence_principal_plancher_bas": type_adjacence_principal_plancher_bas,
                        "type_adjacence_principal_plancher_haut": type_adjacence_principal_plancher_haut,
                        "type_batiment_dpe": type_batiment_dpe,
                        "type_dpe": type_dpe,
                        "type_energie_chauffage": type_energie_chauffage,
                        "type_energie_chauffage_appoint": type_energie_chauffage_appoint,
                        "type_energie_climatisation": type_energie_climatisation,
                        "type_energie_ecs": type_energie_ecs,
                        "type_energie_ecs_appoint": type_energie_ecs_appoint,
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
                        "type_generateur_ecs_anciennete_appoint": type_generateur_ecs_anciennete_appoint,
                        "type_generateur_ecs_appoint": type_generateur_ecs_appoint,
                        "type_installation_chauffage": type_installation_chauffage,
                        "type_installation_ecs": type_installation_ecs,
                        "type_isolation_mur_exterieur": type_isolation_mur_exterieur,
                        "type_isolation_plancher_bas": type_isolation_plancher_bas,
                        "type_isolation_plancher_haut": type_isolation_plancher_haut,
                        "type_materiaux_menuiserie": type_materiaux_menuiserie,
                        "type_plancher_bas_deperditif": type_plancher_bas_deperditif,
                        "type_plancher_haut_deperditif": type_plancher_haut_deperditif,
                        "type_porte": type_porte,
                        "type_production_energie_renouvelable": type_production_energie_renouvelable,
                        "type_ventilation": type_ventilation,
                        "type_vitrage": type_vitrage,
                        "u_baie_vitree": u_baie_vitree,
                        "u_mur_exterieur": u_mur_exterieur,
                        "u_plancher_bas_brut_deperditif": u_plancher_bas_brut_deperditif,
                        "u_plancher_bas_final_deperditif": u_plancher_bas_final_deperditif,
                        "u_plancher_haut_deperditif": u_plancher_haut_deperditif,
                        "u_porte": u_porte,
                        "uw": uw,
                        "version": version,
                        "vitrage_vir": vitrage_vir,
                    },
                    batiment_groupe_dpe_representatif_logement_list_params.BatimentGroupeDpeRepresentatifLogementListParams,
                ),
            ),
            cast_to=BatimentGroupeDpeRepresentatifLogementListResponse,
        )


class BatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
    def __init__(
        self, batiment_groupe_dpe_representatif_logement: BatimentGroupeDpeRepresentatifLogementResource
    ) -> None:
        self._batiment_groupe_dpe_representatif_logement = batiment_groupe_dpe_representatif_logement

        self.list = to_raw_response_wrapper(
            batiment_groupe_dpe_representatif_logement.list,
        )


class AsyncBatimentGroupeDpeRepresentatifLogementResourceWithRawResponse:
    def __init__(
        self, batiment_groupe_dpe_representatif_logement: AsyncBatimentGroupeDpeRepresentatifLogementResource
    ) -> None:
        self._batiment_groupe_dpe_representatif_logement = batiment_groupe_dpe_representatif_logement

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_dpe_representatif_logement.list,
        )


class BatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
    def __init__(
        self, batiment_groupe_dpe_representatif_logement: BatimentGroupeDpeRepresentatifLogementResource
    ) -> None:
        self._batiment_groupe_dpe_representatif_logement = batiment_groupe_dpe_representatif_logement

        self.list = to_streamed_response_wrapper(
            batiment_groupe_dpe_representatif_logement.list,
        )


class AsyncBatimentGroupeDpeRepresentatifLogementResourceWithStreamingResponse:
    def __init__(
        self, batiment_groupe_dpe_representatif_logement: AsyncBatimentGroupeDpeRepresentatifLogementResource
    ) -> None:
        self._batiment_groupe_dpe_representatif_logement = batiment_groupe_dpe_representatif_logement

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_dpe_representatif_logement.list,
        )
