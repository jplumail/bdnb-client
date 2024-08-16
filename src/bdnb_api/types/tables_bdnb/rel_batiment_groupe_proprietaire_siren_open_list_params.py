# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RelBatimentGroupeProprietaireSirenOpenListParams"]


class RelBatimentGroupeProprietaireSirenOpenListParams(TypedDict, total=False):
    bat_prop_denomination_proprietaire: str
    """TODO"""

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    dans_majic_pm: str
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    is_bailleur: str
    """Vrai si le propriÃ©taire est un bailleur social"""

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    siren: str
    """NumÃ©ro de SIREN de la personne morale (FF)"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
