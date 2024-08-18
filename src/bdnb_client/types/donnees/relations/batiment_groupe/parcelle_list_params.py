# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ParcelleListParams"]


class ParcelleListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    parcelle_id: str
    """
    (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    parcelle_principale: str
    """
    Booléen renvoyant 'vrai' si la parcelle cadastrale est la plus grande
    intersectant le groupe de bâtiment
    """

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
