# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DepartementListParams"]


class DepartementListParams(TypedDict, total=False):
    code_departement_insee: str
    """Code département INSEE"""

    code_region_insee: str
    """Code région INSEE"""

    geom_departement: str
    """Géométrie du département"""

    libelle_departement: str
    """Libellé département INSEE"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
