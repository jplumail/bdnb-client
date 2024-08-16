# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JeuDeDonneeListParams"]


class JeuDeDonneeListParams(TypedDict, total=False):
    contrainte_acces: str
    """DÃ©nomination de la contrainte d'accÃ¨s associÃ©e"""

    couverture_spatiale: str
    """Couverture spatiale du jeu de donnÃ©es"""

    couverture_temporelle: str
    """Couverture temporelle du jeu de donnÃ©es"""

    date_publication: str
    """Date de publication du jeu de donnÃ©es"""

    denomination_serie: str
    """DÃ©nomination du jeu de donnÃ©es"""

    description: str
    """Description du jeu de donnÃ©es"""

    limit: str
    """Limiting and Pagination"""

    millesime_jeu_de_donnees: str
    """MillÃ©sime du jeu de donnÃ©es"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
