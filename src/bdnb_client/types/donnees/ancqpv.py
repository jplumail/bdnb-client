# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Ancqpv"]


class Ancqpv(BaseModel):
    code_qp: Optional[str] = None
    """identifiant de la table qpv"""

    commune_qp: Optional[str] = None
    """TODO"""

    geom: Optional[str] = None
    """Géometrie de l'entité"""

    nom_qp: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""
