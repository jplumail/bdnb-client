# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AncqpvListParams"]


class AncqpvListParams(TypedDict, total=False):
    code_qp: str
    """identifiant de la table qpv"""

    commune_qp: str
    """TODO"""

    geom: str
    """Géometrie de l'entité"""

    limit: str
    """Limiting and Pagination"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
