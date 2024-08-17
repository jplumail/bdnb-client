# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReferentielAdministratifIrisListParams"]


class ReferentielAdministratifIrisListParams(TypedDict, total=False):
    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code département INSEE"""

    code_iris: str
    """Code iris INSEE"""

    geom_iris: str
    """Géométrie de l'IRIS"""

    libelle_iris: str
    """Libellé de l'iris"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    type_iris: str
    """Type de l'IRIS"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
