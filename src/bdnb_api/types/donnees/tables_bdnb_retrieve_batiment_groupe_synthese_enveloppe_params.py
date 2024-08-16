# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeParams"]


class TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    classe_inertie: str
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    epaisseur_isolation_mur_exterieur_estim: str
    """
    epaisseur d'isolation moyenne des murs extÃ©rieurs estimÃ©e Ã partir de la
    diffÃ©rence entre le U de mur et le U de mur nu. Dans le cas d'une Ã©paisseur
    dÃ©clarÃ©e c'est directement l'Ã©paisseur dÃ©clarÃ©e qui est considÃ©rÃ©e, dans
    le cas contraire l'Ã©paisseur est estimÃ©e aussi pour les U conventionels de la
    mÃ©thode 3CL DPE.
    """

    epaisseur_lame: str
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
    DPE.
    """

    epaisseur_structure_mur_exterieur: str
    """
    epaisseur moyenne de la partie structure du mur (sans l'isolation rapportÃ©e ni
    les doublages)
    """

    facteur_solaire_baie_vitree: str
    """facteur de transmission du flux solaire par la baie vitrÃ©e.

    coefficient entre 0 et 1
    """

    l_local_non_chauffe_mur: str
    """liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)"""

    l_local_non_chauffe_plancher_bas: str
    """
    liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)
    """

    l_local_non_chauffe_plancher_haut: str
    """
    liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
    DPE 2021)
    """

    l_orientation_baie_vitree: str
    """liste des orientations des baies vitrÃ©es (enum version BDNB)"""

    l_orientation_mur_exterieur: str
    """liste des orientations des murs donnant sur l'extÃ©rieur (enum version BDNB)"""

    limit: str
    """Limiting and Pagination"""

    local_non_chauffe_principal_mur: str
    """liste des locaux non chauffÃ©s en contact avec les murs (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_bas: str
    """
    liste des locaux non chauffÃ©s en contact avec les planchers bas (enum DPE 2021)
    """

    local_non_chauffe_principal_plancher_haut: str
    """
    liste des locaux non chauffÃ©s en contact avec les planchers hauts (enum
    DPE 2021)
    """

    materiaux_structure_mur_exterieur: str
    """
    matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: str
    """materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: str
    """materiaux principal utiliÃ© pour la toiture simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    pourcentage_surface_baie_vitree_exterieur: str
    """pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs"""

    presence_balcon: str
    """
    prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
    solaires du DPE.
    """

    score_fiabilite: str
    """score de fiabilitÃ© attribuÃ© aux informations affichÃ©es.

    En fonction de la source principale et du recoupement des informations de
    plusieurs sources le score peut Ãªtre plus ou moins Ã©levÃ©. Le score maximal de
    confiance est de 10, le score minimal de 1. des informations recoupÃ©es par
    plusieurs sources ont un score de confiance plus Ã©levÃ© que des informations
    fournies par une unique source (voir mÃ©thodo)
    """

    select: str
    """Filtering Columns"""

    source_information_principale: str
    """
    base de donnÃ©es source principale d'oÃ¹ est tirÃ©e directement les informations
    sur les systÃ¨mes Ã©nergÃ©tiques du bÃ¢timent. (pour l'instant pas de
    combinaisons de sources voir mÃ©thodo)
    """

    traversant: str
    """indicateur du cÃ´tÃ© traversant du logement."""

    type_adjacence_principal_plancher_bas: str
    """
    type d'adjacence principale des planchers bas (sont ils en contact avec
    l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)
    """

    type_adjacence_principal_plancher_haut: str
    """
    type d'adjacence principale des planchers haut (sont ils en contact avec
    l'extÃ©rieur ou un local non chauffÃ©) (enum DPE 2021)
    """

    type_batiment_dpe: str
    """type de bÃ¢timent au sens du DPE (maison, appartement ou immeuble).

    Cette colonne est renseignÃ©e uniquement si la source d'information est un DPE.
    """

    type_fermeture: str
    """
    type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: str
    """
    type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
    vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
    BDNB)
    """

    type_isolation_mur_exterieur: str
    """
    type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: str
    """
    type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: str
    """
    type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: str
    """
    type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
    version BDNB)
    """

    type_plancher_bas_deperditif: str
    """
    materiaux ou principe constructif principal des planchers bas (enum version
    BDNB)
    """

    type_plancher_haut_deperditif: str
    """
    materiaux ou principe constructif principal des planchers hauts (enum version
    BDNB)
    """

    type_porte: str
    """type de porte du DPE (enum version DPE 2021)"""

    type_vitrage: str
    """type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)"""

    u_baie_vitree: str
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
    calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: str
    """Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)"""

    u_plancher_bas_brut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers bas brut."""

    u_plancher_bas_final_deperditif: str
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
    mÃ©thode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    u_porte: str
    """Coefficient de transmission thermique moyen des portes (W/mÂ²/K)"""

    uw: str
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es sans prise en
    compte des fermeture (W/mÂ²/K)
    """

    vitrage_vir: str
    """
    le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
    rend plus performant d'un point de vue thermique.
    """

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
