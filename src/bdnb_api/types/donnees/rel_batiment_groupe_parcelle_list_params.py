# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RelBatimentGroupeParcelleListParams"]


class RelBatimentGroupeParcelleListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    parcelle_id: str
    """
    (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    parcelle_principale: str
    """
    BoolÃ©en renvoyant 'vrai' si la parcelle cadastrale est la plus grande
    intersectant le groupe de bÃ¢timent
    """

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
