# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeBdtopoBat"]


class BatimentGroupeBdtopoBat(BaseModel):
    altitude_sol_mean: Optional[int] = None
    """(ign) Altitude au sol moyenne [m]"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    hauteur_mean: Optional[int] = None
    """(ign) Hauteur moyenne des bâtiments [m]"""

    l_etat: Optional[List[str]] = None
    """(ign) Etat des bâtiments"""

    l_nature: Optional[List[str]] = None
    """(ign) Catégorie de nature du bâtiment"""

    l_usage_1: Optional[List[str]] = None
    """(ign) Usage principal du bâtiment"""

    l_usage_2: Optional[List[str]] = None
    """(ign) Usage secondaire du bâtiment"""

    max_hauteur: Optional[int] = None
    """(ign) Hauteur maximale des bâtiments [m]"""
