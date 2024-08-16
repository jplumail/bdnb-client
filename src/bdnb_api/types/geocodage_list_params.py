# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GeocodageListParams"]


class GeocodageListParams(TypedDict, total=False):
    q: Required[str]
    """Adresse texte"""

    autocomplete: int
    """
    Avec autocomplete on peut dÃ©sactiver les traitements dâ€™auto-complÃ©tion
    autocomplete=0
    """

    citycode: str
    """Limite du nombre de rÃ©ponses"""

    lat: str
    """latitude. Avec lat et lon on peut donner une prioritÃ© gÃ©ographique"""

    limit: int
    """Limite du nombre de rÃ©ponses"""

    lon: str
    """longitude. Avec lat et lon on peut donner une prioritÃ© gÃ©ographique"""

    postcode: str
    """Limite du nombre de rÃ©ponses"""

    type: Literal["street", "housenumber", "locality", "municipality"]
    """Limite du nombre de rÃ©ponses"""
