# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeSyntheseEnveloppe"]


class BatimentGroupeSyntheseEnveloppe(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    classe_inertie: Optional[str] = None
    """classe d'inertie du DPE (enum version BDNB)"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

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

    materiaux_structure_mur_exterieur_simplifie: Optional[str] = None
    """materiaux principal utilié pour les murs extérieur simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: Optional[str] = None
    """materiaux principal utilié pour la toiture simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrées sur les murs extérieurs"""

    presence_balcon: Optional[bool] = None
    """
    présence de balcons identifiés par analyse des coefficients de masques solaires
    du DPE.
    """

    score_fiabilite: Optional[int] = None
    """score de fiabilité attribué aux informations affichées.

    En fonction de la source principale et du recoupement des informations de
    plusieurs sources le score peut àªtre plus ou moins élevé. Le score maximal de
    confiance est de 10, le score minimal de 1. des informations recoupées par
    plusieurs sources ont un score de confiance plus élevé que des informations
    fournies par une unique source (voir méthodo)
    """

    source_information_principale: Optional[str] = None
    """
    base de données source principale d'oà¹ est tirée directement les informations
    sur les systèmes énergétiques du bâtiment. (pour l'instant pas de combinaisons
    de sources voir méthodo)
    """

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

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
    plus performant d'un point de vue thermique.
    """
