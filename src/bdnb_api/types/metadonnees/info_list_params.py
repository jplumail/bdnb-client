# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InfoListParams"]


class InfoListParams(TypedDict, total=False):
    limit: str
    """Limiting and Pagination"""

    modifiee: str
    """date de modification"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    publication_schema: str
    """schema de publication"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
