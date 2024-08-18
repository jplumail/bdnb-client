# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SyntheseEnveloppeListParams"]


class SyntheseEnveloppeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    classe_inertie: str
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: str
    """Code département INSEE"""

    epaisseur_isolation_mur_exterieur_estim: str
    """
    epaisseur d'isolation moyenne des murs extérieurs estimée à partir de la
    différence entre le U de mur et le U de mur nu. Dans le cas d'une épaisseur
    déclarée c'est directement l'épaisseur déclarée qui est considérée, dans le cas
    contraire l'épaisseur est estimée aussi pour les U conventionels de la méthode
    3CL DPE.
    """

    epaisseur_lame: str
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
    DPE.
    """

    epaisseur_structure_mur_exterieur: str
    """
    epaisseur moyenne de la partie structure du mur (sans l'isolation rapportée ni
    les doublages)
    """

    facteur_solaire_baie_vitree: str
    """facteur de transmission du flux solaire par la baie vitrée.

    coefficient entre 0 et 1
    """

    l_local_non_chauffe_mur: str
    """liste des locaux non chauffés en contact avec les murs (enum DPE 2021)"""

    l_local_non_chauffe_plancher_bas: str
    """liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)"""

    l_local_non_chauffe_plancher_haut: str
    """
    liste des locaux non chauffés en contact avec les planchers hauts (enum
    DPE 2021)
    """

    l_orientation_baie_vitree: str
    """liste des orientations des baies vitrées (enum version BDNB)"""

    l_orientation_mur_exterieur: str
    """liste des orientations des murs donnant sur l'extérieur (enum version BDNB)"""

    limit: str
    """Limiting and Pagination"""

    local_non_chauffe_principal_mur: str
    """liste des locaux non chauffés en contact avec les murs (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_bas: str
    """liste des locaux non chauffés en contact avec les planchers bas (enum DPE 2021)"""

    local_non_chauffe_principal_plancher_haut: str
    """
    liste des locaux non chauffés en contact avec les planchers hauts (enum
    DPE 2021)
    """

    materiaux_structure_mur_exterieur: str
    """
    matériaux ou principe constructif principal utilisé pour les murs extérieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: str
    """materiaux principal utilié pour les murs extérieur simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: str
    """materiaux principal utilié pour la toiture simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    pourcentage_surface_baie_vitree_exterieur: str
    """pourcentage de surface de baies vitrées sur les murs extérieurs"""

    presence_balcon: str
    """
    présence de balcons identifiés par analyse des coefficients de masques solaires
    du DPE.
    """

    score_fiabilite: str
    """score de fiabilité attribué aux informations affichées.

    En fonction de la source principale et du recoupement des informations de
    plusieurs sources le score peut àªtre plus ou moins élevé. Le score maximal de
    confiance est de 10, le score minimal de 1. des informations recoupées par
    plusieurs sources ont un score de confiance plus élevé que des informations
    fournies par une unique source (voir méthodo)
    """

    select: str
    """Filtering Columns"""

    source_information_principale: str
    """
    base de données source principale d'oà¹ est tirée directement les informations
    sur les systèmes énergétiques du bâtiment. (pour l'instant pas de combinaisons
    de sources voir méthodo)
    """

    traversant: str
    """indicateur du cà´té traversant du logement."""

    type_adjacence_principal_plancher_bas: str
    """
    type d'adjacence principale des planchers bas (sont ils en contact avec
    l'extérieur ou un local non chauffé) (enum DPE 2021)
    """

    type_adjacence_principal_plancher_haut: str
    """
    type d'adjacence principale des planchers haut (sont ils en contact avec
    l'extérieur ou un local non chauffé) (enum DPE 2021)
    """

    type_batiment_dpe: str
    """type de bâtiment au sens du DPE (maison, appartement ou immeuble).

    Cette colonne est renseignée uniquement si la source d'information est un DPE.
    """

    type_fermeture: str
    """
    type de fermeture principale installée sur les baies vitrées du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: str
    """
    type de gaz injecté principalement dans la lame entre les vitrages des baies
    vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)
    """

    type_isolation_mur_exterieur: str
    """
    type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: str
    """
    type d'isolation principal des planchers bas déperditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: str
    """
    type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: str
    """
    type de matériaux principal des menuiseries des baies vitrées du DPE (enum
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
    """type de vitrage principal des baies vitrées du DPE (enum version BDNB)"""

    u_baie_vitree: str
    """
    Coefficient de transmission thermique moyen des baies vitrées en incluant le
    calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: str
    """Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)"""

    u_plancher_bas_brut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers bas brut."""

    u_plancher_bas_final_deperditif: str
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
    méthode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    u_porte: str
    """Coefficient de transmission thermique moyen des portes (W/mÂ²/K)"""

    uw: str
    """
    Coefficient de transmission thermique moyen des baies vitrées sans prise en
    compte des fermeture (W/mÂ²/K)
    """

    vitrage_vir: str
    """
    le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
    plus performant d'un point de vue thermique.
    """

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
