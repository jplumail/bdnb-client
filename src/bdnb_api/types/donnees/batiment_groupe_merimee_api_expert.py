# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeMerimeeAPIExpert"]


class BatimentGroupeMerimeeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    distance_batiment_historique_plus_proche: Optional[int] = None
    """(mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]"""

    nom_batiment_historique_plus_proche: Optional[str] = None
    """(mer:tico) nom du bÃ¢timent historique le plus proche"""

    perimetre_bat_historique: Optional[bool] = None
    """Vrai si l'entitÃ© est dans le pÃ©rimÃ¨tre d'un bÃ¢timent historique"""
