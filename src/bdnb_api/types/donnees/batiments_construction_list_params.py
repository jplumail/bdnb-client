# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentsConstructionListParams"]


class BatimentsConstructionListParams(TypedDict, total=False):
    altitude_sol: str
    """(ign) Altitude moynne au pied du bÃ¢timent physique [m]"""

    batiment_construction_id: str
    """Identifiant unique de l'entrÃ©e batiment_construction."""

    batiment_groupe_id: str
    """(bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_iris: str
    """Code iris INSEE"""

    fictive_geom_cstr: str
    """(ign) BoolÃ©en.

    Si 'True', la gÃ©omÃ©trie est fictive (et la surface au sol n'est pas rÃ©elle),
    sinon elle correspond Ã une emprise au sol rÃ©elle
    """

    geom_cstr: str
    """(ign) GÃ©omÃ©trie multipolygonale de l'enceinte du bÃ¢timent (Lambert-93)"""

    hauteur: str
    """(ign) Hauteur du bÃ¢timent physique [m]"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    rnb_id: str
    """Identifiant unique de l'entrÃ©e RNB.

    Dans le cas d'un double rnb_id pour un mÃªme bÃ¢timent construction, celui
    appartenant au bÃ¢timent construction avec le plus d'emprise au sol est pris en
    compte.
    """

    s_geom_cstr: str
    """(ign) Surface au sol de la gÃ©omÃ©trie de la construction [mÂ²]"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
