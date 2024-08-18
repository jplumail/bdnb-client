# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentConstructionListParams"]


class BatimentConstructionListParams(TypedDict, total=False):
    altitude_sol: str
    """(ign) Altitude moynne au pied du bâtiment physique [m]"""

    batiment_construction_id: str
    """Identifiant unique de l'entrée batiment_construction."""

    batiment_groupe_id: str
    """(bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code département INSEE"""

    code_iris: str
    """Code iris INSEE"""

    fictive_geom_cstr: str
    """(ign) Booléen.

    Si 'True', la géométrie est fictive (et la surface au sol n'est pas réelle),
    sinon elle correspond à une emprise au sol réelle
    """

    geom_cstr: str
    """(ign) Géométrie multipolygonale de l'enceinte du bâtiment (Lambert-93)"""

    hauteur: str
    """(ign) Hauteur du bâtiment physique [m]"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    rnb_id: str
    """Identifiant unique de l'entrée RNB.

    Dans le cas d'un double rnb_id pour un màªme bâtiment construction, celui
    appartenant au bâtiment construction avec le plus d'emprise au sol est pris en
    compte.
    """

    s_geom_cstr: str
    """(ign) Surface au sol de la géométrie de la construction [mÂ²]"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
