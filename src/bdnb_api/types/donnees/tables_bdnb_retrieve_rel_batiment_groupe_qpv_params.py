# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveRelBatimentGroupeQpvParams"]


class TablesBdnbRetrieveRelBatimentGroupeQpvParams(TypedDict, total=False):
    batiment_construction_id: str
    """
    Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

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

    qpv_code_qp: str
    """identifiant de la table qpv"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
