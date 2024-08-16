# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProprietaireListParams"]


class ProprietaireListParams(TypedDict, total=False):
    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_postal: str
    """Code postal"""

    dans_majic_pm: str
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    denomination: str
    """DÃ©nomination du propriÃ©taire (FF)"""

    forme_juridique: str
    """Forme juridique du propriÃ©taire (FF)"""

    libelle_commune: str
    """LibellÃ© de la commune"""

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    personne_id: str
    """
    ConcatÃ©nation de code dÃ©partement et du numÃ©ro de personne Majic3 (FF)
    (appelÃ© aussi NUMÃ‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les
    fichiers des locaux des personnes morales)
    """

    select: str
    """Filtering Columns"""

    siren: str
    """NumÃ©ro de SIREN de la personne morale (FF)"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
