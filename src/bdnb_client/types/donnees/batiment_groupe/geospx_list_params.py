# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GeospxListParams"]


class GeospxListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    croisement_geospx_reussi: str
    """
    le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
    comme réussi
    """

    fiabilite_adresse: str
    """
    Fiabilité des adresses du bâtiment : "vrai" si les Fichiers Fonciers et BDTOpo
    partagent au moins une màªme adresse BAN
    """

    fiabilite_emprise_sol: str
    """Fiabilité de l'emprise au sol du bâtiment"""

    fiabilite_hauteur: str
    """Fiabilité de la hauteur du bâtiment"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
