# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatimentGroupeListParams"]


class BatimentGroupeListParams(TypedDict, total=False):
    groupby: Required[str]
    """colonnes de group by (agrÃ©gation)"""

    colonnes: str
    """
    colonnes pour lesquelles il faut calculer des statistiques (separÃ©es par
    virgules, pas d'espaces). Par default retourne toutes les colonnes ("\\**")
    """

    epsg: int
    """EPSG de sortie pour les gÃ©omÃ©tries. Exemple : 4326"""

    filter: str
    """
    filtre Ã appliquer Ã la population de bÃ¢timents avec syntaxe PostgREST pour les
    operateurs
    """

    output_format: Literal["json", "geojson", "raw_query"]
    """type de sortie.

    valeurs possibles: json, geojson, raw_query raw_query retourne pas les donnÃ©es
    agrÃ©gÃ©es mais uniquement la requÃªte SQL d'agrÃ©gation (pour dÃ©bogage)
    """
