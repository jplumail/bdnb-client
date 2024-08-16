# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FournisseurRetrieveParams"]


class FournisseurRetrieveParams(TypedDict, total=False):
    acronyme: str
    """Acronyme du fournisseur de donnÃ©es"""

    denomination_fournisseur: str
    """DÃ©nomination du fournisseur de donnÃ©es"""

    description: str
    """Description du fournisseur de donnÃ©es"""

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
