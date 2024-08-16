# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BatimentGroupeFfoBatListParams"]


class BatimentGroupeFfoBatListParams(TypedDict, total=False):
    annee_construction: str
    """AnnÃ©e de construction du bÃ¢timent"""

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    limit: str
    """Limiting and Pagination"""

    mat_mur_txt: str
    """(ffo) MatÃ©riaux principal des murs extÃ©rieurs"""

    mat_toit_txt: str
    """(ffo) MatÃ©riau principal des toitures"""

    nb_log: str
    """(rnc) Nombre de logements"""

    nb_niveau: str
    """(ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    usage_niveau_1_txt: str
    """indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
