# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeMerimee"]


class RelBatimentGroupeMerimee(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    distance_batiment_historique: Optional[int] = None
    """
    (mer) Distance entre le batiment_historique et le batiment_construction (si
    moins de 500m) [m]
    """

    merimee_ref: Optional[str] = None
    """identifiant de la table merimee"""
