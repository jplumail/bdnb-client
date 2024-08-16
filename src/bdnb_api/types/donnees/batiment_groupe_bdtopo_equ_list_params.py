# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeBdtopoEquListParams"]


class BatimentGroupeBdtopoEquListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    l_nature: str
    """(ign) CatÃ©gorie de nature du bÃ¢timent"""

    l_nature_detaillee: str
    """(ign) CatÃ©gorie dÃ©taillÃ©e de nature de l'Ã©quipement"""

    l_toponyme: str
    """(ign) Toponymie de l'Ã©quipement"""

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
