# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReferentielAdministratifRegionListParams"]


class ReferentielAdministratifRegionListParams(TypedDict, total=False):
    code_region_insee: str
    """Code rÃ©gion INSEE"""

    geom_region: str
    """GÃ©omÃ©trie de la rÃ©gion"""

    libelle_region: str
    """LibellÃ© de la rÃ©gion"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
