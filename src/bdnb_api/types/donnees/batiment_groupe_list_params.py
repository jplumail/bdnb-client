# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeListParams"]


class BatimentGroupeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_epci_insee: str
    """Code de l'EPCI"""

    code_iris: str
    """Code iris INSEE"""

    code_qp: str
    """identifiant de la table qpv"""

    code_region_insee: str
    """Code rÃ©gion INSEE"""

    contient_fictive_geom_groupe: str
    """
    Vaut "vrai", si la gÃ©omÃ©trie du groupe de bÃ¢timent est gÃ©nÃ©rÃ©e
    automatiquement et ne reprÃ©sente pas la gÃ©omÃ©trie du groupe de bÃ¢timent.
    """

    geom_groupe: str
    """GÃ©omÃ©trie multipolygonale du groupe de bÃ¢timent (Lambert-93)"""

    geom_groupe_pos_wgs84: str
    """Point sur la surface du groupe de bÃ¢timent en WSG84"""

    libelle_commune_insee: str
    """(insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent"""

    limit: str
    """Limiting and Pagination"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    quartier_prioritaire: str
    """Est situÃ© dans un quartier prioritaire"""

    s_geom_groupe: str
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
