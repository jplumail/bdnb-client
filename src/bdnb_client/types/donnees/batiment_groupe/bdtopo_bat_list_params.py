# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BdtopoBatListParams"]


class BdtopoBatListParams(TypedDict, total=False):
    altitude_sol_mean: str
    """(ign) Altitude au sol moyenne [m]"""

    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    hauteur_mean: str
    """(ign) Hauteur moyenne des bâtiments [m]"""

    l_etat: str
    """(ign) Etat des bâtiments"""

    l_nature: str
    """(ign) Catégorie de nature du bâtiment"""

    l_usage_1: str
    """(ign) Usage principal du bâtiment"""

    l_usage_2: str
    """(ign) Usage secondaire du bâtiment"""

    limit: str
    """Limiting and Pagination"""

    max_hauteur: str
    """(ign) Hauteur maximale des bâtiments [m]"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
