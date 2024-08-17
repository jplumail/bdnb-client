# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JeuDeDonneeListParams"]


class JeuDeDonneeListParams(TypedDict, total=False):
    contrainte_acces: str
    """Dénomination de la contrainte d'accès associée"""

    couverture_spatiale: str
    """Couverture spatiale du jeu de données"""

    couverture_temporelle: str
    """Couverture temporelle du jeu de données"""

    date_publication: str
    """Date de publication du jeu de données"""

    denomination_serie: str
    """Dénomination du jeu de données"""

    description: str
    """Description du jeu de données"""

    limit: str
    """Limiting and Pagination"""

    millesime_jeu_de_donnees: str
    """Millésime du jeu de données"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
