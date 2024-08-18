# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TableListParams"]


class TableListParams(TypedDict, total=False):
    description: str
    """Commentaire de la table"""

    external_pk: str

    limit: str
    """Limiting and Pagination"""

    nom_table: str
    """Nom de la table"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    quality_elements: str

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
