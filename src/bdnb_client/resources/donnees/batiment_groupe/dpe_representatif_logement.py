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
from ....types.donnees.batiment_groupe import dpe_representatif_logement_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_dpe_representatif_logement import (
    BatimentGroupeDpeRepresentatifLogement,
)

__all__ = ["DpeRepresentatifLogementResource", "AsyncDpeRepresentatifLogementResource"]


class DpeRepresentatifLogementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DpeRepresentatifLogementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DpeRepresentatifLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DpeRepresentatifLogementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DpeRepresentatifLogementResourceWithStreamingResponse(self)

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeDpeRepresentatifLogement]:
        """Table qui contient les DPE représentatifs de chaque bâtiment de logement.

        Le DPE
        représentatif est soit un DPE issu de l'ancien arràªté qui n'est plus en vigueur
        (arràªté 2012) ou d'un nouveau DPE (arràªté 2021). Pour filtrer ancien et
        nouveau DPE utiliser le booléen `arrete_2021`

        Args:
          annee_construction_dpe: (dpe representatif) année de construction du logement (dpe)

          arrete_2021: précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
              du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
              de 2012.

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          chauffage_solaire: présence de chauffage solaire

          classe_bilan_dpe: Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
              primaire et les émissions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_conso_energie_arrete_2012: classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          classe_emission_ges: classe d'émission GES du DPE 5 usages (chauffage, ECS, climatisation, éclairage
              et auxiliaires). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_emission_ges_arrete_2012: classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation). valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code département INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

          conso_5_usages_ef_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires)en énergie finale (déduit de
              la production pv autoconsommée) (kWhef/mÂ²/an). valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
              de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          date_etablissement_dpe: date de l'établissement du dpe

          date_reception_dpe: date de réception du DPE dans la base de données de l'ADEME

          deperdition_baie_vitree: somme des déperditions par les baies vitrées du DPE (W/K)

          deperdition_mur: somme des déperditions par les murs du DPE (W/K)

          deperdition_plancher_bas: somme des deperditions par les planchers bas du logement (W/K)

          deperdition_plancher_haut: somme des deperditions par les planchers hauts du logement (W/K)

          deperdition_pont_thermique: somme des deperditions par les portes du DPE (W/K)

          deperdition_porte: somme des deperditions par les portes du DPE (W/K)

          ecs_solaire: présence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
              Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
              autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
              valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
              2021 (en vigueur actuellement)

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

          identifiant_dpe: identifiant de la table des DPE ademe

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

          nb_generateur_chauffage: nombre de générateurs de chauffage

          nb_generateur_ecs: nombre de générateurs d'ecs

          nb_installation_chauffage: nombre d'installation de chauffage

          nb_installation_ecs: nombre d'installation d'ecs

          nombre_niveau_immeuble: nombre de niveaux total de l'immeuble

          nombre_niveau_logement: nombre de niveaux du logement (maison ou appartement)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_dpe: période de construction selon la segmentation par grandes périodes
              "énergétiques" du DPE.

          plusieurs_facade_exposee: y a plusieurs facades exposées au vent

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          select: Filtering Columns

          surface_habitable_immeuble: surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
              usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)

          surface_habitable_logement: surface habitable du logement renseignée sauf dans le cas du dpe à l'immeuble.
              (surface habitable au sens du DPE)

          surface_mur_deperditif: somme de la surface de murs donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_mur_exterieur: somme de la surface surface de murs donnant sur l'extérieur

          surface_mur_totale: somme de la surface de murs totale

          surface_plancher_bas_deperditif: somme de la surface de plancher bas donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_plancher_bas_totale: somme de la surface de plancher bas totale

          surface_plancher_haut_deperditif: somme de la surface de plancher haut donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_plancher_haut_totale: somme de la surface de plancher haut totale

          surface_porte: somme de la surface de portes du DPE

          surface_vitree_est: somme de la surface de baies vitrées orientées est du DPE

          surface_vitree_horizontal: somme de la surface de baies vitrées horizontales du DPE (velux la plupart du
              temps)

          surface_vitree_nord: somme de la surface de baies vitrées orientées nord du DPE

          surface_vitree_ouest: somme de la surface de baies vitrées orientées ouest du DPE

          surface_vitree_sud: somme de la surface de baies vitrées orientées sud du DPE

          traversant: indicateur du cà´té traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_batiment_dpe: type de bâtiment au sens du DPE (maison, appartement ou immeuble). Cette colonne
              est renseignée uniquement si la source d'information est un DPE.

          type_dpe: type de DPE. Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son
              objet (logement, immeuble de logement, tertiaire) et la méthode de calcul
              utilisé (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'énergie pour le générateur de chauffage principal (enum version
              simplifiée BDNB)

          type_energie_chauffage_appoint: type d'énergie pour le générateur de chauffage d'appoint (enum version
              simplifiée BDNB)

          type_energie_climatisation: type d'énergie pour le générateur de climatisation principal (enum version
              simplifiée BDNB)

          type_energie_ecs: type d'énergie pour le générateur d'eau chaude sanitaire (ECS) principal (enum
              version simplifiée BDNB)

          type_energie_ecs_appoint: type d'énergie pour le générateur d'eau chaude sanitaire (ECS) d'appoint (enum
              version simplifiée BDNB)

          type_fermeture: type de fermeture principale installée sur les baies vitrées du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injecté principalement dans la lame entre les vitrages des baies
              vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)

          type_generateur_chauffage: type de générateur de chauffage principal (enum version simplifiée BDNB)

          type_generateur_chauffage_anciennete: ancienneté du générateur de chauffage principal

          type_generateur_chauffage_anciennete_appoint: ancienneté du générateur de chauffage d'appoint

          type_generateur_chauffage_appoint: type de générateur de chauffage d'appoint (enum version simplifiée BDNB)

          type_generateur_climatisation: type de générateur de climatisation principal (enum version simplifiée BDNB)

          type_generateur_climatisation_anciennete: ancienneté du générateur de climatisation principal

          type_generateur_ecs: type de générateur d'eau chaude sanitaire (ECS) principal (enum version
              simplifiée BDNB)

          type_generateur_ecs_anciennete: ancienneté du générateur d'eau chaude sanitaire (ECS) principal

          type_generateur_ecs_anciennete_appoint: ancienneté du générateur d'eau chaude sanitaire (ECS) d'appoint

          type_generateur_ecs_appoint: type de générateur d'eau chaude sanitaire (ECS) d'appoint (enum version
              simplifiée BDNB)

          type_installation_chauffage: type d'installation de chauffage (collectif ou individuel) (enum version
              simplifiée BDNB)

          type_installation_ecs: type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
              version simplifiée BDNB)

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

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

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

          version: version du DPE (arràªté 2021). Cenuméro de version permet de tracer les
              évolutions de modèle de données, decontexte réglementaire et de contrà´le mis en
              place sur les DPE. Chaque nouvelle version induit un certain nombre de
              changements substantiels. Certaines données ne sont disponible ou obligatoires
              qu'à partir d'une certaine version

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
            "/donnees/batiment_groupe_dpe_representatif_logement",
            page=SyncDefault[BatimentGroupeDpeRepresentatifLogement],
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
                    dpe_representatif_logement_list_params.DpeRepresentatifLogementListParams,
                ),
            ),
            model=BatimentGroupeDpeRepresentatifLogement,
        )


class AsyncDpeRepresentatifLogementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDpeRepresentatifLogementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDpeRepresentatifLogementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDpeRepresentatifLogementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDpeRepresentatifLogementResourceWithStreamingResponse(self)

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeDpeRepresentatifLogement, AsyncDefault[BatimentGroupeDpeRepresentatifLogement]]:
        """Table qui contient les DPE représentatifs de chaque bâtiment de logement.

        Le DPE
        représentatif est soit un DPE issu de l'ancien arràªté qui n'est plus en vigueur
        (arràªté 2012) ou d'un nouveau DPE (arràªté 2021). Pour filtrer ancien et
        nouveau DPE utiliser le booléen `arrete_2021`

        Args:
          annee_construction_dpe: (dpe representatif) année de construction du logement (dpe)

          arrete_2021: précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
              du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
              de 2012.

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          chauffage_solaire: présence de chauffage solaire

          classe_bilan_dpe: Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
              primaire et les émissions de CO2 sur les 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_conso_energie_arrete_2012: classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation). Valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          classe_emission_ges: classe d'émission GES du DPE 5 usages (chauffage, ECS, climatisation, éclairage
              et auxiliaires). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 31 mars 2021 (en vigueur actuellement)

          classe_emission_ges_arrete_2012: classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation). valable
              uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février 2012

          classe_inertie: classe d'inertie du DPE (enum version BDNB)

          code_departement_insee: Code département INSEE

          conso_3_usages_ep_m2_arrete_2012: consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
              , Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012

          conso_5_usages_ef_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires)en énergie finale (déduit de
              la production pv autoconsommée) (kWhef/mÂ²/an). valable uniquement pour les DPE
              appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          conso_5_usages_ep_m2: consommation annuelle 5 usages
              (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
              de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
              DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)

          date_etablissement_dpe: date de l'établissement du dpe

          date_reception_dpe: date de réception du DPE dans la base de données de l'ADEME

          deperdition_baie_vitree: somme des déperditions par les baies vitrées du DPE (W/K)

          deperdition_mur: somme des déperditions par les murs du DPE (W/K)

          deperdition_plancher_bas: somme des deperditions par les planchers bas du logement (W/K)

          deperdition_plancher_haut: somme des deperditions par les planchers hauts du logement (W/K)

          deperdition_pont_thermique: somme des deperditions par les portes du DPE (W/K)

          deperdition_porte: somme des deperditions par les portes du DPE (W/K)

          ecs_solaire: présence d'ecs solaire

          emission_ges_3_usages_ep_m2_arrete_2012: emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
              Climatisation). valable uniquement pour les DPE appliquant la méthode de
              l'arràªté du 8 février 2012 (kgCO2/m2/an).

          emission_ges_5_usages_m2: emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
              autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
              valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
              2021 (en vigueur actuellement)

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

          identifiant_dpe: identifiant de la table des DPE ademe

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

          nb_generateur_chauffage: nombre de générateurs de chauffage

          nb_generateur_ecs: nombre de générateurs d'ecs

          nb_installation_chauffage: nombre d'installation de chauffage

          nb_installation_ecs: nombre d'installation d'ecs

          nombre_niveau_immeuble: nombre de niveaux total de l'immeuble

          nombre_niveau_logement: nombre de niveaux du logement (maison ou appartement)

          offset: Limiting and Pagination

          order: Ordering

          periode_construction_dpe: période de construction selon la segmentation par grandes périodes
              "énergétiques" du DPE.

          plusieurs_facade_exposee: y a plusieurs facades exposées au vent

          pourcentage_surface_baie_vitree_exterieur: pourcentage de surface de baies vitrées sur les murs extérieurs

          presence_balcon: présence de balcons identifiés par analyse des coefficients de masques solaires
              du DPE.

          select: Filtering Columns

          surface_habitable_immeuble: surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
              usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)

          surface_habitable_logement: surface habitable du logement renseignée sauf dans le cas du dpe à l'immeuble.
              (surface habitable au sens du DPE)

          surface_mur_deperditif: somme de la surface de murs donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_mur_exterieur: somme de la surface surface de murs donnant sur l'extérieur

          surface_mur_totale: somme de la surface de murs totale

          surface_plancher_bas_deperditif: somme de la surface de plancher bas donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_plancher_bas_totale: somme de la surface de plancher bas totale

          surface_plancher_haut_deperditif: somme de la surface de plancher haut donnant sur des locaux non chauffés et sur
              l'extérieur (surfaces déperditives)

          surface_plancher_haut_totale: somme de la surface de plancher haut totale

          surface_porte: somme de la surface de portes du DPE

          surface_vitree_est: somme de la surface de baies vitrées orientées est du DPE

          surface_vitree_horizontal: somme de la surface de baies vitrées horizontales du DPE (velux la plupart du
              temps)

          surface_vitree_nord: somme de la surface de baies vitrées orientées nord du DPE

          surface_vitree_ouest: somme de la surface de baies vitrées orientées ouest du DPE

          surface_vitree_sud: somme de la surface de baies vitrées orientées sud du DPE

          traversant: indicateur du cà´té traversant du logement.

          type_adjacence_principal_plancher_bas: type d'adjacence principale des planchers bas (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_adjacence_principal_plancher_haut: type d'adjacence principale des planchers haut (sont ils en contact avec
              l'extérieur ou un local non chauffé) (enum DPE 2021)

          type_batiment_dpe: type de bâtiment au sens du DPE (maison, appartement ou immeuble). Cette colonne
              est renseignée uniquement si la source d'information est un DPE.

          type_dpe: type de DPE. Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son
              objet (logement, immeuble de logement, tertiaire) et la méthode de calcul
              utilisé (3CL conventionel,facture ou RT2012/RE2020)

          type_energie_chauffage: type d'énergie pour le générateur de chauffage principal (enum version
              simplifiée BDNB)

          type_energie_chauffage_appoint: type d'énergie pour le générateur de chauffage d'appoint (enum version
              simplifiée BDNB)

          type_energie_climatisation: type d'énergie pour le générateur de climatisation principal (enum version
              simplifiée BDNB)

          type_energie_ecs: type d'énergie pour le générateur d'eau chaude sanitaire (ECS) principal (enum
              version simplifiée BDNB)

          type_energie_ecs_appoint: type d'énergie pour le générateur d'eau chaude sanitaire (ECS) d'appoint (enum
              version simplifiée BDNB)

          type_fermeture: type de fermeture principale installée sur les baies vitrées du DPE
              (volet,persienne etc..) (enum version BDNB)

          type_gaz_lame: type de gaz injecté principalement dans la lame entre les vitrages des baies
              vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)

          type_generateur_chauffage: type de générateur de chauffage principal (enum version simplifiée BDNB)

          type_generateur_chauffage_anciennete: ancienneté du générateur de chauffage principal

          type_generateur_chauffage_anciennete_appoint: ancienneté du générateur de chauffage d'appoint

          type_generateur_chauffage_appoint: type de générateur de chauffage d'appoint (enum version simplifiée BDNB)

          type_generateur_climatisation: type de générateur de climatisation principal (enum version simplifiée BDNB)

          type_generateur_climatisation_anciennete: ancienneté du générateur de climatisation principal

          type_generateur_ecs: type de générateur d'eau chaude sanitaire (ECS) principal (enum version
              simplifiée BDNB)

          type_generateur_ecs_anciennete: ancienneté du générateur d'eau chaude sanitaire (ECS) principal

          type_generateur_ecs_anciennete_appoint: ancienneté du générateur d'eau chaude sanitaire (ECS) d'appoint

          type_generateur_ecs_appoint: type de générateur d'eau chaude sanitaire (ECS) d'appoint (enum version
              simplifiée BDNB)

          type_installation_chauffage: type d'installation de chauffage (collectif ou individuel) (enum version
              simplifiée BDNB)

          type_installation_ecs: type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
              version simplifiée BDNB)

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

          type_production_energie_renouvelable: type de production ENR pour le DPE (enum version DPE 2021)

          type_ventilation: type de ventilation (enum version BDNB)

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

          version: version du DPE (arràªté 2021). Cenuméro de version permet de tracer les
              évolutions de modèle de données, decontexte réglementaire et de contrà´le mis en
              place sur les DPE. Chaque nouvelle version induit un certain nombre de
              changements substantiels. Certaines données ne sont disponible ou obligatoires
              qu'à partir d'une certaine version

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
            "/donnees/batiment_groupe_dpe_representatif_logement",
            page=AsyncDefault[BatimentGroupeDpeRepresentatifLogement],
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
                    dpe_representatif_logement_list_params.DpeRepresentatifLogementListParams,
                ),
            ),
            model=BatimentGroupeDpeRepresentatifLogement,
        )


class DpeRepresentatifLogementResourceWithRawResponse:
    def __init__(self, dpe_representatif_logement: DpeRepresentatifLogementResource) -> None:
        self._dpe_representatif_logement = dpe_representatif_logement

        self.list = to_raw_response_wrapper(
            dpe_representatif_logement.list,
        )


class AsyncDpeRepresentatifLogementResourceWithRawResponse:
    def __init__(self, dpe_representatif_logement: AsyncDpeRepresentatifLogementResource) -> None:
        self._dpe_representatif_logement = dpe_representatif_logement

        self.list = async_to_raw_response_wrapper(
            dpe_representatif_logement.list,
        )


class DpeRepresentatifLogementResourceWithStreamingResponse:
    def __init__(self, dpe_representatif_logement: DpeRepresentatifLogementResource) -> None:
        self._dpe_representatif_logement = dpe_representatif_logement

        self.list = to_streamed_response_wrapper(
            dpe_representatif_logement.list,
        )


class AsyncDpeRepresentatifLogementResourceWithStreamingResponse:
    def __init__(self, dpe_representatif_logement: AsyncDpeRepresentatifLogementResource) -> None:
        self._dpe_representatif_logement = dpe_representatif_logement

        self.list = async_to_streamed_response_wrapper(
            dpe_representatif_logement.list,
        )
