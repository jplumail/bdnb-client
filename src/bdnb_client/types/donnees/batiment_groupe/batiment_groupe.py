# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupe"]


class BatimentGroupe(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_epci_insee: Optional[str] = None
    """Code de l'EPCI"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    code_qp: Optional[str] = None
    """identifiant de la table qpv"""

    code_region_insee: Optional[str] = None
    """Code région INSEE"""

    contient_fictive_geom_groupe: Optional[bool] = None
    """
    Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
    et ne représente pas la géométrie du groupe de bâtiment.
    """

    geom_groupe: Optional[str] = None
    """Géométrie multipolygonale du groupe de bâtiment (Lambert-93)"""

    geom_groupe_pos_wgs84: Optional[str] = None
    """Point sur la surface du groupe de bâtiment en WSG84"""

    libelle_commune_insee: Optional[str] = None
    """(insee) Libellé de la commune accueillant le groupe de bâtiment"""

    nom_qp: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    quartier_prioritaire: Optional[bool] = None
    """Est situé dans un quartier prioritaire"""

    s_geom_groupe: Optional[int] = None
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""
