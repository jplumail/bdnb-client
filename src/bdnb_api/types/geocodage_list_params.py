# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GeocodageListParams"]


class GeocodageListParams(TypedDict, total=False):
    q: Required[str]
    """Adresse texte"""

    autocomplete: int
    """
    Avec autocomplete on peut désactiver les traitements dâ€™auto-complétion
    autocomplete=0
    """

    citycode: str
    """Limite du nombre de réponses"""

    lat: str
    """latitude. Avec lat et lon on peut donner une priorité géographique"""

    limit: int
    """Limite du nombre de réponses"""

    lon: str
    """longitude. Avec lat et lon on peut donner une priorité géographique"""

    postcode: str
    """Limite du nombre de réponses"""

    type: Literal["street", "housenumber", "locality", "municipality"]
    """Limite du nombre de réponses"""
