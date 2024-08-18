# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeDpeRepresentatifLogement"]


class BatimentGroupeDpeRepresentatifLogement(BaseModel):
    annee_construction_dpe: Optional[int] = None
    """(dpe representatif) année de construction du logement (dpe)"""

    arrete_2021: Optional[bool] = None
    """
    précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
    du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
    de 2012.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    chauffage_solaire: Optional[bool] = None
    """présence de chauffage solaire"""

    classe_bilan_dpe: Optional[str] = None
    """
    Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
    primaire et les émissions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    classe_conso_energie_arrete_2012: Optional[str] = None
    """classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    classe_emission_ges: Optional[str] = None
    """
    classe d'émission GES du DPE 5 usages (chauffage, ECS, climatisation, éclairage
    et auxiliaires). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    classe_emission_ges_arrete_2012: Optional[str] = None
    """classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation).

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    classe_inertie: Optional[str] = None
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    conso_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    conso_5_usages_ef_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires)en énergie finale (déduit de
    la production pv autoconsommée) (kWhef/mÂ²/an). valable uniquement pour les DPE
    appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    conso_5_usages_ep_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
    de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    date_etablissement_dpe: Optional[str] = None
    """date de l'établissement du dpe"""

    date_reception_dpe: Optional[str] = None
    """date de réception du DPE dans la base de données de l'ADEME"""

    deperdition_baie_vitree: Optional[float] = None
    """somme des déperditions par les baies vitrées du DPE (W/K)"""

    deperdition_mur: Optional[float] = None
    """somme des déperditions par les murs du DPE (W/K)"""

    deperdition_plancher_bas: Optional[float] = None
    """somme des deperditions par les planchers bas du logement (W/K)"""

    deperdition_plancher_haut: Optional[float] = None
    """somme des deperditions par les planchers hauts du logement (W/K)"""

    deperdition_pont_thermique: Optional[float] = None
    """somme des deperditions par les portes du DPE (W/K)"""

    deperdition_porte: Optional[float] = None
    """somme des deperditions par les portes du DPE (W/K)"""

    ecs_solaire: Optional[bool] = None
    """présence d'ecs solaire"""

    emission_ges_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
    Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: Optional[float] = None
    """
    emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
    autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
    2021 (en vigueur actuellement)
    """

    epaisseur_isolation_mur_exterieur_estim: Optional[int] = None
    """
    epaisseur d'isolation moyenne des murs extérieurs estimée à partir de la
    différence entre le U de mur et le U de mur nu. Dans le cas d'une épaisseur
    déclarée c'est directement l'épaisseur déclarée qui est considérée, dans le cas
    contraire l'épaisseur est estimée aussi pour les U conventionels de la méthode
    3CL DPE.
    """

    epaisseur_lame: Optional[int] = None
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
    DPE.
    """

    epaisseur_structure_mur_exterieur: Optional[str] = None
    """
    epaisseur moyenne de la partie structure du mur (sans l'isolation rapportée ni
    les doublages)
    """

    facteur_solaire_baie_vitree: Optional[float] = None
    """facteur de transmission du flux solaire par la baie vitrée.

    coefficient entre 0 et 1
    """

    identifiant_dpe: Optional[str] = None
    """identifiant de la table des DPE ademe"""

    l_local_non_chauffe_mur: Optional[List[str]] = None
    """liste des locaux non chauffés en contact avec les murs (enum DPE 2021)"""

    l_local_non_chauffe_plancher_bas: Optional[List[str]] = None
    """liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)"""

    l_local_non_chauffe_plancher_haut: Optional[List[str]] = None
    """
    liste des locaux non chauffés en contact avec les planchers hauts (enum
    DPE 2021)
    """

    l_orientation_baie_vitree: Optional[List[str]] = None
    """liste des orientations des baies vitrées (enum version BDNB)"""

    l_orientation_mur_exterieur: Optional[List[str]] = None
    """liste des orientations des murs donnant sur l'extérieur (enum version BDNB)"""

    local_non_chauffe_principal_mur: Optional[str] = None
    """liste des locaux non chauffés en contact avec les murs (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_bas: Optional[str] = None
    """liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_haut: Optional[str] = None
    """
    liste des locaux non chauffés en contact avec les planchers hauts (enum
    DPE 2021)
    """

    materiaux_structure_mur_exterieur: Optional[str] = None
    """
    matériaux ou principe constructif principal utilisé pour les murs extérieurs
    (enum version BDNB)
    """

    nb_generateur_chauffage: Optional[int] = None
    """nombre de générateurs de chauffage"""

    nb_generateur_ecs: Optional[int] = None
    """nombre de générateurs d'ecs"""

    nb_installation_chauffage: Optional[int] = None
    """nombre d'installation de chauffage"""

    nb_installation_ecs: Optional[int] = None
    """nombre d'installation d'ecs"""

    nombre_niveau_immeuble: Optional[int] = None
    """nombre de niveaux total de l'immeuble"""

    nombre_niveau_logement: Optional[int] = None
    """nombre de niveaux du logement (maison ou appartement)"""

    periode_construction_dpe: Optional[str] = None
    """
    période de construction selon la segmentation par grandes périodes
    "énergétiques" du DPE.
    """

    plusieurs_facade_exposee: Optional[bool] = None
    """y a plusieurs facades exposées au vent"""

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrées sur les murs extérieurs"""

    presence_balcon: Optional[bool] = None
    """
    présence de balcons identifiés par analyse des coefficients de masques solaires
    du DPE.
    """

    surface_habitable_immeuble: Optional[float] = None
    """
    surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
    usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)
    """

    surface_habitable_logement: Optional[float] = None
    """surface habitable du logement renseignée sauf dans le cas du dpe à l'immeuble.

    (surface habitable au sens du DPE)
    """

    surface_mur_deperditif: Optional[float] = None
    """
    somme de la surface de murs donnant sur des locaux non chauffés et sur
    l'extérieur (surfaces déperditives)
    """

    surface_mur_exterieur: Optional[float] = None
    """somme de la surface surface de murs donnant sur l'extérieur"""

    surface_mur_totale: Optional[float] = None
    """somme de la surface de murs totale"""

    surface_plancher_bas_deperditif: Optional[float] = None
    """
    somme de la surface de plancher bas donnant sur des locaux non chauffés et sur
    l'extérieur (surfaces déperditives)
    """

    surface_plancher_bas_totale: Optional[float] = None
    """somme de la surface de plancher bas totale"""

    surface_plancher_haut_deperditif: Optional[float] = None
    """
    somme de la surface de plancher haut donnant sur des locaux non chauffés et sur
    l'extérieur (surfaces déperditives)
    """

    surface_plancher_haut_totale: Optional[float] = None
    """somme de la surface de plancher haut totale"""

    surface_porte: Optional[float] = None
    """somme de la surface de portes du DPE"""

    surface_vitree_est: Optional[float] = None
    """somme de la surface de baies vitrées orientées est du DPE"""

    surface_vitree_horizontal: Optional[float] = None
    """
    somme de la surface de baies vitrées horizontales du DPE (velux la plupart du
    temps)
    """

    surface_vitree_nord: Optional[float] = None
    """somme de la surface de baies vitrées orientées nord du DPE"""

    surface_vitree_ouest: Optional[float] = None
    """somme de la surface de baies vitrées orientées ouest du DPE"""

    surface_vitree_sud: Optional[float] = None
    """somme de la surface de baies vitrées orientées sud du DPE"""

    traversant: Optional[str] = None
    """indicateur du cà´té traversant du logement."""

    type_adjacence_principal_plancher_bas: Optional[str] = None
    """
    type d'adjacence principale des planchers bas (sont ils en contact avec
    l'extérieur ou un local non chauffé) (enum DPE 2021)
    """

    type_adjacence_principal_plancher_haut: Optional[str] = None
    """
    type d'adjacence principale des planchers haut (sont ils en contact avec
    l'extérieur ou un local non chauffé) (enum DPE 2021)
    """

    type_batiment_dpe: Optional[str] = None
    """type de bâtiment au sens du DPE (maison, appartement ou immeuble).

    Cette colonne est renseignée uniquement si la source d'information est un DPE.
    """

    type_dpe: Optional[str] = None
    """type de DPE.

    Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son objet
    (logement, immeuble de logement, tertiaire) et la méthode de calcul utilisé (3CL
    conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: Optional[str] = None
    """
    type d'énergie pour le générateur de chauffage principal (enum version
    simplifiée BDNB)
    """

    type_energie_chauffage_appoint: Optional[str] = None
    """
    type d'énergie pour le générateur de chauffage d'appoint (enum version
    simplifiée BDNB)
    """

    type_energie_climatisation: Optional[str] = None
    """
    type d'énergie pour le générateur de climatisation principal (enum version
    simplifiée BDNB)
    """

    type_energie_ecs: Optional[str] = None
    """
    type d'énergie pour le générateur d'eau chaude sanitaire (ECS) principal (enum
    version simplifiée BDNB)
    """

    type_energie_ecs_appoint: Optional[str] = None
    """
    type d'énergie pour le générateur d'eau chaude sanitaire (ECS) d'appoint (enum
    version simplifiée BDNB)
    """

    type_fermeture: Optional[str] = None
    """
    type de fermeture principale installée sur les baies vitrées du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: Optional[str] = None
    """
    type de gaz injecté principalement dans la lame entre les vitrages des baies
    vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)
    """

    type_generateur_chauffage: Optional[str] = None
    """type de générateur de chauffage principal (enum version simplifiée BDNB)"""

    type_generateur_chauffage_anciennete: Optional[str] = None
    """ancienneté du générateur de chauffage principal"""

    type_generateur_chauffage_anciennete_appoint: Optional[str] = None
    """ancienneté du générateur de chauffage d'appoint"""

    type_generateur_chauffage_appoint: Optional[str] = None
    """type de générateur de chauffage d'appoint (enum version simplifiée BDNB)"""

    type_generateur_climatisation: Optional[str] = None
    """type de générateur de climatisation principal (enum version simplifiée BDNB)"""

    type_generateur_climatisation_anciennete: Optional[str] = None
    """ancienneté du générateur de climatisation principal"""

    type_generateur_ecs: Optional[str] = None
    """
    type de générateur d'eau chaude sanitaire (ECS) principal (enum version
    simplifiée BDNB)
    """

    type_generateur_ecs_anciennete: Optional[str] = None
    """ancienneté du générateur d'eau chaude sanitaire (ECS) principal"""

    type_generateur_ecs_anciennete_appoint: Optional[str] = None
    """ancienneté du générateur d'eau chaude sanitaire (ECS) d'appoint"""

    type_generateur_ecs_appoint: Optional[str] = None
    """
    type de générateur d'eau chaude sanitaire (ECS) d'appoint (enum version
    simplifiée BDNB)
    """

    type_installation_chauffage: Optional[str] = None
    """
    type d'installation de chauffage (collectif ou individuel) (enum version
    simplifiée BDNB)
    """

    type_installation_ecs: Optional[str] = None
    """
    type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
    version simplifiée BDNB)
    """

    type_isolation_mur_exterieur: Optional[str] = None
    """
    type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: Optional[str] = None
    """
    type d'isolation principal des planchers bas déperditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: Optional[str] = None
    """
    type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: Optional[str] = None
    """
    type de matériaux principal des menuiseries des baies vitrées du DPE (enum
    version BDNB)
    """

    type_plancher_bas_deperditif: Optional[str] = None
    """
    materiaux ou principe constructif principal des planchers bas (enum version
    BDNB)
    """

    type_plancher_haut_deperditif: Optional[str] = None
    """
    materiaux ou principe constructif principal des planchers hauts (enum version
    BDNB)
    """

    type_porte: Optional[str] = None
    """type de porte du DPE (enum version DPE 2021)"""

    type_production_energie_renouvelable: Optional[str] = None
    """type de production ENR pour le DPE (enum version DPE 2021)"""

    type_ventilation: Optional[str] = None
    """type de ventilation (enum version BDNB)"""

    type_vitrage: Optional[str] = None
    """type de vitrage principal des baies vitrées du DPE (enum version BDNB)"""

    u_baie_vitree: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrées en incluant le
    calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: Optional[float] = None
    """Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)"""

    u_plancher_bas_brut_deperditif: Optional[float] = None
    """Coefficient de transmission thermique moyen des planchers bas brut."""

    u_plancher_bas_final_deperditif: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
    méthode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: Optional[float] = None
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    u_porte: Optional[float] = None
    """Coefficient de transmission thermique moyen des portes (W/mÂ²/K)"""

    uw: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrées sans prise en
    compte des fermeture (W/mÂ²/K)
    """

    version: Optional[str] = None
    """version du DPE (arràªté 2021).

    Cenuméro de version permet de tracer les évolutions de modèle de données,
    decontexte réglementaire et de contrà´le mis en place sur les DPE. Chaque
    nouvelle version induit un certain nombre de changements substantiels. Certaines
    données ne sont disponible ou obligatoires qu'à partir d'une certaine version
    """

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
    plus performant d'un point de vue thermique.
    """
