# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MerimeeListParams"]


class MerimeeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    distance_batiment_historique_plus_proche: str
    """(mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]"""

    limit: str
    """Limiting and Pagination"""

    nom_batiment_historique_plus_proche: str
    """(mer:tico) nom du bâtiment historique le plus proche"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    perimetre_bat_historique: str
    """Vrai si l'entité est dans le périmètre d'un bâtiment historique"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
