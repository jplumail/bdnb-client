# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenParams"]


class TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenParams(TypedDict, total=False):
    bat_prop_denomination_proprietaire: str
    """TODO"""

    dans_majic_pm: str
    """(majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm"""

    is_bailleur: str
    """Vrai si le propriétaire est un bailleur social"""

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) nombre de locaux déclarés dans majic_pm"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    siren: str
    """Numéro de SIREN de la personne morale (FF)"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
