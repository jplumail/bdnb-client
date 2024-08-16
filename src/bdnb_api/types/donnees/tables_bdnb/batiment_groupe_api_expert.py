# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeAPIExpert"]


class BatimentGroupeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_epci_insee: Optional[str] = None
    """Code de l'EPCI"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    code_qp: Optional[str] = None
    """identifiant de la table qpv"""

    code_region_insee: Optional[str] = None
    """Code rÃ©gion INSEE"""

    contient_fictive_geom_groupe: Optional[bool] = None
    """
    Vaut "vrai", si la gÃ©omÃ©trie du groupe de bÃ¢timent est gÃ©nÃ©rÃ©e
    automatiquement et ne reprÃ©sente pas la gÃ©omÃ©trie du groupe de bÃ¢timent.
    """

    geom_groupe: Optional[str] = None
    """GÃ©omÃ©trie multipolygonale du groupe de bÃ¢timent (Lambert-93)"""

    geom_groupe_pos_wgs84: Optional[str] = None
    """Point sur la surface du groupe de bÃ¢timent en WSG84"""

    libelle_commune_insee: Optional[str] = None
    """(insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent"""

    nom_qp: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    quartier_prioritaire: Optional[bool] = None
    """Est situÃ© dans un quartier prioritaire"""

    s_geom_groupe: Optional[int] = None
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""
