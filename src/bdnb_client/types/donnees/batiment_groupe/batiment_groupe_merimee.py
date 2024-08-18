# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeMerimee"]


class BatimentGroupeMerimee(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    distance_batiment_historique_plus_proche: Optional[int] = None
    """(mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]"""

    nom_batiment_historique_plus_proche: Optional[str] = None
    """(mer:tico) nom du bâtiment historique le plus proche"""

    perimetre_bat_historique: Optional[bool] = None
    """Vrai si l'entité est dans le périmètre d'un bâtiment historique"""
