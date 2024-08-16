# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RelColonneJeuDeDonneeListParams"]


class RelColonneJeuDeDonneeListParams(TypedDict, total=False):
    denomination_serie: str
    """Dénomination du jeu de données"""

    limit: str
    """Limiting and Pagination"""

    millesime_jeu_de_donnees: str
    """Millésime du jeu de données"""

    nom_colonne: str
    """Nom de la colonne"""

    nom_table: str
    """Nom de la table rattachée"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
