# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HthdListParams"]


class HthdListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    l_nom_pdl: str
    """(hthd) Liste des noms des points de livraisons centraux"""

    l_type_pdl: str
    """(hthd) Liste de type de bâtiment desservis par les PDL"""

    limit: str
    """Limiting and Pagination"""

    nb_pdl: str
    """(hthd) Nombre total de PDL Arcep"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
