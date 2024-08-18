# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeJsonStats"]


class BatimentGroupeJsonStats(BaseModel):
    annee_construction: Optional[int] = None
    """Année de construction du bâtiment.

    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    annee_construction_apres2018: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 2018
      - 3000
    ```
    """

    annee_construction_avant1848: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - -10000
      - 1848
    ```
    """

    annee_construction_de1848_a1900: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1848
      - 1900
    ```
    """

    annee_construction_de1900_a1920: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1900
      - 1920
    ```
    """

    annee_construction_de1920_a1948: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1920
      - 1948
    ```
    """

    annee_construction_de1948_a1960: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1948
      - 1960
    ```
    """

    annee_construction_de1960_a1970: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1960
      - 1970
    ```
    """

    annee_construction_de1970_a1980: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1970
      - 1980
    ```
    """

    annee_construction_de1980_a1990: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1980
      - 1990
    ```
    """

    annee_construction_de1990_a2000: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 1990
      - 2000
    ```
    """

    annee_construction_de2000_a2010: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 2000
      - 2010
    ```
    """

    annee_construction_de2010_a2018: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality:
      - 2010
      - 2018
    ```
    """

    annee_construction_indisponible: Optional[int] = None
    """
    ```yaml
    source_column: annee_construction
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: "NULL"
    ```
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB.

    ```yaml
    source_column: batiment_groupe_id
    source_ref: batiment_groupe
    ```
    """

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune.

    ```yaml
    source_column: code_commune_insee
    source_ref: batiment_groupe
    allow_group_by: true
    allow_filter_by: true
    ```
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE.

    ```yaml
    source_column: code_departement_insee
    source_ref: batiment_groupe
    allow_group_by: true
    allow_filter_by: true
    ```
    """

    code_epci_insee: Optional[str] = None
    """Code de l'EPCI.

    ```yaml
    source_column: code_epci_insee
    source_ref: batiment_groupe
    allow_group_by: true
    allow_filter_by: true
    ```
    """

    code_iris: Optional[str] = None
    """Code iris INSEE.

    ```yaml
    source_column: code_iris
    source_ref: batiment_groupe
    allow_group_by: true
    allow_filter_by: true
    ```
    """

    conso_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012.

    ```yaml
    source_column: conso_3_usages_ep_m2_arrete_2012
    source_ref: batiment_groupe_dpe_representatif_logement
    agg_type: avg
    ```
    """

    conso_5_usages_ep_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
    de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur
    actuellement).

    ```yaml
    source_column: conso_5_usages_ep_m2
    source_ref: batiment_groupe_dpe_representatif_logement
    agg_type: avg
    ```
    """

    distance_batiment_historique_plus_proche: Optional[int] = None
    """
    ```yaml
    source_ref: batiment_groupe_merimee
    source_column: distance_batiment_historique_plus_proche
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    etat_initial_consommation_energie_estim_350_ou_plus: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 350
      - 100000
    ```
    """

    etat_initial_consommation_energie_estim_de0_a50: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 0
      - 50
    ```
    """

    etat_initial_consommation_energie_estim_de100_a150: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 100
      - 150
    ```
    """

    etat_initial_consommation_energie_estim_de150_a200: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 150
      - 200
    ```
    """

    etat_initial_consommation_energie_estim_de200_a250: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 200
      - 250
    ```
    """

    etat_initial_consommation_energie_estim_de250_a350: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 250
      - 350
    ```
    """

    etat_initial_consommation_energie_estim_de50_a100: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 50
      - 100
    ```
    """

    etat_initial_consommation_energie_estim_mean: Optional[float] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: avg
    ```
    """

    etat_initial_consommation_energie_primaire_estim_420_ou_plus: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 420
      - 100000
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de0_a70: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 0
      - 70
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de110_a180: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 110
      - 180
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de180_a250: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 180
      - 250
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de250_a330: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 250
      - 330
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de330_a420: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 330
      - 420
    ```
    """

    etat_initial_consommation_energie_primaire_estim_de70_a110: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 70
      - 110
    ```
    """

    etat_initial_consommation_energie_primaire_estim_mean: Optional[float] = None
    """
    ```yaml
    source_column: etat_initial_consommation_energie_primaire_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: avg
    ```
    """

    etat_initial_ges_estim_100_ou_plus: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 100
      - 100000
    ```
    """

    etat_initial_ges_estim_de0_a6: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 0
      - 6
    ```
    """

    etat_initial_ges_estim_de11_a30: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 11
      - 30
    ```
    """

    etat_initial_ges_estim_de30_a50: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 30
      - 50
    ```
    """

    etat_initial_ges_estim_de50_a70: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 50
      - 70
    ```
    """

    etat_initial_ges_estim_de6_a11: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 6
      - 11
    ```
    """

    etat_initial_ges_estim_de70_a100: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_ges_estim_mean
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality:
      - 70
      - 100
    ```
    """

    etat_initial_risque_canicule_1: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_risque_canicule
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality: "1"
    ```
    """

    etat_initial_risque_canicule_2: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_risque_canicule
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality: "2"
    ```
    """

    etat_initial_risque_canicule_3: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_risque_canicule
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality: "3"
    ```
    """

    etat_initial_risque_canicule_4: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_risque_canicule
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality: "4"
    ```
    """

    etat_initial_risque_canicule_5: Optional[int] = None
    """
    ```yaml
    source_column: etat_initial_risque_canicule
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    agg_modality: "5"
    ```
    """

    etiquette_dpe_2021_initial_a: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_a
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_b: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_b
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_c: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_c
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_d: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_d
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_e: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_e
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_f: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_f
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_initial_g: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment pour l'état actuel du bâtiment.

    ```yaml
    source_column: etiquette_dpe_initial_g
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_a: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_a
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_b: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_b
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_c: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_c
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_d: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_d
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_e: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_e
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_f: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_f
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_2021_renove_g: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage).

    ```yaml
    source_column: etiquette_dpe_renove_g
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    etiquette_dpe_synthese: Optional[str] = None
    """TODO.

    ```yaml
    source_column: etiquette_dpe_synthese_particulier_simple
    source_ref: batiment_groupe_dpe_synthese_app_particulier
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    hauteur_mean: Optional[int] = None
    """(ign) Hauteur moyenne des bâtiments [m].

    ```yaml
    source_column: hauteur_mean
    source_ref: batiment_groupe_bdtopo_bat
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    materiaux_structure_mur_exterieur_simplifie: Optional[str] = None
    """materiaux principal utilié pour les murs extérieur simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment).

    ```yaml
    source_column: materiaux_structure_mur_exterieur_simplifie
    source_ref: batiment_groupe_synthese_enveloppe
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    nb_adresse_valid_ban: Optional[float] = None
    """
    Nombre d'adresses valides différentes provenant de la BAN qui desservent le
    groupe de bâtiment.

    ```yaml
    source_column: nb_adresse_valid_ban
    source_ref: batiment_groupe_adresse
    agg_type: sum
    ```
    """

    nb_batiment: Optional[int] = None
    """Nombre de bâtiments.

    ```yaml
    fixed_value: 1
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_a: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe A.

    ```yaml
    source_column: nb_classe_bilan_dpe_a
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_b: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe B.

    ```yaml
    source_column: nb_classe_bilan_dpe_b
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_c: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe C.

    ```yaml
    source_column: nb_classe_bilan_dpe_c
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_d: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe D.

    ```yaml
    source_column: nb_classe_bilan_dpe_d
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_e: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe E.

    ```yaml
    source_column: nb_classe_bilan_dpe_e
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_f: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe F.

    ```yaml
    source_column: nb_classe_bilan_dpe_f
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_bilan_dpe_g: Optional[float] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe G.

    ```yaml
    source_column: nb_classe_bilan_dpe_g
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_a: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique A.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_a
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_b: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique B.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_b
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_c: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique C.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_c
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_d: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique D.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_d
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_e: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique E.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_e
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_f: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique F.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_f
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_g: Optional[float] = None
    """(dpe) Nombre de DPE de la classe énergétique G.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8
    février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_g
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_classe_conso_energie_arrete_2012_nc: Optional[float] = None
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012.

    ```yaml
    source_column: nb_classe_conso_energie_arrete_2012_nc
    source_ref: batiment_groupe_dpe_statistique_logement
    agg_type: sum
    ```
    """

    nb_logement: Optional[float] = None
    """
    Nombre de logements pour le calcul de lâ€™exposition (il correspond à la
    répartition homogène des logements sociaux associés à la parcelle sur
    lâ€™ensemble des bâtiments contenus, en fonction de leur volumétrie).

    ```yaml
    source_column: nb_log
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    ```
    """

    nb_niveau: Optional[str] = None
    """
    ```yaml
    source_column: nb_niveau
    source_ref: batiment_groupe_ffo_bat
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    perimetre_bat_historique: Optional[str] = None
    """
    ```yaml
    source_column: perimetre_bat_historique
    source_ref: batiment_groupe_merimee
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    perimetre_bat_historique_false: Optional[int] = None
    """
    ```yaml
    source_column: perimetre_bat_historique
    source_ref: batiment_groupe_merimee
    agg_type: sum
    agg_modality: "false"
    ```
    """

    perimetre_bat_historique_true: Optional[int] = None
    """
    ```yaml
    source_column: perimetre_bat_historique
    source_ref: batiment_groupe_merimee
    agg_type: sum
    agg_modality: "true"
    ```
    """

    quartier_prioritaire: Optional[str] = None
    """Est situé dans un quartier prioritaire.

    ```yaml
    source_ref: batiment_groupe
    source_column: quartier_prioritaire
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    quartier_prioritaire_false: Optional[int] = None
    """
    ```yaml
    source_column: quartier_prioritaire
    source_ref: batiment_groupe_qpv
    agg_type: sum
    agg_modality: "false"
    ```
    """

    quartier_prioritaire_true: Optional[int] = None
    """
    ```yaml
    source_column: quartier_prioritaire
    source_ref: batiment_groupe_qpv
    agg_type: sum
    agg_modality: "true"
    ```
    """

    surface_emprise_sol: Optional[int] = None
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe).

    ```yaml
    source_ref: batiment_groupe
    source_column: s_geom_groupe
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    surface_facade_ext: Optional[float] = None
    """Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²].

    ```yaml
    source_column: surface_facade_ext
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    surface_facade_mitoyenne: Optional[float] = None
    """Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²].

    ```yaml
    source_column: surface_facade_mitoyenne
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    surface_facade_totale: Optional[float] = None
    """Estimation de la surface totale de faà§ade (murs + baies) [mÂ²].

    ```yaml
    source_column: surface_facade_totale
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """

    type_isolation_mur_exterieur: Optional[str] = None
    """
    type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
    version BDNB).

    ```yaml
    source_column: type_isolation_mur_exterieur
    source_ref: batiment_groupe_dpe_representatif_logement
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    usage_niveau_1_txt: Optional[str] = None
    """indicateurs d'usage simplifié du bâtiment (verbose).

    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    allow_group_by: false
    allow_filter_by: true
    ```
    """

    usage_niveau_1_txt_dependance: Optional[int] = None
    """
    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: Dépendance
    ```
    """

    usage_niveau_1_txt_resicol: Optional[int] = None
    """
    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: Résidentiel collectif
    ```
    """

    usage_niveau_1_txt_resiindiv: Optional[int] = None
    """
    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: Résidentiel individuel
    ```
    """

    usage_niveau_1_txt_secondaire: Optional[int] = None
    """
    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: Secondaire
    ```
    """

    usage_niveau_1_txt_tertiaire: Optional[int] = None
    """
    ```yaml
    source_column: usage_niveau_1_txt
    source_ref: batiment_groupe_ffo_bat
    agg_type: sum
    agg_modality: Tertiaire & Autres
    ```
    """

    volume_brut: Optional[float] = None
    """Volume brut du bâtiment [m3].

    ```yaml
    source_column: volume_brut
    source_ref: batiment_groupe_simulations_dpe
    agg_type: sum
    ```
    """
