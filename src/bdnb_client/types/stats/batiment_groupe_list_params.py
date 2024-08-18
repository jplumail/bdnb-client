# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatimentGroupeListParams"]


class BatimentGroupeListParams(TypedDict, total=False):
    groupby: Required[str]
    """colonnes de group by (agrégation)"""

    colonnes: str
    """
    colonnes pour lesquelles il faut calculer des statistiques (separées par
    virgules, pas d'espaces). Par default retourne toutes les colonnes ("\\**")
    """

    epsg: int
    """EPSG de sortie pour les géométries. Exemple : 4326"""

    filter: str
    """
    filtre à appliquer à la population de bâtiments avec syntaxe PostgREST pour les
    operateurs
    """

    output_format: Literal["json", "geojson", "raw_query"]
    """type de sortie.

    valeurs possibles: json, geojson, raw_query raw_query retourne pas les données
    agrégées mais uniquement la requàªte SQL d'agrégation (pour débogage)
    """
