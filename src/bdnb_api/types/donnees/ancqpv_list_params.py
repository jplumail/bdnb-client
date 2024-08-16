# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AncqpvListParams"]


class AncqpvListParams(TypedDict, total=False):
    code_qp: str
    """identifiant de la table qpv"""

    commune_qp: str
    """TODO"""

    geom: str
    """GÃ©ometrie de l'entitÃ©"""

    limit: str
    """Limiting and Pagination"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
