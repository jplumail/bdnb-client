# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeBdtopoBatAPIExpert"]


class BatimentGroupeBdtopoBatAPIExpert(BaseModel):
    altitude_sol_mean: Optional[int] = None
    """(ign) Altitude au sol moyenne [m]"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    hauteur_mean: Optional[int] = None
    """(ign) Hauteur moyenne des bÃ¢timents [m]"""

    l_etat: Optional[List[str]] = None
    """(ign) Etat des bÃ¢timents"""

    l_nature: Optional[List[str]] = None
    """(ign) CatÃ©gorie de nature du bÃ¢timent"""

    l_usage_1: Optional[List[str]] = None
    """(ign) Usage principal du bÃ¢timent"""

    l_usage_2: Optional[List[str]] = None
    """(ign) Usage secondaire du bÃ¢timent"""

    max_hauteur: Optional[int] = None
    """(ign) Hauteur maximale des bÃ¢timents [m]"""
