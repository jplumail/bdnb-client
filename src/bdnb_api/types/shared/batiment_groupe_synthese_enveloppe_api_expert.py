# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeSyntheseEnveloppeAPIExpert"]


class BatimentGroupeSyntheseEnveloppeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    classe_inertie: Optional[str] = None
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

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

    materiaux_structure_mur_exterieur_simplifie: Optional[str] = None
    """materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: Optional[str] = None
    """materiaux principal utiliÃ© pour la toiture simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs"""

    presence_balcon: Optional[bool] = None
    """
    prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
    solaires du DPE.
    """

    score_fiabilite: Optional[int] = None
    """score de fiabilitÃ© attribuÃ© aux informations affichÃ©es.

    En fonction de la source principale et du recoupement des informations de
    plusieurs sources le score peut Ãªtre plus ou moins Ã©levÃ©. Le score maximal de
    confiance est de 10, le score minimal de 1. des informations recoupÃ©es par
    plusieurs sources ont un score de confiance plus Ã©levÃ© que des informations
    fournies par une unique source (voir mÃ©thodo)
    """

    source_information_principale: Optional[str] = None
    """
    base de donnÃ©es source principale d'oÃ¹ est tirÃ©e directement les informations
    sur les systÃ¨mes Ã©nergÃ©tiques du bÃ¢timent. (pour l'instant pas de
    combinaisons de sources voir mÃ©thodo)
    """

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

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
    rend plus performant d'un point de vue thermique.
    """
