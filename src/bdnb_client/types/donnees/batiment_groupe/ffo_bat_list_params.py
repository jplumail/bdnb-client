# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FfoBatListParams"]


class FfoBatListParams(TypedDict, total=False):
    annee_construction: str
    """Année de construction du bâtiment"""

    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    limit: str
    """Limiting and Pagination"""

    mat_mur_txt: str
    """(ffo) Matériaux principal des murs extérieurs"""

    mat_toit_txt: str
    """(ffo) Matériau principal des toitures"""

    nb_log: str
    """(rnc) Nombre de logements"""

    nb_niveau: str
    """(ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    usage_niveau_1_txt: str
    """indicateurs d'usage simplifié du bâtiment (verbose)"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
