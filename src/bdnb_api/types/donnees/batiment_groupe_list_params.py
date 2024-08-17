# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeListParams"]


class BatimentGroupeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code département INSEE"""

    code_epci_insee: str
    """Code de l'EPCI"""

    code_iris: str
    """Code iris INSEE"""

    code_qp: str
    """identifiant de la table qpv"""

    code_region_insee: str
    """Code région INSEE"""

    contient_fictive_geom_groupe: str
    """
    Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
    et ne représente pas la géométrie du groupe de bâtiment.
    """

    geom_groupe: str
    """Géométrie multipolygonale du groupe de bâtiment (Lambert-93)"""

    geom_groupe_pos_wgs84: str
    """Point sur la surface du groupe de bâtiment en WSG84"""

    libelle_commune_insee: str
    """(insee) Libellé de la commune accueillant le groupe de bâtiment"""

    limit: str
    """Limiting and Pagination"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    quartier_prioritaire: str
    """Est situé dans un quartier prioritaire"""

    s_geom_groupe: str
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
