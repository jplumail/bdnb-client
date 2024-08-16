# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeMerimeeListParams"]


class BatimentGroupeMerimeeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    distance_batiment_historique_plus_proche: str
    """(mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]"""

    limit: str
    """Limiting and Pagination"""

    nom_batiment_historique_plus_proche: str
    """(mer:tico) nom du bÃ¢timent historique le plus proche"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    perimetre_bat_historique: str
    """Vrai si l'entitÃ© est dans le pÃ©rimÃ¨tre d'un bÃ¢timent historique"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
