# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeDpeRepresentatifLogementAPIExpert"]


class BatimentGroupeDpeRepresentatifLogementAPIExpert(BaseModel):
    annee_construction_dpe: Optional[int] = None
    """(dpe representatif) annÃ©e de construction du logement (dpe)"""

    arrete_2021: Optional[bool] = None
    """
    prÃ©cise si le DPE est un DPE qui est issu de la nouvelle rÃ©forme du DPE
    (arrÃªtÃ© du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification
    antÃ©rieure de 2012.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    chauffage_solaire: Optional[bool] = None
    """prÃ©sence de chauffage solaire"""

    classe_bilan_dpe: Optional[str] = None
    """
    Classe du DPE issu de la synthÃ¨se du double seuil sur les consommations
    Ã©nergie primaire et les Ã©missions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    classe_conso_energie_arrete_2012: Optional[str] = None
    """classe d'Ã©mission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    classe_emission_ges: Optional[str] = None
    """
    classe d'Ã©mission GES du DPE 5 usages (chauffage, ECS, climatisation,
    Ã©clairage et auxiliaires). valable uniquement pour les DPE appliquant la
    mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur actuellement)
    """

    classe_emission_ges_arrete_2012: Optional[str] = None
    """classe d'emission GES du DPE 3 usages (Chauffage, ECS , Climatisation).

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    classe_inertie: Optional[str] = None
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    conso_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
    ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """

    conso_5_usages_ef_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires)en Ã©nergie finale (dÃ©duit
    de la production pv autoconsommÃ©e) (kWhef/mÂ²/an). valable uniquement pour les
    DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    conso_5_usages_ep_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
    (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
    pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    date_etablissement_dpe: Optional[str] = None
    """date de l'Ã©tablissement du dpe"""

    date_reception_dpe: Optional[str] = None
    """date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME"""

    deperdition_baie_vitree: Optional[float] = None
    """somme des dÃ©perditions par les baies vitrÃ©es du DPE (W/K)"""

    deperdition_mur: Optional[float] = None
    """somme des dÃ©perditions par les murs du DPE (W/K)"""

    deperdition_plancher_bas: Optional[float] = None
    """somme des deperditions par les planchers bas du logement (W/K)"""

    deperdition_plancher_haut: Optional[float] = None
    """somme des deperditions par les planchers hauts du logement (W/K)"""

    deperdition_pont_thermique: Optional[float] = None
    """somme des deperditions par les portes du DPE (W/K)"""

    deperdition_porte: Optional[float] = None
    """somme des deperditions par les portes du DPE (W/K)"""

    ecs_solaire: Optional[bool] = None
    """prÃ©sence d'ecs solaire"""

    emission_ges_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: Optional[float] = None
    """
    emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
    autoconsommÃ©e)
    (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
    uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
    vigueur actuellement)
    """

    epaisseur_isolation_mur_exterieur_estim: Optional[int] = None
    """
    epaisseur d'isolation moyenne des murs extÃ©rieurs estimÃ©e Ã partir de la
    diffÃ©rence entre le U de mur et le U de mur nu. Dans le cas d'une Ã©paisseur
    dÃ©clarÃ©e c'est directement l'Ã©paisseur dÃ©clarÃ©e qui est considÃ©rÃ©e, dans
    le cas contraire l'Ã©paisseur est estimÃ©e aussi pour les U conventionels de la
    mÃ©thode 3CL DPE.
    """

    epaisseur_lame: Optional[int] = None
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
    DPE.
    """

    epaisseur_structure_mur_exterieur: Optional[str] = None
    """
    epaisseur moyenne de la partie structure du mur (sans l'isolation rapportÃ©e ni
    les doublages)
    """

    facteur_solaire_baie_vitree: Optional[float] = None
    """facteur de transmission du flux solaire par la baie vitrÃ©e.

    coefficient entre 0 et 1
    """

    identifiant_dpe: Optional[str] = None
    """identifiant de la table des DPE ademe"""

    l_local_non_chauffe_mur: Optional[List[str]] = None
    """liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)"""

    l_local_non_chauffe_plancher_bas: Optional[List[str]] = None
    """
    liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)
    """

    l_local_non_chauffe_plancher_haut: Optional[List[str]] = None
    """
    liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
    DPE 2021)
    """

    l_orientation_baie_vitree: Optional[List[str]] = None
    """liste des orientations des baies vitrÃ©es (enum version BDNB)"""

    l_orientation_mur_exterieur: Optional[List[str]] = None
    """liste des orientations des murs donnant sur l'extÃ©rieur (enum version BDNB)"""

    local_non_chauffe_principal_mur: Optional[str] = None
    """liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_bas: Optional[str] = None
    """
    liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)
    """

    local_non_chauffe_principal_plancher_haut: Optional[str] = None
    """
    liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
    DPE 2021)
    """

    materiaux_structure_mur_exterieur: Optional[str] = None
    """
    matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
    (enum version BDNB)
    """

    nb_generateur_chauffage: Optional[int] = None
    """nombre de gÃ©nÃ©rateurs de chauffage"""

    nb_generateur_ecs: Optional[int] = None
    """nombre de gÃ©nÃ©rateurs d'ecs"""

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
    pÃ©riode de construction selon la segmentation par grandes pÃ©riodes
    "Ã©nergÃ©tiques" du DPE.
    """

    plusieurs_facade_exposee: Optional[bool] = None
    """y a plusieurs facades exposÃ©es au vent"""

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs"""

    presence_balcon: Optional[bool] = None
    """
    prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
    solaires du DPE.
    """

    surface_habitable_immeuble: Optional[float] = None
    """
    surface habitable totale de l'immeuble dans le cas d'un DPE appartement avec
    usage collectif ou d'un DPE immeuble.(surface habitable au sens du DPE)
    """

    surface_habitable_logement: Optional[float] = None
    """surface habitable du logement renseignÃ©e sauf dans le cas du dpe Ã l'immeuble.

    (surface habitable au sens du DPE)
    """

    surface_mur_deperditif: Optional[float] = None
    """
    somme de la surface de murs donnant sur des locaux non chauffÃ©s et sur
    l'extÃ©rieur (surfaces dÃ©perditives)
    """

    surface_mur_exterieur: Optional[float] = None
    """somme de la surface surface de murs donnant sur l'extÃ©rieur"""

    surface_mur_totale: Optional[float] = None
    """somme de la surface de murs totale"""

    surface_plancher_bas_deperditif: Optional[float] = None
    """
    somme de la surface de plancher bas donnant sur des locaux non chauffÃ©s et sur
    l'extÃ©rieur (surfaces dÃ©perditives)
    """

    surface_plancher_bas_totale: Optional[float] = None
    """somme de la surface de plancher bas totale"""

    surface_plancher_haut_deperditif: Optional[float] = None
    """
    somme de la surface de plancher haut donnant sur des locaux non chauffÃ©s et sur
    l'extÃ©rieur (surfaces dÃ©perditives)
    """

    surface_plancher_haut_totale: Optional[float] = None
    """somme de la surface de plancher haut totale"""

    surface_porte: Optional[float] = None
    """somme de la surface de portes du DPE"""

    surface_vitree_est: Optional[float] = None
    """somme de la surface de baies vitrÃ©es orientÃ©es est du DPE"""

    surface_vitree_horizontal: Optional[float] = None
    """
    somme de la surface de baies vitrÃ©es horizontales du DPE (velux la plupart du
    temps)
    """

    surface_vitree_nord: Optional[float] = None
    """somme de la surface de baies vitrÃ©es orientÃ©es nord du DPE"""

    surface_vitree_ouest: Optional[float] = None
    """somme de la surface de baies vitrÃ©es orientÃ©es ouest du DPE"""

    surface_vitree_sud: Optional[float] = None
    """somme de la surface de baies vitrÃ©es orientÃ©es sud du DPE"""

    traversant: Optional[str] = None
    """indicateur du cÃ´tÃ© traversant du logement."""

    type_adjacence_principal_plancher_bas: Optional[str] = None
    """
    type d'adjacence principale des planchers bas (sont ils en contact avec
    l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)
    """

    type_adjacence_principal_plancher_haut: Optional[str] = None
    """
    type d'adjacence principale des planchers haut (sont ils en contact avec
    l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)
    """

    type_batiment_dpe: Optional[str] = None
    """type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble).

    Cette colonne est renseignÃ©e uniquement si la source d'information est un DPE.
    """

    type_dpe: Optional[str] = None
    """type de DPE.

    Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021), son objet
    (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul utilisÃ©
    (3CL conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: Optional[str] = None
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
    simplifiÃ©e BDNB)
    """

    type_energie_chauffage_appoint: Optional[str] = None
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
    simplifiÃ©e BDNB)
    """

    type_energie_climatisation: Optional[str] = None
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur de climatisation principal (enum version
    simplifiÃ©e BDNB)
    """

    type_energie_ecs: Optional[str] = None
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal
    (enum version simplifiÃ©e BDNB)
    """

    type_energie_ecs_appoint: Optional[str] = None
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint
    (enum version simplifiÃ©e BDNB)
    """

    type_fermeture: Optional[str] = None
    """
    type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: Optional[str] = None
    """
    type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
    vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
    BDNB)
    """

    type_generateur_chauffage: Optional[str] = None
    """type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)"""

    type_generateur_chauffage_anciennete: Optional[str] = None
    """anciennetÃ© du gÃ©nÃ©rateur de chauffage principal"""

    type_generateur_chauffage_anciennete_appoint: Optional[str] = None
    """anciennetÃ© du gÃ©nÃ©rateur de chauffage d'appoint"""

    type_generateur_chauffage_appoint: Optional[str] = None
    """type de gÃ©nÃ©rateur de chauffage d'appoint (enum version simplifiÃ©e BDNB)"""

    type_generateur_climatisation: Optional[str] = None
    """type de gÃ©nÃ©rateur de climatisation principal (enum version simplifiÃ©e BDNB)"""

    type_generateur_climatisation_anciennete: Optional[str] = None
    """anciennetÃ© du gÃ©nÃ©rateur de climatisation principal"""

    type_generateur_ecs: Optional[str] = None
    """
    type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal (enum version
    simplifiÃ©e BDNB)
    """

    type_generateur_ecs_anciennete: Optional[str] = None
    """anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal"""

    type_generateur_ecs_anciennete_appoint: Optional[str] = None
    """anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint"""

    type_generateur_ecs_appoint: Optional[str] = None
    """
    type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) d'appoint (enum version
    simplifiÃ©e BDNB)
    """

    type_installation_chauffage: Optional[str] = None
    """
    type d'installation de chauffage (collectif ou individuel) (enum version
    simplifiÃ©e BDNB)
    """

    type_installation_ecs: Optional[str] = None
    """
    type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
    version simplifiÃ©e BDNB)
    """

    type_isolation_mur_exterieur: Optional[str] = None
    """
    type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: Optional[str] = None
    """
    type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: Optional[str] = None
    """
    type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: Optional[str] = None
    """
    type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
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
    """type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)"""

    u_baie_vitree: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
    calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: Optional[float] = None
    """Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)"""

    u_plancher_bas_brut_deperditif: Optional[float] = None
    """Coefficient de transmission thermique moyen des planchers bas brut."""

    u_plancher_bas_final_deperditif: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
    mÃ©thode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: Optional[float] = None
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    u_porte: Optional[float] = None
    """Coefficient de transmission thermique moyen des portes (W/mÂ²/K)"""

    uw: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es sans prise en
    compte des fermeture (W/mÂ²/K)
    """

    version: Optional[str] = None
    """version du DPE (arrÃªtÃ© 2021).

    CenumÃ©ro de version permet de tracer les Ã©volutions de modÃ¨le de donnÃ©es,
    decontexte rÃ©glementaire et de contrÃ´le mis en place sur les DPE. Chaque
    nouvelle version induit un certain nombre de changements substantiels. Certaines
    donnÃ©es ne sont disponible ou obligatoires qu'Ã partir d'une certaine version
    """

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
    rend plus performant d'un point de vue thermique.
    """
