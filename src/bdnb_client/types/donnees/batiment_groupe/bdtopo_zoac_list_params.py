# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BdtopoZoacListParams"]


class BdtopoZoacListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    l_nature: str
    """(ign) Catégorie de nature du bâtiment"""

    l_nature_detaillee: str
    """(ign) Catégorie détaillée de nature de l'équipement"""

    l_toponyme: str
    """(ign) Toponymie de l'équipement"""

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
